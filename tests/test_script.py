import script.uzbek_latin_cyrillic_converter as converter


def test_get_cyrillic_or_same_char():
    param0 = ('s', True)
    expected0 = (1, 'с')
    assert expected0 == converter.get_cyrillic_or_same_char(*param0)

    param1 = ('S', True)
    expected1 = (1, 'С')
    assert expected1 == converter.get_cyrillic_or_same_char(*param1)

    param2 = ('e', True)
    expected2 = (1, 'э')
    assert expected2 == converter.get_cyrillic_or_same_char(*param2)

    param3 = ('E', True)
    expected3 = (1, 'Э')
    assert expected3 == converter.get_cyrillic_or_same_char(*param3)

    param4 = ('e', False)
    expected4 = (1, 'е')
    assert expected4 == converter.get_cyrillic_or_same_char(*param4)

    param5 = ('E', False)
    expected5 = (1, 'Е')
    assert expected5 == converter.get_cyrillic_or_same_char(*param5)


def test_get_space_or_value_from_two_letters_down():
    param0 = ('s', 'h', True)
    expected0 = (2, 'ш')
    assert expected0 == converter.get_space_or_value_from_two_letters_down(*param0)

    param1 = ('S', 'h', True)
    expected1 = (2, 'Ш')
    assert expected1 == converter.get_space_or_value_from_two_letters_down(*param1)

    param2 = ('o', '\'', True)
    expected2 = (2, 'ў')
    assert expected2 == converter.get_space_or_value_from_two_letters_down(*param2)

    param3 = ('O', '\'', True)
    expected3 = (2, 'Ў')
    assert expected3 == converter.get_space_or_value_from_two_letters_down(*param3)

    param4 = ('o', '‘', True)
    expected4 = (2, 'ў')
    assert expected4 == converter.get_space_or_value_from_two_letters_down(*param4)

    param5 = ('O', '‘', True)
    expected5 = (2, 'Ў')
    assert expected5 == converter.get_space_or_value_from_two_letters_down(*param5)

    param6 = ('g', '\'', True)
    expected6 = (2, 'ғ')
    assert expected6 == converter.get_space_or_value_from_two_letters_down(*param6)

    param7 = ('G', '\'', True)
    expected7 = (2, 'Ғ')
    assert expected7 == converter.get_space_or_value_from_two_letters_down(*param7)

    param8 = ('s', 'n', True)
    expected8 = (1, 'с')
    assert expected8 == converter.get_space_or_value_from_two_letters_down(*param8)


def test_get_space_or_value_from_three_letters_down():
    param0 = ('y', 'o', '\'', True)
    expected0 = (3, 'йў')
    assert expected0 == converter.get_space_or_value_from_three_letters_down(*param0)

    param1 = ('Y', 'o', '\'', True)
    expected1 = (3, 'Йў')
    assert expected1 == converter.get_space_or_value_from_three_letters_down(*param1)

    param2 = ('y', 'o', '‘', True)
    expected2 = (3, 'йў')
    assert expected2 == converter.get_space_or_value_from_three_letters_down(*param2)

    param3 = ('s', 'h', 'j', True)
    expected3 = (2, 'ш')
    assert expected3 == converter.get_space_or_value_from_three_letters_down(*param3)

    param4 = ('o', 'b', 'd', True)
    expected4 = (1, 'о')
    assert expected4 == converter.get_space_or_value_from_three_letters_down(*param4)


def test_latin_to_cyrillic():
    assert 'салом' == converter.latin_to_cyrillic('salom')
    assert 'Йўқ' == converter.latin_to_cyrillic("Yo'q")
