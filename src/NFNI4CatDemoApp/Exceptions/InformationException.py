
class MissingDataException(Exception):
    def __init__(self, message, error_code):
        self.error_code = error_code
        self.message = message

    def __str__(self):
        return f"Error Code: {self.error_code} \n {self.message}"