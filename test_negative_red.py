from image_editor import negative_red

def test_passing():
    assert negative_red([[255, 0, 0]]) == [[0, 0, 0]]
    assert negative_red([[0, 255, 7]]) == [[255, 255, 7]]
    assert negative_red([[9, 9, 10]]) == [[255 - 9, 9, 10]]

def test_not_passing():
    assert negative_red([[255, 0, 0]]) != [[0, 4, 0]]
    assert negative_red([[2, 0, 0]]) != []
    assert negative_red([[9, 9, 100]]) != [[9, 9, 9]]
