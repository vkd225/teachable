from __future__ import print_function
import requests
import json

base_url = 'https://todoable.teachable.tech/api'

class TODOABLE(object):
    def __init__(self):
        pass

    def login(username, password):

        '''
        Login into todoable.
        usage: todoable.login(username, password)
        '''

        headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
        url = base_url + '/authenticate'
        response = requests.post(url=url, headers=headers, auth=(username, password))
        if response.status_code == 200:
            return (response.json())
        else:
            return ('invalid credentials')


    def get_lists(token):

        '''
        Get Todoable lists.
        usage: todoable.get_lists(token)
        '''

        headers = {
                'Content-Type': 'application/json',
                'Accept': 'application/json',
                'Authorization': 'Token token={}'.format(token)
                }
        url = base_url + '/lists'
        response = requests.get(url=url, headers=headers)

        if response.status_code == 200:
            return (response.json())
        else:
            return ('invalid token')


    def post_list(token, name):

        '''
        Post a Todoable list.
        usage: todoable.post_lists(token, name)
        '''

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Token token={}'.format(token)
            }
        url = base_url + '/lists'

        data = {
            "list": {
                "name": name
            }
        }
        response = requests.post(url=url, headers=headers, json=data)

        if response.status_code == 201:
            return (response.json())
        elif response.status_code == 401:
            return ('invalid token')
        else:
            return ('list name already used')


    def get_list_tasks(token, list_id):

        '''
        get a Todoable list items.
        usage: todoable.get_list_items(token, list_id)
        '''

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Token token={}'.format(token)
            }
        url = base_url + '/lists/' + list_id

        response = requests.get(url=url, headers=headers)

        if response.status_code == 200:
            return (response.json())
        elif response.status_code == 401:
            return ('invalid token')
        else:
            return ('invalid list id')


    def update_list(token, list_id, name):

        '''
        Updates a Todoable list.
        usage: todoable.update_list(token, list_id, new_name)
        '''

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Token token={}'.format(token)
            }
        url = base_url + '/lists/' + list_id
        data = {
            "list": {
                "name": name
            }
        }

        response = requests.patch(url=url, headers=headers, json=data)

        if response.status_code == 200:
            return ('list updated')
        elif response.status_code == 401:
            return ('invalid token')
        else:
            return ('invalid list id')


    def delete_list(token, list_id):

        '''
        Deletes a Todoable list.
        usage: todoable.delete_list(token, list_id)
        '''

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Token token={}'.format(token)
            }
        url = base_url + '/lists/' + list_id

        response = requests.delete(url=url, headers=headers)

        if response.status_code == 204:
            return ('list deleted')
        elif response.status_code == 401:
            return ('invalid token')
        else:
            return ('invalid list id')


    def post_task_in_list(token, list_id, name):

        '''
        Post an item inside a Todoable list.
        usage: todoable.post_task_in_list(token, list_id, task_name)
        '''

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Token token={}'.format(token)
            }
        url = base_url + '/lists/' + list_id + '/items'

        data = {
            "item": {
                "name": name
            }
        }
        response = requests.post(url=url, headers=headers, json=data)

        if response.status_code == 201:
            return (response.json())
        elif response.status_code == 401:
            return ('invalid token')
        else:
            return ('invalid input')


    def complete_task_in_list(token, list_id, item_id):

        '''
        Mark an item inside a Todoable list as done.
        usage: todoable.post_lists(token, list_id, task_id)
        '''

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Token token={}'.format(token)
            }
        url = base_url + '/lists/' + list_id + '/items/' + item_id +'/finish'

        response = requests.put(url=url, headers=headers)

        if response.status_code == 200:
            return ('marked finished')
        elif response.status_code == 401:
            return ('invalid token')
        else:
            return ('Already marked as done')

    def delete_task_in_list(token, list_id, item_id):

        '''
        Delete an item inside a Todoable list.
        usage: todoable.post_lists(token, list_id, task_id)
        '''

        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Authorization': 'Token token={}'.format(token)
            }
        url = base_url + '/lists/' + list_id + '/items/' + item_id

        response = requests.delete(url=url, headers=headers)

        print ('response: ', response)

        if response.status_code == 204:
            return ('item deleted')
        elif response.status_code == 401:
            return ('invalid token')
        else:
            return ('Already marked as done')
