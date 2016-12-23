#RLG
Robot Learning Gym is a tool to test reinforcement learning algorithms for robotics tasks a la OpenAI's [Universe](https://universe.openai.com/) and/or [Gym](https://gym.openai.com).

The purpose is to evaluate how well the various RL algorithms work on robotics-like tasks by using a standardized and consistent metric.

#Installation
You will need MuJoCo for this to work. Be sure to download the `mjpro` folder and license keys in a clean directory (you will need to move them later).

First, install OpenAI Gym. The instructions can be found [here](https://github.com/openai/gym#installation).
Next, you will need to make sure that you also have the OpenAI interface to MuJoCo. To ensure that this is the case, use [this link](https://github.com/openai/gym#mujoco).
You will need `mujoco-py`, the Python bindings for MuJoCo, which is written in C++. Follow the instructions [here](https://github.com/openai/mujoco-py#obtaining-the-binaries-and-license-key)

<<<<<<< HEAD
#Usage
If all goes well, you should be able to run the `src/__main__.py` script of this package.
Either run `python src/. hand` or `python src/. door` from the root folder
=======
1. Opening a door (currently does not have a robot in the environment), which I developed
2. Lifting a can using a 7 degree-of-freedom robot arm, which is built using an example XML file on the MuJoCo website

And multiple robots:

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
>>>>>>> 7505a4ba1825df45a25b3854dbfbce43b4058864
