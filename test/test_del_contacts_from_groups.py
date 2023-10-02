import random

from model.contact import Contact
from model.group import Group


def test_del_contact_from_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.init_group_creation()
        app.group.fill_group_form(Group(name="name", header="header", footer="footer"))
        app.group.submit_group_creation()
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="firstname", lastname="lastname", address="address",
                                           phonehome="111111", phonemobile="222222", phonework="333333",
                                           phone2="444444", email="test@test.com", email2="test2@test.com",
                                           email3="test3@test.com"))
    old_contacts = db.get_contact_list()
    old_groups = db.get_group_list()
    contact0 = random.choice(old_contacts)
    group0 = random.choice(old_groups)
    old_list = db.get_contacts_in_group(group0.id)
    if len(db.get_contacts_in_group(group0.id)) == 0:
        app.contact.add_contact_to_group_by_id(contact0.id, group0.id)
    old_list = db.get_contacts_in_group(group0.id)
    contact0 = random.choice(old_list)
    app.contact.delete_contact_from_group_by_id(contact0.id, group0.id)
    old_list.remove(contact0)
    new_list = db.get_contacts_in_group(group0.id)
    assert old_list == new_list
