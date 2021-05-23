import random
while(1):
    option=['Stone','Paper','Scissor']
    user=input('Take your move!')
    compmove=[]
    temp=random.randint(1, 3)

    if temp==1:
        compmove.append(option[0])

    elif temp==2:
        compmove.append(option[1])

    elif temp==3:
        compmove.append(option[2])

    if user in compmove:
        print("YAY!you win against me")
    else:
        if 'quit' in user:
            break
        else:
            print(f'I thought of {compmove} TRY AGAIN')

