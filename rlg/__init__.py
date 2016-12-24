from gym.envs.mujoco.mujoco_env import MujocoEnv
import sys
import tasks
import robots #import baxter, darwin, claw, hand, barrett, sandia_hand, atlas, atlas_virtual, pr2, jaco
import agents

__version__ = "1.0.a.dev"

task = {
    'liftcan': tasks.liftcan.LiftCanTask,
    'door': tasks.door.DoorTask,
    'snake': tasks.snake.SnakeTask,
    'beam_balance': tasks.beam_balance.BeamBalanceTask,
    'obstacle_course': tasks.obstacle_course.ObstacleCourseTask,
}

robot = {
    'baxter': robots.baxter.BaxterRobot,
    'darwin': robots.darwin.DarwinRobot,
    'claw': robots.claw.ClawRobot,
    'hand': robots.hand.HandRobot,
    'barrett': robots.barrett.BarrettRobot,
    # NOTE: sandia_hand is currently defective
    'sandia_hand': robots.sandia_hand.SandiaHandRobot,
    'atlas': robots.atlas.AtlasRobot,
    'atlas_virtual': robots.atlas_virtual.AtlasVirtualRobot,
    'pr2': robots.pr2.Pr2Robot,
    'jaco': robots.jaco.JacoRobot,
}
