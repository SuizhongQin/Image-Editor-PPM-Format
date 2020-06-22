from image_editor import extreme_contrast

def test_passing():
    assert extreme_contrast([[255, 0, 0]]) == [[255, 0, 0]]
    assert extreme_contrast([[0, 255, 7]]) == [[0, 255, 0]]
    assert extreme_contrast([[9, 9, 10], [100, 255, 0]]) == [[0, 0, 0], [0, 255, 0]]
    assert extreme_contrast([[126, 255, 127]]) == [[0, 255, 255]]

def test_not_passing():
    assert extreme_contrast([[255, 0, 0]]) != [[0, 0, 0]]
    assert extreme_contrast([[2, 0, 0]]) != []
    assert extreme_contrast([[9, 9, 100]]) != [[255, 0, 0]]
