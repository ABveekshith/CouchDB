import mysql.connector
from engine.connectors.connector import Connector
from engine.extensions import es
# from sqlalchemy import create_engine
# from sqlalchemy import inspect
# import pymysql 

class MysqlConnector(Connector):
    """Implememtation of the Connector:class."""    

    def __init__(self):
        """constructor function."""
        self.connection = None


    def initialize(self,credentials):
        """Validate the credentials with the instance."""
        try:
            dbconfig = {
                'host' : credentials['host'],
                'user' : credentials['user'],
                'password' : credentials['passwd'],
                'database' : credentials['database']
            }
            self.connection = mysql.connector.connect(**dbconfig)

        except ConnectionError as e:
            return False,str(e)
        
    def connect(self,credentials):
        try:
            MysqlConnector.initialize(self,credentials)
            self.connection.close()
            return True,"mysql connected successfully"
        except Exception as e:
            return False,str(e)                

    def list_tables(self,credentials):
        try:
            MysqlConnector.initialize(self,credentials)
            table_names = []
            cursor = self.connection.cursor()
            cursor.execute("show tables")
            tables = cursor.fetchall()
            for table in tables:
                for table_name in table:
                    table_names.append(table_name)
            self.connection.close()
            return table_names
        except Exception as e:
            print(str(e))
            return []

    def list_fields(self, credentials,table_name):
        try:
            MysqlConnector.initialize(self,credentials)
            field_details = []
            cursor = self.connection.cursor()
            query = 'show columns from '+table_name
            cursor.execute(query)
            fields = cursor.fetchall()
            for field in fields:
                field_data = {
                    'name' : field[0],
                    'type' : field[1],
                    'isNull' : field[2]
                }
                field_details.append(field_data)
            self.connection.close()
            return field_details

        except Exception as e:
            return []