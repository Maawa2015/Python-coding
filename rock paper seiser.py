import random

def rock_paper_seiser():
     choice=["rock","paper","seider"]

     while True:
          user_score=0
          computer_score=0
          round_NUMBER=1
          

          print("\nwelcome to rock_paper_seiser game.")
          print("TYPE 'quite' anytime to exite.\n ")


          while True:
               print(f"\n_ _ _ _ _ ROUND{round_NUMBER}_ _ _ _ ")
               print("available:rock, paper, seiser,quite")
               user_choice=input("enter your choice:").lower()
               
               if user_choice == "quit":
                    print("\n1thank you for playing this game")
                    print(f"Final score => you:{user_score} | computer:{computer_score}\n")
                    break
               if user_choice not in choices: