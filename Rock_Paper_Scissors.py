import random
n=int(input('Enter number of chances: '))
Ch = ["R", "P", "S"]
PlayerScore =0
SystemScore = 0
name=input("enter your name please-->\n")
print('''
      -🙏🙏-------WELCOME-------🙏🙏-
                    ''')
print(name,'! Lets begin the game...😊😊 ')
print("-------------------------------------------")
def play_game(): 
      n=int(input('Enter number of chances: '))
      Ch = ["R", "P", "S"]
      PlayerScore =0
      SystemScore = 0
for i in range(1,n):
  
   SystemCh = str(random.choice(Ch))
   PlayerCh = input("\nEnter R for Rock, P for Paper, S for Scissors: \n")
   if PlayerCh in Ch: 
    if PlayerCh== "R" and SystemCh == "P":
     print("System choice: ", SystemCh)
     print("System Won")
     SystemScore+=1
    elif PlayerCh == "P" and SystemCh == "S":
     print("System choice: ", SystemCh)
     print("System Won")
    elif PlayerCh == "S" and SystemCh== "R":
     print("System choice: ", SystemCh)
     print("System Won")
     SystemScore+=1
    elif PlayerCh == SystemCh:
     print("System choice: ", SystemCh)
     print("Tie")
     SystemScore=0
     PlayerScore+=0
    else:
     print(name,"you won this game..🎉🎉🎉🎉")
     print("System choice: ", SystemCh)
     PlayerScore+=1
    
    print("ScoreBoard:")
    print(f"{name} your score is : {PlayerScore} | System: {SystemScore}")
    print(f"You won in Attempt:[{i}]")
    
   else:
    print("Enter R or P or S only!!")
    
    
#main code
play_game()