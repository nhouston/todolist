import uuid
from flask import Flask, jsonify, request
from flask_cors import CORS


LIST = [
    {
        'id': uuid.uuid4().hex,
        'title': 'Finish App',
        'complete': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'upload to Github',
        'complete': True
    },
]


# configuration
DEBUG = True

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

def remove_item(list_id):
    for listItem in LIST:
        if listItem['id'] == list_id:
            LIST.remove(listItem)
            return True
    return False


@app.route('/items', methods=['GET', 'POST'])
def all_list_items():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        LIST.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'complete': post_data.get('complete')
        })
        response_object['message'] = 'List Item added!'
    else:
        response_object['list'] = LIST
    return jsonify(response_object)


@app.route('/items/<list_id>', methods=['PUT', 'DELETE'])
def single_list_item(list_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_item(list_id)
        LIST.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'complete': post_data.get('complete')
        })
        response_object['message'] = 'List updated!'
    if request.method == 'DELETE':
        remove_item(list_id)
        response_object['message'] = 'List removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()