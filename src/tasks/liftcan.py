import numpy as np
from gym import utils
import mujoco_env

class LiftCanEnv(mujoco_env.MujocoEnv, utils.EzPickle):
    def __init__(self):
        utils.EzPickle.__init__(self)
        #second param is frameskip
        mujoco_env.MujocoEnv.__init__(self, 'liftcan/liftcan.xml', 2)

    def _step(self, a):
        living_cost = -0.2
        reward = living_cost + self.get_body_com("box")[2]
        self.do_simulation(a, self.frame_skip)
        ob = self._get_obs()
        #print self.get_body_com("box")[2]
        return ob, reward, self.get_body_com("box")[2] > 0.3, {}#.get_body_com("box")[2], {}

    def reset_model(self):
        qpos = self.init_qpos + self.np_random.uniform(size=self.model.nq, low=-0.01, high=0.01)
        qvel = self.init_qvel + self.np_random.uniform(size=self.model.nv, low=-0.01, high=0.01)
        self.set_state(qpos, qvel)
        return self._get_obs()

    def _get_obs(self):
        return np.concatenate([self.model.data.qpos, self.model.data.qvel]).ravel()

    def viewer_setup(self):
        v = self.viewer
        v.cam.trackbodyid=0
        v.cam.distance = v.model.stat.extent
