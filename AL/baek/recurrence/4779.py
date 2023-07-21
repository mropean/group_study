def khan(str_):
    result = ""
    if len(str_) == 1:
        return str_
    else:
        min_1 = len(str_) // 3
        min_2 = min_1 * 2
        result += khan(str_[:min_1])
        result += " "*(min_2 - min_1)
        result += khan(str_[min_2:])
        return result

while True:    
    try:
        N = int(input())
        print(khan("-"*(3**N)))
    except:
        break