from os import path
import csv

USERS_FILE_PATH = './data/users.csv'
USERS_TEMPLATE_FILE_PATH = './data/users.template.csv'


class DataOperations:
    def create_user_dataset():
        with open(USERS_TEMPLATE_FILE_PATH, newline='') as csvfile:
            reader = csv.reader(
                csvfile, delimiter='|')
            """
                We are only interested with the first line of this file.
                Hence, we are using the counter approach.
            """
            count = 0
            for row in reader:
                if count != 0:
                    break
                else:
                    """
                        Create the users.csv file if it does not exist with the columns same as 'row'.
                    """
                    if path.exists(USERS_FILE_PATH) == True:
                        # do not create a new file
                        return
                    else:
                        # create a new file
                        with open(USERS_FILE_PATH, 'w', newline='') as csvfileforwriting:
                            csvwriter = csv.writer(
                                csvfileforwriting, delimiter='|', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                            firstrow = [row]
                            csvwriter.writerows(firstrow)
                            return
