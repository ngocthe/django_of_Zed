from django.db import connection, transaction

DATABASES = {
    "default": {
        "NAME": "app_data",
        "ENGINE": "django.db.backends.postgresql",
        "USER": "postgres_user",
        "PASSWORD": "s3krit",
    },
    "users": {
        "NAME": "user_data",
        "ENGINE": "django.db.backends.mysql",
        "USER": "mysql_user",
        "PASSWORD": "priv4te",
    },
}


class db_helper:
    def select_sql(self, sql):
        with connection.cursor() as cursor:
            cursor.execute(sql)
            row = cursor.fetchone()
            return row

    def select_time(self):
        with connection.cursor() as cursor:
            cursor.execute("select date()")
            row = cursor.fetchall()
            return row

    # Transection
    @transaction.atomic
    def update_sql(self):
        try:
            with transaction.atomic():
                #do update function
                with connection.cursor() as cursor:
                    cursor.execute("update...")
                    row = cursor.fetchall()
                    return row
        except:
            #do handel excetption
            return "Err"
