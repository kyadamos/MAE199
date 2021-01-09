# MAE199
**********

The task of automating of blood glucose regulation can be done through artificial means for patients with type 1 diabetes (T1D). Much of the literature regarding this problem of T1D implements approaches rooted in control theory; however, with the increasing popularity and viability of artificial intelligence in a multitude of applications, the set of pragmatical solutions to this problem now extends into the realm of machine learning.

# Libraries

For this project, I built, trained, and tested a Deep Q-Network (DQN) to regulate patient BG levels *in silico*. In order to do that, I used three main libraries: PyTorch, OpenAI Gym, and SimGlucose.

## [PyTorch](https://github.com/pytorch/pytorch) 

[PyTorch](https://pytorch.org/) is an open source Python library used in various deep learning applications. I use PyTorch to build and train my neural networks; to see some example notebooks of our Deep Q-Networks (DQN), refer to [kyadamos/notebooks](https://github.com/kyadamos/MAE199/tree/main/notebooks). 

## [OpenAI Gym](https://github.com/openai/gym) 

[OpenAI Gym](https://gym.openai.com/) is a toolkit for developing, testing, and comparing reinforcement learning algorithms. I use OpenAI Gym to create the framework for the reinforcement learning agents to operate in--more specifically, the environment, reward function, and interaction process.

## [SimGlucose](https://github.com/jxx123/simglucose)

SimGlucose is a Python implementation of the [UVA/Padova Type 1 Diabetes Simulator](https://tegvirginia.com/software/t1dms-2014/) that features valuable reinforcement learning tools for research purposes.

# Installation

We recommend that you use pip to install the libraries we use; if you do not have pip installed, follow [this link](https://pip.pypa.io/en/stable/installing/).

## PyTorch Installation

To install the latest version of PyTorch, refer to the PyTorch's [Get Started](https://pytorch.org/get-started/locally/) page.

![PyTorch Install Screenshot](https://github.com/kyadamos/MAE199/blob/main/screenshots/PyTorch_Installation.png)

Once you select the options that suit your preferences, run the install command in the environment you want to use PyTorch in.

We are running PyTorch 1.6.1 for Python on Windows and chose to use Pip as our package manager. Because are not utilizing a CUDA-enabled graphics processing unit, we selected "None" for CUDA, but we recommend selecting the version that reflects your GPU to decrease the training time of your neural network.

## Gym Installation

The installation instructions for Gym can be found [here](https://github.com/openai/gym#installation). 

## SimGlucose Installation

For installing SimGlucose, PLEASE use [their instructions](https://github.com/jxx123/simglucose#installation).