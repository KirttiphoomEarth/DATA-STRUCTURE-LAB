''' ดาวเคราะห์น้อย '''
def asteroid_collision(asts,i):
    if i >= len(asts)-1:
        ans = []
        ans = asts
        print(str(ans).replace(" 0,",'').replace("[0, ",'[').replace(", 0]",']').replace('[0]','[]'))
        return 0
    if asts[i] < 0:
        if asts[i-1] >= 0 and i > 0:
            if abs(asts[i]) == asts[i-1]:
                asts[i-1] = 0
                asts[i] = 0
                asteroid_collision(asts,i-1)
            elif max(abs(asts[i]),asts[i-1]) == abs(asts[i]):
                asts[i-1] = asts[i]
                asts[i] = 0
                asteroid_collision(asts,i-1)
            else:
                asts[i] = asts[i-1]
                asts[i-1] = 0
                asteroid_collision(asts,i-1)
        else:
            asteroid_collision(asts,i+1)
    elif asts[i] > 0 and i <= len(asts)-1:
        if asts[i+1] <= 0:
            if abs(asts[i+1]) == asts[i]:
                asts[i+1] = 0
                asts[i] = 0
                asteroid_collision(asts,i+1)
            elif max(abs(asts[i+1]),asts[i]) == asts[i]:
                asts[i+1] = asts[i]
                asts[i] = 0
                asteroid_collision(asts,i+1)
            else:
                asts[i] = asts[i+1]
                asts[i+1] = 0
                asteroid_collision(asts,i)
        else:
            asteroid_collision(asts,i+1)
    elif asts[i] == 0:
        if i < len(asts)-1:
            asteroid_collision(asts,i+1)
        elif i >= len(asts):
            return 0

x = input("Enter Input : ").replace(', ',',').split(",")
x = list(map(int,x))
asteroid_collision(x,0)
                