"""
    This class is responsible to store the entire state of the PyShop application.
"""

class State:
    """
        The __state value should not be accessed directly,
        instead the get() method should be used.
    """
    __state = {
        'file_path_dict': {
            'users': {
                'file_path': './data/users.csv',
                'template_file_path': './data/users.template.csv',
            },
            'products': {
                'file_path': './data/products.csv',
                'template_file_path': './data/products.template.csv',
            },
        }
    }

    @classmethod
    def set_state(cls, part_of_the_state_to_be_updated):
        """
            This method updates the state.

            This method does not overwrite the state completely.
            It checks whether the part_of_the_state_to_be_updated is there in
            the current state or not. If it is present, it will rewrite that part,
            else it will create a new entry in the top level of the state.
        """

        for new_state_key in part_of_the_state_to_be_updated:
            cls.__state.setdefault(
                new_state_key, part_of_the_state_to_be_updated[new_state_key])

    @classmethod
    def get(cls, key):
        return cls.__state.get(key)
