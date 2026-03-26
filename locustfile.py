from locust import HttpUser, task, between
import random

class TaskUser(HttpUser):
    wait_time = between(1, 3) 

    def on_start(self):
        response = self.client.post("/tasks/", json={"title": "Initial Task", "completed": False})
        if response.status_code == 200:
            self.task_id = response.json()["id"]
        else:
            self.task_id = None

    @task(4)
    def list_tasks(self):
        self.client.get("/tasks/")

    @task(2)
    def get_single_task(self):
        if self.task_id:
            self.client.get(f"/tasks/{self.task_id}")

    @task(4)
    def create_task(self):
        title = f"Task {random.randint(1,1000)}"
        response = self.client.post("/tasks/", json={"title": title, "completed": False})
        if response.status_code == 200:
            self.task_id = response.json()["id"]

    @task(2)
    def full_update_task(self):
        if self.task_id:
            title = f"Updated Task {random.randint(1,1000)}"
            self.client.put(f"/tasks/{self.task_id}", json={"title": title, "completed": True})

    @task(2)
    def partial_update_task(self):
        if self.task_id:
            completed = random.choice([True, False])
            self.client.patch(f"/tasks/{self.task_id}", json={"completed": completed})

    @task(1)
    def delete_task(self):
        if self.task_id:
            self.client.delete(f"/tasks/{self.task_id}")
            self.task_id = None  


'''from locust import HttpUser, task, between

class APIUser(HttpUser):
    # Simulate think time between 1-3 seconds
    wait_time = between(1, 3)

    @task(1)
    def get_test(self):
        self.client.get("/test")

    @task(1)
    def post_test(self):
        self.client.post("/test", json={"name": "test", "value": 123})

    @task(1)
    def put_test(self):
        self.client.put("/test", json={"name": "updated", "value": 456})

    @task(1)
    def patch_test(self):
        self.client.patch("/test", json={"value": 789})

    @task(1)
    def delete_test(self):
        self.client.delete("/test")


locust -f filename
'''