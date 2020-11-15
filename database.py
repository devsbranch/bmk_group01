import sqlite3
from datetime import datetime
from datetime import date

now = datetime.now()
current_time = now.strftime("%H:%M:%S")
current_date = date.today()


conn = sqlite3.connect('mydb.db')
c = conn.cursor()


c.execute("""
             CREATE TABLE IF NOT EXISTS bookmarks 
             (
             bookmark_name TEXT NOT NULL, 
             bookmark_url TEXT NOT NULL, 
             bookmark_description TEXT NOT NULL, 
             date_added TEXT NOT NULL, 
             time TEXT NOT NULL)
          """)


def add_bookmark(bmk_name, bmk_url, bmk_desc):
    c.execute(
        f"""
            INSERT INTO bookmarks (
            bookmark_name, 
            bookmark_url, 
            bookmark_description, 
            date_added, 
            time
            ) 
            VALUES ('{bmk_name}', '{bmk_url}', '{bmk_desc}', '{current_date}', '{current_time}')""")


def show_bookmarks():
    return c.execute("""SELECT * FROM bookmarks""")  # the function runs only if the user selects option R


def update_bookmark(opt, bmk_to_updt, bmk_name, bmk_url,
                    bmk_desc, date_uptd, time):
    if opt == '1':
        c.execute(
            f"""
                UPDATE bookmarks SET 
                bookmark_name = '{bmk_name}', bookmark_url = '{bmk_url}', 
                bookmark_description = '{bmk_desc}', 
                date_added = '{date_uptd}', 
                time = '{time}'
                WHERE bookmark_name = '{bmk_to_updt}'
            """)

    elif opt == '2':
        c.execute(f"""
                      UPDATE bookmarks SET bookmark_name = '{bmk_name}' 
                      date_added = '{date_uptd}', 
                      time = '{time}'
                      WHERE bookmark_name = '{bmk_to_updt}'
                   """)

    elif opt == '3':
        c.execute(f"""
                      UPDATE bookmarks SET bookmark_url = '{bmk_url}' 
                      date_added = '{date_uptd}', 
                      time = '{time}'
                      WHERE bookmark_name = '{bmk_to_updt}'""")

    elif opt == '4':
        c.execute(f"""
                      UPDATE bookmarks SET bookmark_description = '{bmk_desc}',
                      date_added = '{date_uptd}', 
                      time = '{time}'
                      WHERE bookmark_name = '{bmk_to_updt}'
                   """)


def delete_bookmark(bmk_name):
    """Function returns changes that a user  enters."""

    bookmarks = c.execute(f"""DELETE FROM bookmarks WHERE bookmark_name = '{bmk_name}'""")
    return bookmarks


def save_changes():  # this function will be called in the client.py module to save changes made to the database.
    conn.commit()
    print("changes saved")


def db_conn_close():
    c.close()
    conn.close()
