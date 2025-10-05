# to add

def addition(fst_num,scnd_num):
    return fst_num+scnd_num

# to sub

def substraction(fst_num,scnd_num):
    return fst_num-scnd_num

# to mul

def multiplication(fst_num,scnd_num):
    return fst_num*scnd_num

# to div

def division(fst_num,scnd_num):
    return fst_num/scnd_num

# operation call based on input

def operation(operation,fst_num,scnd_num):
    if operation == '+':
        return addition(fst_num,scnd_num)
    elif operation == '-':
        return substraction(fst_num,scnd_num)
    elif operation == '*':
        return multiplication(fst_num,scnd_num)
    elif operation == '/':
        return division(fst_num,scnd_num)

# main 

def main():
    while True:
        fst_num = int(input("Enter Your First Number : "))
        print('+ \n- \n* \n/')
        operation_1 = input("Pick An Operation : ")
        scnd_num = int(input("Enter Your Second Number : "))
        result = operation(operation_1,fst_num,scnd_num)
        print(f'{fst_num} {operation_1} {scnd_num} = {result}')

        while True:
            choice = input(f"Enter 'yes' to continue calculation with {result} or 'no' to start new calculation or 'exit' to exit : ").lower()

            if choice == 'yes':
                operation_2 = input("Pick An Operation : ")
                nxt_num = int(input("Enter Next Number : "))
                result_5 = operation(operation_2,result,nxt_num)
                print(f'{nxt_num} {operation_2} {scnd_num} = {result_5}')
                result = result_5
            elif choice == 'no':
                break
            elif choice == 'exit':
                return
            else:
                print('Invalid Choice!')
main()



