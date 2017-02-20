from gym.envs.mujoco.mujoco_env import MujocoEnv
import gym
import sys
import tasks
from tasks.task import Task
import robots
import agents
import os
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

__version__ = "1.0.a.dev"
__all__ = ['tasks', 'robots', 'agents']

task = {
    'Liftcan-v0': tasks.liftcan.LiftCanTask,
    'Door-v0': tasks.door.DoorTask,
    'Snake-v0': tasks.snake.SnakeTask,
    'BeamBalance-v0': tasks.beam_balance.BeamBalanceTask,
    'ObstacleCourse-v0': tasks.obstacle_course.ObstacleCourseTask,
    'PegInsertion-v0': tasks.peg_insertion.PegInsertionTask
}

robot = {
    'Baxter-v0': robots.baxter.BaxterRobot,
    'Darwin-v0': robots.darwin.DarwinRobot,
    'Claw-v0': robots.claw.ClawRobot,
    'Hand-v0': robots.hand.HandRobot,
    'Barrett-v0': robots.barrett.BarrettRobot,
    # NOTE: sandia_hand is currently defective
    'SandiaHand-v0': robots.sandia_hand.SandiaHandRobot,
    'Atlas-v0': robots.atlas.AtlasRobot,
    'AtlasVirtual-v0': robots.atlas.AtlasVirtualRobot,
    'Pr2-v0': robots.pr2.Pr2Robot,
    'Jaco-v0': robots.jaco.JacoRobot,
}

def make(str_id, tl=1000):
    if str_id in robot:
        env = robot[str_id]()
        env.spec = gym.envs.registration.EnvSpec(str_id, timestep_limit=tl)
        return env
    elif str_id in task:
        env = task[str_id]()
        env.spec = gym.envs.registration.EnvSpec(str_id, timestep_limit=tl)
        return env
    else:
        return gym.make(str_id)
