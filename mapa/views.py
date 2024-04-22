from django.shortcuts import render
from .models import Analise

# Create your views here.
from django.views.generic import TemplateView
from .utils import make_markers_and_add_to_map
import folium
import pandas as pd

def mapinha(request):
    figure = folium.Figure()

    #Fazendo o mapa
    map = folium.Map(
        location = [-9.7, -36],
        zoom_start = 10,
        tiles = 'OpenStreetMap')

    map.add_to(figure)

    #Add o ponto
    """folium.Marker(
        location = [-36, -9],
        popup = 'Integração d Django co o Folium',
        tooltip = 'Folium e Django',
        icon = folium.Icon(icon='fa-coffee', prefix='fa')
    ).add_to(map)"""
    """for house in Analise.objects.all():
        make_markers_and_add_to_map(map, house)"""
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
