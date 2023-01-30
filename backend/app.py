from flask import Flask, render_template, jsonify,request
import json
app = Flask(__name__)

with open('example.JSON', 'r') as file:
    data = json.load(file)
@app.route('/',methods=['GET'])
def home():
    return render_template('b.html')


@app.route('/data', methods=['GET'])
def get_data():
    #with open('example.JSON') as json_file:
   #     data = json.load(json_file)
    return jsonify(data)

@app.route('/data', methods=['POST'])
def update_data():
    data = request.get_json()
    with open('example.JSON', 'w') as json_file:
        json.dump(data, json_file)
    return jsonify({'message': 'Data updated successfully'})

@app.route('/data/<key>', methods=['PATCH'])
def update_data_key(key):
    new_value = request.get_json()['value']
    data[key] = new_value
    with open('example.JSON', 'w') as file:
        json.dump(data, file)
    return jsonify(data) 

if __name__ == "__main__":
    app.run(debug=True)
