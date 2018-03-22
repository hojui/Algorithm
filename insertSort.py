data = [int(e) for e in input().split()]

for h in range(3,0,-1):
    for m in range(0,h,1):
        for i in range(h+m,len(data),h):
            temp = data[i]
            index = i-h
            while(temp<data[index] and index>=0):
                data[index+h] = data[index]
                index = index-h
            data[index+h] = temp

print(data)
