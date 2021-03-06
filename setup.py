from setuptools import setup

setup(
    name='map_game',
    version='1.0',
    author='Andrey Beliy',
    packages=['map_game'],
    description='Simple game',
    install_requires=['click'],
    entry_points={'console_scripts': ['load-xml = map_game.loader:load']},
)
