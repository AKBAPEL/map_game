"""
Загрузка данных из XML файла
"""
import map_game

def test_load_data():
    FILENAME = 'map.xml'
    result = map_game.loader.load(FILENAME)
    assert result


def test_parser():
    result = map_game.loader.parser(xml_object)
    assert 'nodes' in result
    assert 'ways' in result

