# import mysql.connector
# import json

# # Database Connection
# # Database Connection
# conn = mysql.connector.connect(
#     database="ramya",  # Changed from dbname to database
#     user="root",
#     password="ramci@2003R",
#     host="localhost",
#     port=3306  # You can also pass this as an integer
# )
# cur = conn.cursor()

# # Insert data into database
# def insert_data(json_data):
#     data = json.loads(json_data)
    
#     # Insert patient data
#     cur.execute("INSERT INTO patients (name, dob) VALUES (%s, %s) RETURNING id;",
#                 (data["patient_name"], data["dob"]))
#     patient_id = cur.fetchone()[0]

#     # Insert JSON data into forms_data table
#     cur.execute("INSERT INTO forms_data (patient_id, form_json) VALUES (%s, %s);",
#                 (patient_id, json.dumps(data)))

#     conn.commit()
#     print("Data successfully inserted!")

# # Example usage
# insert_data(structured_data)

# # Close the connection
# cur.close()
# conn.close()





# import mysql.connector
# import json

# # Example JSON data as a string.
# # Make sure your JSON string contains the keys "patient_name" and "dob"
# structured_data = '''
# {
#     "patient_name": "John Doe",
#     "dob": "1990-01-01",
#     "additional_info": "Sample data"
# }
# '''

# # Database Connection
# conn = mysql.connector.connect(
#     database="ramya",  # Changed from dbname to database
#     user="root",
#     password="ramci@2003R",
#     host="localhost",
#     port=3306  # Port as an integer
# )
# cur = conn.cursor()

# # Insert data into database
# def insert_data(json_data):
#     data = json.loads(json_data)
    
#     # Insert patient data and get the inserted patient's id.
#     cur.execute(
#         "INSERT INTO patients (name, dob) VALUES (%s, %s);",
#         (data["patient_name"], data["dob"])
#     )
#     # Retrieve the patient id (if your MySQL version supports RETURNING, otherwise use lastrowid)
#     # MySQL Connector does not support RETURNING in INSERT statements.
#     patient_id = cur.lastrowid

#     # Insert JSON data into forms_data table
#     cur.execute(
#         "INSERT INTO forms_data (patient_id, form_json) VALUES (%s, %s);",
#         (patient_id, json.dumps(data))
#     )

#     conn.commit()
#     print("Data successfully inserted!")

# # Example usage
# insert_data(structured_data)

# # Close the connection
# cur.close()
# conn.close()










# import mysql.connector
# import json

# # Read the JSON data from the output.json file
# def read_json_from_file(file_path):
#     with open(file_path, 'r') as file:
#         return json.load(file)

# # Database Connection
# conn = mysql.connector.connect(
#     database="newdatabase",  # Database name
#     user="root",
#     password="ramci@2003R",
#     host="localhost",
#     port=3306
# )
# cur = conn.cursor()

# # Insert data into database
# def insert_data(json_data):
#     data = json_data
    
#     # Insert basic patient data
#     cur.execute(
#         "INSERT INTO patients (name, dob) VALUES (%s, %s);",
#         (data["patient_name"], data["dob"])
#     )
    
#     # Get the inserted patient's id
#     patient_id = cur.lastrowid

#     # Insert detailed form data into forms_data table
#     cur.execute(
#         "INSERT INTO forms_data (patient_id, form_json) VALUES (%s, %s);",
#         (patient_id, json.dumps(data))
#     )

#     # Commit the changes to the database
#     conn.commit()
#     print("Data successfully inserted!")

# # Path to the JSON file
# json_file_path = r'C:\Users\Ramya\Downloads\intern\output.json'

# # Read data from the JSON file
# structured_data = read_json_from_file(json_file_path)

# # Example usage to insert data into the database
# insert_data(structured_data)

# # Close the database connection
# cur.close()
# conn.close()






# import mysql.connector
# import json
# from datetime import datetime

# # Read the JSON data from the output.json file
# def read_json_from_file(file_path):
#     with open(file_path, 'r') as file:
#         return json.load(file)

# # Function to convert date format to MySQL-compatible format (YYYY-MM-DD)
# def convert_date_format(dob):
#     try:
#         # Check if the date is in MM/DD/YY format and convert to YYYY-MM-DD
#         date_obj = datetime.strptime(dob, '%m/%d/%y')  # Parse the date
#         return date_obj.strftime('%Y-%m-%d')  # Convert to MySQL format (YYYY-MM-DD)
#     except ValueError:
#         return dob  # Return original if the format is incorrect or cannot be parsed

# # Database Connection
# conn = mysql.connector.connect(
#     database="newdatabase",  # Database name
#     user="root",
#     password="ramci@2003R",
#     host="localhost",
#     port=3306
# )
# cur = conn.cursor()

# # Insert data into database
# def insert_data(json_data):
#     data = json_data

#     # Convert dob to the correct date format
#     dob = convert_date_format(data["dob"])

#     # Insert basic patient data
#     cur.execute(
#         "INSERT INTO patients (name, dob) VALUES (%s, %s);",
#         (data["patient_name"], dob)  # Use the formatted dob
#     )

#     # Get the inserted patient's id
#     patient_id = cur.lastrowid

#     # Insert detailed form data into forms_data table
#     cur.execute(
#         "INSERT INTO forms_data (patient_id, form_json) VALUES (%s, %s);",
#         (patient_id, json.dumps(data))
#     )

#     # Commit the changes to the database
#     conn.commit()
#     print("Data successfully inserted!")

# # Path to the JSON file
# json_file_path = r'C:\Users\Ramya\Downloads\intern\output.json'

# # Read data from the JSON file
# structured_data = read_json_from_file(json_file_path)

# # Example usage to insert data into the database
# insert_data(structured_data)

# # Close the database connection
# cur.close()
# conn.close()



import mysql.connector
import json
from datetime import datetime

# Read the JSON data from the output.json file
def read_json_from_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Function to convert date format to MySQL-compatible format (YYYY-MM-DD)
def convert_date_format(dob):
    try:
        # Check if the date is in MM/DD/YY format and convert to YYYY-MM-DD
        date_obj = datetime.strptime(dob, '%m/%d/%y')  # Parse the date
        return date_obj.strftime('%Y-%m-%d')  # Convert to MySQL format (YYYY-MM-DD)
    except ValueError:
        return dob  # Return original if the format is incorrect or cannot be parsed

# Database Connection
conn = mysql.connector.connect(
    database="patient_data",  # Database name
    user="root",
    password="ramci@2003R",
    host="localhost",
    port=3306
)
cur = conn.cursor()

# Insert data into database
def insert_data(json_data):
    data = json_data

    # Convert dob to the correct date format
    dob = convert_date_format(data["dob"])

    # Insert basic patient data
    cur.execute(
        "INSERT INTO patients (name, dob) VALUES (%s, %s);",
        (data["patient_name"], dob)
    )
    
    # Get the inserted patient's id
    patient_id = cur.lastrowid

    # Insert patient changes
    cur.execute(
        "INSERT INTO patient_changes (patient_id, since_last_treatment, since_start_of_treatment, last_3_days) VALUES (%s, %s, %s, %s);",
        (patient_id, data["patient_changes"]["since_last_treatment"], data["patient_changes"]["since_start_of_treatment"], data["patient_changes"]["last_3_days"])
    )

    # Insert difficulty ratings
    for activity, rating in data["difficulty_ratings"].items():
        cur.execute(
            "INSERT INTO difficulty_ratings (patient_id, activity, rating) VALUES (%s, %s, %s);",
            (patient_id, activity, rating)
        )

    # Insert pain symptoms
    for symptom, rating in data["pain_symptoms"].items():
        cur.execute(
            "INSERT INTO pain_symptoms (patient_id, symptom, rating) VALUES (%s, %s, %s);",
            (patient_id, symptom, rating)
        )

    # Insert medical assistant data
    medical_data = data["medical_assistant_data"]
    cur.execute(
        "INSERT INTO medical_assistant_data (patient_id, blood_pressure, heart_rate, weight, height, spo2, temperature, blood_glucose, respirations) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);",
        (patient_id, medical_data["blood_pressure"], medical_data["hr"], medical_data["weight"], medical_data["height"], medical_data["spo2"], medical_data["temperature"], medical_data["blood_glucose"], medical_data["respirations"])
    )

    # Insert form data (entire JSON data)
    cur.execute(
        "INSERT INTO forms_data (patient_id, form_json) VALUES (%s, %s);",
        (patient_id, json.dumps(data))
    )

    # Commit the changes to the database
    conn.commit()
    print("Data successfully inserted!")

# Path to the JSON file
json_file_path = r'C:\Users\Ramya\Downloads\intern\output.json'

# Read data from the JSON file
structured_data = read_json_from_file(json_file_path)

# Example usage to insert data into the database
insert_data(structured_data)

# Close the database connection
cur.close()
conn.close()









