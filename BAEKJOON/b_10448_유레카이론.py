triangle = [n*(n+1)//2 for n in range(1,46)]
eureka = [0]*1001

for i in triangle:
    for j in triangle:
        for k in triangle:
            if i+j+k <= 1000:
                eureka[i+j+k] = 1
for i in range(int(input())):
    print(eureka[int(input())])