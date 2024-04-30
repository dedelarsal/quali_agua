from django.shortcuts import render
from .models import Analise

# Create your views here.
from django.views.generic import TemplateView
from .utils import make_markers_and_add_to_map
from folium.plugins import MiniMap
import folium
import pandas as pd
import geopandas as gpd

def mapinha(request):
    figure = folium.Figure()
    url = '/home/Dedel/dedel.pythonanywhere.com/'
    blocoA = url + 'mapa\shp\Bloco A.shp'
    blocoB = url + 'mapa\shp\Bloco B.shp'
    blocoC = url + 'mapa\shp\Bloco C.shp'

    #Fazendo o mapa
    map = folium.Map(
        location = [-9.7, -36],
        zoom_start = 10,
        tiles = 'OpenStreetMap')

    blocoA = gpd.read_file(blocoA)
    blocoB = gpd.read_file(blocoB)
    blocoC = gpd.read_file(blocoC)
    crs = {'init':'epsg:4326'}
    blocoA.to_crs(crs, inplace=True)
    blocoB.to_crs(crs, inplace=True)
    blocoC.to_crs(crs, inplace=True)

    minimap = MiniMap()
    map.add_child(minimap)

    geojson_blocoA = folium.GeoJson(blocoA, name='BRK Ambiental',style_function=lambda feature: {"fillColor": "blue", "color": "blue", "weight": 2, "fillOpacity": 0.3})
    geojson_blocoB = folium.GeoJson(blocoB, name='Águas do Sertão',style_function=lambda feature: {"fillColor": "orange", "color": "orange", "weight": 2, "fillOpacity": 0.3})
    geojson_blocoC = folium.GeoJson(blocoC, name='Verde Alagoas Ambiental',style_function=lambda feature: {"fillColor": "green", "color": "green", "weight": 2, "fillOpacity": 0.3})
    geojson_blocoA.add_child(folium.Popup('BRK Ambiental'))
    geojson_blocoB.add_child(folium.Popup('Águas do Sertão'))
    geojson_blocoC.add_child(folium.Popup('Verde Alagoas Ambiental'))
    geojson_blocoA.add_to(map)
    geojson_blocoB.add_to(map)
    geojson_blocoC.add_to(map)

    map.add_to(figure)

    #Add o ponto
    df = pd.DataFrame(list(Analise.objects.all().values("rua","latitude","longitude","data_analise","parametro","valor_parametro")))
    for ponto in df['latitude'].unique():
        df_ponto = df[df['latitude'] == ponto]
        #dia = df_ponto['data_analise'].unique()[-1]
        #df_ponto = df_ponto[df_ponto['data_analise'] == dia]
        #print(df_ponto)

        make_markers_and_add_to_map(map, df_ponto)

    #renderizando e enviando o template
    figure.render()
    return render(request, 'mapa/mapinha.html', {"map": figure})
