data_for_update = [
    (
        {'a': 'alpha', 'o': 'omega', 'g': 'gamma'},
        {'b': 'beta'},
        {'a': 'alpha', 'b': 'beta', 'g': 'gamma', 'o': 'omega'}
    ),
    (
        {0: 0, 1: 1, 2: 4, 3: 9},
        {4: 16},
        {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
    )
]

data_for_get = [
    (
        {'a': 'alpha', 'b': 'beta', 'g': 'gamma', 'o': 'omega'},
        'b',
        'beta'
    ),
    (
        {0: 0, 1: 1, 2: 4, 3: 9, 4: 16},
        4,
        16
    )
]

data_for_pop = [
    (
        {'a': 'alpha', 'b': 'beta', 'g': 'gamma', 'o': 'omega'},
        'b',
        {'a': 'alpha', 'g': 'gamma', 'o': 'omega'}
    ),
    (
        {0: 0, 1: 1, 2: 4, 3: 9, 4: 16},
        4,
        {0: 0, 1: 1, 2: 4, 3: 9}
    )
]

data_for_join = [
(
        {'a': 'alpha', 'o': 'omega', 'g': 'gamma'},
        {0: 0, 1: 1, 2: 4, 3: 9, 4: 16},
        {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 'a': 'alpha', 'g': 'gamma', 'o': 'omega'}
    ),
    (
        {0: 0, 1: 1, 2: 4, 3: 9},
        {'a': 'alpha', 'b': 'beta', 'o': 'omega', 'g': 'gamma'},
        {0: 0, 1: 1, 2: 4, 3: 9, 'a': 'alpha', 'b': 'beta', 'g': 'gamma', 'o': 'omega'}
    )
]

data_for_invert = [
    (
        {'a': 'alpha', 'b': 'beta', 'g': 'gamma', 'o': 'omega'},
        {'alpha': 'a', 'beta': 'b', 'gamma': 'g', 'omega': 'o'}
    ),
    (
        {0: 0, 1: 1, 2: 4, 3: 9, 4: 16},
        {0: 0, 1: 1, 4: 2, 9: 3, 16: 4}
    )
]