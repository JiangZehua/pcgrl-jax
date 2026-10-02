from setuptools import find_namespace_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(name='pcgrl-jax',
      version='0.5.0',
      author="NYU Game Innovation Lab",
      author_email="sam.earle@nyu.edu",
      description="Procedural Content Generation via Reinforcement Learning (PCGRL), implemented end-to-end in JAX.",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/smearle/pcgrl-jax.git",
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: Apache Software License",
          "Operating System :: OS Independent",
      ],
      packages=find_namespace_packages(include=["purejaxrl", "marl"]),
      )
