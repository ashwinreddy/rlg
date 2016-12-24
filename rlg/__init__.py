from gym.envs.mujoco.mujoco_env import MujocoEnv
import sys
import tasks
from robots import baxter, darwin, claw, hand, barrett, sandia_hand, atlas, atlas_virtual, pr2, jaco
import agents

__version__ = "1.0.a.dev"

task = {
    'liftcan': tasks.liftcan.LiftCanTask,
    'door': tasks.door.DoorTask,
    'snake': tasks.snake.SnakeTask,
    'beam_balance': tasks.beam_balance.BeamBalanceTask
}

robot = {
    'baxter': baxter.BaxterRobot,
    'darwin': darwin.DarwinRobot,
    'claw': claw.ClawRobot,
    'hand': hand.HandRobot,
    'barrett': barrett.BarrettRobot,
    # NOTE: sandia_hand is currently defective
    'sandia_hand': sandia_hand.SandiaHandRobot,
    'atlas': atlas.AtlasRobot,
    'atlas_virtual': atlas_virtual.AtlasVirtualRobot,
    'pr2': pr2.Pr2Robot,
    'jaco': jaco.JacoRobot,
}
# user should do somethinag like this
# agent  = rlg.Agent()
# task = task['liftcan']
# agent.load_task(task)
# task.
print "RLG initialized..."
