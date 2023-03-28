import requests
import uuid     # universally unique identifier

ENDPOINT = "https://teaching-assistant-evaluation.onrender.com"

# response = requests.get(ENDPOINT)
# print(response)

# data = response.json()
# print(data)

# #print the status code
# status_code = response.status_code
# print(status_code)

# # test will pass if call to endpoint is successful (sanity check) 
# def test_can_call_endpoint():
#     response = requests.get(ENDPOINT)
#     assert response.status_code == 200

def test_can_create_task():
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    data = create_task_response.json()

    task_id = data["task"]["task_id"]
    get_task_response = get_task(task_id)
   
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["id"] == payload["id"]  #cols in dataframe
    assert get_task_data["native_english_speaker"] == payload["native_english_speaker"]
    assert get_task_data["course_instructor"] == payload["course_instructor"]
    assert get_task_data["course"] == payload["course"]
    assert get_task_data["semester"] == payload["semester"]
    assert get_task_data["class_size"] == payload["class_size"]


def test_can_update_task():
    # create a task
    payload = new_task_payload()
    create_task_response = create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]
    
    # update the task
    new_payload = {
        "id" : payload["id"],
        "task_id" : task_id,
        "native_english_speaker" : payload["native_english_speaker"],
        "course_instructor" : payload["course_instructor"],
        "course" : payload["course"],
        "semester" : payload["semester"]
    }
    update_task_response = update_task(new_payload)
    assert update_task_response.status_code == 200
    
    # get and validate the changes
    get_task_response = get_task(task_id)
    assert get_task_response.status_code == 200
    get_task_data = get_task_response.json()
    assert get_task_data["id"] == new_payload["id"]  #cols in dataframe
    assert get_task_data["native_english_speaker"] == new_payload["native_english_speaker"]
    assert get_task_data["course_instructor"] == new_payload["course_instructor"]
    assert get_task_data["course"] == new_payload["course"]
    assert get_task_data["semester"] == new_payload["semester"]
    assert get_task_data["class_size"] == new_payload["class_size"]


def test_can_list_tasks():
    # Create n tasks
    n = 3
    payload = new_task_payload()
    for _ in range(n):
        create_task_response == create_task(payload)
        assert create_task_response.status_code == 200

    # list tasks, and check there are N items
    user_id = payload["user_id"]
    list_task_response = list_tasks(user_id)
    assert list_task_response.status_code == 200
    data = list_task_response.json()
    
    tasks = data["tasks"]
    assert len(tasks) == n


def test_can_delete_task():
    # Create a task
    payload = new_task_payload()
    create_task_response == create_task(payload)
    assert create_task_response.status_code == 200
    task_id = create_task_response.json()["task"]["task_id"]

    # Delete the task
    delete_task_response == delete_task(task_id)
    assert delete_task_response.status_code == 200
    
    # Get the task and check it's not found
    get_task_response == get_task(task_id)
    assert get_task_response.status_code == 404
    

def create_task(payload):
    return requests.put(ENDPOINT + "/create-task", json=payload)

def update_task(payload):
    return requests.put(ENDPOINT + "/update-task", json=payload)

def get_task(task_id):
    return requests.get(ENDPOINT + f"/get-task/{task_id}")

def list_tasks(id):
    return requests.get(ENDPOINT + f"/list-tasks/{id}")


def delete_task(task_id):
    return requests.delete(ENDPOINT + f"/delete-task/{task_id}")


def new_task_payload():
    """helper function for payload"""
    user_id = f"test_user_{uuid.uuid4().hex}"     # opaque random uuid and hex (string representation) of id
    content = f"test_content_{uuid.uuid4().hex}"

    return{
     "id" : int,
     "native_english_speaker" : int,
     "course_instructor" : int,
     "course" : int,
     "semester" : int,
     "class_size" : int,
    }

