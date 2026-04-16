import random
# class CouponException(Exception):
#   def __init__(self, msg):
#     print(msg)


class Game:
  def __init__(self,n):
    self.n=n

  def coupon_game(self):
    cnt=0
    distinct_coupons=set()

    while len(distinct_coupons)<self.n:
      val=random.randint(1,self.n)
      cnt+=1

      if val not in distinct_coupons:
        distinct_coupons.add(val)
      else:
        # print("Duplicate coupon generated: ")
        pass


    print("Total number of coupons generated to get all distinct coupons: ",cnt)
    print("Distinct coupons: ",distinct_coupons)



obj=Game(5)
obj.coupon_game()

