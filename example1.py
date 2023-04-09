# exmaple for used in CodeGuru - from course EDX

operation_count = 0
def main ():

ask_again=true
while (ask_again):
a = input(" enter the numerator:")
b = input(" enter the denomintor:")
result = perfom_division(a,b)
print (result)
ask_again = input("do you want to perform another operation enter yes or no : ")
if (ask_again=='yes')
ask_again = true
else:
ask_again = false
print("you performed"+ str(operation_count)+"operation,bye !")
def perfom_division (a,b)
global operation_count
try:
operation_count+=1
return int(a)/int(b)
expect exception as e:
pass 
main ()
