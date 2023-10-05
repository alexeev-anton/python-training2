from sys import maxsize


class Contact:
    def __init__(self, firstname=None, middlename=None, lastname=None, id=None,
                 address=None, phonehome=None, phonemobile=None, phonework=None,
                 phonefax=None, phone2=None, email=None, email2=None, email3=None, bday=None, bmonth=None, byear=None,
                 all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.address = address
        self.phonehome = phonehome
        self.phonemobile = phonemobile
        self.phonework = phonework
        self.phonefax = phonefax
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.bday = bday
        self.bmonth = bmonth
        self.byear = byear
        self.phone2 = phone2
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page


    def __repr__(self):
        return "%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s:%s" % \
            (self.id, self.lastname, self.firstname, self.email, self.email3, self.email2, self.address, self.phonefax,
             self.phonework, self.phonemobile, self.phonehome, self.phone2, self.middlename)


    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) \
            and self.firstname == other.firstname and self.lastname == other.lastname


    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
