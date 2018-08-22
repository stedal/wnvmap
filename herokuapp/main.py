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

#output_file("gmap1.html")

train = pd.read_csv('data/combined_train.csv')
test = pd.read_csv('data/combined_test.csv')
spray = pd.read_csv('data/spray.csv')

group = test[['Longitude', 'Latitude']]
group.drop_duplicates(inplace = True)

map_options = GMapOptions(lat=41.8876, lng=-87.61979, map_type="roadmap", zoom=10)

# For GMaps to function, Google requires you obtain and enable an API key:
#
#     https://developers.google.com/maps/documentation/javascript/get-api-key
#
# Replace the value below with your personal API key:
source = ColumnDataSource(group)

# source = ColumnDataSource(
#     data=dict(lat=[ 30.29,  30.20,  30.29],
#               lon=[-97.70, -97.74, -97.78])
# )
p1 = gmap("AIzaSyCgCcWOfx8aDHE6zyK903AqW5KcohPnyl8", map_options,
          title="Mosquito Trap and Pesticide Spray locations",
         plot_height = 800, plot_width = 800)

p1.x(x="Longitude", y="Latitude", size=12, fill_color="blue", fill_alpha=1, source=source,
    legend="Mosquito Trap Locations")
p1.circle(x="Longitude", y="Latitude", size=7, fill_color="yellow", fill_alpha=0.1, line_alpha = .1,
          line_color = 'yellow', source=source2, legend="Pesticide Spray Locations")
#glyph = X(x="Longitude", y="Latitude", size=7, fill_color="blue", fill_alpha=0.8, source=source)
#p1.add_glyph(source, glyph)
p1.title.align = 'center'
p1.title.text_font_size = '16pt'
p1.legend.location = 'top_right'

#show(p1)
curdoc().add_root(p1)
