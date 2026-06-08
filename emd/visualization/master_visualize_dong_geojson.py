import geopandas as gpd
import geoplot
import geoplot.crs as gcrs
import matplotlib.pyplot as plt

def view_master_dong():
    data = gpd.read_file(
        "emd/final_geojson/법정동_polygon_2026-06-08_기준.json"
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