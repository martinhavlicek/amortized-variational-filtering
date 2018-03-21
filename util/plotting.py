import visdom
import numpy as np


global vis


def init_plot(log_dir):
    """
    Initialize the plotting environment.
    """
    global vis
    vis = visdom.Visdom(port=8097, env=log_dir)
    init_plots()


def init_plots():
    """
    Initialize the plots.
    """
    pass


def save_env():
    """
    Saves the visdom environment.
    """
    global vis
    vis.save([vis.env])


def plot_wrapper():
    raise NotImplementedError
