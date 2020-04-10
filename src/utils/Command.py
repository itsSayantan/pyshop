from .Error import ErrorUtils
from ..state.CommandState import CommandState

class CommandUtils:
    def create_command(raw_command_string=None):
        if raw_command_string == None or len(raw_command_string.strip()) == 0:
            return ErrorUtils('COMMAND_STRING_EMPTY', 'Command string cannot be empty.')
        else:
            parsed_command = raw_command_string.split(' ')
            return { 'main_command': parsed_command[0], 'command_arguments': parsed_command[1:] }

    def execute_command(command=None):
        main_command = command.get('main_command')
        command_arguments = command.get('command_arguments')

        if isinstance(main_command, str) and isinstance(command_arguments, list):
            # check if the command is present in the commands dictionary in the command state
            command = CommandState.get('commands').get(main_command)

            if command != None:
                # execute the corresponding command in the commands dictionary
                return command(command_arguments)
            else:
                return ErrorUtils('COMMAND_NOT_FOUND', 'The command {} was not found.'.format(main_command))
        else:
            return ErrorUtils('INVALID_COMMAND', 'Type a valid command and then press ENTER key. Execute command \'help\' to get the list of available commands.')