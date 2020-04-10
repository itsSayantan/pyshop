import csv
from os import path
from ..utils.Error import ErrorUtils
from ..state.State import State

class PurchaseCommand:
    def execute(command_arguments=None):
        if isinstance(command_arguments, list) == True and len(command_arguments) == 1:
            # read from products.csv file and check if product name exists
            file_path_dict = State.get('file_path_dict')

            fpd_entry = file_path_dict.get('products')
            
            if path.exists(fpd_entry.get('file_path')) == True:
                # products.csv exists

                with open(fpd_entry.get('file_path'), newline='') as csvfile:
                    # skip the first line
                    next(csvfile)

                    reader = csv.reader(csvfile, delimiter='|')
                    
                    for row in reader:
                        # check if the name of the product (row[1]) matches with the sent product name
                        if row[1] == command_arguments[0]:
                            # product name match, print that the prouct has been purchased as of now
                            print('\nSuccess --> The product {} has been purchased.'.format(command_arguments[0]))
                            return
                    
                    # there was no match with the product name
                    return ErrorUtils('PRODUCT_NOT_FOUND', 'The entered product name was not found.')
            else:
                print(ErrorUtils('PRODUCTS_DATASET_MISSING', 'The product dataset is missing. Please restart the application.').get_error())
        else:
            return ErrorUtils('PURCHASE_COMMAND_INVALID_ARGS', 'Invalid arguments sent to the \'purchase\' command. The correct syntax is: \'purchase <product_name>\'')