from Midterm import area_of_circle, inverted_pyramid, hollow_right_triangle

# Test Q1: area_of_circle
def test_area_of_circle():
    assert area_of_circle(5) == 78.54
    assert area_of_circle(3) == 28.27
    assert area_of_circle(0) == 0.0
    assert area_of_circle(10) == 314.16
    
# Test Q2: hollow_right_triangle
def test_hollow_right_triangle():
    assert hollow_right_triangle(1) == "The triangle height should be at least 4."
    assert hollow_right_triangle(4) == "*\n**\n* *\n****"
    assert hollow_right_triangle(5) == "*\n**\n* *\n*  *\n*****"

# Test Q3: inverted_pyramid
def test_inverted_pyramid():
    assert inverted_pyramid(2) == "The pyramid height should be at least 3."
    assert inverted_pyramid(3) == "*****\n ***\n  *"
    assert inverted_pyramid(5) == "*********\n *******\n  *****\n   ***\n    *"


# Run tests
if __name__ == "__main__":
    test_area_of_circle()
    test_inverted_pyramid()
    test_hollow_right_triangle()
    print("All tests passed!")

