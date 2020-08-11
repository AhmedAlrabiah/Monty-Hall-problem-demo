#!/usr/bin/env python
# coding: utf-8

# This is a code to practically and figurally test the Monty Hall problem which is you have three doors and a prize lies behind one of them. You choose one of the doors and then one of the two with no prize doors be opened and you will be asked if you would like to switch your choice to the remaining choice or stay with you the original choice.
# 
# Ahmed Alrabiah,
# 11/8/2020

# In[ ]:


print('Monty Hall problem, Should you switch the door?')


# In[ ]:


import matplotlib.pyplot as plt
import numpy as np


# In[ ]:


userchoice = input('''Do you want entering the choices be automatic or manual?
Enter "1" for automatic entering or "2" for manually: ''')
if userchoice == '1' or userchoice == '2':
    userchoice = int(userchoice)
else:
    print("Error, you didn't choose 1 or 2")


# In[ ]:


while True:
    try:
        N = int(input("How many time should the process repeat? "))
        break
    except:
        print('wrong value, you must enter an integer')
if userchoice == 1:
    staycounter = 0
    switchcounter = 0
    
    for i in range(N):
        choices = [1, 2, 3]
        prize = np.random.randint(1,4)
        flag = np.random.randint(1,4)
        for i in choices:
            if i != flag:
                choices.remove(i)
                break
        if flag == prize:
            staycounter += 1
        elif flag != prize:
            switchcounter += 1
            
            
elif userchoice == 2:
    staycounter = 0
    switchcounter = 0
    
    for i in range(N):
        choices = [1, 2, 3]
        prize = np.random.randint(1,4)
        
        while True:
            flag = input('You are presented with three doors 1, 2, and 3\nOne of the doors hides a prize behind it\nWhich door you would choose: ')
            
            if '1' <= flag <= '3':
                flag = int(flag)
                break
            
            else:
                print('\n\nYou need to choose from 1 to 3 and you entered', flag, '!!!')
        
        for i in choices:
            if i != flag:
                choices.remove(i)
                break
        if flag == prize:
            staycounter += 1
        elif flag != prize:
            switchcounter += 1


# In[ ]:


plt.figure()
plt.bar(['switch', 'stay'], [switchcounter, staycounter])
plt.title('Hall Problem')
plt.xlabel('Final choices')
plt.ylabel('Number of wins')

print('The probability of winning after switching in the', N, 'attempts is', (switchcounter/N)*100, '%.')
print('and the probability of winning after staying in the', N, 'attempts is', (staycounter/N)*100, '%.')


# In[ ]:





# In[ ]:




