from jsonschema import validate
import pytest
import random
import json


import schemas
import api_helpers
from hamcrest import assert_that, contains_string, is_

'''
TODO: Finish this test by...
1) Troubleshooting and fixing the test failure
The purpose of this test is to validate the response matches the expected schema defined in schemas.py
'''


def test_pet_schema():
    test_endpoint = "/pets/1"

    response = api_helpers.get_api_data(test_endpoint)
    pet_data = response.json()
    print("\n", pet_data['id'], type(pet_data['id']))
    print(pet_data['name'], type(pet_data['name']))
    assert response.status_code == 200

    # Validate the response schema against the defined schema in schemas.py
    validate(instance=response.json(), schema=schemas.pet)
    assert isinstance(pet_data['id'], int), f"'id' should be an integer"
    assert isinstance(pet_data['name'], str), f"'name' should be a string"


'''
TODO: Finish this test by...
1) Extending the parameterization to include all available statuses
2) Validate the appropriate response code
3) Validate the 'status' property in the response is equal to the expected status
4) Validate the schema for each object in the response
'''
# Extending the parameterization to include all available statuses


@pytest.mark.parametrize("status", [("available", "pending", "sold")])
def test_find_by_status_200(status):
    test_endpoint = "/pets/findByStatus"
    params = {
        "status": random.choice(status)  # Selecting the Randon Pet Status from Parametrize(

    }
    response = api_helpers.get_api_data(test_endpoint, params)
    assert response.status_code == 200  # Validate the appropriate response code
    pet_status_response = json.loads(response.text)
    print(json.dumps(pet_status_response, indent=2))
    expected_status = ["available", "pending", "sold"]

    if pet_status_response == []:
        print("No Pets in", params, "Status")
    else:
        for status in pet_status_response:
            print("Pet Status id", status['id'], status['status'])
            assert status['status'] in expected_status,  f"'Pet' status is not matching"


'''
TODO: Finish this test by...
1) Testing and validating the appropriate 404 response for /pets/{pet_id}
2) Parameterizing the test for any edge cases
'''


def test_get_by_id_404():
    # TODO...
    test_endpoint = "/pets/-2"
    response = api_helpers.get_api_data(test_endpoint)
    assert response.status_code == 404


def test_create_new_pet_existing_pet_id():
    test_endpoint = "/pets"

    data = {"id": 1,
            "name": "string",
                    "type": "cat",
                    "status": "available"}
    response = api_helpers.post_api_data(test_endpoint, data)
    assert response.status_code == 409
    if response.status_code == 409:
        assert response.json()["message"] == "Pet with ID 1 already exists"
     