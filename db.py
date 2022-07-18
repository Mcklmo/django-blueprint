import pymysql.cursors


class DB:
    def __init__(self, host, user, password, database) -> None:

        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = self.connect()


# Connect to the database

    def connect(self):
        return pymysql.connect(host=self.host,
                               user=self.user,
                               password=self.password,
                               database=self.database,
                               cursorclass=pymysql.cursors.DictCursor)

    def insert(self, tbl, cols, vals):
        if len(cols) != len(vals):
            raise Exception("columns and values must be the same length")
        with self.connection.cursor() as cursor:
            # Create a new record
            sql = f"INSERT INTO `{tbl}` (`{','.join(cols)}`) VALUES ({','.join(vals)})"
            cursor.execute(sql)

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        self.connection.commit()

    def select(self, tbl, cols="*", where=None):
        # where is a string like "id=1"
        if where:
            where = "WHERE "+where
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = f"SELECT {cols} FROM `{tbl}` {where}"
            cursor.execute(sql)
            result = cursor.fetchall()
        return result

    def get_tables(self):
        with self.connection.cursor() as cursor:
            # Read a single record
            sql = f"""
            SELECT table_name FROM information_schema.tables WHERE table_schema = '{self.database}' 
            and table_type='BASE TABLE' and not table_name='sys_config';
            """ # only user tables

            cursor.execute(sql)
            result = cursor.fetchall()
        return [table_dict["TABLE_NAME"] for table_dict in result]
