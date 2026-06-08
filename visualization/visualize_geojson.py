import geopandas as gpd
import geoplot
import geoplot.crs as gcrs
import matplotlib.pyplot as plt

data = gpd.read_file(
    "final_geojson/compiled_geojson_files_geo.json"
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