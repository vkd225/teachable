from todowrapper import TODOABLE
import json
import logging

logger = logging.getLogger()
logging.basicConfig()
logger.setLevel(logging.INFO)

def login(event):
    user = event.get('username', None)
    pwd = event.get('password', None)
    response = TODOABLE.login(user, pwd)
    return (response)

def get_lists(event):
    token = event.get('token', None)
    response = TODOABLE.get_lists(token)
    return (response)

def post_list(event):
    token = event.get('token', None)
    name = event.get('name', None)
    response = TODOABLE.post_list(token, name)
    return (response)

def get_list_tasks(event):
    token = event.get('token', None)
    list_id = event.get('list_id', None)
    response = TODOABLE.get_list_tasks(token, list_id)
    return (response)

def update_list(event):
    token = event.get('token', None)
    list_id = event.get('list_id', None)
    name = event.get('name', None)
    response = TODOABLE.update_list(token, list_id, name)
    return (response)

def delete_list(event):
    token = event.get('token', None)
    list_id = event.get('list_id', None)
    response = TODOABLE.delete_list(token, list_id)
    return (response)

def post_task_in_list(event):
    token = event.get('token', None)
    list_id = event.get('list_id', None)
    name = event.get('name', None)
    response = TODOABLE.post_task_in_list(token, list_id, name)
    return (response)

def complete_task_in_list(event):
    token = event.get('token', None)
    list_id = event.get('list_id', None)
    item_id = event.get('item_id', None)
    response = TODOABLE.complete_task_in_list(token, list_id, item_id)
    return (response)

def delete_task_in_list(event):
    token = event.get('token', None)
    list_id = event.get('list_id', None)
    item_id = event.get('item_id', None)
    response = TODOABLE.delete_task_in_list(token, list_id, item_id)
    return (response)

def lambda_handler(event, context):
    '''
    Lambda function triggered with correct function name and parameters.
    '''
    dispatcher={
        'login':login,
        'get_lists':get_lists,
        'post_list':post_list,
        'get_list_tasks':get_list_tasks,
        'update_list':update_list,
        'delete_list':delete_list,
        'post_task_in_list':post_task_in_list,
        'complete_task_in_list':complete_task_in_list,
        'delete_task_in_list':delete_task_in_list
    }

    function_name = event.get('function')
    try:
        response = dispatcher[function_name](event)
        print (response)
        print (type (response))
        return {'response':response}

    except KeyError:
        raise ValueError('invalid input')


# Entry point for testing
if __name__ == '__main__':
    with open('test_event.json', 'r') as f_in:
        test_event = json.load(f_in)

    response = lambda_handler(test_event,'')
    logger.info(response)