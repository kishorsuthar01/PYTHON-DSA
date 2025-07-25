A=[[1,2,3],
   [4,5,6],
   [7,8,9]]

B=[[5,6,7],
   [3,3,8],
   [5,8,9]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        result[i][j]=A[i][j]+B[i][j]
for r in result:
    print(r)


