import ray
import anyscale
from ray import serve

import boto3

s3 = boto3.client('s3')
#s3.download_file('will-cars-ml-test',
        #'car-pics/Acura_ILX_2013_28_16_110_15_4_70_55_179_39_FWD_5_4_4dr_SLr.jpg', 'car.jpg')

class ResultServer():
    def __init__(self):
        pass

    async def __call__(self, request):
        return {"status":"OK"}
    
class ModelServer():
    def __init__(self):
        pass

    async def __call__(self, request):
        s3paths = await request.json()
        return s3paths

def setup_server():
    serve.create_backend("predict", ModelServer)
    serve.create_backend("status", ResultServer)
    serve.create_endpoint("start", 
            backend="predict", 
            route="/start",
            methods=["POST"])
    serve.create_endpoint("status", 
            backend="status", 
            route="/status",
            methods=["GET"])

def teardown_server():
    [serve.delete_endpoint(x) for x in serve.list_endpoints().keys()]
    [serve.delete_backend(x) for x in serve.list_backends().keys()]


if((__name__) == "__main__"):
    ray.init(address="auto")
    #anyscale.session("dendra-serve").connect()
    serve.start(detached=True)
    #serve.connect()

    setup_server()

