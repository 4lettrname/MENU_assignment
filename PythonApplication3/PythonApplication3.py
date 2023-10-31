customer_order = []
menu = ["pizza £7.30", "pie £3.45","burger £4.50","chips £2.00","onion rings £2.30","a drink £1.50"]
cost = 0.00
for x in menu:
    print(x)
ordering = True
while ordering:
    item = input("please tell me what you would like to order and when you have finished type finish ")

    if item =="pizza":
        cost+= 7.30
        customer_order.append(menu[0])
    elif item =="pie":
        cost+= 3.45
        customer_order.append(menu[1])
    elif item =="burger":
        cost+=4.50
        customer_order.append(menu[2])
    elif item =="chips":
        cost +=2.30
        customer_order.append(menu[3])
    elif item =="onion rings":
        cost+= 2.30
        customer_order.append(menu[4])
    elif item =="a drink":
        cost+= 1.50
        customer_order.append(menu[5])
    elif item =="finish":
        break
print (customer_order,"this costs £",{cost})
