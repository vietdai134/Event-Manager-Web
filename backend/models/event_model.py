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

def get_all_event_registered():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        """SELECT * 
        FROM eventsdetail 
        JOIN eventregistrations ON eventregistrations.EventID = eventsdetail.ID 
        WHERE eventregistrations.gmail = 'alice@example.com'""")
    events = cursor.fetchall()
    cursor.close()
    conn.close()
    return events

def get_all_event_past():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        """SELECT DISTINCT eventsdetail.* 
            FROM eventsdetail
            LEFT JOIN eventcreators ON eventcreators.EventID = eventsdetail.ID
            LEFT JOIN eventregistrations ON eventregistrations.EventID = eventsdetail.ID
            WHERE eventcreators.gmail = "alice@example.com" 
            OR eventregistrations.gmail = 'alice@example.com';
            """)
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