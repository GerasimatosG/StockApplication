import psycopg2


class DBConnection:

    def executeQuery(self, query: str):
        connection = psycopg2.connect(
            dbname="PythonProject",
            user="postgres",
            password="123456",
            host="localhost",
            port="5432"
        )
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
        return connection

    def fetchData(self, query: str):
        try:
            connection = psycopg2.connect(
                dbname="PythonProject",
                user="postgres",
                password="123456",
                host="localhost",
                port="5432"
            )
            cursor = connection.cursor()
            cursor.execute(query)
            results = cursor.fetchall()
            connection.close()
            return results
        except Exception as e:
            print("Error fetching data from PostgreSQL:", e)
            return None
