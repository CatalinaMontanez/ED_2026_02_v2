class Heap:

    def __init__(self):
        self.arreglo = [float('-inf')]

    def insert(self, valor):
        self.arreglo.append(valor)
        i = len(self.arreglo) - 1
        while i > 1 and self.arreglo[i] < self.arreglo[i // 2]:
            self.arreglo[i], self.arreglo[i // 2] = self.arreglo[i // 2], self.arreglo[i]
            i = i//2

    def remove_smallest(self):
        if len(self.arreglo) <= 1:
            return None

        valmin = self.arreglo[1]
        self.arreglo[1] = self.arreglo[-1]
        self.arreglo = self.arreglo[:-1]

        if len(self.arreglo) > 1:
            i = 1
            n = len(self.arreglo) - 1
            while 2*i <= n:
                hijoizq = 2 * i
                hijoder = 2*i+1
                menor = i

                if hijoizq <= n and self.arreglo[hijoizq] < self.arreglo[menor]:
                    menor = hijoizq
                if hijoder <= n and self.arreglo[hijoder] < self.arreglo[menor]:
                    menor = hijoder
                if menor == i:
                    break

                self.arreglo[i], self.arreglo[menor] = self.arreglo[menor], self.arreglo[i]
                i = menor
        return valmin

    def build_heap(self, lista):
        pass
