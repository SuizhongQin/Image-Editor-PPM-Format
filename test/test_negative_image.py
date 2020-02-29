from image_editor import negative_image

def test_passing():
    assert negative_image([[255, 0, 0]]) == [[0, 255, 255]]
    assert negative_image([[0, 255, 7]]) == [[255, 0, 255 - 7]]
    assert negative_image([[9, 9, 10], [100, 255, 0]]) == [[255 - 9, 255 - 9, 255 - 10], [255 - 100, 0, 255]]

def test_not_passing():
    assert negative_image([[255, 0, 0]]) != [[0, 4, 0]]
    assert negative_image([[2, 0, 0]]) != []
    assert negative_image([[9, 9, 100]]) != [[9, 9, 9]]
