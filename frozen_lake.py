#All necessary libraries
import gym
import numpy as np

#We make our frozen lake environment using OpenAI's Gym:
env= gym.make('FrozenLake-v0')

#Look at the complete function of value_iteration() for a better understanding:
def value_iteration(env, gamma = 1.0):
    #First, we initialize the random value table which is 0 for all the states and numbers of iterations
    value_table=np.zeros(env.observation_space.n)
    no_of_iterations=100000
    threshold = 1e-20
    #Then, upon starting each iteration, we copy the value_table to updated_value_table
    for i in range(no_of_iterations):
        updated_value_table=np.copy(value_table)
        #As we calculate next_state_rewards for all actions of a state and append it to our Q value
        #we pick up the maximum Q value and update it as a value of our state
        for state in range(env.observation_space.n):
            Q_value=[]
    
            for action in range(env.action_space.n):
                next_states_rewards = []
        
                for next_sr in env.P[state][action]:
                    trans_prob, next_state, reward_prob, _ = next_sr
                    next_states_rewards.append((trans_prob*(reward_prob+gamma*updated_value_table[next_state])))
                Q_value.append(np.sum(next_states_rewards))
        #pick up the maximum Q value and update it as value of a state value_table[state] =max(Q_value)
        
            value_table[state]=max(Q_value)
        #We defined a variable called threshold and then we will see if the difference is less
        #than our threshold ; if it is less, we break the loop and return the value function as the
        #optimal value function
        if (np.sum(np.fabs(updated_value_table-value_table))<= threshold):
            print('Value-iteration converged at iteration# %d.' %(i+1))
            break
    return value_table

#Thus, we can derive optimal_value_function using the value_iteration
optimal_value_function = value_iteration(env=env, gamma=1.0)

#We calculate the Q value using our optimal value action and
#pick up the actions which have the highest Q value for each state as the optimal policy. We
#do this via a function called extract_policy()
def extract_policy(value_table, gamma=1.0):
    #First, we define the random policy; we define it as 0 for all the states
    policy=np.zeros(env.observation_space.n)

    #Then, for each state, we build a Q_table and for each action in that state
    #we compute the Q value and add it to our Q_table
    for state in range(env.observation_space.n):
        Q_table=np.zeros(env.action_space.n)
        for action in range(env.action_space.n):
            for next_sr in env.P[state][action]:
                trans_prob, next_state, reward_prob, _ =next_sr
                Q_table[action] += (trans_prob*(reward_prob+gamma*value_table[next_state]))
                
    #Then we pick up the policy for the state as the action that has the highest Q value
        policy[state]=np.argmax(Q_table)
    return policy
#Thus, we can derive the optimal_policy as follows:
optimal_policy = extract_policy(optimal_value_function, gamma=1.0)

print (optimal_policy)
