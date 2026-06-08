import geopandas as gpd
import geoplot
import geoplot.crs as gcrs
import matplotlib.pyplot as plt

def view_dong_by_sido(sido_number):
    data = gpd.read_file(
        f"emd/compiled_geojson_files/{sido_number}_geo.json"
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

    print(f"Showing {sido_number}의 법정동")
    plt.show()

view_dong_by_sido(36)