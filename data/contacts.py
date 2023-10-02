import random
import string

from model.contact import Contact

contact = [
    Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1",
            address="address1", phonehome="phonehome1", phonemobile="phonemobile1",
            phonework="phonework1", phonefax="phonefax1", email="", email2="", email3="")
]


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join(
        [random.choice(symbols) for i in range(random.randrange(maxlen))])


testdata = [Contact(firstname="", middlename="", lastname="", address="", phonehome="", phonemobile="",
                    phonework="", phonefax="", email="", email2="", email3="")] + [
               Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 10),
                       lastname=random_string("lastname", 10), address=random_string("address", 10),
                       phonehome=random_string("phonehome", 10), phonemobile=random_string("address", 10),
                       phonework=random_string("phonework", 10), phonefax=random_string("phonefax", 10),
                       email=random_string("email", 10), email2=random_string("email2", 10),
                       email3=random_string("email3", 10))
               for i in range(5)]
