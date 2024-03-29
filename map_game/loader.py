"""
Загрузка файлов из XML файла

"""
import click
from collections import namedtuple
import os
import xml.etree.ElementTree as ET
import map_game.database

Node = namedtuple('Node', 'id lon lat')
Way = namedtuple('Way', 'id nds tags')
Tag = namedtuple('Tag', 'k v')


def _parse_node(node):
    attrs = node.attrib
    return Node(attrs['id'], attrs['lon'], attrs['lat'])


def _parse_way(way):
    attrs = way.attrib
    nds = []
    tags = []
    nid = attrs['id']
    for child in way:
        tagname = child.tag
        attrs = child.attrib
        if tagname == 'nd':
            nds.append(attrs['ref'])
        elif tagname == 'tag':
            tags.append(Tag(attrs["k"], attrs['v']))
    return Way(nid, nds, tags)




def _load(filename: str):
    filename = 'map.xml'
    if os.path.exists(filename):
        tree = ET.parse(filename)
        return tree.getroot()
    raise RuntimeError()



#@click.command()
#@click.argument('filename')
def load(filename: str):
    filename = 'map.xml'
    try:
        db = map_game.database.create()
        root = _load(filename)
        db.save(parser(root))
    except RuntimeError:
        print(F'Файл {filename} не найден')


def parser(root) -> dict:
    osm_info = {'nodes': [],
                'ways': []}
    for child in root:
        tagname = child.tag
        if tagname == 'node':
            node_info = _parse_node(child)
            osm_info['nodes'].append(node_info)
        elif tagname == 'way':
            way_info = _parse_way(child)
            osm_info['ways'].append(way_info)
    return osm_info


if __name__ == "__main__":
    load('map.xml')
