import numpy as np
import gym.wrappers
import tensorflow as tf
import tflearn
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)



class DefaultAgent(object):
    def __init__(self, render=False):
        logger.debug("DefaultAgent constructor called")
        self.obs = None
        self.net_reward = 0
        self.done = False
        self.render = render
        self.step_counter = 0
        self.action = None

    def load_task(self, task, directory):
        self.task = task
        self.monitor = gym.wrappers.Monitor(task, directory, force=True, video_callable=lambda count: count % 100)
        # self.task.monitor.start('/tmp/task-experiment')
        self.obs =  self.task.reset()
        self.episode_steps = task.spec.timestep_limit

    def reset(self):
        self.obs = self.task.reset()
        self.step_counter = 0

    def act(self, **kargs):
        a = kargs['action_space'].sample()
        self.action = a
        return a

    def step(self):
        if self.render:
            self.task.render()
        # print self.task, self.task.action_space
        self.obs, reward, self.done, info = self.task.step(self.act(action_space=self.task.action_space))
        self.net_reward += reward
        self.step_counter += 1
        return self.obs, reward, self.done, info

    def run_episode(self):
        while self.step_counter != self.episode_steps:
            self.step()

    def done(self):
        self.task.close()
