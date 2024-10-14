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


def render_land_map(gdf,border_dgf,sel_cols_for_map,geom='polygon'):
	## only those selected by the user
	if len(gdf)>0:
		m = leafmapF.Map(measure_control=False,draw_control=False)
		url = 'https://wms.geo.admin.ch/?'
		m.add_wms_layer(url,'ch.swisstopo.swissimage',name="swisstopo satellite",maxZoom= None,opacity= [1,0.5],attribution='geoadmin')
		m.add_wms_layer(url,'ch.kantone.cadastralwebmap-farbe',name="cadastral",minZoom=16,maxZoom= None,opacity= 0.45,shown=True,attribution='geoadmin')
		
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
			m.add_gdf(border_dgf[['geometry']],layer_name='gemeinde',info_mode='None',style = style_dict_border)
			m.add_gdf(gdf[sel_cols_for_map],info_mode='on_click',layer_name='parzellen',style = style_dict_land)
			# if 'parcel_table' in st.session_state:
			# 	edited_rows = st.session_state.parcel_table['edited_rows']
			# 	selected_row_ids = list([k for k in edited_rows.keys() if edited_rows[k]['selected']==True])
			# else:
			# 	selected_row_ids = []

			selected_row_ids = []

			if len(selected_row_ids)>0:
				bounds = gdf.iloc[selected_row_ids].total_bounds
			else:
				bounds = border_dgf.total_bounds
				
			
			# m.zoom_to_bounds(bounds)
			
			m.fit_bounds(bounds=[[bounds[1], bounds[0]], [bounds[3], bounds[2]]],
				max_zoom=18
				)
			mp_center = ((bounds[1]+bounds[3])/2,(bounds[0]+bounds[2])/2)
			from streamlit_folium import st_folium
			if (len(selected_row_ids)>0) and ((len(selected_row_ids)<2)):
				print('h')
				st_folium(m,center=mp_center,width=None,height=700,zoom=18)
			elif(len(selected_row_ids)>0) and ((len(selected_row_ids)>=2)):
				st_folium(m,width=None,height=700,zoom=16)
			else:
				st_folium(m,width=None,height=700)
		if geom=='point':
			pass

	
