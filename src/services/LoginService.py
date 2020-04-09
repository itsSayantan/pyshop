from os import path

from ..utils.Error import ErrorUtils

from ..state.State import State

import csv


class LoginService:
    def verify_username(username):
        file_path_dict = State.get('file_path_dict')
        upd = file_path_dict.get('users')

        # check if users.csv exists
        if path.exists(upd.get('file_path')) == True:
            # users.csv exists, read the file

            with open(upd.get('file_path'), newline='') as userscsvfile:
                # skip the first line as it contains the csv headers
                next(userscsvfile)

                reader = csv.reader(userscsvfile, delimiter='|')

                for row in reader:
                    # check of the value in the username column of this row matches the given username
                    if row[1] == username:
                        # match, return
                        return
                    else:
                        # no match, keep on searcing
                        continue

                # no match
                return ErrorUtils('USERNAME_NOT_FOUND', 'Username was not found in the data store.')
        else:
            return ErrorUtils('USER_DATA_FILE_MISSING', 'The user data file is missing. Please restart the application.')

        # read the users.csv file and check if username exists
