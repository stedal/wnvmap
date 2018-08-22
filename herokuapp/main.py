# -*- coding: utf-8 -*-

import pandas as pd
import numpy as np


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
from bokeh.models.markers import X

# Load data
train = pd.read_csv('herokuapp/data/combined_train.csv')
test = pd.read_csv('herokuapp/data/combined_test.csv')
spray = pd.read_csv('herokuapp/data/spray.csv')

map_options = GMapOptions(lat=41.8876, lng=-87.61979, map_type="roadmap", zoom=10)


group = test[['Longitude', 'Latitude']]
group.drop_duplicates(inplace = True)

source = ColumnDataSource(group)
source2 = ColumnDataSource(spray)

TOOLS = 'pan, wheel_zoom, box_zoom, reset, save'

p1 = gmap("AIzaSyCgCcWOfx8aDHE6zyK903AqW5KcohPnyl8", map_options,
          title="Mosquito Trap and Pesticide Spray locations",
         plot_height = 800, plot_width = 800,
         tools = TOOLS)

p1.x(x="Longitude", y="Latitude", size=12, fill_color="blue", fill_alpha=1, source=source,
    legend="Mosquito Trap Locations")
p1.circle(x="Longitude", y="Latitude", size=7, fill_color="green", fill_alpha=0.3, line_alpha = .1,
          line_color = 'yellow', source=source2, legend="Pesticide Spray Locations")


p1.title.align = 'center'
p1.title.text_font_size = '16pt'
p1.legend.location = 'top_right'
p1.legend.background_fill_color = "white"
p1.legend.border_line_color = 'black'
p1.legend.click_policy = 'hide'
curdoc().add_root(p1)
