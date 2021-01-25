import psycopg2
import controller.config as cf

class pypostgresController:
    def __init__(self):
        pass
    
    def connection(self):
        connData = cf.postgresConfig()
        conn = psycopg2.connect(user = connData['username'],
                                  password = connData['password'],
                                  host = connData['hostname'],
                                  port = connData['port'],
                                  database = connData['dbname'])
        
        return conn
    
    def getPostgressVersion(self):
        try:
            connection = self.connection()
            cursor = connection.cursor()
            cursor.execute("SELECT version();")
            record = cursor.fetchone()
            return {
                "return_status":"success",
                "return_message":"You are connected to - {}".format(record)
            }
        except (Exception, psycopg2.Error) as error :
            return {
                "return_status":"failed",
                "return_message":"Error while connecting to PostgreSQL {}".format(str(error))
            }
        finally:
            #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
    
    def costumSelectquery(self,query):
        try:
           connection = self.connection()
           cur = connection.cursor() 
           cur.execute(query)
           rows = cur.fetchall()
           return {
               "return_status":"success",
               "return_message":rows
           }
        except Exception as e:
            return {
                "return_status":"failed",
                "return_message":str(e)
            }
        finally:
            if(connection):
                cur.close()
                connection.close()
                print("PostgreSQL connection is closed")
    
    def costumUpdatequery(self,query):
        try:
           connection = self.connection()
           cur = connection.cursor() 
           cur.execute(query)
           connection.commit()
           return {
               "return_status":"success",
               "return_message":"updated row {} ".format(cur.rowcount)
           }
        except Exception as e:
            return {
                "return_status":"failed",
                "return_message":str(e)
            }
        finally:
            if(connection):
                cur.close()
                connection.close()
                print("PostgreSQL connection is closed")
    
    def costumInsertquery(self,query):
        try:
            connection = self.connection()
            cur = connection.cursor() 
            cur.execute(query)
            connection.commit()
            return {
                "return_status":"success",
                "return_message":"insert to table"
            }
        except Exception as e:
            return {
                "return_status":"failed",
                "return_message":str(e)
            }
        finally:
            if(connection):
                cur.close()
                connection.close()
                print("PostgreSQL connection is closed")
    
    def costumDeletequery(self,query):
        try:
            connection = self.connection()
            cur = connection.cursor() 
            cur.execute(query)
            connection.commit()
            return {
                "return_status":"success",
                "return_message":"delete from table"
            }
        except Exception as e:
            return {
                "return_status":"failed",
                "return_message":str(e)
            }
        finally:
            if(connection):
                cur.close()
                connection.close()
                print("PostgreSQL connection is closed")

