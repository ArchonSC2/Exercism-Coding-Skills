def a_triangle(sides):
    a,b,c = sides
    return all(s > 0 for s in sides) and a + b > c and a + c > b and b + c > a


def equilateral(sides):
    a,b,c = sides
    if not a_triangle(sides):
        return False
    if a == b == c:
        return True
    else:
        return False
    

def isosceles(sides):
    a,b,c = sides
    if not a_triangle(sides):
        return False
    if a == b or b == c or c == a:
        return True
    else:    
        return False
        
    
def scalene(sides):
    if not a_triangle(sides):
        return False
    if not equilateral(sides) and not isosceles(sides):
        return True
    else:
        return False
