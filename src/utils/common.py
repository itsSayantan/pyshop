from os import system, name


class CommonUtils:
    def greet_user(self):
        # clear the screen
        if name == 'nt':
            # windows
            system('cls')
        else:
            # mac and linux
            system('clear')
        print('+++++ WELCOME TO PYSHOP +++++')
