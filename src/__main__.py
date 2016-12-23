from tasks import liftcan, door, snake, beam_balance
from robots import baxter, darwin, claw, hand, barrett, sandia_hand, atlas, atlas_virtual, pr2, jaco

task_choices = {
    'liftcan': liftcan.LiftCanEnv,
    'door': door.DoorEnv,
    'snake': snake.SnakeEnv,
    'beam_balance': beam_balance.BeamBalanceEnv
}

robot_choices = {
    'baxter': baxter.BaxterEnv,
    'darwin': darwin.DarwinEnv,
    'claw': claw.ClawEnv,
    'hand': hand.HandEnv,
    'barrett': barrett.BarrettEnv,
    #'sandia_hand': sandia_hand.SandiaHandEnv,
    'atlas': atlas.AtlasEnv,
    'atlas_virtual': atlas_virtual.AtlasVirtualEnv,
    'pr2': pr2.Pr2Env,
    'jaco': jaco.JacoEnv,
}

def main(env, steps=1000):
    my_env = env()
    obs = my_env.reset()
    done = False
    counter = 0
    if steps == False:
        steps = -1
    while counter != steps and not done:
        my_env.render()
        action = my_env.action_space.sample()
        obs, reward, done, info = my_env.step(action)
        counter += 1

if __name__ == "__main__":
    main(task_choices["beam_balance"])
