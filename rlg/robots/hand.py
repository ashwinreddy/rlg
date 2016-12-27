import numpy as np
from robot import Robot
class HandRobot(Robot):
    def __init__(self):
        Robot.__init__(self, 'hand')

    def _step(self, a):
        reward = 1/np.sum(self.get_body_com("palm") - self.get_body_com("object"))
        self.do_simulation(a, self.frame_skip)
        ob = self._get_obs()
        return ob, reward, False, {}
