class InvalidInputException(Exception):
    """ Raised when unit is not a number """


class InvalidMonthException(Exception):
    """ Raised when months is < 1 or > 12 """


class InvalidPhaseException(Exception):
    """ Raised when phase input is NOT correct """


class InvalidUnitException(Exception):
    """ Raised when Unit input is NOT valid """
