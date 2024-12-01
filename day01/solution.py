import collections

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
    
    # print(sum)

class part_two:
    left = list()
    right = list()
    sum = 0

    for linha in open("input2.txt", "r"):
        entrada = linha.rstrip("\n").split("   ")
        left.append(entrada[0])
        right.append(entrada[1])
    
    
    right_count = collections.Counter(right)
    left_count = collections.Counter(left)
    print(left_count.values())
    
    inter = set(left).intersection(right)

    for key in inter:
        sum += int(key) * right_count[key] * left_count[key]

    print(sum)
