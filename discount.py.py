price=int(input("Enter the price: "))
quantity=int(input("Enter the quantity: "))
amount=price*quantity
if amount>=10000:
    print("Eligible for 10% discount")
    discount=int(amount*10/100)
    print ("discount amount is : ",discount)
    amount=amount-discount
elif amount>=5000:
    print("5% discount is applicable")
    discount=int(amount*5/10)
    amount=amount-discount
    print("discount amount is: ",discount)
elif amount>=3000:
    print("3% discount is applicable")
    discount=int(amount*3/10)
    amount=amount-discount
    print("discount amount is: ",discount)
elif amount>=2000:
    print("2% discount is applicable")
    discount=int(amount*2/10)
    amount=amount-discount
    print("discount amount is: ",discount)
elif amount>1000:
    print("1% discount is applicable")
    discount=int(amount*1/10)
    amount=amount-discount
    print("discount amount is: ",discount)    
else:
    print("no discount is applicable")
    print("payable amount is: ",amount)