#!/usr/bin/python
#dim vars

score = 0
n = 0
#print instructions
print("Penalties quiz for IQA rulebook 2018 - 2020 V1.4")
print("(c) Alex Healey, 2019")
print("IQA Rule Book - http://iqasport.org/wp-content/uploads/2019/02/IQA-Rulebook-2018-20.pdf")
print("Repeat procedure = repeat")
print("Back to hoops = bth")
print("Turnover of possesion = turnover")
print("Blue Card = blue")
print("Yellow Card = yellow")
print("Red Card = red")
print("Player is Ejected = ejection")
print("Standard contact penalty = scp")

if 0 <= n: 
    answer = input(q)
    if 0 <= a <= 1: 
        n +=1
        if answer.lower() == "repeat":
            score +=1
            print("Correct \nYour score is " + str(score) + "/" + str(n) + "\n")
        else:
            print("Incorrect, you must make the player repeat the procedure \nYour score is " + str(score) + "/" + str(n) + "\n")
    if 2 <= a <= 11:
        n +=1
        if answer.lower() == "bth":
            score +=1
            print("Correct \nYour score is " + str(score) + "/" + str(n) + "\n")
        else:
            print("Incorrect, you must send the player back to their hoops \nYour score is " + str(score) + "/" + str(n) + "\n")
    if 12 <= a <= 14:
        n +=1
        if answer.lower() == "turnover":
            score +=1
            print("Correct \nYour score is " + str(score) + "/" + str(n) + "\n")
        else:
            print("Incorrect, there must be a turnover of possession to the other team \nYour score is " + str(score)  + "/" + str(n) + "\n")
    if 15 <= a <= 51:
        n +=1
        if answer.lower() == "blue":
            score +=1
            print("Correct \nYour score is " + str(score) + "/" + str(n) + "\n")
        else: 
            print("Incorrect, a blue card must be issued \nYour score is " + str(score) + "/" + str(n) + "\n")
    if 52 <= a <= 75:
        n +=1
        if answer.lower() == "yellow":
            score +=1
            print("Correct \nYour score is " + str(score) + "/" + str(n) + "\n")
        else:
            print("Incorrect, a yellow card must be issued \nYour score is " + str(score) + "/" + str(n) + "\n")
    if 76 <= a <= 97:
        n +=1
        if answer.lower() == "red":
            score +=1
            print("Correct \nYour score is " + str(score) + "/" + str(n) + "\n")
        else:
            print("Incorrect, a red card must be issued \nYour score is " + str(score) + "/" + str(n) + "\n")
    if 98 <= a <= 101:
        n +=1
        if answer.lower() == "ejection":
            n +=1
            score +=1
            print("Correct \nYour score is " + str(score) + "/" + str(n) + "\n")
        else:
            print("Incorrect, the player must be ejected \nYour score is " + str(score) +"/" + str(n) + "\n")
    if 102<= a <= 114:
        n +=1
        if answer.lower() == "scp":
            score +=1
            print("Correct \nYour score is " + str(score) + "/" + str(n) + "\n")
        else:
            print("Incorrect, standard contact penalty is applied \nYour score is " + str(score)  +"/" + str(n) + "\n")
    if a == 115:
        n +=1
        if answer.lower() == "bth and double bludger turnover":
            score +=1
            print("Correct \nYour score is " + str(score) + "/" + str(n) + "\n")
        else:
            print("Incorrect, the player is sent back to hoops and there is a double bludger turnover\nYour score is " + str(score) + "/" + str(n) + "\n")
    if a == 116:
        n +=1
        if answer.lower() == "blue and quaffle turnover":
            score +=1
            print("Correct \nYour score is " + str(score) + "/" + str(n) + "\n")
        else:
            print("Incorrect, a blue card is issued and the quaffl is turned over \nYour score is " + str(score) + "/" + str(n) + "\n")
input()