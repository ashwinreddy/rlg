import os
import rlg
from rlg.agents import DefaultAgent
a = DefaultAgent(True)

def current_location():
    return os.path.dirname(os.path.abspath(__file__))

class ReacherTask(rlg.Task):
    def __init__(self):
        rlg.Task.__init__(self, current_location() + '/reacher.xml', True)

task = ReacherTask()
a.load_task(task)
a.run_episode()
