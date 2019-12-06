n = int(input())
terms = input().split()
new_terms = [int(i) for i in terms]
k = int(input())
matrix = [ new_terms[i:i+3] for i in range(0,len(new_terms),3)]
for j in matrix:
 print(j)
'''if(k*2==len(new_terms)):
    for i in range(0,2):
        for j in range(0,len(new_terms)//2):
            print(new_terms[j])
        print('\r')
else:
    print('none')'''

'''s= [1,2,3,4,5,6]  
matrix = [ s[i:i+3] for i in range(0,len(s),3) ]
for j in matrix:
    print(j)'''