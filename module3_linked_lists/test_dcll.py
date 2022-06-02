from doubly_circular_linked_list import circleDoubleLinkedList

circule_doble_list = circleDoubleLinkedList()
print('* ' * 3, 'Test of initialisation', ' *' * 3)
print(f'{circule_doble_list}\n{circule_doble_list.reverse()}\n')


print('\nAdd an element with the list empty')
circule_doble_list.unchanged(4)
print(f'{circule_doble_list}\n{circule_doble_list.reverse()}\n')


print('\nGenerate elements with range')
circule_doble_list.range(1, 6)
print(f'{circule_doble_list}\n{circule_doble_list.reverse()}\n')


print('\nGo over the list by steps')
print(circule_doble_list.str_by_steps(12, 'forward'))
print(circule_doble_list.str_by_steps(12, 'backward'), '\n')

print('\nSearch test')
circule_doble_list.search(2)
print(f'{circule_doble_list}\n{circule_doble_list.reverse()}\n')

print('\nReplace an element')
circule_doble_list.replace(3, 'replace_item')
print(f'{circule_doble_list}\n{circule_doble_list.reverse()}\n')

print('\nInsert an element in head')
circule_doble_list.unchanged('unchanged')
print(f'{circule_doble_list}\n{circule_doble_list.reverse()}\n')


print('\nInsert an element in tail')
circule_doble_list.append('append')
print(f'{circule_doble_list}\n{circule_doble_list.reverse()}\n')

print('\nDelete an element in head')
circule_doble_list.changed()
print(f'{circule_doble_list}\n{circule_doble_list.reverse()}\n')


print('\nDelete an element in head tail')
circule_doble_list.pop()
print(f'{circule_doble_list}\n{circule_doble_list.reverse()}\n')


print('\nInsert an element by index')
circule_doble_list.insert("index", 1)
print(f'{circule_doble_list}\n{circule_doble_list.reverse()}\n')

print('\nDelete an element by index: ')
circule_doble_list.delete_by_index(3)
print(f'{circule_doble_list}\n{circule_doble_list.reverse()}\n')


print('\nClear list')
circule_doble_list.clear()
print(f'{circule_doble_list}\n{circule_doble_list.reverse()}\n')
