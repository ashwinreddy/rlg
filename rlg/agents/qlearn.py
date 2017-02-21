from neural_net import NeuralNet

class QLearningAgent(DefaultAgent):
    def __init__(self, render):
        self.net = NeuralNet()
        super(QLearningAgent, self).__init__(render)

    def act(self, **kargs):
        # 1. figure out what actions can be taken
        # 2. Use the net to compute a Q value
        # 3. Take that action
        # 4. see a response, and update
        pass

    def step(self):
        pass
