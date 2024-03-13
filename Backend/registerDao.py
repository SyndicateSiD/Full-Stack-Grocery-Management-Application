# registerDao.py

from sql_connection import get_sql_connection



def register_user(connection, username, password):
    cursor = connection.cursor()

    # Check if the username already exists
    query = "SELECT * FROM users WHERE username = %s"
    data = (username,)

    cursor.execute(query, data)

    existing_user = cursor.fetchone()

    if existing_user:
        cursor.close()
        return False  # Username already taken

    # If username is not taken, register the user
    query = "INSERT INTO users (username, password) VALUES (%s, %s)"
    data = (username, password)

    cursor.execute(query, data)

    connection.commit()

    cursor.close()

    return True  # Registration successful

if __name__ == '__main__':
    connection = get_sql_connection()
    #username = "user1"  # Replace with the desired username
    #password = "pass1"  # Replace with the desired password
    #result = register_user(connection, username, password)
    #print(result)

