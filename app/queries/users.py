from queries.pool import pool
from models.users import UserIn

class UserQueries:
    ##### Write a user to the database. #####
    def create_user(self, user: UserIn):
        with pool.connection() as conn:
            with conn.cursor() as db:
                result = db.execute(
                    """
                        INSERT INTO users
                            (name, dob, email, city, state, country)
                        VALUES
                            (%s, %s, %s, %s, %s, %s)
                        RETURNING id;
                    """,
                    [user.name, user.dob, user.email, user.city, user.state, user.country],
                )
                id = result.fetchone()[0]
        if id is not None:
            return self.get_user(id)

    def get_user(self, user_id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT users.*
                    FROM users
                    WHERE users.id = %s
                    """,
                    [user_id],
                )
                row = db.fetchone()
                return self.user_record_to_dict(row, db.description)

    ##### Get all users from database #####
    def get_users(self):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT *
                    FROM users
                    """,
                )
                users = []
                rows = db.fetchall()
                for row in rows:
                    user = self.user_record_to_dict(row, db.description)
                    users.append(user)
                return users

    ##### Get a specific user from database #####
    def get_user(self, user_id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    SELECT *
                    FROM users
                    WHERE users.id = %s
                    """,
                    [user_id],
                )
                row = db.fetchone()
                print(f"******* USER DATA TO RETURN: {row}")
                return self.user_record_to_dict(row, db.description)

    def user_record_to_dict(self, row, description):
        user = None
        if row is not None:
            user = {}
            user_fields = {
                "id",
                "name",
                "dob",
                "email",
                "city",
                "state",
                "country",
            }
            for i, column in enumerate(description):
                if column.name in user_fields:
                    user[column.name] = row[i]
        return user
