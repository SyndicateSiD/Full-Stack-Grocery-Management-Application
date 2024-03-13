import mysql.connector

__cnx = None

def get_sql_connection():
  print("Connectiong...")
  global __cnx

  if __cnx is None:
    __cnx = mysql.connector.connect(user='root', password='Bob2152@', database='Binod Grocery Store 1')

  return __cnx
