"""
Тестирование загрузчика данных
"""
import map_game.loader
import map_game.database

def test_database_pack():
    FILENAME = 'map.xml'
    result = map_game.loader._load(FILENAME)
    parsed = map_game.loader.parser(result)
    db = map_game.database.Database()
    packed = db._pack(parsed)

    assert 'Points' in packed
    assert 'Roads' in packed
    assert 'Houses' in packed
    assert 'Areas' in packed

