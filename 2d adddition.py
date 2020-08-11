lists=[[1,2,3],[2,3,5],[4,1,5]]
lis2=[[1,2,3],[2,3,5],[4,1,5]]
d=len(lis2)
sums=[[]]
for i in range(0,d):
    for j in range(0,d):
        sums[0][0].append(lists[i][j]+lis2[i][j])
        #print(i,j)


print(sums)
