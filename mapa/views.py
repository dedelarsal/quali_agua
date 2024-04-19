from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
import folium


class MapView(TemplateView):
    template_name = 'map.html'

    def get_context_data(self, **kwargs):
        figure = folium.Figure()

        #Fazendo o mapa
        map = folium.Map(
            location = [-36, -9],
            zoom_start = 11,
            tiles = 'OpenStreetMap')

        map.add_ti(figure)

        #Add o ponto
        folium.Marker(
            location = [-36, -9],
            popup = 'Integração d Django co o Folium',
            tooltip = 'Folium e Django',
            icon = folium.Icon(icon='fa-coffee', prefix='fa')
        ).add_to(map)

        #renderizando e enviando o template
        figure.render()
        return ("map" : figure)
