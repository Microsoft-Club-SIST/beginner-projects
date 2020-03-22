#Genin Projects
#Jajanken is japanese for the rock-paper-scissors 
#So this is a subtle sort of tribute to Gon from the anime HunterXHunter lel.
#I'm just geeking out.
#No GUI sorry ain't flashy, maybe i'll add later

import random as nen

#First Gon has to choose between the 3 modes of Nen. 
#1.Enhancement - Rock
#2.Emission - Paper
#3.Transmutation - Scissors

while True:
    
    print("""What form of nen-offense will you use Gon? \n 
1.ROCK : An extension of the ENHANCEMENT form of nen type which Gon named after his favorite game Jajanken. Enhancement increases the strength of a person who uses nen is almost all aspects and is most suitable for close range battle setups. So it is highly inefficient against emission [ Paper ] attack types and effiecent for fighting Transmutations [ Scissor ] types as the strength of their transmuted items are not able to withstand the impact.\n  
2.PAPER : An extension of the EMISSION form of nen type. Emission is most suitable for long range combat and is highly efficient for Assassins and against Enhancement types [ ROCK ]. However it loses against transmutation types [SCISSOR]. \n 
3.SCISSOR : An extension of the TRANSMUTATION form on nen type. Transmutation grants the nen user the better grasp in transmuting efficient physical forms of nen which may or may not be able to cut through other nen barriers and cut through almost all form of other earthly objects if the user is trained enough. However the strength of the forms transmuted are not as strong themselves so they crumble in the face of Enhancers [ Rock ] and are easily able to cut through the attacks of Emitters [ Paper ] """
          )
    print("Choose now from 1/2/3, it doesn't really matter if you read that or not. I just geeked out")
    gon_choice = int(input())
    
    while(gon_choice>3 or gon_choice<1):
        print("What form of nen-offense will you use Gon? \n 1.ROCK \n 2.PAPER \n 3.SCISSOR")
        gon_choice = int(input())
    
    if gon_choice == 1:
        gon_choice_name = "ROCK"
        print(gon_choice_name)
    elif gon_choice ==2:
        gon_choice_name = "PAPER"
    else:
        gon_choice_name = "SCISSOR"
    
    print("Gon : Ja...jan..ken.." + gon_choice_name)
    
#Neferopitou is shit at this game so she just guesses using the random module
    pitou_choice = nen.randint(1,3)
    
    while(gon_choice == pitou_choice):
        pitou_choice = nen.randint(1,3)
    
    if pitou_choice == 1:
        pitou_choice_name = "ROCK"
    elif pitou_choice ==2:
        pitou_choice_name = "PAPER"
    else:
        pitou_choice_name = "SCISSOR"
    
    print("Neferopitou : I can't let the King down "+ pitou_choice_name)
    
    
    #Conditions for winning the fight
    if((gon_choice==1 and pitou_choice ==2)or(gon_choice == 2 and pitou_choice == 1)):
        print("The fight is won by emission -> PAPER")
        result = "PAPER"
    elif(gon_choice==2 and pitou_choice ==3)or(gon_choice == 3 and pitou_choice == 2):
        print("The fight is won by Transmutation -> SCISSOR")
        result = "SCISSOR"
    else:
        print("The fight is won by enhancement -> ROCK")
        result = "ROCK"
    
    #Checking who wins
    if result == gon_choice_name:
        print(" <======== GON's JAJANKEN WINS =========> \n")
        print("<======= Neferepitou could not save KING MERUEM =======>")
    else:
        print("Neferopitou killed Gon and the whole fucking manga got cancelled \n ")
    
    print("Gon.. do you want to use restrain and covenant to beat the shit out of Neferopitou? Y/N \n")
    ans = input()
    if ans == "Y" or ans =="y" :
        print("I will murder you Pitou")
        continue
    else:
        break

print("If you didn't kill pitou you're an idiot, if you did you can still hope for a new HunterXHunter anime adaptation. Damn i'm so desperate.")
