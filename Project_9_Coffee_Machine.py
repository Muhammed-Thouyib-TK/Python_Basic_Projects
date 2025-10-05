# database

money = 0
data = {'water':150,'milk':200,'coffee powder':50}
store = {'latte' :{'items' : {'water':30,'milk':150,'coffee powder':15},'money':170},
          'espresso' :{'items' : {'water':30,'milk':0,'coffee powder':15},'money':70},
          'cappuccino' :{'items' : {'water':30,'milk':60,'coffee powder':15},'money':150}}

# to check the resources

def resource_check(items):
    for i in items:
        if data[i]<items[i]:
            print(f'Sorry There no enough {i}')
            return False
    return True

# to make the payment

def payment():
    print("Insert Your coins")
    five = int(input('How Many 5rs Coins: '))
    ten = int(input('How Many 10rs Coins: '))
    twenty = int(input('How Many 20rs Coins: '))

    total = five*5 + ten*10 + twenty*20
    return total

# to finalize the payment

def final_payment_check(final_payment,amount):
    if final_payment>=amount:
        global money
        money += amount
        change  = final_payment-amount
        print(f'Here is your Change {change}')
        return True
    else:
        print('No Sufficent Money......Your amount is Refunded!')
        return False

# to make the coffee

def making(choice,items):
    for item in items:
        data[item] -= items[item]
    print(f"Here is Your {choice}.....Enjoy!")
    
# main

def main():
    while True:
        choice = input("What You Would Like to Have ? [latte / espresso / cappuccino] : ").lower()

        if choice == 'off':
            break
        elif choice == 'report':
            print(f'Water : {data['water']} \nMilk : {data['milk']} \nCoffee Powder : {data["coffee powder"]} \nProfit : {money}')
        else:
            product = store[choice]
            items = product['items']
            amount = product['money']

            if resource_check(items):
                final_payment = payment()
                if final_payment_check(final_payment,amount):
                    making(choice,items)

main()





        
