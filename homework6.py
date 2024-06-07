my_dict = {'Kolya': 1, 'Serega': 2, 'Pavel': 3}
print(f'Dict: {my_dict}')
print(f'Existing value: {my_dict['Kolya']}')
print(f'Nonexisting value: {my_dict.get('Alesha')}')
my_dict.update({'Tarzan': 8, 'Oompa-Loompa': 12})
print(f'Deleted value: {my_dict.pop('Tarzan')}')
print(f'Modified dictionary: {my_dict}')

my_set = {5, 5, 5, 2, 2, 6, 'Car', False, (4, 99)}
print(f'Set: {my_set}')
my_set.add(77)
my_set.add('Book')
my_set.remove(5)
print(f'Modified set: {my_set}')
