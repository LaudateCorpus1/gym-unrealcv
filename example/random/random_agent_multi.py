import argparse
import gym_unrealcv
import gym
from gym import wrappers
import cv2
import time

class RandomAgent(object):
    """The world's simplest agent!"""
    def __init__(self, action_space):
        self.action_space = action_space

    def act(self, observation, reward, done):
        return self.action_space.sample()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=None)
    parser.add_argument("-e", "--env_id", nargs='?', default='UnrealTrackingMPRoom-DiscreteColor-v2',
                        help='Select the environment to run')
    parser.add_argument("-r", "--render", default=False, metavar='G', help='show env using cv2')
    args = parser.parse_args()
    env = gym.make(args.env_id)

    agent_0 = RandomAgent(env.action_space)
    agent_1 = RandomAgent(env.action_space)

    episode_count = 100
    rewards = 0
    done = False

    for i in range(episode_count):
        env.seed(i)
        obs = env.reset()
        count_step = 0
        t0 = time.time()
        while True:
            action_0 = agent_0.act(obs, rewards, done)
            action_1 = agent_0.act(obs, rewards, done)
            # action_1 = agent_1.act(obs, rewards, done)
            obs, rewards, done, _ = env.step([action_0, action_1])
            count_step += 1
            if args.render:
                img = env.render(mode='rgb_array')
                #  img = img[..., ::-1]  # bgr->rgb
                cv2.imshow('show', img)
                cv2.waitKey(1)
            if done:
                fps = count_step / (time.time() - t0)
                print ('Fps:' + str(fps))
                break

    # Close the env and write monitor result info to disk
    env.close()


