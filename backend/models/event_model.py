# models/event_model.py

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


def get_all_event_Public():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM eventsdetail WHERE EventType = 'PL'")
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

def register_event(event_id, gmail):
    conn = get_db_connection() 
    cursor = conn.cursor(dictionary=True)
    
    try:
        query = """
        INSERT INTO eventregistrations (Gmail, EventID)
        VALUES (%s, %s)
        """
        cursor.execute(query, (gmail, event_id))  
        conn.commit() 
        return "event registered successfully"
    except Exception as e:
        conn.rollback() 
        return f"Failed to registered event: {e}"
    finally:
        cursor.close()
        conn.close()  
