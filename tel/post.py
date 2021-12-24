

        
   
  
import psycopg2
from config import host, user, password, db_name

username = 5
taekname = 55
  
try:
    # connect to exist database
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name    
    )
    connection.autocommit = True
    

    
    with connection.cursor() as cursor:
        cursor.execute(
            "SELECT version();"
        )
        
        print(f"Server version: {cursor.fetchone()}")
        

    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """CREATE TABLE users(
    #             id serial PRIMARY KEY,
    #             first_name varchar(50) NOT NULL,
    #             nick_name varchar(50) NOT NULL);"""
    #     )
        
    #     # connection.commit()
    #     print("[INFO] Table created successfully")
        
    with connection.cursor() as cursor:
        cursor.execute(
            """INSERT INTO user1 (user_name, date_of_birth ) VALUES
            (%s, %s );""", (f'{username}',f'{taekname}')
            )
        
    #     print("[INFO] Data was succefully inserted")
        
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """SELECT nick_name FROM users WHERE first_name = 'Oleg';"""
    #     )
        
    #     print(cursor.fetchone())
        
    # with connection.cursor() as cursor:
    #     cursor.execute(
    #         """DROP TABLE users;"""
    #     )
        
    #     print("[INFO] Table was deleted")
    
except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")