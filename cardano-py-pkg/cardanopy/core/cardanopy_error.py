

class CardanoPyError(Exception):
    message: None
    return_code: 0

    def __init__(self, message: str, return_code: int = 0):
        self.message = message
        self.return_code = return_code
