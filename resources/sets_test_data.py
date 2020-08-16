set_for_testing = [{'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}]
in_set = 'apple', 'orange', 'pear', 'banana'
a = {'a', 'r', 'b', 'c', 'd'}
b = {'l', 'c', 'm', 'z', 'a'}

data_for_uniq_letters_in_set = [
    (
        'abracadabra',
        'alacazam',
        {'r', 'd', 'b'}
    )
]

data_for_all_letters_in_sets = [
    (
        a,
        b,
        {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
    )
]

data_for_letters_in_both_sets = [
    (
        a,
        b,
        {'a', 'c'}
    )
]

data_for_letters_not_in_both_sets = [
    (
        a,
        b,
        {'r', 'd', 'b', 'm', 'z', 'l'}
    )
]