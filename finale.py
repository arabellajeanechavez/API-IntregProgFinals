from flask import Flask, jsonify, request
from flask_pymongo import PyMongo
from flask import request
from bson import ObjectId
import json
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bcrypt import Bcrypt  


app = Flask(__name__)


# MongoDB connection
app.config['MONGO_URI'] = 'mongodb://localhost:27017/FinalExam'
app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'
mongo = PyMongo(app)

bcrypt = Bcrypt(app)

jwt = JWTManager(app)

# MY METHODS
@app.route('/ngos/barangay-records', methods=['GET'])
@jwt_required()
def get_ngos_barangay_records():
    
    current_user = get_jwt_identity()
    barangay_records = list(mongo.db.Barangay.find({}, {'_id': False}))

    print(barangay_records)

    return jsonify(barangay_records)

@app.route('/ngos/evacuation-centers', methods=['GET'])
@jwt_required()
def get_ngos_evacuation_centers():
    current_user = get_jwt_identity()
    evacuation_centers = list(mongo.db.evacuation_centers.find({}, {'_id': False}))
    return jsonify(evacuation_centers)

# GET endpoint to retrieve barangay data
@app.route('/barangay', methods=['GET'])
@jwt_required()
def get_barangay_records():
    current_user = get_jwt_identity()
    barangay_records = list(mongo.db.Barangay.find({}, {'_id': False}))
    return jsonify(barangay_records)

# PUT endpoint to update barangay records
@app.route('/barangay/update-records', methods=['PUT'])
@jwt_required()
def update_barangay_records():
    current_user = get_jwt_identity()
    try:
        data = request.get_json()
        barangay_id = data.get('BarangayID')
        updated_field = data.get('UpdatedField')
        new_value = data.get('NewValue')

        if not barangay_id or not updated_field or new_value is None:
            return jsonify({'error': 'Missing required fields'}), 400

        # Here will update in MongoDB using BarangayID
        result = mongo.db.Barangay.update_one(
            {"BarangayID": barangay_id},
            {"$set": {updated_field: new_value}}
        )

        if result.matched_count == 0:
            return jsonify({'error': 'No matching record found'}), 404

        return jsonify({'message': 'Record updated successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

# POST endpoint to /barangay/update-situation
@app.route('/barangay/update-situation', methods=['PUT'])
@jwt_required()
def update_barangay_situation():
    try:
        current_user = get_jwt_identity()
        data = request.get_json()
        barangay_id = data.get('BarangayID')
        updated_field = data.get('UpdatedField')
        new_value = data.get('NewValue')

        if not barangay_id or not updated_field or new_value is None:
            return jsonify({'error': 'Missing required fields'}), 400

        result = mongo.db.Barangay.update_one(
            {"BarangayID": barangay_id},
            {"$set": {updated_field: new_value}}
        )

        return jsonify({'message': 'Barangay situation updated successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

        print("Received Data:", data)
        print("MongoDB Update Result:", result.raw_result)

        if result.matched_count == 0:
            return jsonify({'error': 'No matching record found'}), 404

        return jsonify({'message': 'Barangay situation updated successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
# POST endpoint to update-disaster-status
@app.route('/institutions/update-disaster-status', methods=['PUT'])
@jwt_required()
def update_disaster_status():
    current_user = get_jwt_identity()
    try:
        data = request.get_json()
        print("Received Data:", data)  
        disaster_id = data.get('disasterID')
        new_status = data.get('status')

        
        result = mongo.db.Institution.update_one(
            {"disasterID": disaster_id},
            {"$set": {"status": new_status}}
        )

        print("MongoDB Update Result:", result.raw_result)  

        if result.matched_count == 0:
            return jsonify({'error': 'Disaster not found'}), 404

        if result.modified_count == 0:
            return jsonify({"error": "No changes applied"}), 404

        return jsonify({'message': 'Disaster status updated successfully'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500



# POST endpoint for feedback and reporting
@app.route('/institutions/feedback-and-reporting', methods=['POST'])
@jwt_required()
def feedback_and_reporting():
    current_user = get_jwt_identity()
    data = request.get_json()
   
    feedback_reports_collection = mongo.db.feedback_reports
   
    result = feedback_reports_collection.insert_one(data)

    if result.inserted_id:
        return jsonify({"message": "Feedback/report submitted successfully"}), 201
    else:
        return jsonify({"error": "Failed to submit feedback/report"}), 500

    

# DELETE endpoint para to delete barangay information
@app.route('/barangay/delete-information', methods=['DELETE'])
@jwt_required()
def delete_barangay_information():
    current_user = get_jwt_identity()
    data = request.get_json()
    barangay_id = data.get('BarangayID')

    
    result = mongo.db.Barangay.delete_one({"BarangayID": barangay_id})

    if result.deleted_count > 0:
        return jsonify({"message": "Barangay information deleted successfully"})
    else:
        return jsonify({"error": "Barangay not found"}), 404
    

# POST endpoint to add a new barangay
@app.route('/ngos/add-barangay', methods=['POST'])
@jwt_required()
def add_barangay():
    try:
        data = request.get_json()

        # Ensure required fields are provided
        required_fields = ['BarangayID', 'Population', 'Households', 'VulnerabilityAssessment']
        for field in required_fields:
            if field not in data:
                return jsonify({'error': f'{field} is required'}), 400

        # Check if BarangayID already exists
        existing_barangay = mongo.db.Barangay.find_one({'BarangayID': data['BarangayID']})
        if existing_barangay:
            return jsonify({'error': 'BarangayID already exists'}), 409

        # Insert new barangay into MongoDB
        result = mongo.db.Barangay.insert_one(data)

        if result.inserted_id:
            return jsonify({'message': 'Barangay added successfully'}), 201
        else:
            return jsonify({'error': 'Failed to add barangay'}), 500

    except Exception as e:
        return jsonify({'error': str(e)}), 500


#USERS
# Registration endpoint
@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    data['password'] = hashed_password
    result = mongo.db.USERS.insert_one(data)

    if result.inserted_id:
        return jsonify({"message": "User registered successfully"}), 201
    else:
        return jsonify({"error": "Failed to register user"}), 500

# Login endpoint
@app.route('/login', methods=['POST'])
def login_user():
    data = request.get_json()
    user = mongo.db.USERS.find_one({"username": data['username']})

    if user:
        stored_hashed_password = user.get('password', '')
        if stored_hashed_password and bcrypt.check_password_hash(stored_hashed_password, data['password']):
            # Create access token
            access_token = create_access_token(identity=str(user['_id']))
            return jsonify(access_token=access_token), 200
        else:
            print("Password mismatch or invalid stored hash method")
            return jsonify({"error": "Invalid username or password"}), 401
    else:
        print("User not found")
        return jsonify({"error": "Invalid username or password"}), 401
# Example protected route using JWT (unchanged)
@app.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200
















if __name__ == '__main__':
    app.run(debug=True)


