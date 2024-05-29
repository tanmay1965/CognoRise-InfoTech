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
if c=='+':
	print(a+b)
elif c=='-':
	print(a-b)
elif c=='*':
	print(a*b)
elif c=='/':
	print(a/b)
elif c=='%':
	print(a%b)
elif c=='**':
	print(a**b)
elif c=='//':
	print(a//b)
else :
	print('Wrong option')
