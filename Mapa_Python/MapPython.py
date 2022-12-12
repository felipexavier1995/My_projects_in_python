# PT-BR
#       Folium é uma API para gerar um arquivo formato HTML para mostrar localização.
# EN
#       Folium is an API to generate an HTML format file to display location.
import folium


m = folium.Map(
    location=[-22.9523316,-43.2202015],
    tiles='Stamen Terrain',
    zoom_start=16
)
folium.Marker(
    [-22.9523316,-43.2202015], 
    popup="<i> Corcovado <i>",
    tooltip='Click Aqui!'
).add_to(m)


m.save("C:/Users/felip/Desktop/Projeto Pyhton/index.html")

