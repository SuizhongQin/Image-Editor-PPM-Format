from image_editor import negative_green

def test_passing():
    assert negative_green([[255, 0, 0]]) == [[255, 255, 0]]
    assert negative_green([[0, 255, 7]]) == [[0, 0, 7]]
    assert negative_green([[9, 9, 10], [100, 255, 0]]) == [[9, 255 - 9, 10], [100, 0, 0]]

def test_not_passing():
    assert negative_green([[255, 0, 0]]) != [[0, 4, 0]]
    assert negative_green([[2, 0, 0]]) != []
    assert negative_green([[9, 9, 100]]) != [[9, 9, 9]]
