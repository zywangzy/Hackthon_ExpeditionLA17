"""
    This file get the estimation of fishing production of each port in Morocco.
    Proof of estimating fish yield with chlorophy concentration is in:
    http://journals.plos.org/plosone/article?id=10.1371/journal.pone.0028945
"""

import json, math

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

def get_supply():
    geojson_obj = load_json_file('../RoadHandler/PortByType.geojson')
    port_list = dict()
    for feature in geojson_obj['features']:
        if 'properties' in feature:
            obj_id = feature['properties']['OBJECTID']
            lat_deg = feature['properties']['LAT_DEG']
            lon_deg = feature['properties']['LONG_DEG']
            port_list[(lat_deg, lon_deg)] = obj_id
    print 'length is ' + str(len(port_list))
    with open('ChlorophyConcentration.txt') as file:
        for line in file:
            object_id = int(line.split(',')[1])
            plankton = float(line.split(',')[4])
            for key, value in port_list.iteritems():
                if value == object_id:
                    port_list[key] = plankton
                    break
    return port_list

if __name__ == '__main__':
    port_production = get_supply()
    # get the weighted fishing production estimation from chlorophy concentration
    sum = 0
    for key, value in port_production.iteritems():
        sum = sum + value
    print 'sum is ' + str(sum)
    total_amount = 2.5e6
    domestic_ratio = 0.2
    for key, value in port_production.iteritems():
        port_production[key] = value * 1.0 / sum * total_amount * domestic_ratio
        print str(key) + ' -> ' + str(port_production[key])
