# Creating the API with Flask and Python
from flask import Flask, jsonify, request
import user_controller, video_controller
from db import create_tables

app = Flask(__name__)

 # Creating the base route for the user/video
@app.route("/user", methods=["GET"])
def get_users():
    users = user_controller.get_users()
    return jsonify(users)

@app.route("video", methods=["GET"])
def get_videos():
    videos = video_controller.get_videos()
    return jsonify(videos)

# Creating the post route for the user/video
@app.route("/user", methods=["POST"])
def insert_user():
    user_details = request.get_json()
    username = user_details["username"]
    pseudo = user_details["pseudo"]
    email = user_details["email"]
    password = user_details["password"]
    result = user_controller.insert_user(username, pseudo, email, password)
    return jsonify(result)

@app.route("/video", methods=["POST"])
def insert_video():
    video_details = request.get_json()
    name = video_details["name"]
    duration = video_details["duration"]
    user_id = video_details["user_id"]
    source = video_details["source"]
    view = video_details["view"]
    enabled = video_details["enabled"]
    result = video_controller.insert_video(name, duration, user_id, source, view, enabled)
    return jsonify(result)

# Creating the Update route for the user/video
@app.route("/user", methods=["PUT"])
def update_user():
    user_details = request.get_json()
    id = user_details['id']
    username = user_details["username"]
    pseudo = user_details["pseudo"]
    email = user_details["email"]
    result = user_controller.insert_user(id, username, pseudo, email)
    return jsonify(result)


@app.route("/video", methods=["PUT"])
def update_video():
    video_details = request.get_json()
    id = video_details["id"]
    name = video_details["name"]
    duration = video_details["duration"]
    user_id = video_details["user_id"]
    source = video_details["source"]
    view = video_details["view"]
    enabled = video_details["enabled"]
    result = video_controller.insert_video(id, name, duration, user_id, source, view, enabled)
    return jsonify(result)

# Creating the delete route user/video
@app.route("/user/<id>", methods=["DELETE"])
def delete_user(id):
    result = user_controller.delete_user(id)
    return jsonify(result)


@app.route("/video/<id>", methods=["DELETE"])
def delete_video(id):
    result = video_controller.delete_video(id)
    return jsonify(result)

# Creating the get user/video by id
@app.route("/user/<id>", methods=["GET"])
def get_user_by_id(id):
    user = user_controller.get_by_id(id)
    return jsonify(user)


@app.route("/video/<id>", methods=["GET"])
def get_video_by_id(id):
    video = video_controller.get_by_id(id)
    return jsonify(video)


# if the main script is execute run the following
if __name__ == "__main__":
    create_tables()
    app.run(debug=True)