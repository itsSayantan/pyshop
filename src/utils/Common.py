from os import system, name


class CommonUtils:
    @classmethod
    def clear_screen(cls):
        # clear the screen
        if name == 'nt':
            # windows
            system('cls')
        else:
            # mac and linux
            system('clear')

    @classmethod
    def greet_user(cls):
        cls.clear_screen()
        print('+++++ Welcome to PyShop +++++\n')
        print('Enter command \'help\' to get list of avaible commands and \'exit\' to exit the application.')
