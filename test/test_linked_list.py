from linked_list import LinkedList

ls1 = LinkedList()

def test_append():
    tested_list = LinkedList()
    actual = tested_list.append(2)
    expected = True
    assert actual == expected


def test_delete():
    tested_list = LinkedList()
    tested_list.append(7)
    actual = tested_list.delete_node(7)
    expected = True
    assert actual == expected

print(ls1)

def test_get_item():
    tested_list = LinkedList()

    tested_list.append(16)
    tested_list.append(17)
    tested_list.append(18)


    actual = tested_list[1]
    expected = 17
    assert actual == expected


def test_len():
    tested_list = LinkedList()

    tested_list.append(1)
    tested_list.append(2)
    tested_list.append(3)
    tested_list.append(4)
    tested_list.append(5)

    actual = len(tested_list)
    expected = 5
    assert actual == expected
