import sqlite3


def connect_to_db():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn


def initial_setup():
    conn = connect_to_db()
    conn.execute(
        """
        DROP TABLE IF EXISTS hobbies;
        """
    )
    conn.execute(
        """
        CREATE TABLE hobbies (
          id INTEGER PRIMARY KEY NOT NULL,
          name TEXT,
          location TEXT,
          description TEXT
        );
        """
    )
    conn.commit()
    print("Table created successfully")

    hobbies_seed_data = [
        ("Hiking", "Zion National Park", "Exploring nature trails and scenic views."),
        ("Photography", "Downtown Kanab", "Capturing urban and landscape images."),
        ("Pottery", "Kanab Arts Center", "Creating clay art and functional pieces."),
        ("Stargazing", "Bryce Canyon", "Observing celestial bodies in the night sky."),
        ("Rock Climbing", "Red Cliffs", "Scaling sandstone cliffs and boulders.")
    ]
    conn.executemany(
        """
        INSERT INTO hobbies (name, location, description)
        VALUES (?,?,?)
        """,
        hobbies_seed_data,
    )
    conn.commit()
    print("Seed data created successfully")

    conn.close()


if __name__ == "__main__":
    initial_setup()

def hobbies_all():
    conn = connect_to_db()
    rows = conn.execute(
        """
        SELECT * FROM hobbies
        """
    ).fetchall()
    return [dict(row) for row in rows]

def hobbies_create(name, location, description):
    conn = connect_to_db()
    row = conn.execute(
        """
        INSERT INTO hobbies (name, location, description)
        VALUES (?, ?, ?)
        RETURNING *
        """,
        (name, location, description),
    ).fetchone()
    conn.commit()
    return dict(row)