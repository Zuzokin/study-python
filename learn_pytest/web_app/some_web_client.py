import requests
import json
from datetime import datetime

URL = "https://www.avito.ru/"
USER_ID = "0db33beea6a1114d77a1f3e7b0515ff5"


class SomeResourceClient:
    def __init__(self, url):
        self._url = url

    def __user_get_status(self, user_id):
        resp = requests.get(f"{self._url}web/2/user/get-status/{user_id}")
        # здесь должна быть проверка на 404 и другие нештатные ответы, но в качестве обучения ее нет :)
        data = json.loads(resp.text)
        return data

    def get_user_last_action_time(self, user_id):
        data = self.__user_get_status(user_id)
        last_action_time = data["lastActionTime"]
        time_diff = data["timeDiff"]
        return datetime.fromtimestamp(last_action_time - time_diff)


if __name__ == "__main__":
    some_resource_client = SomeResourceClient(url=URL)
    print(some_resource_client.get_user_last_action_time(user_id=USER_ID))
