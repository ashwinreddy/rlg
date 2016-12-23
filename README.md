#RLG
Robot Learning Gym is a tool to test reinforcement learning algorithms for robotics tasks a la OpenAI's [Universe](https://universe.openai.com/) and/or [Gym](https://gym.openai.com).

The purpose is to evaluate how well the various RL algorithms work on robotics-like tasks by using a standardized and consistent metric.

#Installation
You will need MuJoCo for this to work. Be sure to download the `mjpro` folder and license keys in a clean directory (you will need to move them later).

First, install OpenAI Gym. The instructions can be found [here](https://github.com/openai/gym#installation).
Next, you will need to make sure that you also have the OpenAI interface to MuJoCo. To ensure that this is the case, use [this link](https://github.com/openai/gym#mujoco).
You will need `mujoco-py`, the Python bindings for MuJoCo, which is written in C++. Follow the instructions [here](https://github.com/openai/mujoco-py#obtaining-the-binaries-and-license-key)

#Usage
If all goes well, you should be able to run the `src/__main__.py` script of this package.
Either run `python src/. hand` or `python src/. door` from the root folder
