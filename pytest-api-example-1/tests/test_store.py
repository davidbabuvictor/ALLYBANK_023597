from jsonschema import validate
import pytest
import schemas
import api_helpers
import random
import json
from hamcrest import assert_that, contains_string, is_

'''




TODO: Finish this test by...
1) Creating a function to test the PATCH request /store/order/{order_id}
2) *Optional* Consider using @pytest.fixture to create unique test data for each run
2) *Optional* Consider creating an 'Order' model in schemas.py and validating it in the test
3) Validate the response codes and values
4) Validate the response message "Order and pet status updated successfully"
'''
random_pet_id = random.randint(100, 200)  # unique test data for each run
global_order_id = ""


@pytest.mark.flaky(reruns=3, reruns_delay=2)  # if id alreday exist re-run
def test_create_new_pet():
    test_endpoint = "/pets"

    data = {"id": random_pet_id,
            "name": "string",
                    "type": "cat",
                    "status": "available"}
    response = api_helpers.post_api_data(test_endpoint, data)
    assert response.status_code == 201


def test_new_order_by_id():
    test_endpoint = "/store/order"

    data = {
        "pet_id": random_pet_id}

    response = api_helpers.post_api_data(test_endpoint, data)
    assert response.status_code == 201
    create_new_order_response = json.loads(response.text)
    print(json.dumps(create_new_order_response, indent=2))
    global global_order_id
    global_order_id = create_new_order_response['id']


@pytest.mark.parametrize("status", [("available", "pending", "sold")])
def test_patch_update_order_by_id(status):

    # Replace global_order_id)
    test_endpoint = f"/store/order/{global_order_id}"

    data = {
        "status": random.choice(status)}
    response = api_helpers.patch_api_data(test_endpoint, data)
    # Validate the appropriate response code for updating the order id
    assert response.status_code == 200
    _update_order_response = response.json()
    assert _update_order_response["message"] == "Order and pet status updated successfully"
