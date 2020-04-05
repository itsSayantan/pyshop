from src.state.State import State

from src.utils.Common import CommonUtils
from src.utils.Data import DataUtils
from src.utils.Error import ErrorUtils

from src.controllers.LoginController import LoginController


class Main:
    def initialize_application():
        # try to create the data files
        response = DataUtils.create_dataset(['users'])

        if isinstance(response, ErrorUtils) == True:
            print(response.get_error())

        # initiate the login flow
        login_res = LoginController.initiateLoginFlow()

        if isinstance(login_res, ErrorUtils) == True:
            print(login_res.get_error())


# show initial greeting message and initialize the application
c = CommonUtils()
c.greet_user()

Main.initialize_application()

while input('\nType a command and press ENTER: ') != 'exit':
    State.set_state({'name': 'Sayantan', 'age': 25})
    print(State.get('name'))
