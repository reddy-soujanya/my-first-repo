from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage
users = {}

# Helper function to save data to file
def save_to_file():
    with open('users.json', 'w') as f:
        import json
        json.dump(users, f)

# Helper function to load data from file
def load_from_file():
    try:
        with open('users.json', 'r') as f:
            import json
            global users
            users = json.load(f)
    except FileNotFoundError:
        pass

# Load existing data
load_from_file()

@app.route('/users', methods=['GET'])
def get_all_users():
    return jsonify(users), 200

@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    user_id = str(len(users) + 1)
    if 'name' in data and 'email' in data:
        users[user_id] = {
            "name": data['name'],
            "email": data['email']
        }
        save_to_file()
        return jsonify({"id": user_id}), 201
    return jsonify({"error": "Name and email are required"}), 400

@app.route('/users/<user_id>', methods=['PUT'])
def update_user(user_id):
    if user_id in users:
        data = request.json
        users[user_id].update(data)
        save_to_file()
        return jsonify(users[user_id]), 200
    return jsonify({"error": "User not found"}), 404

@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    if user_id in users:
        del users[user_id]
        save_to_file()
        return jsonify({"message": "User deleted"}), 200
    return jsonify({"error": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
