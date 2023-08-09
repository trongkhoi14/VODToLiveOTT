import gevent.monkey
gevent.monkey.patch_all()

from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 5)  

    @task
    def get_admin_users(self):
        self.client.get("/admin_users")

    @task
    def get_total_videos(self):
        self.client.get("/total_videos")
