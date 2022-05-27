class CustomBaseException(Exception):
    pass


class UnacceptableHourError(CustomBaseException):
    pass


class UnacceptableMinuteError(CustomBaseException):
    pass


class UnacceptableIntervalError(CustomBaseException):
    pass
