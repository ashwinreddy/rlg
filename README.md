#RLG
Robot Learning Gym is a tool to test reinforcement learning algorithms for robotics tasks a la [OpenAI Gym](https://gym.openai.com/).

The purpose is to evaluate how well the various RL algorithms work by using a standardized and consistent metric.

##Features
RLG has a compilation of different MuJoCo tasks and robots

##Development
Currently, tasks are being built using the MuJoCo simulation environment and some code borrowed from Gym.
There are two tasks:

1. Opening a door (currently does not have a robot in the environment), which I developed
2. Lifting a can using a 7 degree-of-freedom robot arm, which is built using an example XML file on the MuJoCo website

And here are the robots:
1. Baxter, downloaded from the MuJoCo Resources (had to edit lines 37-40 to get it to work correctly)
2. Darwin (from MJC Resources)
3. Hand/Claw
4. Barrett Hand
5. Atlas (v5 and virtual)
6. PR2
7. Kinova arms
8. Snake swimmer
9. Beam balance

##Dependencies
1. MuJoCo
2. OpenAI Gym with MuJoCo Python bindings

##Todo List
- [ ] Incorporate OpenAI Gym tasks
- [ ] Clean up API, allow testing of algorithms
- [ ] Base class for different environments (allow reward function to be overriden)
- [ ] Debug Sandia Hand, STL files not loading for some reason?
- [ ] Build website, add documentation (readme + wiki)
- [ ] Define reward functions
- [ ] Implement more tasks
- [ ] Allow mix-and-match for robots and tasks
- [ ] Develop code to facilitate transfer Learning
- [ ] Implement various RL algorithms as benchmarks
