import requests
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib import colors as mpcolors
import yaml
import pandas as pd
def load_configs_list():
	# try:
	with open('./configs.yaml') as file:
		configs_list = yaml.load(file, Loader=yaml.FullLoader)
	# except:
	# 	configs_list = []
	return configs_list

configs_list = load_configs_list()


from thefuzz import fuzz
def fuzzy_match(s1,s2):
    return max([fuzz.ratio(s1, s2),fuzz.partial_ratio(s1, s2),fuzz.token_sort_ratio(s1, s2),fuzz.token_set_ratio(s1, s2),fuzz.partial_token_sort_ratio(s1,s2)])


@st.cache_data()
def get_gwr_codes():
	import ssl
	ssl._create_default_https_context = ssl._create_unverified_context
	## https://www.housing-stat.ch/de/madd/ech-0206.html
	gwr_codes = pd.read_excel("https://www.housing-stat.ch/files/GWRCodes.xlsx")
	# [['CODE','MERKMAL','KURZTEXT_DE','LANGTEXT_DE']]
	return gwr_codes

@st.cache_data
def get_oereb_gemeinde_kantons():
	return pd.read_parquet(configs_list['oereb_gemeinde_kantons'])


@st.cache_data
def get_zip_kanton_mapping():
	return pd.read_parquet(configs_list['zip_kanton_mapping_fn'])

def click_featch_ads_button():
		st.session_state.featch_ads_button = True

def click_featch_land_parcel_button():
		st.session_state.featch_land_parcel_button = True



def get_hex_from_float(float_value,cmap_name='RdYlBu_r'):
	color_map = plt.get_cmap(cmap_name)
	return mpcolors.rgb2hex(color_map(float_value), keep_alpha=True)



def query_duckdb_s3_lambda(s3_query):

	base_url = "https://reqzxh2vvh.execute-api.eu-central-1.amazonaws.com/v1?"
	params = {
			  "event_query":s3_query
			  }
	response = requests.get(base_url,params=params)
	if response.status_code == 200:
		return response.status_code,response.json()
	else:
		print(s3_query)
		return response.status_code,[]





def get_time_stamps_from_columname(colname,time_stamp_granularity,exclude_timestamp=[2024,202403]):
	from_year = int(colname.split("_")[-2][:-1])
	from_q = int(colname.split("_")[-2][-1])
	to_year = int(colname.split("_")[-1][:-1])
	to_q = int(colname.split("_")[-1][-1])
	all_ts = []
	if time_stamp_granularity=='quarterly':
		Qs = [1,2,3,4]
		for y in range(from_year,to_year+1):
			for q in Qs:
				ts = int(f"{y}{q}")
				if ts <= int(f"{to_year}{to_q}"):
					all_ts.append(ts)
	else:
		for y in range(from_year,to_year+1):
			ts = int(f"{y}")
			all_ts.append(ts)
	all_ts = [ts for ts in all_ts if ts not in exclude_timestamp]
	return all_ts


import requests
import streamlit as st
import matplotlib.pyplot as plt
from matplotlib import colors as mpcolors
import yaml
from PIL import Image

import pandas as pd
def load_configs_list():
	# try:
	with open('./configs.yaml') as file:
		configs_list = yaml.load(file, Loader=yaml.FullLoader)
	# except:
	# 	configs_list = []
	return configs_list

configs_list = load_configs_list()


from thefuzz import fuzz
def fuzzy_match(s1,s2):
    return max([fuzz.ratio(s1, s2),fuzz.partial_ratio(s1, s2),fuzz.token_sort_ratio(s1, s2),fuzz.token_set_ratio(s1, s2),fuzz.partial_token_sort_ratio(s1,s2)])


@st.cache_data()
def get_gwr_codes():
	import ssl
	ssl._create_default_https_context = ssl._create_unverified_context
	## https://www.housing-stat.ch/de/madd/ech-0206.html
	gwr_codes = pd.read_excel("https://www.housing-stat.ch/files/GWRCodes.xlsx")
	# [['CODE','MERKMAL','KURZTEXT_DE','LANGTEXT_DE']]
	return gwr_codes

@st.cache_data
def get_oereb_gemeinde_kantons():
	return pd.read_parquet(configs_list['oereb_gemeinde_kantons'])


@st.cache_data
def get_zip_kanton_mapping():
	return pd.read_parquet(configs_list['zip_kanton_mapping_fn'])

def click_featch_ads_button():
		st.session_state.featch_ads_button = True

def click_featch_land_parcel_button():
		st.session_state.featch_land_parcel_button = True

def load_ads_button():
	pass
	# st.session_state.edited_financial_df = edited_financial_df

		# st.session_state.featch_ads_button = True

def get_hex_from_float(float_value,cmap_name='RdYlBu_r'):
	color_map = plt.get_cmap(cmap_name)
	return mpcolors.rgb2hex(color_map(float_value), keep_alpha=True)


def query_duckdb_s3_lambda(s3_query):
	
	base_url = "https://reqzxh2vvh.execute-api.eu-central-1.amazonaws.com/v1?"
	params = {
			  "event_query":s3_query
			  }
	response = requests.get(base_url,params=params)
	if response.status_code == 200:
		return response.status_code,response.json()
	else:
		print(s3_query)
		return response.status_code,[]





def get_time_stamps_from_columname(colname,time_stamp_granularity,exclude_timestamp=[2024,202404]):
	from_year = int(colname.split("_")[-2][:-1])
	from_q = int(colname.split("_")[-2][-1])
	to_year = int(colname.split("_")[-1][:-1])
	to_q = int(colname.split("_")[-1][-1])
	all_ts = []
	if time_stamp_granularity=='quarterly':
		Qs = [1,2,3,4]
		for y in range(from_year,to_year+1):
			for q in Qs:
				ts = int(f"{y}{q}")
				if ts <= int(f"{to_year}{to_q}"):
					all_ts.append(ts)
	else:
		for y in range(from_year,to_year+1):
			ts = int(f"{y}")
			all_ts.append(ts)
	all_ts = [ts for ts in all_ts if ts not in exclude_timestamp]
	return all_ts




def unflod_values(stats_df,
				  selected_type_of_ad,
				  sel_ad_property_type,
				  analytics,
				  time_stamp_granularity,
				  pct,
				  y_col_type = int
				  ):
	
	stats_col_translation = configs_list['stats_col_translation']
	# if selected_type_of_ad == 'buy': selected_type_of_ad_stat = 
	# if selected_type_of_ad == : selected_type_of_ad_stat = 'rent'
			
	selected_type_of_ad_stat = 'rent'
	col_kws = {'ppsqm':f"{stats_col_translation[selected_type_of_ad]}_{stats_col_translation[sel_ad_property_type]}_{analytics}_{pct}pct_in_zipcode_{time_stamp_granularity}_",
				"count":f"{stats_col_translation[selected_type_of_ad]}_{stats_col_translation[sel_ad_property_type]}_{analytics}_in_zipcode_{time_stamp_granularity}_",
				"vacancy":f"{stats_col_translation[selected_type_of_ad_stat]}_{stats_col_translation[sel_ad_property_type]}_{analytics}_in_zipcode_{time_stamp_granularity}_"
	}
	
	colname = [c for c in stats_df.columns if col_kws[analytics] in c][0]

	

	all_ts = get_time_stamps_from_columname(colname,time_stamp_granularity,exclude_timestamp=[20243])
	vs = [eval(v) for v in stats_df[colname]]
	vs = [v[:len(all_ts)] for v in vs]
	zips = stats_df["zip_code"].values
	chart_values = []
	for i in range(len(zips)):
		for j in range(len(all_ts)):
			chart_values.append([zips[i],vs[i][j],all_ts[j]])     
	if time_stamp_granularity == 'annual':
		x_n = 'year'
	else:
		x_n = 'quarters'
	
	
	
	pcts_dict = {5:"5%",25:"25%",50:"median",75:"75%",95:"95%"}
	
	pretty_columns = {
			"rent_apartment_ppsqm":f'{pcts_dict[pct]} monthly rental price/m² (apartment)',
			"rent_hause_ppsqm":f'{pcts_dict[pct]} monthly rental price/m² (house)',
			"sale_apartment_ppsqm":f'{pcts_dict[pct]} sale price/m² (apartment)',
			"sale_hause_ppsqm":f'{pcts_dict[pct]} sale price/m² (house)',
			"rent_apartment_count":'no of published for rent (apartment)',
			"rent_hause_count":'no of published for rent (house)',
			"sale_apartment_count":'no of published for sales (apartment)',
			"sale_hause_count":'no of published for sales (house)',
			"rent_apartment_vacancy":'vacancy rate (%) (apartment)',
			"rent_hause_vacancy":'vacancy rate (%) (house)'
	}


	try:
		y_n = pretty_columns[f"{stats_col_translation[selected_type_of_ad]}_{stats_col_translation[sel_ad_property_type]}_{analytics}"]
	except:
		y_n = pretty_columns[f"{stats_col_translation[selected_type_of_ad_stat]}_{stats_col_translation[sel_ad_property_type]}_{analytics}"]
	
	
	
	category_n = 'zip code'
	chart_values_df = pd.DataFrame(data=chart_values,columns=[category_n,y_n,x_n])
	chart_values_df = chart_values_df.loc[chart_values_df[y_n]!=-9999]
	chart_values_df[category_n] = chart_values_df[category_n].astype(str)

	if y_col_type == int: chart_values_df[y_n] = chart_values_df[y_n].astype(int)
	return chart_values_df,category_n,y_n,x_n

