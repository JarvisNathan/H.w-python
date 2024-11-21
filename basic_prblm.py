'''num1= 5
num2= 4
print(num1+num2)

num1= 5
num2= 4
num3=num1+num2
print(f'the number is {num3}')

a=[1,2,3,4]

for i in a:
   print(i)

a=[1,2,3,4]
res=0
for i in a:
   res=res+i
   # print(res)
print(res)

a=0
for i in range(0,11):
	a=a+i
	print(a)

for i in range(11,0,-1):
	print(i)

for i in range(0,10):
	print(i)

num1=int(input('enter the number or ill kill you! :'))

num2=int(input('enter the number or ill definetly kill you! :'))

print(f'your numbers were {num1} and also {num2}')



num1=int(input('enter the number or ill kill you! :'))

num2=int(input('enter the number or ill definetly kill you! :'))

num3=num1+num2

print(num3)


num1=int(input('enter the number or ill kill you! :'))

num2=int(input('enter the number or ill definetly kill you! :'))

num3=0

for i in range(num1,num2+1):
	num3=num3+i
print(num3)


for i in range(1,11):
	if i % 2 == 0:
		print(f'the number {i} is even')
	else:
		print(f'the number {i} is odd')


a=1232
b=0
for i in str(a):
	b=b+int(i)
print(b)

mark =float(input('enter the grading of  the exam:'))
if mark >= 80:
	print('you have got GPA5')
elif mark >=70:
	print('you have got GPA4')
else:
	print('you are a donkey')

row = 6
for i in range(1,row+1):
	print('@' * i)

row = 7
for i in range(row+1,1,-1):
	print('@' * i)

table= 10
for i in range(1,11):
	print(f'{table}*{i}={table*i}')

n=7

fact=1
for i in range(1,n+1):
	fact= fact*i
print(fact)

a=[4,5,8,4,6,5,9,3]
print(max(a))


a=[4,5,8,4,6,5,9,3]
max_num = 0
for i in a:
	if i > max_num:
		max_num = i
print(max_num)

a=[4,5,8,4,6,5,9,3]

trgt=4
count=0
for i in a:
	if i == trgt:
		count=count +1
print(f'the count of {trgt} is {count}')


h='olleh'
rev=' '
for i in h:
	rev=i + rev
print(rev)


pri = 43
count=0
for i in range(1,pri+1):
	if pri % i==0:
		count=count+1
if count == 2:
	print(f'the number {pri} is a prime number')
else:
	print(f'the number {pri} is not a prime number')'''
