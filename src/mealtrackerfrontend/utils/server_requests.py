import requests
import utils.configuration as configuration

class ServerRequest():
    def __init__(self):
        # TAKE FROM CONFIG
        self.backend_url = configuration.app_config['DEFAULT']["backend_url"]
        # self.input = input

    def insert_meal(self, meal):
        # BUILD THE BODY OF THE REQUEST STARTING FROM MEAL INFO
        req_url = self.backend_url + "/meal/"
        print(req_url)
        print("Meal:", meal)
        res = requests.post(req_url, json=meal)

        if res.status_code == 201:
            return True
        else:
            print("Error in insertion", res.status_code, res.text)
            return False