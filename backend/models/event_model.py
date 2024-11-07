# models/event_model.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import get_db_connection

def get_all_event_created(gmail):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute(
        """SELECT * 
        FROM eventsdetail 
        JOIN eventcreators ON eventcreators.EventID = eventsdetail.ID 
        WHERE eventcreators.gmail = %s""",(gmail,))
    events = cursor.fetchall()
    cursor.close()
    conn.close()
    return events

def get_users():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM userinfo")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users
def get_users_gmail_model(gmail):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM userinfo WHERE Gmail=%s", (gmail,))
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users if users else None

def add_userinfo_model(name, email, phone, password, createat, updateat):
    conn = get_db_connection()  # Kiểm tra kết nối với cơ sở dữ liệu
    cursor = conn.cursor()
    check_query = "SELECT * FROM userinfo WHERE Gmail = %s"
    cursor.execute(check_query, (email,))
    existing_user = cursor.fetchone()  # Lấy một kết quả nếu tồn tại

    if existing_user:
        cursor.close()
        conn.close()
        return "Email already exists" 
    
    query = """
    INSERT INTO userinfo (FullName, Gmail, PhoneNumber, CreatedAt, UpdatedAt, password)
    VALUES (%s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (name, email, phone, createat, updateat, password))
    conn.commit()
    cursor.close()
    conn.close()
    return "User added successfully"

def get_all_event_registered(gmail):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        """SELECT * 
        FROM eventsdetail 
        JOIN eventregistrations ON eventregistrations.EventID = eventsdetail.ID 
        WHERE eventregistrations.gmail = %s""",(gmail,))
    
    events = cursor.fetchall()
    cursor.close()
    conn.close()
    return events

def get_all_event_past(gmail):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        """SELECT DISTINCT eventsdetail.* 
            FROM eventsdetail
            LEFT JOIN eventcreators ON eventcreators.EventID = eventsdetail.ID
            LEFT JOIN eventregistrations ON eventregistrations.EventID = eventsdetail.ID
            WHERE eventcreators.gmail = %s  
            OR eventregistrations.gmail = %s
            """,(gmail,gmail,))
    events = cursor.fetchall()
    cursor.close()
    conn.close()
    return events


def get_all_event_Public(gmail):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    # cursor.execute("SELECT * FROM eventsdetail WHERE EventType = 'PL'")
    cursor.execute("""
                        SELECT DISTINCT eventsdetail.*
                        FROM eventsdetail 
                        WHERE eventsdetail.EventType = 'PL'
                        AND NOT EXISTS (
                            SELECT 1 
                            FROM eventcreators 
                            WHERE eventcreators.EventID = eventsdetail.ID 
                            AND eventcreators.Gmail = %s
                        )
                        AND NOT EXISTS (
                            SELECT 1 
                            FROM eventregistrations 
                            WHERE eventregistrations.EventID = eventsdetail.ID 
                            AND eventregistrations.Gmail = %s
                        );
                    """,(gmail,gmail,))
    events = cursor.fetchall()
    cursor.close()
    conn.close()
    return events

def get_event_Public(event_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM eventsdetail WHERE  ID=%s",(event_id,))
    events = cursor.fetchall()
    cursor.close()
    conn.close()
    return events

# def register_event(event_id, gmail):
#     conn = get_db_connection() 
#     cursor = conn.cursor(dictionary=True)
    
#     try:
#         query = """
#         INSERT INTO eventregistrations (Gmail, EventID)
#         VALUES (%s, %s)
#         """
#         cursor.execute(query, (gmail, event_id))  
#         conn.commit() 
#         return "event registered successfully"
#     except Exception as e:
#         conn.rollback() 
#         return f"Failed to registered event: {e}"
#     finally:
#         cursor.close()
#         conn.close()  
def register_event(event_id, gmail):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        # Bước 1: Thêm bản ghi vào bảng eventregistrations
        insert_query = """
        INSERT INTO eventregistrations (Gmail, EventID)
        VALUES (%s, %s)
        """
        cursor.execute(insert_query, (gmail, event_id))
        
        # Bước 2: Cập nhật RegisteredCount trong bảng eventsdetail
        update_query = """
        UPDATE eventsdetail
        SET RegisteredCount = RegisteredCount + 1
        WHERE ID = %s
        """
        cursor.execute(update_query, (event_id,))
        
        conn.commit()
        return "Event registered successfully"
    except Exception as e:
        conn.rollback()
        return f"Failed to register event: {e}"
    finally:
        cursor.close()
        conn.close()

def cancel_register_event(gmail,event_id):
    conn = get_db_connection() 
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = """
        DELETE FROM eventregistrations
        WHERE Gmail = %s AND EventID = %s;
        """
        cursor.execute(query, (gmail, event_id))  
        
        update_query = """
        UPDATE eventsdetail
        SET RegisteredCount = RegisteredCount - 1
        WHERE ID = %s
        """
        cursor.execute(update_query, (event_id,))
        
        conn.commit() 
        return "cancel registered successfully"
    except Exception as e:
        conn.rollback() 
        return f"Failed to cancel registered event: {e}"
    finally:
        cursor.close()
        conn.close()  

def delete_event(gmail,event_id):
    conn = get_db_connection() 
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = """
        DELETE FROM eventcreators
        WHERE Gmail = %s AND EventID = %s;
        """
        cursor.execute(query, (gmail, event_id))  
        conn.commit() 
        return "event deleted successfully"
    except Exception as e:
        conn.rollback() 
        return f"Failed to delete event: {e}"
    finally:
        cursor.close()
        conn.close()  


def add_event(EventType, EventName,StartTime,EndTime,Location,EventImages,Description,RegisteredCount,MaxAttendees,Gmail):
    conn = get_db_connection() 
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = """
        INSERT INTO eventsdetail (EventType, EventName, 
        StartTime, EndTime, Location, EventImages, Description, RegisteredCount, MaxAttendees)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (EventType, EventName,StartTime,EndTime,Location,EventImages,Description,RegisteredCount,MaxAttendees))  
        
        # Get the ID of the newly inserted event
        event_id = cursor.lastrowid
        
        # Insert into eventcreators table
        creator_query = """
        INSERT INTO eventcreators (Gmail, EventID)
        VALUES (%s, %s)
        """
        cursor.execute(creator_query, (Gmail, event_id))
        
        conn.commit() 
        return "event added successfully"
    except Exception as e:
        conn.rollback() 
        return f"Failed to add event: {e}"
    finally:
        cursor.close()
        conn.close() 
        
        
def edit_info_user(FullName,Gmail,PhoneNumber):
    conn = get_db_connection() 
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = """
        UPDATE userinfo
        SET FullName = %s, PhoneNumber = %s
        WHERE Gmail = %s;
        """
        cursor.execute(query, (FullName, PhoneNumber, Gmail))  
        
        conn.commit() 
        return "user updated successfully"
    except Exception as e:
        conn.rollback() 
        return f"Failed to update user: {e}"
    finally:
        cursor.close()
        conn.close() 
        
        
def get_list_regis(event_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    try:
        cursor.execute("""
            SELECT userinfo.FullName, userinfo.Gmail, userinfo.PhoneNumber
            FROM userinfo
            LEFT JOIN eventregistrations ON eventregistrations.Gmail = userinfo.Gmail
            WHERE eventregistrations.EventID = %s
            """, (event_id,))
        lists = cursor.fetchall()
        return lists
    except Exception as e:
        print(f"Error retrieving registrations: {e}")
        return []
    finally:
        cursor.close()
        conn.close()
        
def edit_info_event(ID,StartTime,EndTime,Location,Description,MaxAttendees):
    conn = get_db_connection() 
    cursor = conn.cursor(dictionary=True)
    
    try:
        # query = """
        # UPDATE eventsdetail
        # SET EventType = %s, EventName = %s,StartTime = %s, EndTime = %s,
        #     Location = %s, EventImages = %s,Description = %s, MaxAttendees = %s
        # WHERE ID = %s;
        # """
        
        query = """
        UPDATE eventsdetail
        SET StartTime = %s, EndTime = %s,
            Location = %s, Description = %s, MaxAttendees = %s
        WHERE ID = %s;
        """
        cursor.execute(query, (StartTime,EndTime,Location,Description,MaxAttendees,ID))  
        
        conn.commit() 
        return "event updated successfully"
    except Exception as e:
        conn.rollback() 
        return f"Failed to update event: {e}"
    finally:
        cursor.close()
        conn.close() 
        
        
def send_email(recipient_email, subject, message):
    sender_email = "bot134mail@gmail.com"
    sender_password = "ycmm fhko zfej slps"

    # Tạo đối tượng email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject

    # Gắn nội dung email
    msg.attach(MIMEText(message, 'plain'))

    try:
        # Kết nối tới máy chủ Gmail 
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.set_debuglevel(1)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        print("Email đã được gửi thành công.")
    except Exception as e:
        print(f"Lỗi khi gửi email: {e}")
    finally:
        server.quit()
        
def get_eventID_regis(gmail):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        """
        SELECT eventregistrations.EventID 
        from eventregistrations 
        where eventregistrations.Gmail="bob@example.com";
        WHERE eventregistrations.gmail = %s""",(gmail,))
    
    events = cursor.fetchall()
    cursor.close()
    conn.close()
    return events