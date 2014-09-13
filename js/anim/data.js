var anim = anim || {};

anim.shapeData = {
    'T': {
        'width': 240,
        'height': 240,
        'vertices': {
            'A': [0, 0],
            'B': [100, 0],
            'C': [140, 0],
            'D': [240, 0],
            'E': [0, 40],
            'F': [100, 40],
            'G': [140, 40],
            'H': [240, 40],
            'I': [140, 140],
            'J': [100, 240],
            'K': [140, 240],
            'L': [100, 140]
        },

        'triangles': [
            ['A', 'E', 'F', [['A', 'E', false], ['E', 'F', false]]],
            ['A', 'F', 'B', [['A', 'B', true]]],
            ['B', 'F', 'C', [['B', 'C', true]]],
            ['C', 'F', 'G', []],
            ['C', 'G', 'H', [['G', 'H', false]]],
            ['C', 'H', 'D', [['C', 'D', true], ['H', 'D', false]]],
            ['F', 'I', 'G', [['I', 'G', false]]],
            ['F', 'L', 'I', [['F', 'L', false]]],
            ['L', 'J', 'I', [['L', 'J', false]]],
            ['J', 'I', 'K', [['J', 'K', false], ['K', 'I', false]]]
        ]
    },

    'V': {
        'width': 120,
        'height': 200,
        'vertices': {
            'A': [0, 0],
            'B': [40, 0],
            'C': [80, 0],
            'D': [120, 0],
            'E': [20, 97],
            'F': [60, 150],
            'G': [100, 97],
            'H': [40, 240],
            'I': [80, 240]
        },

        'triangles': [
            ['A', 'E', 'B', [['A', 'B', true], ['A', 'E', false]]],
            ['B', 'E', 'F', [['B', 'F', true]]],
            ['E', 'H', 'F', [['E', 'H', false]]],
            ['F', 'H', 'I', [['H', 'I', false]]],
            ['F', 'I', 'G', [['I', 'G', false]]],
            ['C', 'F', 'G', [['C', 'F', false]]],
            ['C', 'G', 'D', [['G', 'D', false], ['C', 'D', true]]]
        ]
    }
};
