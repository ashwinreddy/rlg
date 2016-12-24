import rlg
from rlg.agents import DefaultAgent
a = DefaultAgent(True)
task = rlg.task['obstacle_course']()
a.load_task(task)
a.run_episode()
