import numpy as np
from gym import utils
from gym.envs.mujoco.mujoco_env import MujocoEnv

class Robot(MujocoEnv, utils.EzPickle):
    def __init__(self, pathname='default'):
        utils.EzPickle.__init__(self)
        MujocoEnv.__init__(self, pathname + '/' + pathname + '.xml', 2)

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
