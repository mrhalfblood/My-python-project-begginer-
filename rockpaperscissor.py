
#Welcome to my beginner project of rock paper scissors game...I have used random module and time module for this project...I will add more features in future like point system and simple animation system...but before that i have to learn more about python programming language...



import random
import time

print("\t\t\t\t\t\twelcome to rock paper scissors game")

user_name = input("\n\t\t\t In order to play you have to input your name \n\t\t\t Enter your full name :")


print(f"\n\n \t\t\t KITA : Hi {user_name} ,I am KITA...🤗")
time.sleep(0.75)

print("\n\t\t\t KITA: do you want to play rock paper scissors?(y/n): ")
time.sleep(0.5)


#I am using \t\t\t & \n\n for decoration purpose only

while True:
    reply = input(f"\t\t\t {user_name}'s reply :").lower()
    if reply == "n":

        print("\t\t\t KITA: Why the hell you wasted my time..?😡🤬")

        break

    elif reply=="y":
        time.sleep(0.5)
        print("\n\n\t\t\t KITA: Great! Let's start the game...🤗:")
         
        list=["r", "p", "s"]
        names={"r": "Rock", "p": "Paper", "s": "Scissors"}

        

    

#main logic

        while True:
            time.sleep(2)
            user_choice=input(f"\t\t\t KITA: Choose your option \n\t\t\t Type: \n\t\t\t\t\t 'r' for Rock \n\t\t\t\t\t 'p' for Paper \n\t\t\t\t\t 's' for scissor  \n\t\t\t{user_name}'s choice: ").lower()
            if user_choice not in list:

                dialogue1=["Are you blind or something else?","i think your keyboard is broken..fix it and try again ","are you an idiot ?🙄😑","you don't know how to type?","Choose correct option you moron"]
                
                print(f"\t\t\t KITA : {random.choice(dialogue1)}")

            else:

                choice = random.choice(list)

                option = names[choice]
                time.sleep(1)

                print("\n\t\t\t KITA : Wait..I am calculating result using NASA computer....!!")
                time.sleep(3)

                if choice==user_choice :
                    print(f"\n\n\t\t\t KITA : Oops we did same..😅 I have also chosen {option} too , it's Tie")

                elif (user_choice=="r" and choice=="p")or(user_choice=="p" and choice=="s")or(user_choice=="s" and choice=="r") :
                    print(f"\n\n\t\t\t KITA : you can't even beat me..😂😂.I have chosen {option},I won !!! ")

                else:
                    print(f"\n\n\t\t\t KITA : you beated me.😣😣.I have chosen {option},You won ...!!")


        
            time.sleep(2.5)
            print("\n\t\t\t KITA : Do you want to play again with me..🤨😉?(yes/no)")
            

            while True:

                ending=input(f"\n\t\t\t{user_name}'s reply :").strip().lower()
                
                if (ending !="yes") and (ending!="no"):
                    ending_dialogue1=["Enter a valid answer","Are you kidding..?","I just wanted to kniw if it is yes or no 😒😒","type correctly you idiot...."]
                    print(f"\t\t\t KITA : {random.choice(ending_dialogue1)}")
                    time.sleep(0.5)

                else: 
                    break 

            if ending=="no":
                    ending_dialogue2=['it was a nice gameplay ','thanks for playing','Hope you will play soon..😏😏']
                    print(f"\t\t\t KITA :{random.choice(ending_dialogue2)}")

                    break
            

        break
    # Finally it ends here,,,latwer I will add point system and simple animation system...but before that i have yo learn ....   
                
    else : 
        dialogue2=[" Look at your keyboard and type correct option..🤬","Are you blind or something else?","i think your keyboard is broken..fix it and try again ","are you an idiot ?🙄😑","Chnage your nymber of glasses and type correctly..😶","Look closely what you have typed...","Write it carefully.."]

        print(f"\n\t\t\t KITA : {random.choice(dialogue2)}")
        

        time.sleep(1)

    







