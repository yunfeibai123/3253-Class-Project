# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:45:16 2019

@author: yunfebai
"""
import numpy as np
import matplotlib.pyplot as plt

def score_parameter_plot(cv_results,param_name, plot_title,score_min,score_max):
    fig, ax = plt.subplots()
    tickLocations=np.arange(len(cv_results['params']))
    labels=[a[param_name] for a in cv_results['params']]
    ax.bar(tickLocations, cv_results['mean_test_score'], color='wheat', edgecolor='#8B7E66', linewidth=4.0, align='center')
    ax.set_xticks(ticks= tickLocations)
    ax.set_xticklabels(labels)
    ax.set_ylim((score_min,score_max))       
    ax.set_title(plot_title)
    ax.set_ylabel('mean_test_score')
    ax.set_xlabel(param_name)
    fig.tight_layout(pad=1)