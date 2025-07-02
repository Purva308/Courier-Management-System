# Task 9: Database Interaction
import mysql.connector
from sqlalchemy import create_engine
from util.db_prop_util import DBPropertyUtil

class DBConnUtil:
    @staticmethod
    def get_connection(connection_string):
        try:
            if not connection_string:
                raise ValueError("Connection string is None or empty")
            engine = create_engine(connection_string)

            connection=engine.raw_connection()

            cursor = connection.cursor()
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            if result and result[0] == 1:
                print("Database connection successful!")
            else:
                print(" Connection test failed.")

            return connection
        except Exception as e:
            print(f"Error establishing database connection: {str(e)}")
        return None





