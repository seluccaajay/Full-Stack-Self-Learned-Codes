n = int(input())
list = list(input().split(","))
k = int(input())
new_list = [int(i) for i in list]
new_list.sort(reverse = True)
if(k>0 and k<100):
 print(new_list[k-1])