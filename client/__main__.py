import requests
import json
import sys


def run():
    """
        Usage:
        python client "{username}" "{message}"
    """
    url = "http://localhost:4000/jsonrpc"
    headers = {'content-type': 'application/json'}

    payload = {
        "method": "post_message",
        "params": {
            'name': sys.argv[1],
            'message': sys.argv[2]
        },
        "jsonrpc": "2.0",
        "id": 0,
    }

    response = requests.post(
        url, data=json.dumps(payload), headers=headers).json()

    print(response)

if __name__ == "__main__":
    run()
