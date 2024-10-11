import streamlit as st
import pandas as pd
import numpy as np
import datetime
# from utils import *
from maputils import *


@st.cache_data
def load_parcels():
	gdf = gpd.read_parquet(f"static/data/CIVIDI_CBRE_potential.parquet")
	return gdf

@st.cache_data
def load_borders():
	gdf = gpd.read_parquet('static/data/CIVIDI_CBRE_borders.parquet')
	return gdf

def preprocess_data(gdf):
	for c in gdf.columns:
		if c == 'geometry':
			pass
		else:
			gdf.loc[(gdf[c]==-99)|(gdf[c]==-9), c] = None
			try:
				gdf[c] = gdf[c].astype(str)
			except:
				pass
			gdf.loc[(gdf[c]=='None')|(gdf[c]=='nan'), c] = None
			
		
	tdf = gdf.T.dropna(how='all').T
	gdf = gdf[tdf.columns]

	return gdf


@st.fragment()
def render_parcels():
	with st.spinner("Loading the parcels..."):
		parcels_gdf = preprocess_data(load_parcels())
		
		borders_gdf = load_borders()
		sel_cols_for_map = ['egrid','geometry',
							'land area',
							'latest construction year in land',
							'latest construction period in land',
							'land plot area ratio',
							'land number of buildings',
							'oereb_TypeCode',
							'oereb_TypeCode_Text',
							'oereb_TypeCode_Description',
							'oereb_Gesamthoehe',
							'oereb_Gebaeudehoehe_Max',
							'oereb_Firsthoehe_Max',
							'oereb_Ausnuetzungsziffer_Min',
							'oereb_Ausnuetzungsziffer_Max',
							'oereb_Baumassenziffer_Min',
							'oereb_Baumassenziffer_Max',
							'oereb_Ueberbauungsziffer_Min',
							'oereb_Ueberbauungsziffer_Max',
							'oereb_Vollgeschosse_Max',
							'oereb_Dachgeschosse_Max',
							'oereb_Untergeschosse_Max',
							'oereb_Freiflaechenziffer_Min',
							'oereb_Wohnanteil_Min',
							'oereb_Wohnanteil_Max',
							'oereb_Gewerbeanteil_Min',
							'oereb_Gewerbeanteil_Max']
		sel_cols_for_map = [c for c in sel_cols_for_map if c in parcels_gdf.columns]
	with st.spinner("Loading the map..."):
		render_land_map(parcels_gdf,borders_gdf,sel_cols_for_map,geom='polygon')
		column_config = {}
		column_config['building zone extract pdf'] = st.column_config.LinkColumn("ÖREB extract", display_text="ÖREB extract")
		
		st.data_editor(
			parcels_gdf.drop(columns=['geometry']),
			column_config=column_config,
			)
	