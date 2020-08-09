#This is a project on a billing system through python

#created by shaurya
#created on 11-06-2019
#finished on 12-06-2019
total = 0
while(1):
    #printing the menu
    print("Menu")

    a = print("1. Burger --------------------------  200 Rs")
    b = print("2. milk shake --------------------------  400 Rs per glass")
    c = print("3. French Fries--------------------------  150 Rs per plate")
    d = print("4. Cold cofee --------------------------  450 Rs per glass")
    e = print("5. Pizza--------------------------  430 Rs per plate")
    f = print("6. Chips--------------------------  20 Rs per packet")

    print("Input User")

    print("what do you want enter the number's")

    ch = int(input())

    print("Item Quantity")

    s = int(input())
    if ch == 1:
        total = total + (200 * s);
    elif ch == 2:
        total = total + (400 * s);
    elif ch == 3:
        total = total + (150 * s);
    elif ch == 4:
        total = total + (450 * s);
    elif ch == 5:
        total = total + (430 * s);
    elif ch == 6:
        total = total + (20 * s);
    con = input("Do you want to countinue Y/N")
    if(con == 'N' or con == 'NO' or con == 'no' or con == 'n' or con == 'nO'):
        break

print("The total amount is Rs. " + str(total))
