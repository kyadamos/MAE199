import gym
import numpy as np

# Basic agent class
class Agent():
    def __init__(self, env):
        self.action_space = env.action_space
        self.observation_space = env.observation_space
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
        
# Q-Learning agent
class QAgent(Agent):
    def __init__(self, env):
        super().__init__(env)
        print('action size =',env.action_space.n)

    def buildQ(self):
        # Initialize the Q-table
        self.q_table = 1e-2*np.random.random([self.observation_space, self.action_size])
    
    def get_action(self, state):
        # Explore or exploit
        q_state = self.q_table[state]
        eps_greedy = np.argmax(q_state)

    def train(self, experience):
        state, action, next_state, reward, done = experience
        
        q_next = self.q_table[next_state]
        q_next = np.zeros([self.action_size]) if done else q_next
        q_target = rewrad + self.discount_rate * np.max(q_next)

        q_update = q_target - self.q_table[state, action]
        self.q_table[state, action] += self.learning_rate * q_update

        if done:
            self.eps = self.eps * 0.99
        
if __name__ == '__main__':

    from sim_envs.simglucose_gym_env import T1DSimEnv

    env = gym.make('simglucose-adolescent2-v0')
    episodes = 50
    agent = QAgent(env)
    # print("action space",agent.action_space,env.action_space)
    # print("obs space",agent.obs_space,env.observation_space)
    for episode in range(episodes):
        observation = env.reset()
        done = False
        for t in range(50):
            env.render(mode = "human")
            action = agent.act()
            observation, reward, done, info = env.step(action)
            if done:
                print("Episode finished after {} timesteps".format(t+1))
                break

    env.close()