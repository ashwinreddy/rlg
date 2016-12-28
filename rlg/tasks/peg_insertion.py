from task import Task
import numpy as np

class PegInsertionTask(Task):
    def __init__(self):
        self.viewer = None
        Task.__init__(self, 'peg_insertion')

    def _step(self, a):
        reward = 1/(np.linalg.norm(self.get_body_com("ball") - np.array([0.0, 0.3, -0.35])))
        self.do_simulation(a, self.frame_skip)
        ob = self._get_obs()
        return ob, reward, False, {}
