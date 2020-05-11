def minion_game(string):
    score1,score2=0,0
    for i in range(len(string)):
        if string[i] in "AEIOU":
            score2+=len(s)-i
        else:
            score1+=len(s)-i
    if score1>score2:
        print("Stuart "+str(score1))
    elif score1<score2:
        print("Kevin "+str(score2))
    else:
        print("Draw")

if __name__ == '__main__' :
    s = input()
    minion_game(s)
