import os
import anyscale
import json
import ray
import time

from anyscale.sdk.anyscale_client.sdk import AnyscaleSDK

@ray.remote
class SessionManager():
    def read_token(self):
        try:
            creds_file = os.path.expanduser("~/.anyscale/credentials.json")
            token = json.load(open(creds_file,))["cli_token"]
        except:
            token = os.environ.get("ANYSCALE_CLI_TOKEN")
        return token


    # this local function skirts the yaml thing -- which points to its need
    def _launch_session(self):
        ANYSCALE_CLI_TOKEN= self.read_token()
        self.sdk = AnyscaleSDK(ANYSCALE_CLI_TOKEN)

        # This value must be derived or stored somewhere.
        # thes values are all 'scratch'
        KNOWN_GOOD_BUILD_ID="bld_2fLwy0UYmDbJBduciCEnOp"
        ANYSCALE_CLOUD_ID = "cld_6ViOfmT65Dm6trwRJ34AxJ"
        ANYSCALE_SEEWEED_PROJECT_ID = "prj_5enuFtOUIBNu8ZFcluAJBZ"
        num_workers=6
        head_node_type = "m5.2xlarge"
        worker_node_type = "m5.2xlarge"
        compute_template = self.sdk.create_compute_template({
            "name": f"seeweed_ct_{time.time()}",
            "project_id": ANYSCALE_SEEWEED_PROJECT_ID,
            "config": {
                "cloud_id": ANYSCALE_CLOUD_ID,
                "max_workers": num_workers,
                "region": "us-west-2",
                "allowed_azs": None,
                "head_node_type": {"instance_type": head_node_type,
                    "name": "gpu_large"},
                "worker_node_types": [{"instance_type": worker_node_type,
                    "max_workers": num_workers,
                    "min_workers": num_workers,
                    "name": "worker-node-0",
                    "use_spot": False}],
                "gcp": None,
                "azure": None,
                "aws": {}
                }
            })
        compute_template_id = compute_template.result.id

        sess_name = f"test-launch-{time.time()}"
        session = self.sdk.create_session({
            "name": sess_name,
            "project_id": ANYSCALE_SEEWEED_PROJECT_ID,
            "compute_template_id": compute_template_id,
            "build_id": KNOWN_GOOD_BUILD_ID,
            "uses_app_config": True
        })
        return session.result.id

    def launch(self, prefixes):
        session_id = self._launch_session()
        self.sdk.start_session(session_id, {})
        #sdk.run predictor in session.
        return session_id

    
if (__name__=="__main__"):
    ray.init(address="auto")
    session_manager = SessionManager.options(name="session_manager", lifetime="detached").remote()
    #session_manager = SessionManager()
    #session_manager.launch.remote("")


