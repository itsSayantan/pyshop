import sys
from src.state.State import State

from src.utils.Common import CommonUtils
from src.utils.Data import DataUtils
from src.utils.Error import ErrorUtils
from src.utils.Command import CommandUtils

from src.controllers.LoginController import LoginController

class Main:
    def initialize_application():
        # try to create the data files
        r1 = DataUtils.create_dataset(['users', 'products'])

        if isinstance(r1, ErrorUtils) == True:
            print(response.get_error())

            sys.exit()
        else:
            # remove this in the later version
            r2 = DataUtils.populate_dummy_data()

            if isinstance(r1, ErrorUtils) == True:
                print(response.get_error())

                sys.exit()
            else:
                # dataset creation successful
                # initiate the login flow

                login_res = LoginController.initiateLoginFlow()

                while isinstance(login_res, ErrorUtils) == True:
                    print(login_res.get_error())

                    login_res = LoginController.initiateLoginFlow()




# show initial greeting message and initialize the application
c = CommonUtils()
c.greet_user()

Main.initialize_application()

while True:
    raw_command_input = input('\nType a command and press ENTER: ')

    # sanitize the input - for future release

    # parse raw command
    r1 = CommandUtils.create_command(raw_command_input)

    if isinstance(r1, ErrorUtils) == True:
        if r1.get_error_type() == 'COMMAND_STRING_EMPTY':
            print(r1.get_error())
            continue
        sys.exit()
    else:
        # execute the parsed command
        r2 = CommandUtils.execute_command(r1)
        if isinstance(r2, ErrorUtils):
            print(r2.get_error())
