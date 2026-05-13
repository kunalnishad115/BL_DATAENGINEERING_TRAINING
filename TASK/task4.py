import numpy as np

np.random.seed(1)

engagement = np.random.randint(30,300,size=(14,6))

print(engagement)

total_time = engagement.sum(axis=0)

print(total_time)

avg_time=engagement.mean(axis=0)
print(avg_time)

high_engag=np.where(avg_time>150)
print(high_engag)

rank=np.argsort(avg_time)[::-1]
print(rank+1)