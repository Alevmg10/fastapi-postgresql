import psycopg2
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


# Parameters for our connection
myconn = psycopg2.connect(
    database=os.getenv("DBNAME"),
    user=os.getenv("DBUSER"),
    password=os.getenv("DBPASSWORD"),
    host=os.getenv("DBHOST")
)


# Connect to database

def connect_db():

    # Create cursor that will allows us to make sql queries
    mycur = myconn.cursor()

    mycur.execute("SELECT version();")
    record = mycur.fetchone()
    print(f"Database Version: {record}")


def create_table():

    connect_db()
    mycur = myconn.cursor()

    query = ''' CREATE TABLE employees ( id BIGSERIAL PRIMARY KEY NOT NULL,
										first_name VARCHAR(50) NOT NULL,
										last_name VARCHAR(50) NOT NULL,
										phone VARCHAR(100) NOT NULL,
										email VARCHAR(200) NOT NULL,
										department VARCHAR(100) NOT NULL) '''
    mycur.execute(query)
    mycur.close()
    myconn.commit()

    print("Table created")
