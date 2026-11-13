class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor, imagen=False):
        self.arreglo.append(valor)
        i = len(self.arreglo) - 1
        while i > 1 and self.arreglo[i] < self.arreglo[i//2]:
            self.arreglo[i], self.arreglo[i//2] = self.arreglo[i//2], self.arreglo[i]
            i = i//2
        if imagen:
            self._mostrar_imagen()

    def remove_smallest(self, imagen=False):
        if len(self.arreglo) <= 1:
            if imagen:
                self._mostrar_imagen()
            return None

        valmin = self.arreglo[1]
        ultimo = self.arreglo.pop()
        if len (self.arreglo) > 1:
            self.arreglo[1] = ultimo 
            self._bajar(1)
        if imagen:
            self._mostrar_imagen()
        return valmin

    def build_heap(self, lista, imagen=False):
        self.arreglo = [float('-inf')] + list(lista)
        n = len(self.arreglo) - 1
        for i in range(n//2, 0, -1):
            self._bajar(i)
        if imagen:
            self._mostrar_imagen()

    def _bajar(self, i):
        n = len(self.arreglo) - 1
        while 2 * i <= n:
            menor = i
            izq = 2*i
            der = 2*i+1
            if self.arreglo[izq] < self.arreglo[menor]:
                menor = izq
            if der <= n and self.arreglo[der] < self.arreglo[menor]:
                menor = der
            if menor == i:
                break
            self.arreglo[i], self.arreglo[menor] = self.arreglo[menor], self.arreglo[i]
            i = menor

    def _mostrar_imagen(self):
        import matplotlib.pyplot as plt

        n=len(self.arreglo) - 1
        niveles = n.bit_length() if n > 0 else 1
        hojas = 2 ** (niveles - 1)

        pos = {}
        for i in range(1, n+1):
            nivel = i.bit_length() - 1
            k = i - 2 ** nivel
            pos[i] = ((k+0.5) /2**nivel, -nivel)

        ancho = min(max(4, hojas * 0.7), 20)
        alto = max(2.5, niveles * 1.3)
        fig, ax = plt.subplots(figsize=(ancho, alto))

        for i in range(2, n+1):
            x0, y0= pos[i//2]
            x1, y1 = pos[i]
            ax.plot([x0,x1], [y0, y1], color='gray', zorder=1)

        radio = 1100 if hojas <=8 else (600 if hojas <=16 else 300)
        for i in range(1, n+1):
            x,y = pos[i]
            ax.scatter([x], [y], s=radio, color='lightblue', edgecolors='black', zorder=2)
            ax.text(x, y, str(self.arreglo[i]), ha='center', va='center',
                    fontsize=10 if hojas <= 16 else 7, zorder=3)        

        if n == 0:
            ax.text(0.5, 0, '(heap vacío)', ha='center', va='center')
        ax.set_xlim(0, 1)
        ax.set_ylim(-niveles + 0.4, 0.6)
        ax.axis('off')
        plt.show()

if __name__ == "__main__":
    h = Heap()
    h.build_heap([31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16,
                  15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
    print(h.arreglo)

