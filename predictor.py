
import boto3


#s3.download_file('will-cars-ml-test',
        #'car-pics/Acura_ILX_2013_28_16_110_15_4_70_55_179_39_FWD_5_4_4dr_SLr.jpg', 'car.jpg')


@ray.remote
class Predictor():

    def __init__(self):
        self.s3 = boto3.resource('s3')

    def predict(self):
        print("Kicking off request for inference")
        cars = self.s3.Bucket('will-cars-ml-test')
        retval = []
        for prefix in prefixes["prefixes"]:
            for o in cars.objects.filter(Prefix=prefix):
                print(o.key)
                retval.append({o.key, o.get()["ContentLength"]})
        return str(retval)



