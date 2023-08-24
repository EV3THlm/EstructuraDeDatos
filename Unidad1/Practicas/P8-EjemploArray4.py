versiones_plone = [2.1, 2.5, 3.6];
print(f'{versiones_plone}');

versiones_plone.extend([4])
print(f'{versiones_plone}');

versiones_plone.extend(range(5,7));
print(f'{versiones_plone}');