from src.utils.common import CommonUtils
from src.state.State import State

c = CommonUtils()

c.greet_user()

while input('Type a command and press ENTER: ') != 'exit':
    State.set_state({'name': 'Sayantan', 'age': 25})
    print(State.get('name'))
