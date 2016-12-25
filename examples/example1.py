import rlg
from rlg.agents import DefaultAgent
a = DefaultAgent(True)
task = rlg.robot['pr2']()
a.load_task(task)
a.run_episode()
