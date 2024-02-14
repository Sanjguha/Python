import art
import random
from Game_data import data
from replit import clear
print(art.logo)

def selection():
  selected_list =random.sample(data,2)
  
  return selected_list

def check(First,Second):
  if First["follower_count"] > Second["follower_count"]:
     return First
  else:
    return Second    

def game():
  score=0
  is_game_on=True
  while is_game_on:
    List=selection()
    First=List[0]
    print(f' Compare A :{First["name"]}, a {First["description"]}, from {First["country"]}.')
    print(art.vs)
    Second=List[1]
    print(f' Compare B :{Second["name"]}, a {Second["description"]}, from {Second["country"]}.')
    answer= check(First,Second)
    if input("\n Who has more followers ? Type 'A' or 'B' :").lower() =='a':
      clear()
      print(art.logo)
      if( First == answer):
          score+=1
          print(f"\n You're right ! Current score: {score}.")
  
      else:
        print(f"\n Sorry, That's Wrong. Final score: {score}.")
        return
    else:
      clear()
      print(art.logo)
      if( Second == answer):
        score+=1
        print(f"\nY ou're right ! Current score: {score}.")

      else:
        print(f"\n Sorry, That's Wrong. Final score: {score}.")
        return

game()
print("End Game")
