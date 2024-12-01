class part_one:
    left = list()
    right = list()
    sum = 0
    
    for linha in open("input.txt", "r"):
        entrada = linha.rstrip("\n").split("   ")
        entrada = [int(e) for e in entrada]
        left.append(entrada[0])
        right.append(entrada[1])
    
    left.sort()
    right.sort()
    
    for l, r in zip(left, right):
        sum += abs(l - r)
    
    print(sum)
