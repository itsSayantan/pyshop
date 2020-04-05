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
        print('+++++ WELCOME TO PyShop +++++')
        print('Enter command help to get list of avaible commands and exit to exit the application.')
