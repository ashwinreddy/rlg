#RLG
Robot Learning Gym is a tool to test reinforcement learning algorithms for robotics tasks a la OpenAI's [Universe](https://universe.openai.com/) and/or [Gym](https://gym.openai.com).

The purpose is to evaluate how well the various RL algorithms work on robotics-like tasks by using a standardized and consistent metric.

#Installation
You will need MuJoCo for this to work. Obtain a 30 day free trial license or purchase a license from [here](https://www.roboti.us/license.html). Be sure to download the `mjpro` [folder](https://www.roboti.us/) and license keys in a clean directory (you will need to move them later).

First, install OpenAI Gym using these [instructions](https://github.com/openai/gym#installation) or [these ones](https://gym.openai.com/docs).
Next, you will need to make sure that you also have the OpenAI interface to MuJoCo. If you did a full install, this should have already been installed. Make sure that this is the case (if you are lost, use [this link](https://github.com/openai/gym#mujoco)).
You will need `mujoco-py`, the Python bindings for MuJoCo, which is written in C++. Follow the instructions [here](https://github.com/openai/mujoco-py#obtaining-the-binaries-and-license-key)

##Usage
If all goes well, you should be able to run the `src/__main__.py` script of this package.
Either run `python src/. hand` or `python src/. door` from the root folder (where ever you cloned this repository)

##Available tasks and robots
Tasks:

1. Opening a door (currently does not have a robot in the environment), which I developed
2. Lifting a can using a 7 degree-of-freedom robot arm, which is built using an example XML file on the MuJoCo website

Robots (downloaded using [MuJoCo Resources](http://www.mujoco.org/forum/index.php?resources/), some had errors and needed slight edits to work):

1. Baxter
2. Darwin
3. Hand/Claw
4. Barrett Hand
5. Atlas
6. PR2
7. Kinova arms
8. Snake swimmer
9. Beam balance

##Todo List
- [ ] Incorporate MuJoCo OpenAI Gym tasks (at least the ones that are semi-robotic)
- [ ] Create a system where users can ask for tasks based on difficulty
- [ ] Clean up API, allow easy testing of algorithms like Gym
- [ ] Develop a base class for different environments since most MuJoCo tasks are fairly similar, main difference is the reward function
- [ ] Debug the Sandia Hand robot: STL files not loading for some reason
- [ ] Build website, add documentation (readme + wiki + website)
- [ ] Implement more tasks and define reward functions for all tasks
- [ ] Allow mix-and-match for robots and tasks
- [ ] Develop code to facilitate transfer learning (group tasks by similarity)
- [ ] Implement various RL algorithms as benchmarks 
