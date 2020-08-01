import main


def gender():
    product = main.main()
    list_gend = []
    for list_gen in product:
        for gen in list_gen['genders']:
            list_gend.append(gen)
    return set(list_gend)