from art import logo, vs

print(logo)

from game_data import data
import random
from replit import clear

thingA = random.choice(data)
thingB = random.choice(data)
if thingB == thingA:
    thingB = random.choice(data)

compare_A_name = thingA['name']
compare_A_follower_count = thingA['follower_count']
compare_A_description = thingA['description']
compare_A_country = thingA['country']

compare_B_name = thingB['name']
compare_B_follower_count = thingB['follower_count']
compare_B_description = thingB['description']
compare_B_country = thingB['country']

print(
    f"Compare A: {compare_A_name}, {compare_A_description}, from {compare_A_country}"
)
print(vs)
print(
    f"Compare B: {compare_B_name}, {compare_B_description}, from {compare_B_country}"
)
user_input = input("Who has more followers? Type 'A' or 'B': ").upper()

flag = True
score = 0
while flag == True:
    if compare_A_follower_count > compare_B_follower_count and user_input == 'A':
        score+=1
        clear()
        print(f'You are correct! Score is {score}')

        
        compare_A_name = compare_B_name
        compare_A_follower_count = compare_B_follower_count
        compare_A_description = compare_B_description
        compare_A_country = compare_B_country

        # thingA = random.choice(data)
        thingB = random.choice(data)
        if thingB == thingA:
            thingB = random.choice(data)
      
        compare_B_name = thingB['name']
        compare_B_follower_count = thingB['follower_count']
        compare_B_description = thingB['description']
        compare_B_country = thingB['country']

        print(
    f"Compare A: {compare_A_name}, {compare_A_description}, from {compare_A_country}"
)
        print(vs)
        print(
    f"Compare B: {compare_B_name}, {compare_B_description}, from {compare_B_country}"
)
        user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
    elif compare_B_follower_count > compare_A_follower_count and user_input == 'B':
          score+=1
          clear()
          print(f'You are correct! Score is {score}')

          # thingA = random.choice(data)
          
          compare_A_name = compare_B_name
          compare_A_follower_count = compare_B_follower_count
          compare_A_description = compare_B_description
          compare_A_country = compare_B_country

          thingB = random.choice(data)
          if thingB == thingA:
              thingB = random.choice(data)
      
          compare_B_name = thingB['name']
          compare_B_follower_count = thingB['follower_count']
          compare_B_description = thingB['description']
          compare_B_country = thingB['country']

          print(
    f"Compare A: {compare_A_name}, {compare_A_description}, from {compare_A_country}"
)
          print(vs)
          print(
    f"Compare B: {compare_B_name}, {compare_B_description}, from {compare_B_country}")
          user_input = input("Who has more followers? Type 'A' or 'B': ").upper()
    else:
      clear()
      print(f'Sorry.That is wrong! Final score is {score}')
      flag = False
