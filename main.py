from src.state.State import State
from src.utils.common import CommonUtils
from src.utils.data import DataOperations


class Main:
    def initialize_application():
        # try to create the data files
        DataOperations.create_user_dataset()
        # initiate the login flow


Main.initialize_application()
c = CommonUtils()

# c.greet_user()

while input('\nType a command and press ENTER: ') != 'exit':
    State.set_state({'name': 'Sayantan', 'age': 25})
    print(State.get('name'))
