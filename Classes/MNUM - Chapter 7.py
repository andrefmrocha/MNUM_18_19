import math
def math_func(x):
    return pow(2*x+1, 2) - 5 * math.cos(10 * x)



def aurea_method(x1, x2, func, minimum, error):
    A = (math.sqrt(5) - 1)/2
    B = pow(A, 2)
    prev_x = 0
    x3 = 0
    x4 = 0
    while abs(x1 - x2) > error:
        x3 = x1 + A * (x2 - x1)
        x4 = x1 + B * (x2 - x1)
        if(minimum):
            func_3 =  - func(x3)
            func_4 = - func(x4)
        else:
            func_3 = func(x3)
            func_4 = func(x4)
        if(func_3 < func_4):
            x2 = x4
        else:
            x1 = x3
    return_value = min(x1, x2)
    return return_value, func(return_value)

def math_func_x_y(x,y):
    return pow(y, 2) - 2 * x * y - 6 * y + 2 * pow(x, 2) + 12

def func_dev_x(x, y):
    return -2 * y + 4 *x

def func_double_x_x(x, y):
    return 4

def func_double_x_y(x, y):
    return -2

def func_dev_y(x, y):
    return 2 * y - 2 * x - 6

def func_double_y_x(x, y):
    return 2

def func_double_y_y(x, y):
    return 2

def math_func_2_x_y(x, y):
    return 2 * x * y + 2 * x - pow(x ,2) - 2 * pow(y, 2)
def func_2_dev_x(x, y):
    return 2 * y + 2 - 2*x

def func_2_dev_y(x, y):
    return 2 * x - 4 * y

def multidimensional_search(x, y, h, gradient, min, error, func):
    prev_x = 0
    prev_y = 0
    while abs(x - prev_x) > error or abs(y - prev_y) > error:
        if(min):
            prev_x = x
            prev_y = y
            x = prev_x - h * gradient[0](prev_x, prev_y)
            y = prev_y - h * gradient[1](prev_x, prev_y)
            if(func(x,y) < func(prev_x, prev_y)):
                h*=2
            elif (func(x,y) > func(prev_x, prev_y)):
                h/=2

        else:
            prev_x = x
            prev_y = y
            x = prev_x - h * -gradient[0](prev_x, prev_y)
            y = prev_y - h * -gradient[1](prev_x, prev_y)
            if(func(x,y) > func(prev_x, prev_y)):
                h*=2
            elif (func(x,y) < func(prev_x, prev_y)):
                h/=2
    return x, y, func(x,y)




# print(aurea_method(-1, 0, math_func, False, 10**(-3)))
# print(multidimensional_search(1, 1, 1, [func_dev_x, func_dev_y], True, 10**(-3), math_func_x_y))
# print(multidimensional_search(-1, 1, 1, [func_2_dev_x, func_2_dev_y], False, 10**(-3), math_func_2_x_y))




def quadric(x, y, gradient, hamilton, error):
    prev_x = 0
    prev_y = 0
    while abs(x - prev_x) > error or abs(y - prev_y) > error:
        prev_x = x
        prev_y = y
        H = 1 / (hamilton[0][0](prev_x, prev_y) * hamilton[1][1](prev_x, prev_y) - hamilton[1][0](prev_x, prev_y)*hamilton[0][1](prev_x, prev_y))
        print(H)


print(quadric(1, 1, [func_dev_x, func_dev_y],[[func_double_x_x, func_double_x_y], [func_double_y_x, func_double_y_y]], 10**(-3)))