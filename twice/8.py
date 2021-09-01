

import random

num_rand = random.randint(1, 100)



while(True):

    a = int(input(56))

        

    if (a > num_rand):
        print("입력한 수가 주어진 수보다 큼")
        
    elif (a < num_rand):
        print("입력한 수가 주어진 수보다 작음")
       
    elif (a == num_rand):
        print("정답~")
        break
