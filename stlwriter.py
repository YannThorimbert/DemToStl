"""Takes an hmap as input, gives ASCII stl as output
#-------------------------------------------------------------------------------
# Name:        stlwriter.py
#
# Author:      Yann Thorimbert
#
# Created:     06.02.2017
#-------------------------------------------------------------------------------
"""
from __future__ import print_function, division


def get_triangles_offset(h,x,y,dh,dx,ox,oy):
    xox = (x+ox)
    yoy = (y+oy)
    bottomleft  =   (xox*dx,    yoy*dx,   h[x,y]*dh)
    topright    =   ((xox+1)*dx,  (yoy+1)*dx, h[x+1,y+1]*dh)
    topleft     =   (xox*dx,    (yoy+1)*dx, h[x,y+1]*dh)
    bottomright =   ((xox+1)*dx,  yoy*dx,   h[x+1,y]*dh)
    return (bottomleft, bottomright, topright), (bottomleft,topright,topleft) #attention ordre

def write_stl(hmap,outfile,dh,dx):
    f = open(outfile,"w")
    f.write("solid terrain\n")
    w,h = hmap.shape
    print("Writing STL " + outfile + "...",end="")
    print("width, height = ", w, h)
    for x in range(w-1):
        if x%100 == 0:
            print(round(x*100./w), "%")
        for y in range(h-1):
            for v1,v2,v3 in get_triangles_offset(hmap,x,y,dh,dx,-w//2,-h//2):
                s1 = " ".join([format(value,"e") for value in v1])
                s2 = " ".join([format(value,"e") for value in v2])
                s3 = " ".join([format(value,"e") for value in v3])
                f.write("   facet normal 0 0 0\n")
                f.write("       outer loop\n")
                f.write("           vertex "+s1+"\n")
                f.write("           vertex "+s2+"\n")
                f.write("           vertex "+s3+"\n")
                f.write("       endloop\n")
                f.write("   endfacet\n")
    f.write("endsolid terrain\n")
    f.close()
    print("STL written.")