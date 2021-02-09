class BoardException(Exception):
    pass

class BoardOutException(BoardException):
    def __str__(self):
        return "Shot out of the battlefield!"

class BoardUsedException(BoardException):
    def __str__(self):
        return "You have already shot at these coordinates!"

class BoardWrongShipException(BoardException):
    pass
