import time
from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    
    car_pics = {"prefixes":[
        "car-pics/Acura_ILX",
    ]}
    wait_time = between(1, 2.5)
    HOST="http://localhost:8000"

    @task
    def post_job(self):
        response = self.client.post("/start", json=self.car_pics)


    @task(2)
    def view_items(self):
        for item_id in range(10):
            self.client.get("/status")
            time.sleep(1)

    def on_start(self):
        pass

resp = requests.post("http://localhost:8000/start", json = {"prefixes":[]})
