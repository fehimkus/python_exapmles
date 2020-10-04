#First we need to import necessary libraries
import gym_bandits
import gym
import numpy as np

env= gym.make('BanditTenArmedGaussian-v0')

#Our action space will be 10 as we have 10 arm
env.action_space

#Lets initialize all variables------------------------------------

#Number of rounds
num_rounds=20000

#count of number of items an arm was pulled
count=np.zeros(10)

#sum of rewards of each arm
sum_rewards=np.zeros(10)

#Q value which is the average reward
Q=np.zeros(10)

#Now we define epsilon_greedy funcyion----------------------------
def epsilon_greedy(epsilon):
    rand=np.random.random()
    if rand<epsilon:
        action=env.action_space.sample()
    else:
        action=np.argmax(Q)
    return action

#Start pulling the arm---------------------------------------------
for i in range(num_rounds):
    #select the arm using epsilon greedy
    arm=epsilon_greedy(0.5)

    #get the reward
    observation, reward, done, info =env.step(arm)

    #update the count of that arm
    count[arm] += 1

    #sum the rewards obtained from the arm
    sum_rewards[arm] += reward

    #calculate Q value which is the average rewards of the arm
    Q[arm]=sum_rewards[arm]/count[arm]

print('the optimal arm is{}'.format(np.argmax(Q)))

















    

    
