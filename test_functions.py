def test_find_y():
    from function import find_y
    assert find_y((0, 0), (2, 2), 1) == 1

def test_is_on_line():
    from function import is_on_line
    assert is_on_line((0, 0), (2, 2), (1, 1)) == True
    assert is_on_line((0, 0), (2, 2), (1, 2)) == False
