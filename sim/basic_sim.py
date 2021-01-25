import gym
import wrapped_gym_env
from agent import randomAgent
import simglucose.envs

def basic_reward(BG):
    if BG[-1] > 180:
        return -1
    elif BG[-1] < 70:
        return -2
    else:
        return 1

# Create the environment
env = gym.make('simglucose-adult1-v0')

# Select an agent
Agent = randomAgent(env)
episodes = 5

# Run the simulation
for i in range(episodes):
    obs = env.reset()
    for t in range(20):
        env.render(mode = "human")
        actddd = Agent.act()
        obs, reward, done, info = env.step(actddd)
        if done:
            break

env.close()