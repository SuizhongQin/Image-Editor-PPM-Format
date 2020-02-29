from image_editor import only_red

def test_passing():
    assert only_red([[255, 0, 0]]) == [[255, 0, 0]]
    assert only_red([[2, 2, 2]]) == [[2, 0, 0]]
    assert only_red([[9, 9, 10]]) == [[9, 0, 0]]

def test_not_passing():
    assert only_red([[255, 0, 0]]) != [[0, 0, 0]]
    assert only_red([[2, 0, 0]]) != []
    assert only_red([[9, 9, 100]]) != [[9, 9, 9]]
