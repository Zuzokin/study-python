import pytest

from web_app.some_web_client import SomeResourceClient, URL, USER_ID
import responses
from datetime import datetime


@responses.activate
def test_some_web_client():
    valid_json_answer = {
        "lastActionTime": 1698049432,
        "timeDiff": 9441,
    }
    some_resource_client = SomeResourceClient(URL)
    responses.add(
        method=responses.GET,
        url=f"{URL}web/2/user/get-status/{USER_ID}",
        json=valid_json_answer,
        status=200,
    )
    response = some_resource_client.get_user_last_action_time(user_id=USER_ID)
    assert response == datetime.fromtimestamp(
        valid_json_answer["lastActionTime"] - valid_json_answer["timeDiff"]
    )


@responses.activate
def test_some_web_client_error():
    valid_json_answer = {"errors": ["Not found"]}
    responses.add(
        method=responses.GET,
        url=f"{URL}web/2/user/get-status/-{USER_ID}",
        json=valid_json_answer,
        status=200,
    )
    with pytest.raises(KeyError):
        some_resource_client = SomeResourceClient(URL)
        response = some_resource_client.get_user_last_action_time(user_id="-" + USER_ID)
