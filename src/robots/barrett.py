import numpy as np
from gym import utils
import mujoco_env

class BarrettEnv(mujoco_env.MujocoEnv, utils.EzPickle):
    def __init__(self):
        utils.EzPickle.__init__(self)
        #second param is frameskip
        mujoco_env.MujocoEnv.__init__(self, 'barrett/wam_7dof_wam_bhand.xml', 2)

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
