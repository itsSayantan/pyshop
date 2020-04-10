class ErrorUtils:
    def __init__(self, error_type, error_message):
        self.error_type = error_type
        self.error_message = error_message

    def get_error_type(self):
        return self.error_type

    def get_error(self):
        return self.error_type + ': ' + self.error_message
