#imports
import random
import sys
#Offences
off= [#repeat procedure offences
      "Sub violation \n",#0
      "Knockout procedure violation \n", #1
      #back to hoops offenses
      "Illegally failing to replace a lost headband \n", #2
      "Second false restart \n", #3
      "Improper immunity claim \n", #4
      "Minor invlaid immunity claim \n", #5
      "Minor illegal interposition interaction\n", #6
      "Minor failure to avoid a prpopelled quaffle \n", #7
      "Intentionally or egregiously illegally going or remaining out of bounds \n", #8
      "Inbounding procedure violation \n", #9
      "Illegally pursing the snitch \n", #10
      "Delaying the completetion of the turnover procedure \n", #11
      #turnover offenses
      "Unintentional natural motion violation \n", #12
      "Incidental interposition ball interference \n", #13
      "Illegal reset \n", #14
      #blue card offenses
      "If the speaking captain or team staffer substaially illegally enters the pitch or affects play while illegally on the pitch\n", #15
      "Repeated substution violations\n", #16
      "Interacting with play before correcting substution violation\n", #17
      "Intentionally and Illegally leaving the sub or bench area with the intent of circumventing other rules \n", #18
      "A sub intentionally and illegally outside of both sub and bench area \n", #19
      "The sub has failed to make every effort to make a reasonable effor to avoid the play \n", #20
      "Entering play with illegally long or sharp fingernails \n", #21 
      "Entering play without wearing mandatory equipment \n", #22
      "Intentionally removing manditory equipment while in play \n", #23
      "Entering play without a legal or recognisable jersey number \n", #24
      "Penalty for speaking captian for having 2 players wearing the same number in the play area \n", #25
      "Using illegal additional equipment in play \n", #26
      "Changing position headbands after the brooms down call \n", #27
      "Changing location behind the keeper zone line after the brooms down call \n", #28
      "Penalty for a false start \n", #29
      "Illegal timeout request \n", #30
      "Seeker false start \n", #31
      "Intentionally and illegally interacting with a dead quaffle \n", #32
      "Illegally resetting an opponents hoops \n", #33
      "Unitentionally, repeatedly dislodging hoops \n", #34
      "Illegally contacting an opponent with a held bludger \n", #35
      "Illegally interacting with play while knocked out \n", #36
      "Affecting play while unknowingly knocked out \n", #37
      "Illegally batting a bludger \n", #38
      "Illegally blocking a bludger \n", #39
      "Illegal bludger swat \n", #40
      "Struck Beater violation \n", #41
      "Improper immunity claim \n", #42
      "Invalid immunity claim \n", #43
      "Immunity violation \n", #44
      "Repeated use of explicit or vulgar language \n", #45
      "Illegally using a ball of one's own position \n", #46
      "Failure to aviod a propelled quaffle \n", #47
      "A sub or knocked out player illegally failing to make a reasonable effort to avoid the ball \n", #48
      "Illegal second kick \n", #49
      "Propelling a ball with the intent of sending any ball out of bounds \n", #50
      "Illegally using verbal or visual referee signals\n", #51
      #yellow card offenses
      "Feigning an injury \n", #52
      "Intentionally illegally moving during a stoppage \n", #53
      "Intentionally illegally moving or taking hold of a ball during a stoppage \n", #54
      "Recklessly dislodging a hoop \n", #55
      "Willfully ignoring being knocked out \n", #56
      "Intentionally or repeatedly violating the knockout procedure \n", #57
      "Illegal contact while knocked out \n", #58
      "Intentional natural motion violation \n", #59
      "Dangerous kick \n", #60
      "Kicking an opponent \n", #61
      "Illegally hurdling or attempting to hurdle any person \n", #62
      "Illegally contacting a helpless receiver \n", #63
      "Playing recklessly \n", #64
      "Illegal interpostion interaction \n", #65
      "Illegaly interacting with a knocked out opponent \n", #66
      "Unsportsman like conduct \n", #67
      "Pretending to be fouled \n",  #68
      "Using a ball to intentionally interact with the snitch runner \n", #69
      "Interposition ball interfence \n", #70
      "Illegally unintentionally blocking a propelled quaffle from scoring \n", #71
      "Intentionally or blatantly ignoring a boundary call \n", #72
      "Willfully ignoring a turnover call \n", #73
      "Failing to immediately proceed to the penalty box after being carded \n", #74
      "Disregarding an offical's directive \n", #75
      #red card offenses
      "Intentional sideline inteference \n", #76
      "Knowingly initiating a new play with a broken broom \n", #77
      "Using equipment in play that was disallowed by a game offical \n", #78
      "Using equipment explicitly barred by the tournament director \n", #79
      "Illegally altering game equipment \n", #80
      "Wearing forbidden equipment \n", #81
      "Intentional interposition goaltending \n", #82
      "Intentionally disloding a hoop \n", #83
      "Moving or altering a hoop to affect whether the quaffle will pass through it \n", #84
      "Violent or egregious illegal kick \n", #85
      "Violent or egregiously illegally hurdling any person \n", #86
      "Charging a helpless reciever \n", #87
      "Tackling a helpless reciever \n", #88
      "Playing egregiously recklessly \n", #89
      "Egregiously illegal contact against an opponent, spectator, official or event staffer \n", #90
      "Violent or egregious illegal interposition interaction \n", #91
      "Violently or egregiously illegally interacting with a knocked out opponent \n", #92
      "Egregious unsportsmanlike conduct \n", #93
      "Engaging in a physical altercation with an opponent, spectator, official or event staffer \n", #94
      "Intentionally spitting at or on an opponent, spectator, offcial or event staffer \n", #95
      "Serious foul play \n", #96
      "Intentionally and illegally blocking a score \n", #97
      #ejection offenses
      "Egregiously illegal contact against a teammate \n", #98
      "Egregious internal unsportsmanlike conduct \n", #99
      "Engaging in a physical altercation with a teammate \n", #100
      "Intentionally spitting at or on a teammate \n", #101
      #standard contact penalty offenses
      "Illegal physical contact \n", #102
      "Illegal pick \n", #103
      "Illegally charging a picking player \n", #104
      "Illegal slide \n", #105
      "Illegal dive \n", #106
      "Illegal contact through a teammate \n", #107
      "Illegal attempt to steal \n", #108
      "Illegal contact from behind \n", #109
      "Illegal body block \n", #110
      "Illegal push \n", #111
      "Illegal charge \n", #112
      "Illegal wrap \n", #113
      "Illegal interaction with the snitch runner \n", #114
      "Third bludger interference \n", #115
      "Delay of game \n" #116
        ]
#dim vars
question = random.sample(range(0,len(off)),len(off))
score = 0
n = 0
#display score function
def dis_score(correct, total):
    print("\n")
    print("Quiz Stopped")
    print("Your final score is " + str(correct) + "/" + str(total))
    print("Press Enter to exit")
    input()
#intro
print("###########################################################################################")
print("# Penalties quiz for IQA rulebook 2018 - 2020 V1.6                                        #")
print("# (c) Alex Healey, TreasDev, 2019                                                         #")
print("# IQA Rule Book - http://iqasport.org/wp-content/uploads/2019/02/IQA-Rulebook-2018-20.pdf #")
print("# Repeat procedure = repeat                                                               #")
print("# Back to hoops = bth                                                                     #")
print("# Turnover of possesion = turnover                                                        #")
print("# Blue Card = blue                                                                        #")
print("# Yellow Card = yellow                                                                    #")
print("# Red Card = red                                                                          #")
print("# Player is Ejected = ejection                                                            #")
print("# Standard contact penalty = scp                                                          #")
print("# Back To Hoops and Double bludger turnover = bth and double bludger turnover             #")
print("# Quaffle turnover = qt                                                                   #")
print("# Exit = endgame                                                                          #")
print("###########################################################################################")
print("\n")
for num in question:
    answer = input(off[num])
    if answer.lower() == 'endgame' and n != 0:
        dis_score(score, n)
        break
    elif answer.lower() == 'endgame' and n == 0:
        sys.exit()
    else:
        if 0 <= num <= 1: 
            n +=1
            if answer.lower() == "repeat":
                score +=1
                print("Correct \nYour score is " + str(score) + "/" + str(n) + "\n")
            else:
                print("Incorrect, you must make the player repeat the procedure \nYour score is " + str(score) + "/" + str(n) + "\n")
        if 2 <= num <= 11:
            n +=1
            if answer.lower() == "bth":
                score +=1
                print("Correct \nYour score is " + str(score) + "/" + str(n) + "\n")
            else:
                print("Incorrect, you must send the player back to their hoops \nYour score is " + str(score) + "/" + str(n) + "\n")
        if 12 <= num <= 14:
            n +=1
            if answer.lower() == "turnover":
                score +=1
                print("Correct \nYour score is " + str(score) + "/" + str(n) + "\n")
            else:
                print("Incorrect, there must be a turnover of possession to the other team \nYour score is " + str(score)  + "/" + str(n) + "\n")
        if 15 <= num <= 51:
            n +=1
            if answer.lower() == "blue":
                score +=1
                print("Correct \nYour score is " + str(score) + "/" + str(n) + "\n")
            else: 
                print("Incorrect, a blue card must be issued \nYour score is " + str(score) + "/" + str(n) + "\n")
        if 52 <= num <= 75:
            n +=1
            if answer.lower() == "yellow":
                score +=1
                print("Correct \nYour score is " + str(score) + "/" + str(n) + "\n")
            else:
                print("Incorrect, a yellow card must be issued \nYour score is " + str(score) + "/" + str(n) + "\n")
        if 76 <= num <= 97:
            n +=1
            if answer.lower() == "red":
                score +=1
                print("Correct \nYour score is " + str(score) + "/" + str(n) + "\n")
            else:
                print("Incorrect, a red card must be issued \nYour score is " + str(score) + "/" + str(n) + "\n")
        if 98 <= num <= 101:
            n +=1
            if answer.lower() == "ejection":
                n +=1
                score +=1
                print("Correct \nYour score is " + str(score) + "/" + str(n) + "\n")
            else:
                print("Incorrect, the player must be ejected \nYour score is " + str(score) +"/" + str(n) + "\n")
        if 102<= num <= 114:
            n +=1
            if answer.lower() == "scp":
                score +=1
                print("Correct \nYour score is " + str(score) + "/" + str(n) + "\n")
            else:
                print("Incorrect, standard contact penalty is applied \nYour score is " + str(score)  +"/" + str(n) + "\n")
        if num == 115:
            if answer.lower() == "bth and double bludger turnover":
                n +=1
                score +=1
                print("Correct \nYour score is " + str(score) + "/" + str(n) + "\n")
            else:
                print("Incorrect, the player is sent back to hoops and there is a double bludger turnover\nYour score is " + str(score) + "/" + str(n) + "\n")
        if num == 116:
            if answer.lower() == "blue and qt":
                n +=1
                score +=1
                print("Correct \nYour score is " + str(score) + "/" + str(n) + "\n")
            else:
                print("Incorrect, a blue card is issued and the quaffle is turned over \nYour score is " + str(score) + "/" + str(n) + "\n")