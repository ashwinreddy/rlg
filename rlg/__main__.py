# import sys
# import rlg.tasks
# from rlg.robots import baxter, darwin, claw, hand, barrett, sandia_hand, atlas, atlas_virtual, pr2, jaco
# from rlg.agents import agent
#
# task = {
#     'liftcan': tasks.liftcan.LiftCanTask,
#     'door': tasks.door.DoorTask,
#     'snake': tasks.snake.SnakeTask,
#     'beam_balance': tasks.beam_balance.BeamBalanceTask
# }
#
# robot = {
#     'baxter': baxter.BaxterRobot,
#     'darwin': darwin.DarwinRobot,
#     'claw': claw.ClawRobot,
#     'hand': hand.HandRobot,
#     'barrett': barrett.BarrettRobot,
#     # NOTE: sandia_hand is currently defective
#     'sandia_hand': sandia_hand.SandiaHandRobot,
#     'atlas': atlas.AtlasRobot,
#     'atlas_virtual': atlas_virtual.AtlasVirtualRobot,
#     'pr2': pr2.Pr2Robot,
#     'jaco': jaco.JacoRobot,
# }
#
# def main(env_class, steps=1000):
#     env = env_class()
#     obs = env.reset()
#     done = False
#     counter = 0
#     if steps == False:
#         steps = -1
#     while counter != steps and not done:
#         env.render()
#         action = env.action_space.sample()
#         obs, reward, done, info = env.step(action)
#         counter += 1
#
# if __name__ == "__main__":
#     # task["door"] is an env for the task of opening a door
#     # robot["hand"] is an env which includes a hand as well as an object on a table (pick-n-place task)
#     main(robot["sandia_hand"])
