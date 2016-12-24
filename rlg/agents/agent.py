class DefaultAgent(object):
    def __init__(self, render=False, episode_step=1000):
        self.obs = None
        self.net_reward = 0
        self.done = False
        self.render = render
        self.step_counter = 0
        self.episode_step = episode_step

    def load_task(self, task):
        self.task = task
        self.obs =  self.task.reset()

    def act(self, **kargs):
        return kargs['action_space'].sample()

    def step(self):
        if self.render:
            self.task.render()
        self.obs, reward, self.done, info = self.task.step(self.act(action_space=self.task.action_space))
        self.net_reward += reward
        self.step_counter += 1

    def run_episode(self):
        while self.step_counter != self.episode_step:
            self.step()
