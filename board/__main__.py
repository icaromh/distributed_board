from time import sleep
import requests
import json


def get_messages():
    """
        Request for messages to the server via JSON-RPC
        Return the messages list
    """
    url = "http://localhost:4000/jsonrpc"
    headers = {'content-type': 'application/json'}

    payload = {
        "method": "get_messages",  # method to call in server
        "jsonrpc": "2.0",
        "id": 1,
    }

    response = requests.post(
        url, data=json.dumps(payload), headers=headers
    ).json()

    return response


def print_message(data):
    """
        Format message to show in console
        the format is {name}: {message}
    """
    name = data.get('name')
    message = data.get('message')
    print(f'{name}: {message}')


def run():
    """
        Run the Mural main function
        get messages each 10 seconds
    """
    while True:
        res = get_messages()

        for data in res.get('result'):
            print_message(data)

        sleep(10)  # in sec


if __name__ == '__main__':
    run()
