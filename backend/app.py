# app.py

from flask import Flask
from flask_cors import CORS
from views.event_view import *
from flask import Flask, request, jsonify

app = Flask(__name__)
CORS(app)


@app.route('/api/created-event/<string:gmail>', methods=['GET'])
def get_event_created(gmail):
    return get_event_created_view(gmail)
    

@app.route('/api/public-event/<string:gmail>', methods=['GET'])
def get_all_event_public(gmail):
    return get_all_event_public_view(gmail)

@app.route('/api/public-event/<int:event_id>', methods=['GET'])
def get_event_public(event_id):
    event = get_event_public_view(event_id)
    if event:
        return jsonify(event)  
    else:
        return jsonify({"error": "Event not found"}), 404


@app.route('/api/registered-event/<string:gmail>', methods=['GET'])
def get_event_registered(gmail):
    return get_event_registered_view(gmail)

@app.route('/api/past-event/<string:gmail>', methods=['GET'])
def get_event_past(gmail):
    return get_event_past_view(gmail)

@app.route('/api/Login', methods=['GET'])  
def get_users():
    return get_users_view()

@app.route('/api/Login/<gmail>', methods=['GET'])
def get_userinfo_gmail_route(gmail):
    user_login_info = get_users_view_gmail(gmail)  # Gọi hàm controller
    if user_login_info: 
        return jsonify(user_login_info)  
    else:
        return jsonify({"error": "User not found"}), 404
    
@app.route('/api/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    print("Received data:", data)
    
    name = data.get('FullName')
    email = data.get('Gmail')
    phone = data.get('PhoneNumber')
    password = data.get('password')
    createat = data.get('CreatedAt')
    updateat = data.get('UpdatedAt')

    result = add_userinfo_view(name, email, phone, password, createat, updateat)
    
    return jsonify({'message': result}), 201

@app.route('/api/register_event', methods=['POST'])
def event_register():
    data = request.get_json()
    print("Received data:", data)
    
    gmail = data.get('Gmail')
    event_id = data.get('event_id')
    
    # Kiểm tra nếu thiếu dữ liệu đầu vào
    if not gmail or not event_id:
        return jsonify({'message': 'Gmail and EventID are required fields'}), 400

    result = register_event_view(event_id, gmail)
    return jsonify({'message': result}), 201

@app.route('/api/cancelRegistered', methods=['DELETE'])
def cancel_register():
    data = request.get_json()
    print("Received data:", data)
    
    gmail = data.get('Gmail')
    event_id = data.get('event_id')
    
    if not gmail or not event_id:
        return jsonify({'message': 'Gmail and EventID are required fields'}), 400

    result = cancel_register_view(gmail,event_id)
    return jsonify({'message': result}), 201

@app.route('/api/delete_Event', methods=['DELETE'])
def delete_event():
    data = request.get_json()
    print("Received data:", data)
    
    gmail = data.get('Gmail')
    event_id = data.get('event_id')
    
    if not event_id:
        return jsonify({'message': 'EventID are required fields'}), 400

    result = delete_event_view(gmail,event_id)
    return jsonify({'message': result}), 201

@app.route('/api/add_event', methods=['POST'])
def add_event_route():
    data = request.get_json()
    print("Received data:", data)
    
    EventType = data.get('EventType')
    EventName = data.get('EventName')
    StartTime = data.get('StartTime')
    EndTime = data.get('EndTime')
    Location = data.get('Location')
    EventImages = data.get('EventImages')
    Description = data.get('Description')
    RegisteredCount = data.get('RegisteredCount',0)
    MaxAttendees = data.get('MaxAttendees')
    Gmail=data.get('Gmail')
    result = add_event_view(EventType, EventName,StartTime,EndTime,
                         Location,EventImages,Description,RegisteredCount
                         ,MaxAttendees,Gmail)
    return jsonify({'message': result}), 201

@app.route('/api/edit_user', methods=['PUT'])
def edit_user_route():
    data = request.get_json()
    print("Received data:", data)
    
    FullName = data.get('FullName')
    Gmail = data.get('Gmail')
    PhoneNumber = data.get('PhoneNumber')

    # Gọi hàm cập nhật với các tham số đã lấy từ dữ liệu đầu vào
    result = edit_user_view(FullName, Gmail, PhoneNumber)
    
    # Trả về phản hồi với mã trạng thái 200
    return jsonify({'message': result}), 200


@app.route('/api/user_list/<int:event_id>', methods=['GET'])
def get_user_list_regis(event_id):
    event = user_list_view(event_id)
    if event:
        return jsonify(event)  
    else:
        return jsonify({"error": "Event not found"}), 404

@app.route('/api/edit_event', methods=['PUT'])
def edit_event_route():
    data = request.get_json()
    print("Received data:", data)
    
    ID = data.get('ID')
    StartTime = data.get('StartTime')
    EndTime = data.get('EndTime')
    Location = data.get('Location')
    Description = data.get('Description')
    MaxAttendees = data.get('MaxAttendees')

    result = edit_event_view(ID,StartTime,EndTime,Location,Description,MaxAttendees)
    
    # Trả về phản hồi với mã trạng thái 200
    return jsonify({'message': result}), 200


@app.route('/api/send_notification', methods=['POST'])
def send_notification():
    data = request.get_json()
    recipient_email = data.get('recipient_email')
    subject = data.get('subject')
    message = data.get('message')

    # Gửi email
    send_email_view(recipient_email, subject, message)

    return jsonify({"message": "Email sent successfully!"})

@app.route('/api/eventid_regis/<string:gmail>', methods=['GET'])
def get_eventID_regis(gmail):
    return get_eventID_regis_view(gmail)

@app.route('/api/change_password', methods=['PUT'])
def change_password_route():
    data = request.get_json()
    print("Received data:", data)
    
    Password = data.get('Password')
    Gmail = data.get('Gmail')

    result = update_password_view(Password,Gmail)
    
    # Trả về phản hồi với mã trạng thái 200
    return jsonify({'message': result}), 200

@app.route('/api/check_oldPassword/<string:gmail>', methods=['GET'])
def check_oldPassword(gmail):
    return check_oldPassword_view(gmail)


if __name__ == '__main__':
    app.run(debug=True)


