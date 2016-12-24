import numpy as np
from gym import utils
from gym.envs.mujoco.mujoco_env import MujocoEnv
import os
from os import path

class Task(MujocoEnv, utils.EzPickle):
    def __init__(self, pathname='default.xml'):
        print "Task is being initialized..."
        utils.EzPickle.__init__(self)
        filename = pathname + '/' + pathname + '.xml'
        pathname = os.path.join(os.path.dirname(__file__), '..', 'assets', filename)
        print "Loading {}".format(pathname)
        MujocoEnv.__init__(self, pathname, 2)

    def _step(self, a):
        reward = 1
        self.do_simulation(a, self.frame_skip)
        ob = self._get_obs()
        return ob, reward, False, {}

    def reset_model(self):
        qpos = self.init_qpos + self.np_random.uniform(size=self.model.nq, low=-0.01, high=0.01)
        qvel = self.init_qvel + self.np_random.uniform(size=self.model.nv, low=-0.01, high=0.01)
        self.set_state(qpos, qvel)
        return self._get_obs()

    def _get_obs(self):
        return np.concatenate([self.model.data.qpos, self.model.data.qvel]).ravel()

    def viewer_setup(self):
        self.viewer.cam.distance = self.model.stat.extent * 0.5
        self.viewer.cam.lookat[2] += .8
        self.viewer.cam.elevation = -20
