#We import necessary libraries
import gym
import random

#Now we make our environment using a gym and visualization
env = gym.make('Taxi-v3')
env.render()

#First initialize our learning rate alpha, epsilon value and gamma
alpha=0.4
gamma=0.999
epsilon=0.017

#Then we initialize Q table; it has a dictionary that stores
#the state-action value pair as (state, action)

q = {}
for s in range(env.observation_space.n):
    for a in range(env.action_space.n):
        q[(s,a)] = 0
    
#we will define the funcktion for updating the q table via
#our Q learning update rule
def update_q_table(prev_state, action, reward, nextstate, alpha, gamma):
    qa= max([q[(nextstate, a)] for a in range(env.action_space.n)])
    q[(prev_state, action)] += alpha*(reward +gamma * qa - q[(prev_state, action)])

#we define a function for performing the epsilon-greedy policy
#where we pass state and epsilon value
#we generate some random number in uniform distribution and
#if the number is less than the epsilon, we explore a different
#action in the state or else we exploit the action that has max q value
def epsilon_greedy_policy(state, epsilon):
    if random.uniform(0,1) < epsilon:
        return env.action_space.sample()
    else:
        return max(list(range(env.action_space.n)), key = lambda x: q[(state, x)])

    #we will see how to perform Qlearning, putting together all these functions:
    #for each episode
for i in range(8000):

    r=0
    #first we initialize the environment
    prev_state=env.reset()
    while True:
        #in each state we select action by epsilon greedy policy
        action=epsilon_greedy_policy(prev_state,epsilon)
        #then we take the selected action and move to the next state
        nextstate, reward, done, _=env.step(action)
        #and we update the q valueusing the update_q_table() function
        #which updates q table according to our pdate rule.

        update_q_table(prev_state, action, reward, nextstate, alpha, gamma)
        #then we update the previous state as next state
        prev_state = nextstate

        #and store the rewards in r
        r += reward

        #if done i.e if we reached the terminal state of the episode
        #if break the loop and start the next episode
        if done:
            break

    print("total reward: ", r)

env.close()

