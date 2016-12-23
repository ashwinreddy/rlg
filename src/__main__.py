import sys
import tasks
from robots import baxter, darwin, claw, hand, barrett, sandia_hand, atlas, atlas_virtual, pr2, jaco

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

def main(Robot, steps=1000):
    my_Robot = Robot()
    obs = my_Robot.reset()
    done = False
    counter = 0
    if steps == False:
        steps = -1
    while counter != steps and not done:
        my_Robot.render()
        action = my_Robot.action_space.sample()
        obs, reward, done, info = my_Robot.step(action)
        counter += 1

if __name__ == "__main__":
    # task["door"] is an Robotironment for the task of opening a door
    # robot["hand"] is an Robotironment which includes a hand as well as an object on a table (pick-n-place task)
    main(robot["sandia_hand"])
