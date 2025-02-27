

def pressure(height,density,gravity):
    calculate_pressure = height * density * gravity
    return calculate_pressure

print("The total pessure exerted is: " + str(pressure(2,6.5,10)))
# the str convrts the float answer into a string
# variables used in the function are declared wth the function
# values to be calculated are not put in the function, rather in theprint satement
