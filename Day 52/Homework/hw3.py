def unique_in_order(sequence):
    result = []  
    
    for i, element in enumerate(sequence):
        if i == 0 or element != sequence[i - 1]:
            result.append(element)
    
    return result
