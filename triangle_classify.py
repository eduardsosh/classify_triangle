"""
Python script to get the type of triangle from side lenghts a,b and c
"""
import math

TOLERANCE = 1e-8

def lt_or_equals(a,b)->bool:
    return a <= b or math.isclose(a, b, rel_tol=TOLERANCE, abs_tol=TOLERANCE)

def equals(a,b)->bool:
    return math.isclose(a,b,rel_tol=TOLERANCE,abs_tol=TOLERANCE)


def classify_triangle(a, b, c) -> str:
    # Let , also work as a decimal seperator
    a = a.replace(',','.')
    b = b.replace(',','.')
    c = c.replace(',','.')

    inputs = {'a': a, 'b': b, 'c': c}
    for var_name, value in inputs.items():
        try:
            float(value)
        except ValueError:
            return f"Error in input '{var_name}': not a valid floating-point number!"
    
    a = float(a)
    b = float(b)
    c = float(c)
    
    MAX_LENGHT = 1_000_000_000.0
    if(a > MAX_LENGHT or b > MAX_LENGHT or c > MAX_LENGHT):
        return "Error: Side/s too long!"
    
    if not(a > 0 and b > 0 and c > 0):
        return "Error: Invalid side lenght/s!"
    
    # Check wether side lenghts are correct
    if (lt_or_equals(a+b,c) or lt_or_equals(a+c,b) or lt_or_equals(c+b,a)):
        return "Error: Triangle doesn't exist!"
    
    
    # is equilateral?
    if(equals(a,b) and equals(b,c)):
        return "Equilateral Triangle"
    
    # is Isosceles?
    if(equals(a,b) or equals(b,c) or equals(a,c)):
        return "Isosceles Triangle"
    else:
        return "Scalene Triangle"
    


print(classify_triangle("-1", "2", "2"))
print(classify_triangle("1", "20", "15,5"))
print(classify_triangle("1000000000000000", "20", "15,5"))
print(classify_triangle("15.5", "20", "15,5"))
print(classify_triangle("0.001", "0.001", "0.001"))
print(classify_triangle("3", "4", "5"))
print(classify_triangle("-1", "2", "2"))

def test_classify(*additional):
    inputs = [("-1", "2", "2"),
              ("1", "20", "15,5"),
              ("1000000000000000", "20", "15,5"),
              ("15.5", "20", "15,5"),
              ("0.001", "0.001", "0.001"),
              ("3", "4", "5"),
              ("-1", "2", "2")]
    
    inputs.append(additional)



