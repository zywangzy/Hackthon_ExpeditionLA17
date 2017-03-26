import json

def load_json_file(filename):
    plain_text = open(filename).read()
    
    # Make the plain text can be recognized by the json module.
    plain_text = plain_text.replace(',}', '}')
    plain_text = plain_text.replace(',]', ']')
    plain_text = plain_text.replace('}]}]}', '}]}')
    plain_text = " ".join(plain_text.split("\n"))
    plain_text = plain_text.replace("\\", "")
    
    data = json.loads(plain_text)
    return data

def get_road_linestring():
    geojson_obj = load_json_file('RoadNetwork.geojson')
    linestring = dict()
    for feature in geojson_obj['features']:
        if 'geometry' in feature and 'coordinates' in feature['geometry']:
            first = feature['geometry']['coordinates'][0]
            second = feature['geometry']['coordinates'][-1]
            linestring[((first[0], first[1]), (second[0], second[1]))] = feature['geometry']['coordinates']
            linestring[((second[0], second[1]), (first[0], first[1]))] = feature['geometry']['coordinates']
    return linestring

if __name__ == '__main__':
    roads = get_road_linestring()
    for srcdst, road in roads.iteritems():
        print str(srcdst) + ' -> ' + str(road)
