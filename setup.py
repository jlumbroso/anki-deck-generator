from setuptools import setup, find_packages

setup(
    name='anki_deck_generator',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'click',
        'colorama',
        'genanki',
    ],
    entry_points='''
        [console_scripts]
        anki_deck_generator=anki_deck_generator:generate_anki_deck
    ''',
)
