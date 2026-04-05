def a_triangle(sides):
    """Defines a triangle based on the rules of being a triangle.

    param -sides defined by side_a, side_b, side_c
    """
    side_a, side_b, side_c = sides
    return all(sides > 0 for sides in sides) and side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a


def equilateral(sides):
    """Defines an equilateral triangle.

    param -sides defined by side_a, side_b, side_c
    """
    side_a, side_b, side_c = sides
    if not a_triangle(sides):
        return False
    if side_a == side_b == side_c:
        return True
    return False
    

def isosceles(sides):
    """Defines an isosceles triangle.

    param -sides defined by side_a, side_b, side_c
    """
    side_a, side_b, side_c = sides
    if not a_triangle(sides):
        return False
    if side_a == side_b or side_b == side_c or side_c == side_a:
        return True
    return False
        
    
def scalene(sides):
    """Defines a scalene triangle.

    param -sides defined by side_a, side_b, side_c
    """
    if not a_triangle(sides):
        return False
    if not equilateral(sides) and not isosceles(sides):
        return True
    return False
