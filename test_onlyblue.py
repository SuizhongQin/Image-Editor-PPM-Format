from image_editor import only_blue

def test_passing():
    assert only_blue([[255, 0, 0]]) == [[0, 0, 0]]
    assert only_blue([[2, 55, 44]]) == [[0, 0, 44]]
    assert only_blue([[9, 55, 10]]) == [[0, 0, 10]]

def test_not_passing():
    assert only_blue([[255, 0, 0]]) != [[0, 255, 0]]
    assert only_blue([[2, 0, 0]]) != []
    assert only_blue([[9, 9, 100]]) != [[9, 9, 9]]
