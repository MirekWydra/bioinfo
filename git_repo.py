# %%
import csv
import random
# %%
randfile = open("Random.csv", "w")
writer = csv.writer(randfile, delimiter=",")
# %%
for i in range(100000):
     pair = random.randint(1, 100), random.randint(1, 100)
     writer.writerow(pair)

randfile.close()
# %%
