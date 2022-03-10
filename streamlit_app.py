import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.decomposition import PCA
import plotly.graph_objects as go
import plotly.express as px
import streamlit as st



import home, data_vis, playlist_visualisation

# path_github = ""

PAGES = {
    "Home page": home,
    "Visualisation": playlist_visualisation,
    "Tensorflow Projector": data_vis
 }

# st.sidebar.write('### Menu')

selection = st.sidebar.radio('### Menu', list(PAGES.keys()))
page = PAGES[selection]
page.app()
