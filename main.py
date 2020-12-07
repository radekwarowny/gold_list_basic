#!/usr/bin/env python
try:
    import os
    import pickle
    import random
    import sys
    import getpass
    import time
    import datetime
    from pyfiglet import Figlet
except ImportError:
    import pip

    pip.main(['install', '--user', 'os'])
    pip.main(['install', '--user', 'pickle'])
    pip.main(['install', '--user', 'random'])
    pip.main(['install', '--user', 'sys'])
    pip.main(['install', '--user', 'getpass'])
    pip.main(['install', '--user', 'time'])
    pip.main(['install', '--user', 'datetime'])

    import os
    import pickle
    import random
    import sys
    import getpass
    import time
    import datetime
    from pyfiglet import Figlet

"""main.py: Simple program based on GOLD LIST METHOD"""

__author__ = "Radek Warowny"
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Radek Warowny"
__email__ = "radekwarownydev@gmail.com"
__status__ = "Demo"


def main():
    # INTERFACES

    dict_language = None
    dict_name = None

    def show_book():
        os.system('clear||cls')
        print("**********************************************************************************")
        print("**********************************************************************************")
        print("**                                                                              **")
        print("**                               @@                                             **")
        print("**                              @@@@@@@ /@@@,                                   **")
        print("**                             @@@@@@@@@@ *@@@&                                 **")
        print("**                           ,@@@@@@@@@@@@@ *@@@@                               **")
        print("**                          @@@@@@@@@@@@@@@@@ ,@@@@                             **")
        print("**                        @@@@@@@@@@@@@@@@@@@@@ ,@@@@                           **")
        print("**                      @@@@@@@@@@@@@@@@@@@@@@@@@ .@@@@                         **")
        print("**                   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ,@@@@,                      **")
        print("**             ,@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ,@@@@@                    **")
        print("**       @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ,@@@@@                  **")
        print("**      @  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ .@@@@@                **")
        print("**      @@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ .@@@@@              **")
        print("**      @@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@            **")
        print("**      @@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ .@@@@@&         **")
        print("**      @@@@@@@@@  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@       **")
        print("**        @@@@@@@@@. @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ .@@@@@@@@     **")
        print("**          @@@@@@@@@/ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ ,@@@@@@@       **")
        print("**            @@@@@@@@@% @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ @@@@@@@         **")
        print("**              @@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@@ @@@@@     **")
        print("**                @@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  @@@@@  @@@@@@@@    **")
        print("**                  @@@@@@@@@@ @@@@@@@@@@@@@@@@@@@@@@@@@@ .@@@@& @@@@@@@@       **")
        print("**                    @@@@@@@@@@ #@@@@@@@@@@@@@@@@@@@@  @@@@@ @@@@@@@@  @@#     **")
        print("**                      @@@@@@@@@@ *@@@@@@@@@@@@@@#  @@@@. %@@@@@@  @@@@        **")
        print("**                        @@@@@@@@@@  @@@@@@@@   @@@@,  @@@@@#  @@@,   @@@@     **")
        print("**                          @@@@@@@@@@  @   @@@@(  #@@@@#  *@@&   @@@@@@@@@     **")
        print("**                            @@@@@@@@@ @@#   @@@@    @@@   @@@@@@@@@@&         **")
        print("v*                              @@@@@@@ @@#   .@@@   @@@@@@@@@@&                **")
        print("**                                @@@@@ @@    @@@@@@@@@@@                       **")
        print("**                                  @@@ @@@@@@@@@@                              **")
        print("**                                    @ @@@                                     **")
        print("**                                                                              **")
        print("**********************************************************************************")
        print("**********************************************************************************")

        time.sleep(2)
        show_logo()
        time.sleep(2)

    def show_help():
        os.system('clear||cls')

        show_logo()

        os.system('clear||cls')
        show_logo()

        print("\n\t\tIf you struggle with learning a foreign language ")
        time.sleep(1)
        print("\t\tof if you're tired of flashcards and memorising glossaries ")
        time.sleep(1)
        print("\t\tthen you may find this program useful.\n")
        time.sleep(1)
        print("\t\tPRESS ENTER TO CONTINUE\n")

        input("\n\t\t\t")
        if input() == 'q':
            show_menu()
        os.system('clear||cls')
        show_logo()

        print("\n\t\tYou start by typing words from the dictionary.")
        time.sleep(1)
        print("\t\tThen you wait for at least two weeks.")
        time.sleep(1)
        print("\t\tWhen you revisit the words again ")
        time.sleep(1)
        print("\t\tyou should be able to remember around 30% of them.")
        time.sleep(1)
        print("\t\tYou then repeat the process until you remember more and more words.")
        time.sleep(1)
        print("\t\tPRESS ENTER TO CONTINUE\n")

        input("\n\t\t\t")
        if input() == 'q':
            show_menu()
        os.system('clear||cls')

    def show_logo():

        os.system('clear||cls')

        print("\n  ░██████╗░░█████╗░██╗░░░░░██████╗░  ██╗░░░░░██╗░██████╗████████╗")
        print("  ██╔════╝░██╔══██╗██║░░░░░██╔══██╗  ██║░░░░░██║██╔════╝╚══██╔══╝")
        print("  ██║░░██╗░██║░░██║██║░░░░░██║░░██║  ██║░░░░░██║╚█████╗░░░░██║░░░")
        print("  ██║░░╚██╗██║░░██║██║░░░░░██║░░██║  ██║░░░░░██║░╚═══██╗░░░██║░░░")
        print("  ╚██████╔╝╚█████╔╝███████╗██████╔╝  ███████╗██║██████╔╝░░░██║░░░")
        print("  ░╚═════╝░░╚════╝░╚══════╝╚═════╝░  ╚══════╝╚═╝╚═════╝░░░░╚═╝░░░")
        print("  by Radek                                        PRESS q to QUIT\n")

    def show_intro():
        pass

    def show_credits():

        os.system('clear||cls')
        show_logo()
        print("\n\n\t\t\tMADE BE RADEK\n")
        time.sleep(1)
        sys.exit(0)

    def show_login():

        os.system('clear||cls')
        show_logo()

        username = input("\n\t\t\tUSERNAME: ")

        if username == 'q':
            show_credits()
            sys.exit()

        password = getpass.getpass("\n\t\t\tPASSWORD: ")

        return username, password

    def show_register():

        os.system('clear||cls')
        show_logo()

        print("\n\t\t\tREGISTRATION")
        name = input("\n\t\t\tNAME: ")
        if name == 'q':
            sys.exit()
        email = input("\n\t\t\tEMAIL: ")

        return name, email

    def show_menu():

        os.system('clear||cls')
        show_logo()

        print("\n\t\t\t1. DICTIONARIES")
        print("\t\t\t2. DISTILLATIONS")
        print("\t\t\t3. WORD COUNT")
        print("\t\t\t4. HELP")
        print("\n\t\t\tPRESS 'ENTER' TO START")

        print('\n\t\t\t', end='')
        user_input = input()
        menu_logic(user_input)

    def show_dicts():

        try:
            os.system('clear||cls')
            show_logo()

            print("\n\t\t\tAVAILABLE DICTIONARIES")
            print()
            print("\t\t\t1. ES")
            print("\t\t\t2. DE")
            print("\t\t\t3. FR")
            print("\t\t\t4. PL")
            print("\t\t\t4. EN THESAURUS")

            print()

            output = input('\n\t\t\t')

            return dicts_logic(output)
        except ValueError:
            print("\n\t\tINVALID INPUT")
            show_dicts()

    def show_all_words():
        try:
            os.system('clear||cls')
            show_logo()

            print("\n\t\t\t WORD COUNT\n\n")

            number = all_words()
            number = str(number)

            custom_fig = Figlet(font='catwalk')
            print(custom_fig.renderText("                        {}".format(number)))
            output = input('\n\t\t\t')
            show_menu()
            return dicts_logic(output)
        except ValueError:
            print("\n\t\tINVALID INPUT")
            show_menu()

    def dicts_logic(user_input):

        global dict_language, dict_name

        if user_input == 'q':
            show_menu()
        elif int(user_input) == 1:
            dict_name = 'ES.csv'
        elif int(user_input) == 2:
            dict_name = 'DE.csv'
        elif int(user_input) == 3:
            dict_name = 'FR.csv'
        elif int(user_input) == 4:
            dict_name = 'PL.txt'
        elif int(user_input) == 5:
            dict_name = 'THESESAURUS.csv'
        else:
            dict_name = 'PL.txt'

        dict_language = dict_name
        show_menu()

    def dict_sample_line(name):

        if name is None:
            file_name = 'dicts/PL.csv'
        else:
            file_name = 'dicts/{}'.format(name)

        count = len(open(file_name).readlines())
        n = random.randrange(1, count)
        try:
            line = open(file_name, 'r').readlines()[n]
            line = line.replace(';', '-')
            line = line.replace(',', '')
            line = line.replace('  ', ' ')
            line = line.replace('   ', ' ')
            line = line.replace('    ', ' ')
            line = line.replace('     ', ' ')
            line = line.replace('      ', ' ')
            line = line.replace('       ', ' ')

            output = line.title()
            return output
        except ValueError as e:
            print(e)

    def list_interface():

        os.system('clear||cls')

        word_count = len(user_words)

        print("*** WORD ************** EXPLANATION   ***   WORD NO {}   ****   PRESS 'q' TO QUIT   ***\n".format(
            word_count))
        print("***", dict_sample_line(dict_language))

        list_input()

    def show_hidden_word():

        # os.system('clear||cls')

        w = old_words()
        value = w[1]

        print("***", value)
        time.sleep(3)

    def distillations_interface():

        os.system('clear||cls')

        w = old_words()

        key = w[0]
        value = w[1]

        if w[1] is None:
            word_count = 0
            length = 0
        else:
            word_count = len(w)
            length = len(value)

        print("\n ***                  * D * I * S * T * I * L * L * A * T * I * O * N *                  ***")
        print("\n *** WORD   **************   EXPLANATION   ***   WORD NO {}   ****   PRESS 'q' TO QUIT   ***\n".format(
            word_count))
        print()
        print(" ***", str(key) + '   ', end='')

        for n in range(length):
            print("* ", end='')

        distillation_input()

    def distillation_input():

        data = login_data
        dict_word = old_words_list

        print('\n     ', end='')
        user_word = input()

        if user_word == "":
            show_hidden_word()
            distillations_interface()
        elif user_word == "q":
            print('list saved: ')
            show_menu()
        elif user_word == "l":
            print(load_lists(data[0]))
            time.sleep(3)
            list_interface()
        else:
            try:
                # splits user input into key word and explanation
                # adds date
                word = user_word.split(' ', 1)[0]
                explanation = user_word.split(' ', 1)[1]
                word = str(word.title())
                explanation = str(explanation.title())
                if dict_word[0] in user_words:
                    del user_words[dict_word[0]]

                else:
                    pass
                time_now = datetime.datetime.now()
                dist_list[word] = [explanation, time_now, data[0]]
                save_distilled_list(data[0], dist_list)
                save_lists(data[0], user_words)
                show_hidden_word()
                distillations_interface()


            except IndexError:
                print("\n\tEXPLANATION MUST NOT BE BLANK.")
                time.sleep(2)
                distillations_interface()

    # LOGIC

    # load and save files

    def load_logins():
        # Looks for login data files.
        try:
            file_object = open('logins.pydata', 'rb')
            data = pickle.load(file_object)
            file_object.close()
            return data
        # If file not found, creates temporary list to store login.
        except Exception as e:
            show_intro()
            return {}

    def save_logins(u, p, n_e):

        # Saves login data file

        username = u
        password = p
        name = n_e[0]
        email = n_e[1]

        logins[username] = password, name, email

        try:
            file_object = open('logins.pydata', 'wb')
            pickle.dump(logins, file_object)
            file_object.close()
        except Exception as e:
            print("\t\tNOT ABLE TO SAVE DATA.")
            print(e)

    def load_distilled_list(u):

        # Looks for user distilled lists file
        username = u
        file_name = "lists/distilled_{}.pydata".format(username)

        try:
            file_object = open(file_name, 'rb')
            my_list = pickle.load(file_object)
            file_object.close()

            return my_list

        except Exception as e:
            # print(e)
            # print("\t\tCREATING LOCAL LIST FILE")
            return {}

    def save_distilled_list(u, u_l):
        username = u
        user_list = u_l

        current_dir = os.getcwd()

        lists_dir = os.path.join(current_dir, r'lists')
        if not os.path.exists(lists_dir):
            os.makedirs(lists_dir)

        os.chdir(lists_dir)

        file_name = "distilled_{}.pydata".format(username)

        try:
            file_object = open(file_name, 'wb')
            pickle.dump(user_list, file_object)
            file_object.close()
        except Exception as e:
            print("\t\tUNABLE TO SAVE LIST FILE.")
            print(e)
        os.chdir('..')

    def load_lists(u):

        # Looks for user lists file
        username = u
        file_name = "lists/{}.pydata".format(username)

        try:
            file_object = open(file_name, 'rb')
            my_list = pickle.load(file_object)
            file_object.close()

            return my_list

        except Exception as e:
            # print(e)
            # print("\t\tCREATING LOCAL LIST FILE")
            return {}

    def save_lists(u, u_l):

        username = u
        user_list = u_l

        current_dir = os.getcwd()

        lists_dir = os.path.join(current_dir, r'lists')
        if not os.path.exists(lists_dir):
            os.makedirs(lists_dir)

        os.chdir(lists_dir)

        file_name = "{}.pydata".format(username)

        try:
            file_object = open(file_name, 'wb')
            pickle.dump(user_list, file_object)
            file_object.close()
        except Exception as e:
            print("\t\tUNABLE TO SAVE LIST FILE.")
            print(e)
        os.chdir('..')

    def all_words():
        words = load_lists(login_data[0])
        n = 0
        for word in words:
            n += 1
        return n

    def old_words():
        try:
            time_now = datetime.datetime.now()
            words = load_lists(login_data[0])
            oldest = min(words.values())
            key = None
            foo = []
            items = words.items()
            for item in items:
                if item[1] == oldest:
                    foo.append(item[0])

            word = {foo[0]: [oldest[0], oldest[1], oldest[2]]}
            for k in word.keys():
                key = k

            explanation = oldest[0]
            date = oldest[1]
            five_minutes = datetime.timedelta(minutes=30)
            if time_now - oldest[1] < five_minutes:
                key = 'NO OLD WORDS YET'
                explanation, date, word = None, None, None
            else:
                pass
                print(time_now - oldest[1])
            return key, explanation, date, word
        except ValueError:
            print("\n\t\t\tCOMPUTATION ERROR")

    def skill_levels():

        levels = [('Beginner', 1), ('Novice', 2), ('Neophyte', 3), ('Apprentice', 5), ('Bodger', 7),
                 ('Fellow', 11), ('Journeyman', 17), ('Practitioner', 25), ( 'Adept', 38), ('Expert', 57),
                 ('Scholar', 86), ('Erudite', 129), ('Master', 194), ('Savant', 291), ('Sage', 437),
                 ('Grand Master', 656), ('Provost', 985), ('Illuminatus', 1477), ('Epic', 2216), ('Doyen', 3325),
                 ('Maha Thera', 4987), ('God', 7481), ('Unreal', 11222)]

        
        """
        if distilled words == levels[0][1]:
            print(levels[0])"""

    # # # # # # # # #

    def login_logic():

        username = user_credentials[0]
        password = user_credentials[1]

        try:
            if len(username) < 3:
                print("\n\t\t\tINPUT MUST BE LONGER")
                time.sleep(2)
                show_login()
            if username not in logins:
                if password not in logins:
                    name_email = show_register()
                    save_logins(username, password, name_email)
                else:
                    print("\n\t\t\tusername or password incorrect")
                    time.sleep(2)
            else:
                load_lists(username)
                # load_dicts()
        except ValueError:

            print("\n\t\t\tINVALID INPUT")

        return username, password

    def menu_logic(u_i):

        option_input = u_i
        try:
            if option_input == "q":
                show_credits()
            elif option_input == "":
                list_interface()
            elif int(option_input) == 1:
                show_dicts()
            elif int(option_input) == 2:
                distillations_interface()
            elif int(option_input) == 3:
                show_all_words()
            elif int(option_input) == 4:
                show_help()
            else:
                print("\n\t\tINVALID INPUT")
                time.sleep(1)
                show_menu()
            os.system('clear||cls')
        except ValueError:
            print("\n\t\tINVALID INPUT")
            show_menu()

    def list_input():

        data = login_data

        print('\n\n   ', end=' ')
        user_word = input()

        if user_word == "":
            list_interface()
        elif user_word == "q":
            save_lists(data[0], user_words)
            print('list saved: ')
            show_menu()
        elif user_word == "l":
            print(load_lists(data[0]))
            time.sleep(3)
            list_interface()
        else:
            try:
                # splits user input into key word and explanation
                # adds date

                word = user_word.split(' ', 1)[0]
                explanation = user_word.split(' ', 1)[1]
                word = str(word.title())
                explanation = str(explanation.title())
                time_now = datetime.datetime.now()
                user_words[word] = [explanation, time_now, data[0]]
                list_interface()

            except IndexError:
                print("\n\tEXPLANATION MUST NOT BE BLANK.")
                time.sleep(2)
                list_interface()

    def show_account():
        os.system("clear||cls")

        show_logo()

        print("CURRENT LEVEL: ")

    show_book()
    logins = load_logins()
    user_credentials = show_login()

    # dict_dataFrame = load_dicts()

    # word_explanation = load_words()  # (word, explanation)
    login_data = login_logic()  # (username, password)
    user_words = load_lists(login_data[0])
    old_words_list = old_words()
    dist_list = load_distilled_list(login_data[0])
    current_list = {}

    show_menu()


if __name__ == '__main__':
    main()






