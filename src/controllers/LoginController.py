from ..services.LoginService import LoginService

from ..utils.Error import ErrorUtils


class LoginController:
    def initiateLoginFlow():
        # show message
        print('\n+++++ LOGIN +++++\n')

        # take username input
        username = input('Enter username: ')

        # validate username input
        if len(username.strip()) == 0:
            return ErrorUtils('INVALID_USERNAME_INPUT', 'Please enter a valid username,')

        # verify whether username exists in the users dataset

        response = LoginService.verify_username(username)

        if isinstance(response, ErrorUtils) == True:
            # login unsuccessful because of some reason
            return response
