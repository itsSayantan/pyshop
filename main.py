from src.state.State import State
from src.utils.Common import CommonUtils
from src.utils.Data import DataUtils
from src.utils.Error import ErrorUtils


class Main:
    def initialize_application():
        # try to create the data files
        response = DataUtils.create_dataset(['users'])

        if isinstance(response, ErrorUtils) == True:
            print(response.get_error())

        # initiate the login flow


Main.initialize_application()
c = CommonUtils()

# c.greet_user()

while input('\nType a command and press ENTER: ') != 'exit':
    State.set_state({'name': 'Sayantan', 'age': 25})
    print(State.get('name'))
