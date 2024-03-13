# loginDao.py

from sql_connection import get_sql_connection

def validate_dev_user(connection, username, password):
    cursor = connection.cursor()

    query = "SELECT * FROM devusers WHERE username = %s AND password = %s"
    data = (username, password)

    cursor.execute(query, data)

    user = cursor.fetchone()

    cursor.close()

    return user is not None

if __name__ == '__main__':
    connection = get_sql_connection()
    #username = "user1"  # Replace with the desired username
    #password = "pass1"  # Replace with the desired password
    #result = validate_user(connection, username, password)
    #print(result)

