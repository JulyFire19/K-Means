import random

file = open("shuju.txt", 'w')
for i in range(2000000):
    file.writelines(str(i) + " 1:" + str(round(random.uniform(1,1000),1)) +
                    " 2:" +  str(round(random.uniform(1,10000),1)) +
                    " 3:" + str(round(random.uniform(500,1500),1)) + '\n')
file.close()

# + " 1:" + str(random()) + " 2:" + str(random()) + " 3:" + str(random())