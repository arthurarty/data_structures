from contact_list_dics import contacts


def test_contacts():
    result = contacts([['add', 'hack'], ['add', 'hackerrank'], ['find', 'hac'], ['find', 'hak']])
    assert result != [2, 1, 0]
    assert result == [2, 0]


test_contacts()


def test_similar_characters():
    result = contacts([
        ['add', 's'],
        ['add', 'ss'],
        ['add', 'sss'],
        ['add', 'ssss'],
        ['add', 'sssss'],
        ['find', 's'],
        ['find', 'ss'],
        ['find', 'sss'],
        ['find', 'ssss'],
        ['find', 'sssss'],
        ['find', 'ssssss']
    ])
    assert result == [5, 4, 3, 2, 1, 0]


test_similar_characters()
