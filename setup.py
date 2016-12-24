from setuptools import setup, find_packages
# print find_packages()
setup(name='rlg',
      version='1.0.a.dev',
      description='Platform for testing robot RL algorithms',
      url='http://github.com/ashwinreddy/rlg',
      author='Ashwin Reddy',
      author_email='19ashwinr@students.harker.org',
      license='MIT',
      packages=find_packages(),
      install_requires=[
        'gym',
        'mujoco-py',
        'numpy'
      ],
      include_package_data=True,
      zip_safe=False)
