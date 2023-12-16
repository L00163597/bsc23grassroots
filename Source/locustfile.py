from locust import HttpUser, task, between


class MyUser(HttpUser):
    wait_time = between(1, 3)  # A user waits between 1 to 3 seconds between tasks

    @task
    def my_task(self):
        self.client.get("http://127.0.0.1:8000")