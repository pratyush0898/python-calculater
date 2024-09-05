print("Calculator")

num1 = int(input('enter number 1: '))
num2 = int(input('enter number 2: '))
opr = input('enter oprater: ')

if opr == '+':
  print(num1+num2)
  
elif opr == '-':
    print(num1-num2)
elif opr == '*':
    print(num1*num2)
elif opr == '/':
    print(num1/num2)
else:
    print('Error')