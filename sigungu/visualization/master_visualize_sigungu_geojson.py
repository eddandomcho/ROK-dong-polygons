import geopandas as gpd
import geoplot
import geoplot.crs as gcrs
import matplotlib.pyplot as plt

def view_master_sigungu():
    data = gpd.read_file(
        "sigungu/final_geojson/시군구_polygon_2026-06-08_기준.json"
    )

    data = data.explode(index_parts=False)

    geoplot.polyplot(
        data,
        projection = gcrs.AlbersEqualArea(),
        edgecolor = 'darkgrey',
        facecolor = 'lightgrey',
        linewidth = .3,
        figsize = (12,8)
    )

    plt.show()

view_master_sigungu()