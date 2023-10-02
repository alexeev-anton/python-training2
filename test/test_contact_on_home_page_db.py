import re

from model.contact import Contact


def test_contact_on_home_page_db(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="firstname", lastname="lastname", address="address",
                                           phonehome="111111", phonemobile="222222", phonework="333333",
                                           phonefax="444444", email="test@test.com"))
    db_contacts = sorted(db.get_contact_list(), key=Contact.id_or_max)
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    assert len(db_contacts) == len(contacts_from_home_page)
    for i in range(len(db_contacts)):
        print(str(i))
        print(db_contacts[i])
        print(contacts_from_home_page[i])

    for i in range(len(db_contacts)):
        assert db_contacts[i].id == contacts_from_home_page[i].id
        assert db_contacts[i].firstname == contacts_from_home_page[i].firstname
        assert db_contacts[i].lastname == contacts_from_home_page[i].lastname
        assert db_contacts[i].address == contacts_from_home_page[i].address
        assert merge_phones_like_home_page(db_contacts[i]) == contacts_from_home_page[i].all_phones_from_home_page
        assert merge_emails_like_home_page(db_contacts[i]) == contacts_from_home_page[i].email


def clear_phones(s):
    return re.sub("[()/ -]", "", s)


def merge_phones_like_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: clear_phones(x), filter(lambda x: x is not None,
                                                                                     [contact.phonehome, contact.phonemobile, contact.phonework, contact.phone2]))))


def merge_emails_like_home_page(contact):
    return "\n".join(filter(lambda x: x != "", map(lambda x: x, filter(lambda x: x is not None,
                                                                       [contact.email, contact.email2, contact.email3]))))
