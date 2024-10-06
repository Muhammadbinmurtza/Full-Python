def grade(per : int)-> str:
    if per >= 80:
        return "A+" 
    elif per >= 70:
        return "A"
    elif per >= 60:
        return "B"
    elif per >= 50:
        return "C"
    elif per >= 40:
        return "D"
    else:
        return "F"
result =grade(82)
print(result)

