import ray
import anyscale
from ray import serve
import time

class ResultServer():
    def __init__(self):
        pass

    async def __call__(self, request, session_id):
        return {"location":f"/status/{session_id}"}
    
class ModelServer():
    def __init__(self):
        self.session_manager = ray.get_actor("session_manager")

    async def __call__(self, request):
        prefixes = await request.json()
        session_ref = self.session_manager.launch.remote(prefixes)
        session_id = ray.get(session_ref)
        return {"status":"Started", "location":f"/status/{session_id}"}
    #TODO sessions can accumulate


def setup_server():
    serve.create_backend("predict", ModelServer)
    serve.create_backend("status", ResultServer)
    serve.create_endpoint("start", 
            backend="predict", 
            route="/start",
            methods=["POST"])
    serve.create_endpoint("status", 
            backend="status", 
            route="/status/{session_id}",
            methods=["GET"])

def teardown_server():
    [serve.delete_endpoint(x) for x in serve.list_endpoints().keys()]
    [serve.delete_backend(x) for x in serve.list_backends().keys()]


if((__name__) == "__main__"):
    ray.init(address="auto")
    #anyscale.session("dendra-serve").app_config("seeweed-serve:1").connect()
    serve.start(detached=True)
    #serve.connect()
    #serve.teardown_server()
    setup_server()

#https://session-4cne62g9jztvzuwaua8uwa.anyscaleuserdata.com/serve
