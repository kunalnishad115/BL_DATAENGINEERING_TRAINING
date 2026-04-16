import random
class Game:
  def __init__(self, starting_amount, goal_amount, n):
    self.amount = starting_amount
    self.goal = goal_amount
    self.n = n
  
  def play_game(self):
    win_count=0
    bet_count=0

    for i in range(self.n):
      cash=self.amount
      cnt=0

      while cash>0 and cash<self.goal:
        cnt+=1
        if random.random()<0.5:
          cash+=1
        else:
          cash-=1
        
      if cash==self.goal:
        win_count+=1

    bet_count+=cnt

    win_percentage=(win_count/self.n)*100
    loss_percentage=100-win_percentage
    average_bets=bet_count/self.n

    print(f"Win percentage: {win_percentage:.2f}%")
    print(f"Loss percentage: {loss_percentage:.2f}%")
    print(f"Average bets: {average_bets:.2f}")


obj=Game(10, 20, 1000)
obj.play_game()

