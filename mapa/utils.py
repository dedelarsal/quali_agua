import folium

def make_markers_and_add_to_map(map, df):
    popup = "<h4>" + df['rua'].unique()[0] + " - " + str(df['data_analise'].unique()[0]) + "</h4>"
    flag = folium.Icon(icon='fa-vial-circle-check', prefix='fa', color='green')
    for i in df.parametro.unique():
        for id, row in df[df['parametro'] == i].iterrows():
            popup += "<p>" + row.parametro + " = " + row.valor_parametro + "</p>"

            if row.parametro == 'Coliformes Totais':
                if float(row.valor_parametro) > 0:
                    flag = folium.Icon(icon='fa-vial-virus', prefix='fa', color='red')
            if row.parametro == 'E. coli':
                if float(row.valor_parametro) > 0:
                    flag = folium.Icon(icon='fa-vial-virus', prefix='fa', color='red')
            if row.parametro == 'Cloro Residual Livre (mg/L)':
                if float(row.valor_parametro) < 0.2 or float(row.valor_parametro) > 5:
                    flag = folium.Icon(icon='fa-vial-virus', prefix='fa', color='red')
            if row.parametro == 'Turbidez (uT)':
                if float(row.valor_parametro) > 5:
                    flag = folium.Icon(icon='fa-vial-virus', prefix='fa', color='red')
            if row.parametro == 'Cor Aparente (uH)':
                if float(row.valor_parametro) > 15:
                    flag = folium.Icon(icon='fa-vial-virus', prefix='fa', color='red')

    folium.Marker(
            location = [df.latitude.unique()[0], df.longitude.unique()[0]],

            popup = folium.Popup(popup, min_width=300, max_width=300),
            icon = flag
        ).add_to(map)
