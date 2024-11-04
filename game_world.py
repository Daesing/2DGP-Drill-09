
#world[0] = background
#world[1] = foreground
world = [[],[],[]]

def add_object(o,depth):
    world[depth].append(o)


def update():
    for layer in world:
        for o in layer:
            o.update()


def render():
    for layer in world:
        for o in layer:
            o.draw()


def remove_object(o):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
    print(f'CRITICAL: wrong delete object{o}')