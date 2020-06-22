from image_editor import only_green

def test_passing():
    assert only_green([[255, 0, 0]]) == [[0, 0, 0]]
    assert only_green([[0, 255, 7]]) == [[0, 255, 0]]
    assert only_green([[9, 9, 10]]) == [[0, 9, 0]]

def test_not_passing():
    assert only_green([[255, 0, 0]]) != [[0, 4, 0]]
    assert only_green([[2, 0, 0]]) != []
    assert only_green([[9, 9, 100]]) != [[9, 9, 9]]
