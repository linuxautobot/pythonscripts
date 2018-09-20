from locust import HttpLocust, TaskSet, task
import json
import uuid

#ab = str(uuid.uuid1()).replace('-','')
#data1 = {"screen_id":"test","show":"userresponses","episode_id":"test","user_id":ab+"@gmail.com"}
#headers = {'Content-type': 'application/json'}
#
class UserBehavior(TaskSet):
#    def on_start(self):
#        """ on_start is called when a Locust start before any task is scheduled """
#        self.login()

    @task
    def login(self):

	ab = str(uuid.uuid1()).replace('-','')
	data1 = {"screen_id":"test","show":"userresponses","episode_id":"test","user_id":ab+"@gmail.com"}
	headers = {'Content-type': 'application/json'}
        res=(self.client.post("/dev/api/answer",json=data1))
	print(res.text)
	#return res.text

#    @task
#    def profile(self):
#        self.client.post("/dev/api/acrdata",json=data1)
#        #self.client.get("/dev/api/acrdata")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 1000
    max_wait = 20000
