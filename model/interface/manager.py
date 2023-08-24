import datetime
from abc import ABC, abstractmethod
from typing import List, Tuple, Union

from model.interface.entity import Entry, Person, OperationStatus


class AbstractEntryManager(ABC):
    @abstractmethod
    def add(self, entry: Entry) -> OperationStatus:
        """
        Add new Entry to storage
        :param entry: the entry to be added
        """
        pass

    def get(self, from_date: datetime.datetime, to_date: datetime.datetime) -> Tuple[OperationStatus, List[Entry]]:
        """
        Gets list of Entries in the specified range
        :param from_date: start of the range (including)
        :param to_date: end of the range (including)
        :return: Tuple, where first is result of operation and second is list of entries
        """
        pass

    def edit(self, edit: Entry, new: Entry) -> OperationStatus:
        """
        Finds entry in storage and replace it to new
        :param edit: entry to be edited
        :param new: new entry that will replace old one
        """
        pass

    def delete(self, entry: Entry) -> OperationStatus:
        """
        Deletes entry from storage.
        :param entry: entry to be deleted
        """
        pass
