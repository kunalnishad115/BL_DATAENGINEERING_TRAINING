import random

def gambler_game(starting_amount, goal_amount, simulations):
  total_wins=0
  total_bets=0

  for i in range(simulations):
    cash=starting_amount
    bets=0

    while cash>0 and cash<goal_amount:
      bets+=1

      
      if random.random()<0.5:
        cash+=1  # win scenario
      else:
        cash-=1  # lose scenario

    if cash==goal_amount:
      total_wins+=1

    total_bets+=bets


  win_percentage = (total_wins / simulations) * 100
  loss_percentage = 100 - win_percentage
  avg_bets = total_bets / simulations

  print("Total Wins:", total_wins)
  print("Win %:", win_percentage)
  print("Loss %:", loss_percentage)
  print("Average Bets:", avg_bets)










starting_amount=int(input("Enter the starting Game amount: "))
goal_amount=int(input("Enter the Goal amount: "))
simulations=int(input("Enter the number of Simulations: "))

gambler_game(starting_amount, goal_amount, simulations)