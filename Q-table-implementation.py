
# coding: utf-8

# In[1]:


import gym
import numpy as np
env = gym.make('FrozenLake-v0')


# In[26]:


Q = np.zeros([env.observation_space.n,env.action_space.n])
lr=.8
y = 0.95
num_episodes = 2000
reward_list = []
for i in range(num_episodes) :
    s = env.reset()
    reward_All = 0
    d = False
    j = 0
    while j < 99 :
        j+=1
        a = np.argmax(Q[s,:] + np.random.randn(1,env.action_space.n)*(1./(i+1)))
        s1,r,d,_ = env.step(a)
        Q[s,a] = Q[s,a] + lr * (r + y *(np.max(Q[s1, :] - Q[s,a]))) 
        reward_All += r
        s = s1
        if d == True:
            break
    reward_list.append(reward_All)
print ("Score over time: ")
print (str(sum(reward_list)/num_episodes) ) 
print ("Final Q-Table Values")
print (Q)  

