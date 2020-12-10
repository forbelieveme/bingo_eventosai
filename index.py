import numpy as np
import pandas as pd


df = pd.read_csv('cartonescomas2.csv')


def verificarIntervalos(data):
    nombre = {'campos': [
        {'col': [
            'n1b1',
            'n1b2',
            'n1b3',
            'n1b4',
            'n1b5',
        ],
            'low':14,
            'high':16},
        {'col': [
            'n1i1',
            'n1i2',
            'n1i3',
            'n1i4',
            'n1i5',
        ],
            'low':29,
            'high':31},
        {'col': [
            'n1n1',
            'n1n2',
            'n1n3',
            'n1n4',
            'n1n5',
        ],
            'low':30,
            'high':46},
        {'col': [
            'n1g1',
            'n1g2',
            'n1g3',
            'n1g4',
            'n1g5',
        ],
            'low':45,
            'high':61},
        {'col': [
            'n1o1',
            'n1o2',
            'n1o3',
            'n1o4',
            'n1o5',
        ],
            'low':60,
            'high':76},

    ],
        'letra': ['b', 'i', 'n', 'g', 'o']
    }

    for counti, i in enumerate(nombre['campos']):
        nombre['info'+nombre['letra'][counti]] = data.loc[:, i['col']]

    for counti, i in enumerate(nombre['campos']):
        for countj, j in enumerate(i['col']):
            letra = nombre['letra'][counti]
            base = nombre['info'+letra]
            temp = base[(base[j] < i['low']) | (base[j] > i['high'])]
            print(temp)


def main():
    verificarIntervalos(df)

main()
