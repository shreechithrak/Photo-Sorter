from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

from Photo_sort_master.face_dataset_creator import main as photosort
app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')

def index():
    return render_template('2.html')

@app.route("/camera",methods=['POST'])
def camera():
    data = request.json
    name = data.get('name')
    # Process the received name here, for example:
    status = photosort(name)
    return jsonify({'message': 'Received name: ' + status})


if __name__ == '__main__':
    app.run(debug=True)
