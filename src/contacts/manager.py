class ContactManager:
    """
    Represents a manager for a list of contacts.
    """
    def __init__(self, csvfilename: str, fieldnames: list):
        self.csvfilename: str = csvfilename
        self.fieldnames: list = fieldnames