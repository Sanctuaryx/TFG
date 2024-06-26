import sqlite3
import os

# Function to insert data into hands table
def insert_hand(cursor, roll, pitch, yaw, finger1, finger2, finger3, finger4, finger5, gyro1, gyro2, gyro3, accel1, accel2, accel3, calib1, calib2, calib3, calib4):
    cursor.execute('''
    INSERT INTO hands (roll, pitch, yaw, finger1, finger2, finger3, finger4, finger5, gyro1, gyro2, gyro3, accel1, accel2, accel3, calib1, calib2, calib3, calib4)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (roll, pitch, yaw, finger1, finger2, finger3, finger4, finger5, gyro1, gyro2, gyro3, accel1, accel2, accel3, calib1, calib2, calib3, calib4))
    return cursor.lastrowid

# Function to insert data into gestures table
def insert_gesture(cursor, name, left_hand_id, right_hand_id):
    cursor.execute('''
    INSERT INTO gestures (name, left_hand_id, right_hand_id)
    VALUES (?, ?, ?)
    ''', (name, left_hand_id, right_hand_id))

def create_tables(cursor):
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS hands (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        roll REAL,
        pitch REAL,
        yaw REAL,
        finger1 INTEGER,
        finger2 INTEGER,
        finger3 INTEGER,
        finger4 INTEGER,
        finger5 INTEGER,
        mean_acceleration REAL,
        td_acceleration REAL,
        mean_angular_velocity REAL,
        std_angular_velocity REAL,
        gyro_axis INTEGER,
        accel_axis INTEGER,
    )
    ''')
    
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS gestures (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        left_hand_id INTEGER,
        right_hand_id INTEGER,
        FOREIGN KEY (left_hand_id) REFERENCES hands(id),
        FOREIGN KEY (right_hand_id) REFERENCES hands(id)
    )
    ''')
    
def setup_data():
    return [
        {
            "name": "gesture_1_STATIC",
            "left_hand": (2.0, 2.0, 2.0, 2, 2, 2, 2, 2, 0.0, 0.0, 0.0, 0.0, 0, 0),
            "right_hand": (2.0, 2.0, 2.0, 2, 2, 2, 2, 2, 0.0, 0.0, 0.0, 0.0, 0, 0)
        },
        
        {
            "name": "gesture_100_DYNAMIC",
            "left_hand": (3.0, 3.0, 3.0, 3, 3, 3, 3, 3, 3.0, 3.0, 3.0, 3.0, 2, 2),
            "right_hand": (3.0, 3.0, 3.0, 3, 3, 3, 3, 3, 0.0, 0.0, 0.0, 0.0, 0, 0)
        }
    ]

def setup_database():
    # Specify the directory where you want to store the database file
    database_dir = '../../resources/SQL/int_dataBase'
    database_file = 'gestures.db'
    database_path = os.path.join(database_dir, database_file)
    
    os.makedirs(database_dir, exist_ok=True)
    conn = sqlite3.connect(database_path)
    cursor = conn.cursor()

    create_tables(cursor)
    data = setup_data()
    
    for row in data:
        name = row["name"]
        left_hand_data = row["left_hand"]
        right_hand_data = row["right_hand"]
        
        left_hand_id = insert_hand(cursor, *left_hand_data)
        right_hand_id = insert_hand(cursor, *right_hand_data)
        
        insert_gesture(cursor, name, left_hand_id, right_hand_id)
    
    conn.commit()
    conn.close()

    print(f"Database and tables created successfully at {database_path}.")

if __name__ == '__main__':
    setup_database()
