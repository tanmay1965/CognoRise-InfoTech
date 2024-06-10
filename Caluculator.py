a=int(input('Enter a Value'))
b=int(input('Enter a Value'))
print('1.+')
print('2.-')
print("3.*")
print('4./')
print('5.%')
print('6.**')
print('7.//')
c=input('select your option')
if c=='1':
	print(a+b)
elif c=='2':
	print(a-b)
elif c=='3':
	print(a*b)
elif c=='4':
	print(a/b)
elif c=='5':
	print(a%b)
elif c=='6':
	print(a**b)
elif c=='7':
	print(a//b)
else :
	print('Wrong option')
