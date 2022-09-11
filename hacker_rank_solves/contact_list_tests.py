from contact_list import contacts


def test_contacts():
    result = contacts([['add', 'hack'], ['add', 'hackerrank'], ['find', 'hac'], ['find', 'hak']])
    assert result != [2, 1, 0]
    assert result == [2, 0]


test_contacts()
