import pytest
import  json


with open("data.json") as f:
    test_data = json.load(f)["tests"]


@pytest.mark.parametrize("data", test_data)
def test_dynamic_cases(webpage, data):
    # Auth user
    webpage.auth.auth_user()
    # Navigate to the specified section
    webpage.dash.navigate_by_text(text = data["navigateTo"])
    # Verify the task is in the correct column
    webelem = webpage.dash.verify_task_in_column(task=data['verifyTask'],column=data['column'])
    # Verify the tags in task
    webpage.dash.verify_tags_in_task(webelem=webelem,tags=data['tags'])
    # User logout
    webpage.auth.logout()

