from todowrapper import TODOABLE
from pytest import fixture


@fixture
def todoable_keys():
    # Responsible only for returning the test data
    return {
        "username": "your username",
        "password": "your password",
        "token": "your token id",
        "list_id": "your list id",
        "add_list_name": "your list name",
        "update_list_name": "Updated list name",
        "add_task_name": "Name of the task",
        "item_id": "your item id"
    }

def test_login(todoable_keys):
    """
    Test API Call for login
    """

    username = todoable_keys.get('username')
    password = todoable_keys.get('password')
    response = TODOABLE.login(username, password)

    assert isinstance(response, dict)
    assert response.get('token') != None

def test_get_lists(todoable_keys):
    """
    Test API Call for get_list
    """

    token = todoable_keys.get('token')
    response = TODOABLE.get_lists(token)

    assert isinstance(response, dict)
    assert response.get('lists') != None

def test_post_list(todoable_keys):
    """
    Test API Call for post_list
    """

    token = todoable_keys.get('token')
    name = todoable_keys.get('add_list_name')
    response = TODOABLE.post_list(token, name)

    assert isinstance(response, dict)
    assert response.get('name') != None


def test_get_list_tasks(todoable_keys):
    """
    Test API Call for get_list_tasks
    """

    token = todoable_keys.get('token')
    list_id = todoable_keys.get('list_id')
    response = TODOABLE.get_list_tasks(token, list_id)

    assert isinstance(response, dict)
    assert response.get('items') != None

def test_update_list(todoable_keys):
    """
    Test API Call for update_list
    """

    token = todoable_keys.get('token')
    list_id = todoable_keys.get('list_id')
    name = todoable_keys.get('update_list_name')
    response = TODOABLE.update_list(token, list_id, name)

    assert isinstance(response, str)
    assert response == 'list updated'


def test_post_task_in_list(todoable_keys):
    """
    Test API Call for post_task_in_list
    """

    token = todoable_keys.get('token')
    list_id = todoable_keys.get('list_id')
    name = todoable_keys.get('add_task_name')
    response = TODOABLE.post_task_in_list(token, list_id, name)

    assert isinstance(response, dict)
    assert response.get('name') != None


def test_complete_task_in_list(todoable_keys):
    """
    Test API Call for test_complete_task_in_list
    """

    token = todoable_keys.get('token')
    list_id = todoable_keys.get('list_id')
    item_id = todoable_keys.get('item_id')
    response = TODOABLE.complete_task_in_list(token, list_id, item_id)

    assert isinstance(response, str)
    assert response == 'marked finished'


def test_delete_task_in_list(todoable_keys):
    """
    Test API Call for delete_task_in_list
    """

    token = todoable_keys.get('token')
    list_id = todoable_keys.get('list_id')
    item_id = todoable_keys.get('item_id')
    response = TODOABLE.delete_task_in_list(token, list_id, item_id)

    assert isinstance(response, str)
    assert response == 'item deleted'



def test_delete_list(todoable_keys):
    """
    Test API Call for delete_list
    """

    token = todoable_keys.get('token')
    list_id = todoable_keys.get('list_id')
    response = TODOABLE.delete_list(token, list_id)

    assert isinstance(response, str)
    assert response == 'list deleted'
