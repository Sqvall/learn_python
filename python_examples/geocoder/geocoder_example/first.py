import geocoder

g = geocoder.ip('me')
# print(g.osm)
# print(g.geojson)

g = geocoder.osm(g.latlng, method='reverse')
print(g)
