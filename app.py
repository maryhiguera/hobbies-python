from flask import Flask, request
import db

app = Flask(__name__)


@app.route("/hobbies.json")
def index():
    return db.hobbies_all()

@app.route("/hobbies.json", methods=["POST"])
def create():
    name = request.args.get("name")
    location = request.args.get("location")
    description = request.args.get("description")
    return db.hobbies_create(name, location, description)

@app.route("/hobbies/<id>.json")
def show(id):
    return db.hobbies_find_by_id(id)

@app.route("/hobbies/<id>.json", methods=["PATCH"])
def update(id):
    hobbie = db.hobbies_find_by_id(id)
    name = request.args.get("name") or hobbie["name"]
    location = request.args.get("location") or hobbie["location"]
    description = request.args.get("description") or hobbie["description"]
    return db.hobbies_update_by_id(id, name, location, description)

@app.route("/hobbies/<id>.json", methods=["DELETE"])
def destroy(id):
    return db.hobbies_destroy_by_id(id)