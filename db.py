import pymysql.cursors


# Connect to the database
def connect(host,user,password,database):
    return pymysql.connect(host=host,
                             user=user,
                             password=password,
                             database=database,
                             cursorclass=pymysql.cursors.DictCursor)


def insert(connection,tbl, cols,vals):
    if len(cols) != len(vals):
        raise Exception("columns and values must be the same length")
    with connection.cursor() as cursor:
        # Create a new record
        sql = f"INSERT INTO `{tbl}` (`{','.join(cols)}`) VALUES ({','.join(vals)})"
        cursor.execute(sql)

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()

def select(connection,tbl,cols="*",where=None):
    # where is a string like "id=1"
    if where:
        where="WHERE "+where
    with connection.cursor() as cursor:
        # Read a single record
        sql = f"SELECT {cols} FROM `{tbl}` {where}"
        cursor.execute(sql)
        result = cursor.fetchall()
    return result

def get_tables(connection):
    with connection.cursor() as cursor:
        # Read a single record
        sql = "SHOW TABLES"
        cursor.execute(sql)
        result = cursor.fetchall()
    return result