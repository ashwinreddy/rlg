import numpy as np
import gym.wrappers
import tensorflow as tf
import tflearn

class DefaultAgent(object):
    def __init__(self, render=False, episode_steps=1000):
        self.obs = None
        self.net_reward = 0
        self.done = False
        self.render = render
        self.step_counter = 0
        self.episode_steps = episode_steps
        self.action = None

    def load_task(self, task, directory):
        self.task = task
        self.monitor = gym.wrappers.Monitor(directory, force=True, video_callable=lambda count: count % 100)(task)
        # self.task.monitor.start('/tmp/task-experiment')
        self.obs =  self.task.reset()

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
        # self.task.monitor.close()

class QLearner(DefaultAgent):
    def __init__(self, render=False, episode_steps=1000):
        DefaultAgent.__init__(self, render, episode_steps)
        self.network = self.model()
        self.gamma   = 0.9

    def model(self):
        input_data = tflearn.input_data(shape=[None, 31])
        fc1 = tflearn.fully_connected(input_data, 64)
        fc2 = tflearn.fully_connected(fc1, 9)
        net = tflearn.regression(fc2)
        model = tflearn.DNN(net)
        return model

    def load_task(self, task, directory):
        DefaultAgent.load_task(self, task, directory)
        self.s = self.obs
        self.s_prime = None
        self.done = False

    def step(self):
        return DefaultAgent.step(self)

    def act(self, **kargs):
        return kargs['action_space'].sample()
