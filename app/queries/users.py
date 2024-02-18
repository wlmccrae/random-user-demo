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
                return self.user_record_to_dict(row, db.description)

    ##### Update a user's info #####
    def update_user(self, user_id, user_data):
        with pool.connection() as conn:
            with conn.cursor() as db:
                params = [
                    user_data.name,
                    user_data.dob,
                    user_data.email,
                    user_data.city,
                    user_data.state,
                    user_data.country,
                    user_id,
                ]
                db.execute(
                    """
                    UPDATE users
                    SET name = %s
                    , dob = %s
                    , email = %s
                    , city = %s
                    , state = %s
                    , country = %s
                    WHERE id = %s
                    RETURNING id
                    , name
                    , dob
                    , email
                    , city
                    , state
                    , country
                    """,
                    params,
                )
                record = None
                row = db.fetchone()
                if row is not None:
                    record = {}
                    for i, column in enumerate(db.description):
                        record[column.name] = row[i]
                return record

    ##### Delete a specific user #####
    def delete_user(self, user_id):
        with pool.connection() as conn:
            with conn.cursor() as db:
                db.execute(
                    """
                    DELETE FROM users
                    WHERE users.id = %s
                    """,
                    [user_id],
                )
                db.execute(
                    """
                    SELECT *
                    FROM users
                    WHERE users.id = %s
                    """,
                    [user_id],
                )
                row = db.fetchone()
        if row is not None:
            return False
        else:
            return True

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
