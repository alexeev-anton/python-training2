import random

from model.contact import Contact
from model.group import Group


def test_add_contact_in_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.init_group_creation()
        app.group.fill_group_form(Group(name="test2", header="header", footer="footer"))
        app.group.submit_group_creation()
    if len(db.get_contact_list()) == 0:
        app.contact.create_contact(Contact(firstname="firstname", lastname="lastname", address="address",
                                           phonehome="111111", phonemobile="222222", phonework="333333",
                                           phone2="444444", email="test@test.com", email2="test2@test.com",
                                           email3="test3@test.com"))
    list_groups = db.get_group_list()
    group0 = random.choice(list_groups)
    old_list = db.get_contacts_in_group(group0.id)
    add_list = db.get_contacts_not_in_group(group0.id)
    if len(add_list) == 0:
        app.contact.create_contact(Contact(firstname="firstname", lastname="lastname", address="address",
                                           phonehome="111111", phonemobile="222222", phonework="333333",
                                           phone2="444444", email="test@test.com", email2="test2@test.com",
                                           email3="test3@test.com"))
        add_list = db.get_contacts_not_in_group(group0.id)
    contact0 = random.choice(add_list)
    app.contact.add_contact_to_group_by_id(contact0.id, group0.id)
    new_list = db.get_contacts_in_group(group0.id)
    old_list.append(contact0)
    assert sorted(old_list, key=Group.id_or_max) == sorted(new_list, key=Group.id_or_max)
