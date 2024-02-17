steps = [
    [
        """
        CREATE TABLE users (
        id SERIAL PRIMARY KEY NOT NULL,
        name VARCHAR(100) NOT NULL,
        dob varchar(100) NOT NULL,
        email VARCHAR(320) NULL UNIQUE,
        city VARCHAR(100) NULL,
        state VARCHAR(100) NULL,
        country VARCHAR(100) NOT NULL
        );
        """,
        """
        DROP TABLE users;
        """,
    ],
]
