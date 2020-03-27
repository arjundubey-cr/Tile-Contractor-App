
print("--------------------------Tile Contractor APP---------------------------")
print("------------------------------------------------------------------------")
print("->Grab the amazing discounts available at store")
print(":::Enter the dimensions of surface and grab the amazing discounts:::") 
length = float(input("Enter the length(in feet): "))
breadth = float(input("Enter the breadth(in feet): "))
area = length*breadth
rate=20.0
discount=0.00
if area<=200:
    discount=5
elif area<=500:
    discount=10
elif area<=1000:
    discount=15
else:
    discount=20

print("CONGRATULATIONS!\nYou are our lucky costumer for today. You'll be offered a discount")
print("------------------------------------------------------------------------")
print("Bill Amount:: $"+str(area*rate) + "(Area = " + str(area) + " sq. feet)")
print("Discount:: $" + str(discount*0.01*area) + "(" + str(discount)+"%)")
print("Final Bill Amount: $" + str((area*rate)-(discount*0.01*area)))
print("Dear Customer, Thanks for Showing your interest.")
