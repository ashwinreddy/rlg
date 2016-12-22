from tasks import door
from tasks import liftcan
if __name__ == "__main__":
    my_env = liftcan.LiftCanEnv()
    obs = my_env.reset()
    done = False
    for _ in range(1000):
        my_env.render()
        action = my_env.action_space.sample()
        print action
        obs, reward, done, info = my_env.step(action)
