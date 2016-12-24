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
