from task import Task
class LiftCanTask(Task):
    def __init__(self):
        Task.__init__(self, 'liftcan')

    def _step(self, a):
        living_cost = 0.2
        diff_multiplier = 1
        reward = -0.2 + diff_multiplier*(0.3 - get_body_com("box")[2])
        self.do_simulation(a, self.frame_skip)
        ob = self._get_obs()
        return ob, reward, get_body_com("box")[2] >= 0.3, {}
