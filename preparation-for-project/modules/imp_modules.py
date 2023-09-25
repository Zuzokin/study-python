import importlib


def imp_mods(mods, _globals=None):
    _globals.update({mod: importlib.import_module(mod) for mod in mods})
    print('модули установлены')

    # print('Факториал из модуля', math.factorial(random.randint(1, 10)))
