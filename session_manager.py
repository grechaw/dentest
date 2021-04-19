import os
import anyscale
import json
import time

from anyscale.sdk.anyscale_client.sdk import AnyscaleSDK

def read_token():
    try:
        creds_file = os.path.expanduser("~/.anyscale/credentials.json")
        token = json.load(open(creds_file,))["cli_token"]
    except:
        token = os.environ.get("ANYSCALE_CLI_TOKEN")
    return token

ANYSCALE_CLI_TOKEN= read_token()
sdk = AnyscaleSDK(ANYSCALE_CLI_TOKEN)

# This value must be derived or stored somewhere.
# thes values are all 'scratch'
KNOWN_GOOD_BUILD_ID="bld_2fLwy0UYmDbJBduciCEnOp"
ANYSCALE_CLOUD_ID = "cld_6ViOfmT65Dm6trwRJ34AxJ"
ANYSCALE_SEEWEED_PROJECT_ID = "prj_5enuFtOUIBNu8ZFcluAJBZ"


# this local function skirts the yaml thing -- which points to its need
def _launch_session():
    num_workers=6
    head_node_type = "m5.2xlarge"
    worker_node_type = "m5.2xlarge"
    compute_template = sdk.create_compute_template({
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
    session = sdk.create_session({
        "name": sess_name,
        "project_id": ANYSCALE_SEEWEED_PROJECT_ID,
        "compute_template_id": compute_template_id,
        "build_id": KNOWN_GOOD_BUILD_ID,
        "uses_app_config": True
    })
    return session.result.id

def launch_predictor(prefixes):
    #session_id = _launch_session()
    #sdk.start_session(session_id, {})
    session_id = "yep"
    #sdk.run predictor in session.
    return session_id

    
#launch_predictor.remote()


