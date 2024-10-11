import warnings
from typing import Optional, Union, Any, Callable, Dict, Tuple
import leafmap
import leafmap.foliumap as leafmapF
import pandas as pd
import folium
import matplotlib.pyplot as plt
from matplotlib import colors as mpcolors
import geopandas as gpd
import streamlit as st
import requests
from utils import *
configs_list = load_configs_list()

def render_land_map(gdf,border_dgf,sel_cols_for_map,geom='polygon'):
	## only those selected by the user
	if len(gdf)>0:
		m = leafmapF.Map(measure_control=False,draw_control=False)
		url = 'https://wms.geo.admin.ch/?'
		m.add_wms_layer(url,'ch.swisstopo.swissimage',name="swisstopo satellite",maxZoom= 26,opacity= [1,0.5],attribution='geoadmin')
		m.add_wms_layer(url,'ch.kantone.cadastralwebmap-farbe',name="land parcels",minZoom=18,maxZoom= 26,opacity= 0.45,shown=True,attribution='geoadmin')
		
		style_dict_border = {
                    "stroke": True,
                    "color": '#fd9869',
                    "weight": .7,
                    "opacity": 1,
                    "fill": True,
                    "fillColor": "#fd9869",
                    "fillOpacity": 0.1,
                    # "dashArray": "9"
                    # "clickable": True,
                }
		
		style_dict_land = {
                    "stroke": True,
                    "color": '#892881',
                    "weight": 4,
                    "opacity": 1,
                    "fill": True,
                    "fillColor": "#892881",
                    "fillOpacity": 0.4,
                    # "dashArray": "9"
                    # "clickable": True,
                }

		if geom=='polygon':
			m.add_gdf(border_dgf[['geometry']],info_mode='None',style = style_dict_border)
			m.add_gdf(gdf[sel_cols_for_map],info_mode='on_click',style = style_dict_land)
			bounds = border_dgf.total_bounds
			m.zoom_to_bounds(bounds)
			m.to_streamlit(height=700)

		if geom=='point':
			pass

	
