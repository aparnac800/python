ist1=input("enter the colors for list1 seperated by commas:")
list2=input("enter the colors for list2 seperated by comma:")
l1=list1.split(',')
l2=list2.split(',')
result=set(l1)-set(l2)
print(result)