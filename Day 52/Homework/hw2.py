def break_camel_case(s):
    result = ""
    
    for char in s:
        if char.isupper():
            result += " "  
        result += char   
    
    return result
