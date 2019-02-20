def main():
num=int(input("enter the number:"))
sum=0
temp=num
while temp>0:
digit=temp%10
sum+=digit**3
temp//=10
if num==sum:
print("yes")
else:
print("no")
if_name_=='_main_':
main()
