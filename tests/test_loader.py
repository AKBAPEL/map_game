"""
Загрузка данных из XML файла
"""
import map_game.loader


def test_parser():
    FILENAME = 'map.xml'
    result = map_game.loader._load(FILENAME)
    parsed = map_game.loader.parser(result)

    assert 'nodes' in parsed
    assert 'ways' in parsed

