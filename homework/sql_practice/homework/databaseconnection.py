import psycopg2


class DatabaseConnection:
    def __init__(self, database='illia', user='illia',
                 password='pass', host='localhost'):
        self.database = database
        self.user = user
        self.password = password
        self.host = host

    def __enter__(self):
        self.connection = psycopg2.connect(
            database=self.database,
            user=self.user,
            password=self.password,
            host=self.host,
        )
        cursor = self.connection.cursor()
        return cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type or exc_val or exc_tb:
            self.connection.close()
        else:
            self.connection.commit()
            self.connection.close()
        return False
