def logical_operations(x, y):
    # and, or, not, True, False, None
    result = None
    
    if x and y:
        result = True
    elif not x or not y:
        result = False
        
    return result
