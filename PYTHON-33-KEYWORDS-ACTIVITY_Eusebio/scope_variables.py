global_var = 10

def outer_function():
    nonlocal_var = 20
    
    def inner_function():
        nonlocal nonlocal_var
        global global_var
        nonlocal_var = 30
        global_var = 15

    return inner_function
