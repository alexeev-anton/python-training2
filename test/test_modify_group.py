from random import randrange

from model.group import Group


def test_modify_group_name(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.init_group_creation()
        app.group.fill_group_form(Group(name="group"))
        app.group.submit_group_creation()
    old_groups = db.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="group_upd")
    group.id = old_groups[index].id
    app.group.modify_group_by_id(group.id, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)