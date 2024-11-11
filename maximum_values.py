a=[1,2,3,4,5,6,7,8,9,10]
maximum=a[0]
for v in a[1:]:
    if(v>maximum):
        maximum=v
print(maximum)
print(max(a))