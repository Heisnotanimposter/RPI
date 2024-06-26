from flask import Flask, request, jsonify

app = Flask(__name__)
data_store = []

@app.route('/data', methods=['POST'])
def receive_data():
    data = request.json
    data_store.append(data)
    return jsonify(success=True)

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data_store)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)