import art
import random
from replit import clear

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)
def calculate_score(card_list):
  total=0
  total= sum(card_list)
  if(total == 21):
    return 0
  elif total >21:
    for card in range(len(card_list)):
      if(card_list[card]==11):
        card_list[card]=1
    total= sum(card_list)
    return total
  else:
    return total

def compare (user, comp):
  if user> comp:
    print(" You Win \n Game Over.")
  elif user<comp:
    print(" You Loose. \n Game Over")
  else:
    print(" Its a Draw . \n Game Over")

def blackjack():
    game_on= True
    print(art.card_logo)
    user_cards = []
    computer_cards = []
    for _ in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())
    print(f" Your cards : {user_cards} \n")
    print(f" Computer First cards : {computer_cards[0]} \n")
    score_user =calculate_score(user_cards)
    score_computer=calculate_score(computer_cards)
    if score_computer==0:
      print(" Game over - BLACKJACK , Computer Win")
      game_on=False
    elif score_user==0:
      print(" Game over - BLACKJACK , You Win")
      game_on=False
    else:
      print(f" Your total score is {score_user}\n")
    if game_on:
      user_final= False
      while not user_final:
        if input(" Draw the another card, Press Y or N \n").lower() =="y":
          user_cards.append(deal_card())
          print(f" Your cards : {user_cards} \n")
          print(f" Computer First cards : {computer_cards[0]} \n")
          score_user=calculate_score(user_cards)
          print(f" Your total score is {score_user}\n")
          if (score_user >21 or score_user==0):
             user_final= True
        else:
          user_final= True
     # print(f" Your final hand score is {score_user}\n")
      if score_user==0:
        score_user=21
        print("BLACKJACK , YOU win")
      elif score_user >21:
        print("Exceed 21 , YOU loose")
      else:
        print(" Computer Turn\n")
        print(f" Computer cards : {computer_cards} \n")
        print(f" Computer total score is {score_computer}\n")
        while score_computer < 17:
          print(" Computer draw one card\n")
          computer_cards.append(deal_card())
          print(f" computer cards : {computer_cards} \n")
          score_computer=calculate_score(computer_cards)
          print(f" Computer total score is {score_computer}\n")
          if score_computer >21:
            print("Exceed 21 , YOU Win") 
          elif(score_computer ==0):
              print("Computer Win")


       # print(f" Computer final hand score is {score_computer}")
    print(f" \n Your cards {user_cards}, Your final hand score is {score_user}\n")
    print(f" Computer cards : {computer_cards}, final hand score is {score_computer}\n")
    if(score_user< 21 and score_computer< 21):
      compare(score_user,score_computer)
    if(input("\n wanna play again Y or N \n")).lower()== "y":
      clear()
      blackjack()
    else:
      print("GoodBye")


if(input("Wany to play BLACKJACK Game ? Y or N \n")).lower() == "y":
  blackjack()
else:
  print("Game Over")
