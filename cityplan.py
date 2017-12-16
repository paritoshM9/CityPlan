r,c=input().strip().split(' ')
r,c=int(r),int(c)
oldplan=[]
for i in range(r):
   temp=input().strip()
   row=list(temp)
   oldplan.append(row)

new1=[['' for j in range(c)]for i in range(r)]
new1[0][0]='B'
for row in range(1,r):
    if(new1[row-1][0]=='B'):
        new1[row][0]='G'
    else:
        new1[row][0]='B'
for row in range(r):
    for col in range(1,c):
        if(new1[row][col-1]=='B'):
            new1[row][col]='G'
        else:
            new1[row][col]='B'
new2=[['' for j in range(c)]for i in range(r)]
new2[0][0]='G'
for row in range(1,r):
    if(new2[row-1][0]=='B'):
        new2[row][0]='G'
    else:
        new2[row][0]='B'
for row in range(r):
    for col in range(1,c):
        if(new2[row][col-1]=='B'):
            new2[row][col]='G'
        else:
            new2[row][col]='B'            
#comparing the old plan with new1
cost1=0
cost2=0
for row in range(r):
    for col in range(c):
        if(oldplan[row][col]=='B' and new1[row][col]=='G'):
            cost1+=5
        elif(oldplan[row][col]=='G' and new1[row][col]=='B'):
            cost1+=3
        else:
            continue
#comparing the old plan with new2
        
for row in range(r):
    for col in range(c):
        if(oldplan[row][col]=='B' and new2[row][col]=='G'):
            cost2+=5
        elif(oldplan[row][col]=='G' and new2[row][col]=='B'):
            cost2+=3
        else:
            continue    
print(min(cost1,cost2))
