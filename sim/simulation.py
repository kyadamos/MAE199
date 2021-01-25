import gym

from sim_envs import GymGlucose
from agent import randomAgent, QAgent

def basic_reward(BG):
    if BG[-1] > 180:
        return -1
    elif BG[-1] < 70:
        return -2
    else:
        return 1

# Create the environment
env = gym.make('simglucose-adult1-v0')

# Random Agent
# agent = randomAgent(env)

# Q-Learning Agent
agent = QAgent(env)
episodes = 5

# Run the simulation
for i in range(episodes):
    obs = env.reset()
    for t in range(50):
        env.render(mode = "human")
        action = agent.act()
        obs, reward, done, info = env.step(action)
        if done:
            break

env.close()