from tasks import liftcan, door
from robots import baxter, darwin, claw, hand, barrett, sandia_hand

task_choices = {
    'liftcan': liftcan.LiftCanEnv,
    'door': door.DoorEnv,
}

robot_choices = {
    'baxter': baxter.BaxterEnv,
    'darwin': darwin.DarwinEnv,
    'claw': claw.ClawEnv,
    'hand': hand.HandEnv,
    'barrett': barrett.BarrettEnv,
    #'sandia_hand': sandia_hand.SandiaHandEnv,
}

def main(env, steps=1000):
    my_env = env()
    obs = my_env.reset()
    done = False
    counter = 0
    if steps == False:
        -1
    while counter != steps and not done:
        my_env.render()
        action = my_env.action_space.sample()
        obs, reward, done, info = my_env.step(action)
        counter += 1

if __name__ == "__main__":
    main(robot_choices["sandia_hand"])
