my_dict = {
    'tuple': (1, 4, 'Artem', '4', 3),
    'list': ['word', 9, [1, 2, 3], False, 5],
    'dict': {'one': 2, 'two': 'dog', 'three': (0, 9), 'four': '45', 'five': 100},
    'set': {7, 'A', 'b', True, 99}
}

print(my_dict['tuple'][-1])
my_dict['list'].append(['Lenya', 2])
my_dict['list'].pop(1)
my_dict['dict']['i am a tuple'] = 'tuple not i am'
my_dict['dict'].pop('two')
my_dict['set'].add(-1)
my_dict['set'].pop()

print(my_dict)
