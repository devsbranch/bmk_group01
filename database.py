import sqlite3
# ##
conn = sqlite3.connect('mydb.db')
c = conn.cursor()


# c.execute("""CREATE TABLE bookmarks (bookmark_name TEXT NOT NULL, bookmark_url TEXT NOT NULL, bookmark_description
# TEXT NOT NULL)""")


def add_bookmark(bmk_name, bmk_url, bmk_desc):
    c.execute(
        f"""INSERT INTO bookmarks (bookmark_name, bookmark_url, bookmark_description) VALUES ('{bmk_name}', '{bmk_url}', '{bmk_desc}')""")


def show_bookmarks():
    return c.execute("""SELECT * FROM bookmarks""")  # the #function runs only if the user selects option R


def update_bookmark(opt, bmk_to_updt, bmk_name, bmk_url,
                    bmk_desc):
    if opt == '1':
        c.execute(
            f"""UPDATE bookmarks SET bookmark_name = '{bmk_name}', bookmark_url = '{bmk_url}', bookmark_description = '{bmk_desc}'
                      WHERE bookmark_name = '{bmk_to_updt}'""")
    elif opt == '2':
        c.execute(f"""UPDATE bookmarks SET bookmark_name = '{bmk_name}' WHERE bookmark_name = '{bmk_to_updt}'""")

    elif opt == '3':
        c.execute(f"""UPDATE bookmarks SET bookmark_url = '{bmk_url}' WHERE bookmark_name = '{bmk_to_updt}'""")

    elif opt == '4':
        c.execute(f"""UPDATE bookmarks SET bookmark_description = '{bmk_desc}' WHERE bookmark_name = '{bmk_to_updt}'""")


def delete_bookmark(bmk_name):
    """Function returns changes that a user  enters."""

    bookmarks = c.execute(f"""DELETE FROM bookmarks WHERE bookmark_name = '{bmk_name}'""")
    return bookmarks


def save_changes():
    conn.commit()
    print("changes saved")
