"""
The following functions are used in the process of data collection, filtering, transforming, and organizing the data into CSV files.
"""

#importing the necessary packages
import numpy as np
import pandas as pd
import os
import difflib
import ast
import requests
import plotly.express as px 
import json
import seaborn as sns
import matplotlib.pyplot as plt
import re

from random import gauss as gs, uniform as uni, seed
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.metrics import euclidean_distances
from scipy.spatial.distance import cdist
from datetime import datetime
from sklearn.metrics.pairwise import linear_kernel
from sklearn.model_selection import train_test_split, GridSearchCV,\
cross_val_score, RandomizedSearchCV
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import f1_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
import xgboost
from numpy import asarray
from numpy import savetxt

import warnings
warnings.filterwarnings("ignore")
pd.set_option('display.max_columns', 300)
pd.set_option('display.max_rows', 200)
pd.options.display.max_colwidth = 100
plt.style.use('seaborn')


# helper functions
# Getting playlist data and saving as dataframe


def playlist_calls(playlist_id, headers):
    """
    This function gets playlist data from api
    """

    base_url = 'https://api.spotify.com/v1/playlists/'

    url = base_url + playlist_id
    
    responses = requests.get(url, headers=headers)
    
    return responses.json()   

# find difference between two lists
def Diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))









