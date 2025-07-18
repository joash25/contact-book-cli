class Contact:
    """
    Represents a single contact in a list of contacts.
    
    Each contact has:
    - a `name` property that represents the contact's name
    - a `phone` property that represents the contact's phone number
    - an `email` property that represents the contact's email address
    """
    def __init__(self, name: str, phone: str, email: str):
        self.name: str = name
        self.phone: str = phone
        self.email: str = email

    def to_dict(self) -> dict:
        """
        Returns the contact as a dictionary.
        """
        return {"name": self.name, "phone": self.phone, "email": self.email}