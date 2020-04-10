from ..utils.Common import CommonUtils

class HelpCommand:
    def execute(command_arguments=None):
        CommonUtils.clear_screen()

        print('************************************')
        print('*********** PYSHOP HELP ************')
        print('************************************\n')
        print('List of available commands:\n')
        print(' - exit --> Exit the PyShop application.')
        print(' - help --> Lists all available commands.')
        print(' - purchase <product_name> --> Makes a purchase of the product named <product_name>.')