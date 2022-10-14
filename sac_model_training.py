import gym
import os
from stable_baselines3 import SAC
import highway_env

env = gym.make("parking-v0")

env.reset()

models_dir = "models/SAC"
logdir = "logs"

if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(logdir):
    os.makedirs(logdir)

model = SAC(policy="MultiInputPolicy", verbose=1, env=env, tensorboard_log=logdir)

TIMESTAMPS = 10000

for i in range(1,30):
    model.learn(total_timesteps=TIMESTAMPS, reset_num_timesteps=False, tb_log_name="SAC")
    model.save(f"{models_dir}/{TIMESTAMPS*i}")