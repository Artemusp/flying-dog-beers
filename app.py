import datetime

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly
from dash.dependencies import Input, Output
import flask
#import dash
#import dash_html_components as html
from flask import  jsonify,abort
#import audiofile

#user = audiofile.user
app = flask.Flask(__name__)
# RPS_DELAY = 0.34 # 1.5 ? audio.py vk_api
@app.route('/')
def index():
    return 'Hello Flask app'


# @server.route('/songs/<string:songName>', methods=['GET'])
# def getSong(songName):
#     songs = []
#     #print("1")
#     response = (user.searchSong(songName,10))
#     #print(2)
#     #print(response)
#     #songs = response.first
#     for j in response:
#         #j["url"] = j["url"]#audiofile.codeSample(j["url"])
#         #print(3)
#         songs.append(j)
#         # break
#     #print(4)
#     return jsonify(songs)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = False
    for j in tasks:
        if j["id"] == task_id:

            task = j
    print(task)
    if not task:
        abort(404)
    return jsonify(task)

if __name__ == '__main__':
    app.run()




# @server.route('/todo/api/v1.0/test')
# def get_test():
#     tests= Post.query.filter_by(author=current_user).all()
#     return jsonify(tests)
