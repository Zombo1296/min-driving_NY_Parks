import requests, bs4, json, googlemaps
from datetime import datetime

res = requests.get('https://parks.ny.gov/recreation/trails/trails-in-state-parks.aspx')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text,"lxml")
#type(noStarchSoup)
elems = noStarchSoup.select('.lst-arw li a')
parkNames = []
startPoint = []
for elem in elems:
    parkNames.append(elem.getText())
    # home address, start point: Forest Hills Stadium
    # for now. need to compare every park to the other parks
    startPoint.append('Forest Hills Stadium') 

gmaps = googlemaps.Client(key='my google api key')

now = datetime.now()
#google can only take 10 requests at a time, need to bypass this
res = gmaps.distance_matrix(startPoint[0:10],parkNames[0:10],departure_time=now)
for x in range(0,10,1):
    print(parkNames[x]+"--"+res['rows'][0]['elements'][x]['duration']['text'])

    
'''
Beblow is on-going testing code. Purpose is to process park to park driving time
and make each park a undirected graph node and make driving time between each park
a weight for each edge.
'''

from collections import defaultdict

class Graph(object):
    """ Graph data structure, undirected by default. """

    def __init__(self, connections, directed=False):
        self._graph = defaultdict(set)
        self._directed = directed
        self.add_connections(connections)

    def add_connections(self, connections):
        """ Add connections (list of tuple pairs) to graph """

        for node1, node2 in connections:
            self.add(node1, node2)

    def add(self, node1, node2):
        """ Add connection between node1 and node2 """

        self._graph[node1].add(node2)
        if not self._directed:
            self._graph[node2].add(node1)

    def remove(self, node):
        """ Remove all references to node """

        for n, cxns in self._graph.iteritems():
            try:
                cxns.remove(node)
            except KeyError:
                pass
        try:
            del self._graph[node]
        except KeyError:
            pass

    def is_connected(self, node1, node2):
        """ Is node1 directly connected to node2 """

        return node1 in self._graph and node2 in self._graph[node1]

    def find_path(self, node1, node2, path=[]):
        """ Find any path between node1 and node2 (may not be shortest) """

        path = path + [node1]
        if node1 == node2:
            return path
        if node1 not in self._graph:
            return None
        for node in self._graph[node1]:
            if node not in path:
                new_path = self.find_path(node, node2, path)
                if new_path:
                    return new_path
        return None

    def __str__(self):
        return '{}({})'.format(self.__class__.__name__, dict(self._graph))


connections = [('Allegany State Park', 'Artpark State Park'), 
               ('Artpark State Park', 'Bayard Cutting Arboretum State Park')]
g = Graph(connections)
pprint(g._graph)
g.add('E', 'D')