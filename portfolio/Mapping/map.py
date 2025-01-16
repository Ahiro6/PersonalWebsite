import folium
# import pandas as pd
# from coordinates import longitude, latitude, names, area
from portfolio.Mapping.for_pandas import GetData

# folium.Popup(str(na), parse_html=True)


# volcano obj
vol = GetData("PersonnalWebsite/static/mapping/volcanoes.txt", "txt")
latitude_v = vol.get_column("LAT")
longitude_v = vol.get_column("LON")
name = vol.get_column("NAME")
elev = vol.get_column("ELEV")

# resort obj
res = GetData("PersonnalWebsite/static/mapping/resorts.csv", "csv")
latitude = res.get_column("Latitude")
longitude = res.get_column("Longitude")
names = res.get_column("International Name")
area = res.get_column("Area")

maps = folium.Map(location=[-26.2041, 28.0473], zoom_start=6, tiles="Stamen Terrain", min_zoom=2.5)
# tiles = "Stamen Terrain"

icon_blue = folium.Icon(color="blue")
icon_green = folium.Icon(color="green")
icon_red = folium.Icon(color="red")

rg = folium.FeatureGroup(name="Nature Resorts in South Africa")
vg = folium.FeatureGroup(name="Volcanoes in America")
myCO_group = folium.FeatureGroup(name="My Coordinates")
pg = folium.FeatureGroup(name="Population")


def color_volc(elevation):
    if elevation < 1500:
        return 'yellow'
    elif 3000 > elevation >= 1500:
        return '#9ACD32'
    else:
        return 'green'


def color_resort(area_resort):
    if area_resort < 1000:
        return '#00d8e6'
    elif 1000 <= area_resort < 5000:
        return '#0059b3'
    elif 5000 <= area_resort < 10000:
        return '#004d99'
    elif 10000 <= area_resort < 50000:
        return '#004080'
    elif 50000 <= area_resort < 100000:
        return '#003366'
    elif area_resort > 100000:
        return '#00264d'


pg.add_child(folium.GeoJson(data=open("PersonnalWebsite/static/mapping/world.json", "r", encoding="utf-8-sig").read(),
                            style_function=lambda x: {
                                'fillColor': 'yellow' if 1000 < x['properties']['POP2005'] < 20000000
                                else 'orange' if 20000000 < x['properties']['POP2005'] < 40000000
                                else 'red', 'color': 'lightred'}))
maps.add_child(pg)

for lat, lon, na, ar in zip(latitude, longitude, names, area):
    rg.add_child(
        folium.CircleMarker(location=(lat, lon), popup=folium.Popup(str(na + "\n" + str(ar) + "km"), parse_html=True),
                            fill_color=color_resort(ar), color='black', fill_opacity=1.0, radius=6))
maps.add_child(rg)

for lt, ln, nm, el in zip(latitude_v, longitude_v, name, elev):
    vg.add_child(
        folium.CircleMarker(location=(lt, ln), popup=folium.Popup(str(nm + "\n" + str(el) + "m"), parse_html=True),
                            fill_color=color_volc(el), color='darkgreen', fill_opacity=0.7, radius=6))
maps.add_child(vg)

mark_myLoc = folium.CircleMarker(location=(-26.2041, 28.0473), popup="I live here", fill_color='red', color='red',
                                 fill_opacity=0.7)
myCO_group.add_child(mark_myLoc)
maps.add_child(myCO_group)

maps.add_child(folium.LayerControl())
maps.save("PersonnalWebsite/templates/Maps.html")
