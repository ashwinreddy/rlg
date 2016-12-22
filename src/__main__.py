import custom
import swimmer
import inverted_pendulum
if __name__ == "__main__":
    my_env = custom.CustomEnv()
    obs = my_env.reset()
    done = False
    for _ in range(1000):
        my_env.render()
        action = my_env.action_space.sample()
        print action
        obs, reward, done, info = my_env.step(action)
        #print my_env.model.nu, my_env.model.nv
