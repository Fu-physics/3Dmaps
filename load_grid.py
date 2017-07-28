import numpy as np
import bpy


data = np.loadtxt(open("/Users/fuli/Desktop/googlemaps/geo_data.csv", "rb"), delimiter=",", skiprows=1)

elevation = data[:,2]
print(elevation)
print(int((elevation.size)**(1/2)))

divisions = int((elevation.size)**(1/2))

bpy.ops.mesh.primitive_grid_add(x_subdivisions=divisions, y_subdivisions=divisions, radius=divisions-1, view_align=False, enter_editmode=False, location=(0, 0, 0))


