import numpy as np
import rlg
import os
import tensorflow as tf
import logging
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
logger.info("Starting...")

r = tf.placeholder(tf.float32, shape=())
tf.summary.scalar('reward', r)
merged = tf.summary.merge_all()
init = tf.global_variables_initializer()

writer = tf.summary.FileWriter('./data/random_hard')

agent = rlg.agents.DefaultAgent(True)

agent.load_task(rlg.make('PegInsertion-v0'), './gym_data/random_experiment_cartpole')
print agent.episode_steps#, agent.task.envspec.timestep_limit
sess = tf.Session()
sess.run(init)
for episode in xrange(10):
    agent.reset()
    for t in xrange(agent.episode_steps):
        # agent.task.render()
        s_prime, reward, done, info = agent.step()
        with open("./file_data/random.csv", "a") as f:
            f.write("{}, {}, {}\n".format(episode, t, reward))
        summary = sess.run(merged, feed_dict={r: reward})
        writer.add_summary(summary, t)
        #if done:
        #    agent.reset()
sess.close()
