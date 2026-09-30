from goodrich.ch08.linked_binary_tree import LinkedBinaryTree


def es_completo(T):
    """Retorna True si el LinkedBinaryTree T es completo."""
    if T.is_empty():
        return True

    lista = [T.root()]
    encontroh = False

    while len(lista) > 0:
        p = lista.pop(0)

        if p is None:
            encontroh = True
        else:
            if encontroh:
                return False

            lista.append(T.left(p))
            lista.append(T.right(p))
    return True

def camino(T, p, q):
    """Retorna el camino de p a q como string: 'H -> D -> B -> E'."""
    def obtenerancestros(nodo):
        lista = []
        actual = nodo
        while actual is not None:
            lista.append(actual)
            actual = T.parent(actual)
        return lista

    ancestrosp = obtenerancestros(p)
    ancestrosq = obtenerancestros(q)

    i = len(ancestrosp) - 1
    j = len(ancestrosq) - 1

    idp = 0
    idq = 0

    while i >= 0 and j >= 0 and ancestrosp[i] == ancestrosq[j]:
        idp = i
        idq = j
        i -= 1
        j -= 1

    subida = ancestrosp[:idp +1]
    bajada = ancestrosq[:idq]
    bajada.reverse()

    total = subida +  bajada

    return ' -> '.join(str(nodo.element()) for nodo in total)

if __name__ == "__main__":
    # tus pruebas (opcional)
    pass
