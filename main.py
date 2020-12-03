import folium
import pandas

data = pandas.read_csv("volcano_db.csv")

lat = list(data["Latitude"])
lan = list(data["Longitude"])
elev = list(data["Elev"])
name = list(data["Volcano Name"])


def color_decider(el):
    if el < 1000:
        return "green"
    elif 1000 <= el < 3000:
        return "orange"
    else:
        return "red"


map = folium.Map(location=[23.5, 80.6], zoom_start=4)

fg = folium.FeatureGroup(name="My Map")
for lt, ln, el, nm in zip(lat, lan, elev, name):
    fg.add_child(folium.CircleMarker(
        location=[lt, ln], popup=str(nm)+'('+str(el)+"m)", radius=6, fill_color=color_decider(el), color='grey', fill_opacity=0.7))


map.add_child(fg)

map.save("map.html")
