# Built-in
import csv

# My Module
from .contact import Contact

class ContactManager:
    """
    Represents a manager for a list of contacts.
    """
    def __init__(self, csvfilename: str, fieldnames: list[str]):
        self.csvfilename: str = csvfilename
        self.fieldnames: list[str] = fieldnames
        self.contacts: list[Contact] = []

    def add(self, contact: Contact):
        """
        Adds a contact to the contact list.
        """
        with open(self.csvfilename, "a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, self.fieldnames)
            writer.writerow(contact.to_dict())
            self.contacts.append(contact)