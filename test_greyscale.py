from image_editor import greyscale

def test_passing():
    assert greyscale([[255, 0, 0]]) == [[85, 85, 85]]
    assert greyscale([[2, 0, 0]]) == [[0, 0, 0]]
    assert greyscale([[9, 9, 10]]) == [[9, 9, 9]]

def test_not_passing():
    assert greyscale([[255, 0, 0]]) != [[0, 0, 0]]
    assert greyscale([[2, 0, 0]]) != []
    assert greyscale([[9, 9, 100]]) != [[9, 9, 9]]
