def median(text):
    
    ll = []
    x = ""

    if len(text) == 1:
        return text
    elif len(text) == 0:
        return text
    else:
        for i in range(len(text)):
            if text[i] > x:
                x += text[i]
                
            else:
                ll.append(x)
                x=""
                continue

    #comparing the bigger substr
    return max(ll)






           


median("a")
