import sqlite3
from datetime import datetime
from datetime import date

# now = datetime.now()
# current_time = now.strftime("%H:%M:%S")
# current_date = date.today()


conn = sqlite3.connect('mydb.db')  # connect to database
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


class CreateBookmark:  # This class create a bookmark using the add_bookmark method. The properties will be the values the bookmark will have.
    def __init__(self, bmk_name, bmk_url, bmk_desc, date, time):
        self.bmk_name = bmk_name
        self.bmk_url = bmk_url
        self.bmk_desc = bmk_desc
        self.date = date
        self.time = time

    def add_bookmark(self): # This method is called when user selects option 'C' to create a bookmark with values entered by user. 
        c.execute(f"""
            INSERT INTO bookmarks (
            bookmark_name, 
            bookmark_url, 
            bookmark_description, 
            date_added, 
            time
            ) 
            VALUES ('{self.bmk_name}', '{self.bmk_url}', '{self.bmk_desc}', '{self.date}', '{self.time}')""")


class ReadBookmarks(object): # This class is will initiate when user selects option 
    def show_bookmarks(self):
        return c.execute("""SELECT * FROM bookmarks""")  # the function runs only if the user selects option R


class UpdateBookmark:
    def __init__(self, date, time):
        self.date = date
        self.time = time
        
    def update_bookmark(self, *args): # the update_bookmark method will be called whenuser selects option 'U'. The *args parameter is used
                                      # since the number of arguments is not fixed and will vary according to what the user wants to update to the bookmark
                                      # So the arguments will passed into the sql query by getting the positionof the argument required using indexes.
        if args[0] == '1':
            c.execute(
                f"""
                    UPDATE bookmarks SET 
                    bookmark_name = '{args[2]}', bookmark_url = '{args[3]}', 
                    bookmark_description = '{args[4]}', 
                    date_added = '{self.date}', 
                    time = '{self.time}'
                    WHERE bookmark_name = '{args[1]}'
                """)

        elif args[0] == '2':
            c.execute(f"""
                            UPDATE bookmarks SET bookmark_name = '{args[2]}',
                            date_added = '{self.date}', 
                            time = '{self.time}'
                            WHERE bookmark_name = '{args[1]}'
                        """)

        elif args[0] == '3':
            c.execute(f"""
                            UPDATE bookmarks SET bookmark_url = '{args[2]}',
                            date_added = '{self.date}', 
                            time = '{self.time}'
                            WHERE bookmark_name = '{args[1]}'""")

        elif args[0] == '4':
            c.execute(f"""
                            UPDATE bookmarks SET bookmark_description = '{args[2]}',
                            date_added = '{self.date}', 
                            time = '{self.time}'
                            WHERE bookmark_name = '{args[1]}'
                        """)


class DeleteBookmark: # Will initiate when user selects option 'D' to delete bookmark. The book mark name the only value needed and it will be passed into the
                      # delete_bookmark method and the sql query will be executed. 
    def __init__(self, bmk_name):
        self.bmk_name = bmk_name

    def delete_bookmark(self): 
        """Function returns changes that a user  enters."""
        c.execute(f"""DELETE FROM bookmarks WHERE bookmark_name = '{self.bmk_name}'""")


def save_changes():  # this function will be called in the client.py module to save changes made to the database.
    conn.commit()
    print("changes saved")


def db_conn_close():
    c.close()
    conn.close()
    