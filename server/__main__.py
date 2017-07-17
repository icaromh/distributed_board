import copy

from jsonrpc import JSONRPCResponseManager, dispatcher
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

messages = []  # The messages list as global variable


@dispatcher.add_method
def post_message(**kwargs):
    """
        Append a message to messges list
    """
    messages.append({
     'name': kwargs.get('name', 'Unknow'),
     'message': kwargs.get('message', ''),
    })

    return "Message appended"


@dispatcher.add_method
def get_messages(**kwargs):
    """
        Copy messages list to a local variable
        Clear messages list
        Return all messages to client
    """
    all_messages = copy.copy(messages)
    del messages[:]
    return all_messages


@Request.application
def application(request):
    response = JSONRPCResponseManager.handle(
        request.data, dispatcher)
    return Response(response.json, mimetype='application/json')


if __name__ == '__main__':
    run_simple('localhost', 4000, application)
