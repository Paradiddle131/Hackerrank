vals=map(int,input().split())
n,k=vals[0], vals[1]
cost=map(int,input().split())
total=sum(cost)
aCharge=total/2
bActual=(total-(cost[k])) / 2
bCharged=input()
if bCharged!=bActual:
    print(bCharged-bActual)
else:
    print("Bon Appetit")

"""

def bonAppetit(bill, k, b):
    charge = 0
    billB = []
    for i in bill:
        if bill.index(i) != k: 
            billB.append(i)
    charge = int(b - sum(billB)/2)
    #return (charge if b != sum(billB)/2 else "Bon Appetit")
    if b != sum(billB)/2:
        return charge
    else:
        return "Bon Appetit"

print(bonAppetit([3, 10, 2, 9], 1, 7))

"""