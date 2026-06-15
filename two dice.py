import random
lst=[]
while True:
    choice=input("You want to play (yes/no): ")
    if choice=='yes':
        dice1=random.randint(1,6)
        print(dice1)
        dice2=random.randint(1,6)
        print(dice2)
        sum=dice1+dice2
        print(sum)
        lst.append(sum)
    elif choice=='no':
        print('GoodBye')
        print("The Roll History: ",lst)
        print("The maximum number on your dices is:",max(lst))
        break
    else:
        print("Invalid output")
    










