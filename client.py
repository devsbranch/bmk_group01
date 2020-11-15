import database
from datetime import datetime
from datetime import date

now = datetime.now()
time_updated = now.strftime("%H:%M:%S")
date_updated = date.today()


def user_menu():
    """This presents the user with options available for selection.
    :argument None
    :parameter None
    """
    user_options = {
        'A': 'Create new bookmark',
        'R': 'Read bookmark (s)',
        'U': 'Update existing bookmark',
        'D': 'Delete existing bookmark',
        'Q': 'Quit program'
    }
    print('\nPlease select an option amongst the letters on the left')
    for action, descr in user_options.items():
        print(f'{action} : {descr}')


def user_input():
    """This will process user inputs entered by the user from command line.
    we have one parameter in this function that is the user_choice.
    """
    while True:  # The while loop will keep the program running and the user is the one stop the program by entering
        # 'Q' (quit).
        user_menu()
        user_choice = input('Please select a letter option from the menu above: ')

        if user_choice == 'A':
            """Within this function there are three more parameters,
            that is bmk_name, bmk_url,bmk_desc that will allow the user to enter their input.
            """

            bmk_name = input("Enter a name for your Bookmark:  ")
            bmk_url = input("Enter url for your Bookmark:  ")
            bmk_desc = input("Enter description for your Bookmark:  ")
            database.add_bookmark(bmk_name, bmk_url, bmk_desc)
            database.save_changes()
            print("bookmark added")
            continue

        elif user_choice == 'R':
            """If the user selects R from the menu this should just show details that were entered.
            where the for loop on index 0, shows the index where bmk_name is and where 1 shows bmk_url
            and where 2 shows the description.
            """
            bookmarks = database.show_bookmarks()
            for i in bookmarks:
                print(
                    f"bookmark name > {i[0]},  bookmark url > {i[1]},  bookmark description > {i[2]}, date added > {i[3]},  time > {i[4]}")
            print("Process finished")
            continue

        elif user_choice == 'U':
            """within this parameter we have two more parameters.
            That is bmk_to_update where the input the user enters will  be stored in that variable
            the same happens with values_to_update.
            """
            bmk_to_updt = input('What is the name of your bookmark you want to update?   ')
            values_to_updt = input(f"""What do you want to update to {bmk_to_updt}? Select option
                                1. Everything
                                2. change the bookmark name
                                3. change the bookmark url
                                4. change the bookmark description
                                """)
            while True:  # the loop will keep running the code inside until the user selects a valid option
                # then the loop will break

                if values_to_updt == '1':
                    bmk_name = input("Enter a name for your Bookmark:  ")
                    bmk_url = input("Enter url for your Bookmark:  ")
                    bmk_desc = input("Enter description for your Bookmark")
                    database.update_bookmark('1', bmk_to_updt, bmk_name, bmk_url, bmk_desc, date_updated, time_updated)
                    print('bookmark updated')
                    break
                elif values_to_updt == '2':
                    bmk_name = input("Enter a name for your Bookmark:  ")
                    database.update_bookmark('2', bmk_to_updt, bmk_name, '', '', date_updated, time_updated)
                    print('bookmark updated')
                    break
                elif values_to_updt == '3':
                    bmk_url = input("Enter a url for your Bookmark:  ")
                    database.update_bookmark('3', bmk_to_updt, '', bmk_url, '', date_updated, time_updated)
                    print('bookmark updated')
                    break

                elif values_to_updt == '4':
                    bmk_desc = input("Enter a description for your Bookmark:  ")
                    database.update_bookmark('4', bmk_to_updt, '', '', bmk_desc, date_updated, time_updated)
                    print('bookmark updated')
                    break
                elif values_to_updt not in ['1', '2', '3', '4']:
                    print("invalid option")
                    break
            database.save_changes()
            continue

        elif user_choice == 'D':
            """This parameter allows the user to delete the bookmark they no longer want."""

            bmk_name = input("Enter a name for your Bookmark you want to delete:  ")
            database.delete_bookmark(bmk_name)
            database.save_changes()
            print("Bookmark deleted")
            continue

        elif user_choice == 'Q':  # The program will exit the loop.
            print("Program stopped")
            break

        else:
            print("INVALID OPTION SELECTED")
            continue
    database.db_conn_close()  # the function will run when the while loop is exited since the user selects option Q.
    # then function will close the connection to the database.


user_input()
"""This function just storing the input entered by the user."""
