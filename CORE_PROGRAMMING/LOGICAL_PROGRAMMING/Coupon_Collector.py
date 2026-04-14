import random
def fun(n):
  collected_coupons=set()
  cnt=0

  while len(collected_coupons)<n:
    new_coupon=random.randint(1,n)
    cnt+=1
    

    if new_coupon not in collected_coupons:
      collected_coupons.add(new_coupon)
    else:
      print(f"Duplicate coupon {new_coupon} found. Ignoring.")

  print(f"Total coupons collected:", collected_coupons)
  print(f"Total random numbers generated: {cnt}")



number_of_coupons=int(input("Enter the number of unique coupons: "))
fun(number_of_coupons)