from random import randrange

from model.contact import Contact


def test_modify_contact(app, db, check_ui):
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(
            Contact(firstname="firstname", middlename="middlename", lastname="lastname", address="address", phonehome="111111",
                    phonemobile="222222", phonework="333333", phonefax="444444", email="test@test.com"))
    old_contacts = db.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="firstname1", middlename="middlename1", lastname="lastname1", address="address1", phonehome="555555",
                      phonemobile="666666")
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_id(contact.id, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = db.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
