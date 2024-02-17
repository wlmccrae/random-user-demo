steps = [
    [
        """
        CREATE TABLE users (
        id SERIAL PRIMARY KEY NOT NULL,
        email VARCHAR(320) NOT NULL UNIQUE,
        name VARCHAR(100) NOT NULL
        );
        """,
        """
        DROP TABLE users;
        """,
    ],
]
