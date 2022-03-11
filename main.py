N = int(input())
line1 = input()
line2 = input()
line3 = input()
line4 = input()
charecters1 = list()
charecters2 = list()
charecters3 = list()
charecters4 = list()
next=False
count = 0
for x in range(N):
        for char in line1:
            charecters1.append(char)
        for char in line2:
            charecters2.append(char)
        for char in line3:
            charecters3.append(char)
        for char in line4:
            charecters4.append(char)
        word = input()
        for char in word:
            if char in charecters2:
                charecters2.clear()
                continue
            elif char in charecters1:
                charecters1.clear()
                continue
            elif char in charecters3:
                charecters3.clear()
                continue
            elif char in charecters4:
                charecters4.clear()
                continue
            else:
                print("NO")
                next=True;
                break
        if next!=True:
            print("YES")
        else:
            next=False
            continue