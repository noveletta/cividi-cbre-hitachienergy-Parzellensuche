import streamlit as st
# st.set_page_config(page_title='Semanta, your smart search assistant',page_icon=':house:',layout="wide")
st.set_page_config(
    page_title="smart search enabled",
    page_icon="static/images/noveletta_logo.png",
    layout="wide",
	initial_sidebar_state= "auto", #"auto", "expanded", "collapsed"
	# menu_items = {"About":'This is *Noveletta Search*  \
	# 		   *Powered by [Noveletta DataHub](https://www.linkedin.com/company/noveletta/)*'
	# 		   }
)
import gc

from utils import *
from search_results_utils import *


st.markdown("""
    <style>
		.appview-container .main .block-container{{
		padding-left: 100rem}}
	</style>
	""", unsafe_allow_html=True)

# st.image("./images/semanta-logo.png",width=150)
st.markdown("""
				 *smart search enabled*""")
# st.markdown("")

# potential_tab
check_longlist,aufgabe = st.tabs(["Ergebnisse",'Aufgabe'])


with check_longlist:
	render_parcels()
with aufgabe:
	st.markdown('''
### Aufgabe
Für die Umsiedlung eines Industriebetriebs sucht die CBRE im Auftrag von Hitachi Energy nach
passenden Parzellen. Vier Parzellen werden bereits evaluiert. Um die Suche zu vervollständigen,
sollen weitere Optionen gefunden und evaluiert werden. Cividi führt dazu eine automatisierte Suche
basierend auf den untenstehenden Kriterien durch. Sollten dabei passende Parzellen identifiziert
werden, so sollen diese von CBRE und ihrer Partnerin Sito weiter evaluiert und unter Umständen
mit den Eigentümern Kontakt aufgenommen werden. 

#### Kriterien:
1. **Nutzung: Produktions- und Büroflächen;**
    - Die folgenden Zonen werden als erstes Filterkriterium genutzt: Zonen mit "Industrie xx"
2. **Flächentyp: Bauland**
    - Als zweites Filterkriterium werden Parzellen ohne Bebauung, sowie nachgelagert mit einer Bebauung von vor 1994 gesucht. Es wird dabei angenommen, dass Bauten, die älter als 30 Jahre sind, durch Neubauten ersetzt werden könnten.
3. **Fläche: Bauland für min. 20’000 m² Produktionsfläche mit Büroanteil.**
    - Als drittes Kriterium suchen wir Parzellen mit einem Potenzial für 20’000 m2 auf einem (Erd-)Geschoss. Wir gehen davon aus, dass die Produktion nur eingeschossig organisiert werden kann. Büronutzungen können gestapelt werden, sind aber in der Menge
untergeordnet.
4. **Lage: Zürich Stadt, Flughafenregion, Furttal, Limmattal, Grossraum Baden**
    - Als viertes Kriterium suchen wir in folgendem Einzugsgebiet:
      Zurich, Kloten, Rümlang, Oberglatt, Baden (AG), Neuenhof, Wettingen, Ennetbaden, Würenlos, Killwangen, Spreitenbach, Dietikon, Schlieren, Urdorf, Unterengstringen, Oberengstringen, Regensdorf, Dällikon, Niederhasli, Oberglatt, Niederglatt, Bülach, Bachenbülach, Winkel, Opfikon, Wallisellen, Bassersdorf, Dietlikon, Dübendorf
5. **Verfügbarkeit: Operativer Start bis spätestens Ende 2029/2030**
    - *Dieses Kriterium können wir nicht abbilden. Es muss bei positiv identifizierten Parzellen spezifisch ermittelt werden, zB durch Sito*.
6. **Vertragsform: Präferiert wird eine Anmietung / ein möglicher Ankauf ist nicht ausgeschlossen**
    - *Auch dieses Kriterium können wir nicht ermitteln.*
7. **Weiteres: Generell soll eine Gebäudehöhe von 22m angestrebt werden, mindestens aber 10- 15m**
    - Wir können aus Online verfügbaren Daten die Höhen ermitteln für den Kanton Zürich. Für den Kanton Aargau werden die möglichen Höhen statistisch aus den Bestandsgebäuden abgeleitet.
    - **Die 22m werden primär nur für einen Bereich (Testlabor/Tower) benötigt. Es ist aber wichtig, dass eine Gebäudehöhe von 22 m möglich ist.**   
''')