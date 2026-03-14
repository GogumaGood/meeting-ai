from db import cursor, conn

def save_meeting(filename, transcript, summary):

    cursor.execute(
        """
        INSERT INTO meetings (filename, transcript, summary)
        VALUES (%s, %s, %s)
        """,
        (filename, transcript, summary)
    )

    conn.commit()