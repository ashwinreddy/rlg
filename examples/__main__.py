import numpy as np
import rlg
import os
agent = rlg.agents.DefaultAgent(True)

class PegInsertionTask(rlg.tasks.task.Task):
    def __init__(self):
        self.viewer = None
        rlg.tasks.task.Task.__init__(self, os.path.dirname(__file__) + '/example.xml', True)

    def _step(self, a):
        reward = 1/(np.sum(self.get_body_com("ball") - np.array([0.0, 0.3, -0.35]))**2)
        self.do_simulation(a, self.frame_skip)
        ob = self._get_obs()
        return ob, reward, False, {}

agent.load_task(PegInsertionTask(), '/tmp/experiment_1')
for episode in xrange(1):
    for t in xrange(200):
        agent.task.render()
        s_prime, reward, done, info = agent.step()
        print reward
