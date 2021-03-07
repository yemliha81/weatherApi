def calc(s):
    
    couples = []
    for i in range(int(s)):
        x = i+1
        y = i+2
        while y <= s:
            couples.append(str(x)+'-'+str(y))
            y += 2
        x += 1
        
    print(couples)
    print(len(couples))

calc(10)