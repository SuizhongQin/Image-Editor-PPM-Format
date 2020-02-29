from image_editor import negative_blue

def test_passing():
    assert negative_blue([[255, 0, 0]]) == [[255, 0, 255]]
    assert negative_blue([[0, 255, 7]]) == [[0, 255, 255 - 7]]
    assert negative_blue([[9, 9, 10]]) == [[9, 9, 255 - 10]]

def test_not_passing():
    assert negative_blue([[255, 0, 0]]) != [[0, 4, 0]]
    assert negative_blue([[2, 0, 0]]) != []
    assert negative_blue([[9, 9, 100]]) != [[9, 9, 9]]
