import datetime


class Person:
    """Describes person object (admin, client etc)"""
    def __init__(self,
                 surname: str,
                 name: str,
                 patronymic: str,
                 birthday: datetime.date,
                 phone: int,
                 comment: str):
        self.surname = surname
        self.name = name
        self.patronymic = patronymic
        self.birthday = birthday
        self.phone = phone
        self.comment = comment


class Entry:
    """Describes the Entry on service object"""
    def __init__(self,
                 time: datetime.datetime,
                 client: Person,
                 service: str):
        self.time = time
        self.client = client
        self.service = service


class OperationStatus:
    """Describes the result of the requester operation """
    def __init__(self,
                 success: bool,
                 message: str,
                 error: Exception):
        self.success = success
        self.message = message
        self.error = error
