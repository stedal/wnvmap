# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.neighbors import KernelDensity

#Imports for Bokeh
from bokeh.io import curdoc,show, output_file
from bokeh.layouts import row,column, widgetbox
from bokeh.plotting import figure, gmap
from bokeh.io import output_notebook, show
from bokeh.models import ColumnDataSource, HoverTool, Plot, GMapOptions
from bokeh.embed import components, file_html
from bokeh.transform import factor_cmap
from bokeh.models.widgets import Panel, Tabs
from bokeh.resources import CDN
from bokeh.palettes import Spectral6

#output_file("gmap1.html")

map_options = GMapOptions(lat=30.2861, lng=-97.7394, map_type="roadmap", zoom=11)

# For GMaps to function, Google requires you obtain and enable an API key:
#
#     https://developers.google.com/maps/documentation/javascript/get-api-key
#
# Replace the value below with your personal API key:
p1 = gmap("AIzaSyCgCcWOfx8aDHE6zyK903AqW5KcohPnyl8", map_options, title="Austin")

source = ColumnDataSource(
    data=dict(lat=[ 30.29,  30.20,  30.29],
              lon=[-97.70, -97.74, -97.78])
)

p1.circle(x="lon", y="lat", size=15, fill_color="blue", fill_alpha=0.3, source=source)


show(p1)
curdoc().add_root(p1)
