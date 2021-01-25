import gym
import numpy as np
import simglucose.envs
import wrapped_gym_env
from gym.wrappers import FlattenObservation

# Basic agent class
class Agent():
    def __init__(self, env):
        self.action_space = env.action_space
        self.observation_space = env.observation_space
        print("action space = ", self.action_space)
        print("observation space = ", self.observation_space)
        return
    
    def act(self):
        return 0

# Agent that performs random actions
class randomAgent():
    def __init__(self, env):
        self.action_size = env.action_space
        print("action size = ", env.action_space)
        return

    def act(self):
        return self.action_size.sample()
        

class QAgent(Agent):
    def __init__(self, env):
        super().__init__(env)

    def buildQ(self):
        # Initialize the Q-table
        self.q_table = e-2*np.random.random([self.observation_space, self.action_space])
    
    def get_action(self, state):
        # Explore or exploit
        q_state = self.q_table[state]
        eps_greedy = np.argmax(q_state)

if __name__ == '__main__':

    env = gym.make('simglucose-adolescent2-v0')

    episodes = 50
    Agent = Agent(env)

    for episode in range(episodes):
        observation = env.reset()
        done = False
        for t in range(50):
            env.render(mode = "human")
            action = Agent.act()
            observation, reward, done, info = env.step(action)
            if done:
                print("Episode finished after {} timesteps".format(t+1))
                break

    env.close()
