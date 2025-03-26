def logical_operations(x, y):

    result = None
    
    if x and y:
        result = True
    elif not x or not y:
        result = False
        
    return result
