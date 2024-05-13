import math

def lt_or_equals(a,b)->bool:
    TOLERANCE = 1e-8
    return a <= b or math.isclose(a, b, rel_tol=TOLERANCE, abs_tol=TOLERANCE)


def classify_triangle(a, b, c) -> str:
    #Initial input sanitation
    errors = list()

    inputs = {'a': a, 'b': b, 'c': c}
    for var_name, value in inputs.items():
        try:
            float(value)
        except ValueError:
            return f"Error in input '{var_name}': not a valid floating-point number!"
        
    # Check if a triangle exists
    if not(a > 0 and b > 0 and c > 0):
        return "Error: Invalid side lenght/s!"
    
    # Check wether side lenghts are correct
    if (lt_or_equals(a+b,c) or lt_or_equals(a+c,b) or lt_or_equals(c+b,a)):
        return "Error: Triangle doesn't exist!"
    
    # Make a max limit on the side lenght
    MAX_LENGHT = 1_000_000_000
    if(a > MAX_LENGHT or b > MAX_LENGHT or c > MAX_LENGHT):
        return "Error: Side/s too long!"
    


print(classify_triangle("10", "20", "30"))
print(classify_triangle("10", "20x", "30"))
