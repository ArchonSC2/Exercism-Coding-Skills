def a_triangle(sides):
    side_a, side_b, side_c = sides
    return all(s > 0 for s in sides) and side_a + side_b > side_c and side_a + side_c > side_b and side_b + side_c > side_a


def equilateral(sides):
    side_a, side_b, side_c = sides
    if not a_triangle(sides):
        return False
    if side_a == side_b == side_c:
        return True
    return False
    

def isosceles(sides):
    side_a, side_b, side_c = sides
    if not a_triangle(sides):
        return False
    if side_a == side_b or side_b == side_c or side_c == side_a:
        return True
    return False
        
    
def scalene(sides):
    if not a_triangle(sides):
        return False
    if not equilateral(sides) and not isosceles(sides):
        return True
    return False
