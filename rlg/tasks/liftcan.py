from task import Task
import numpy as np
class LiftCanTask(Task):
    def __init__(self):
        Task.__init__(self, 'liftcan')
        # print self.viewer
        self.viewer = None

    def _step(self, a):
        living_cost = 0.2
        diff_multiplier = 1
        reward = -0.2 + diff_multiplier*(0.3 - self.get_body_com("box")[2])
        self.do_simulation(a, self.frame_skip)
        ob = self._get_obs()
        return ob, reward, self.get_body_com("box")[2] >= 0.3, {}

    def _get_obs(self):
        return np.concatenate([self.model.data.qpos, self.model.data.qvel]).ravel()
