class InputArgumentsError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message
    def __str__(self):
        return f'Error {self.code}: {self.message}'
