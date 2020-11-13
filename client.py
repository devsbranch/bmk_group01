import database


def user_menu():  # Presents the user with options available for selection
    user_options = {
        'A': 'Create new bookmark',
        'R': 'Read bookmark (s)',
        'U': 'Update existing bookmark',
        'D': 'Delete existing bookmark'
    }
    print('\nPlease select an option amongst the letters on the left')
    for action, descr in user_options.items():
        print(f'{action} : {descr}')


def user_input():  # Will process user inputs entered bu user from command line
    while True:  # The while loop will keep the program running and the user is the one stop the program by entering
        # 'Q' (quit).
        user_menu()  # Will show available options
        user_choice = input('Please select a letter option from the menu above: ')

        if user_choice not in ['A', 'R', 'U', 'D']:
            print("INVALID OPTION SELECTED")
            continue
            # If user enters option other than which is available, user will e shown "INVALID OPTION SELECTED".
            # The continue statement makes it possible to go back to the beginning of the loop and prompt user to enter
            # the correct option

        elif user_choice == 'A':
            bmk_name = input("Enter a name for your Bookmark:  ")
            bmk_url = input("Enter url for your Bookmark:  ")
            bmk_desc = input("Enter description for your Bookmark:  ")
            database.add_bookmark(bmk_name, bmk_url, bmk_desc)
            database.save_changes()
            print("bookmark added")
            continue

        elif user_choice == 'R':
            bookmarks = database.show_bookmarks()
            for i in bookmarks:
                print(i[0], i[1], i[2])
            print("Process finished")
            continue

        elif user_choice == 'U':
            bmk_to_updt = "What is the name of your bookmark you want to update?   "
            values_to_updt = f"""What do you want to update to {bmk_to_updt}? Select option
                                1. Everything
                                2. change the bookmark name
                                3. change the bookmark url
                                4. change the bookmark description
                                """
            while True:
                if values_to_updt == '1':
                    bmk_name = input("Enter a name for your Bookmark:  ")
                    bmk_url = input("Enter url for your Bookmark:  ")
                    bmk_desc = input("Enter description for your Bookmark")
                    database.update_bookmark('1', bmk_to_updt, bmk_name, bmk_url, bmk_desc)
                    print('bookmark updated')
                    break
                elif values_to_updt == '2':
                    bmk_name = input("Enter a name for your Bookmark:  ")
                    database.update_bookmark('2', bmk_to_updt, bmk_name, '', '')
                    print('bookmark updated')
                    break
                elif values_to_updt == '3':
                    bmk_url = input("Enter a url for your Bookmark:  ")
                    database.update_bookmark('2', bmk_to_updt, '', bmk_url, '')
                    print('bookmark updated')
                    break

                elif values_to_updt == '4':
                    bmk_desc = input("Enter a description for your Bookmark:  ")
                    database.update_bookmark('2', bmk_to_updt, '', '', bmk_desc)
                    print('bookmark updated')
                    break
                elif values_to_updt not in ['1', '2', '3', '4']:
                    print("invalid option")
                    break
            database.save_changes()
            continue
        elif user_choice == 'D':
            bmk_name = input("Enter a name for your Bookmark you want to delete:  ")
            database.delete_bookmark(bmk_name)
            database.save_changes()
            print("Bookmark deleted")
            continue


user_input()
