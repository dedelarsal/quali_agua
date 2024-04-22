import folium

def make_markers_and_add_to_map(map, df):
    popup = "<h4>" + df['rua'].unique()[0] + " - " + str(df['data_analise'].unique()[0]) + "</h4>"
    for i in df.parametro.unique():
        for id, row in df[df['parametro'] == i].iterrows():
            popup += "<p>" + row.parametro + " = " + row.valor_parametro + "</p>"
    folium.Marker(
            location = [df.latitude.unique()[0], df.longitude.unique()[0]],

            popup = folium.Popup(popup, min_width=300, max_width=300),
            icon = folium.Icon(icon='fa-home', prefix='fa')
        ).add_to(map)
