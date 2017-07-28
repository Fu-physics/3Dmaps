import bpy
import bmesh

import numpy as np


data = np.loadtxt(open("/Users/fuli/Desktop/googlemaps/geo_data.csv", "rb"), delimiter=",", skiprows=1)

elevation = data[:,2]
print(elevation)



print("----- Begin ... ------")

bpy.ops.object.mode_set(mode='EDIT')

mesh_1=bmesh.from_edit_mesh(bpy.context.object.data)

#verts = [0 for v in mesh_1.verts:]

print(mesh_1.verts[0].co)

print("------ selected points---------")
for v in mesh_1.verts:
    print(v.co)
    #print(v.co[1])
'''
    if (v.co[0] == -1.0 and v.co[1] == -1.0):
        print(v.co)
        v.co[2] = -.0
        
'''
        
print("--------   END !  -------")


