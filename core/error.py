class DuplicateResourceException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg

class InvalidValueException(Exception):
    def __init__(self, msg):
        super().__init__(msg)
        self.msg = msg