class nodoselfSimple(object):
    info, siguiente = None, None


class Lista(object):
    def __init__(self):
        self.inicio = None
        self.tamanio = 0


    def insertar(self, info):
        nodo = nodoselfSimple()
        nodo.info = info
        if self.inicio is None:
            nodo.siguiente = self.inicio
            self.inicio = nodo
        else:
            actual = self.inicio
            siguiente = self.inicio.siguiente
            while siguiente is not None:
                actual = actual.siguiente
                siguiente = siguiente.siguiente
            nodo.siguiente = siguiente
            actual.siguiente = nodo
        self.tamanio += 1


    def imprimir(self):
        actual = self.inicio
        txt = "["
        while actual is not None:
            if actual.siguiente != None:
                txt = f"{txt}{actual.info}, "
            else:
                txt = f"{txt}{actual.info}]"
            actual = actual.siguiente
        print(txt)


    def largo(self):
        return self.tamanio


    def eliminar(self, info):
        data = None
        # saber si es el primero de la self
        if(self.inicio.info == info):
            data = self.inicio
            self.inicio = self.inicio.siguiente
            self.tamanio -= 1
        else:
            actual = self.inicio
            siguiente = self.inicio.siguiente
            while (siguiente is not None and info != siguiente.info):
                actual = actual.siguiente
                siguiente = siguiente.siguiente
            # saber si es el ultimo de la self
            if(siguiente is not None):
                data = siguiente.info
                actual.siguiente = siguiente.siguiente
                self.tamanio -= 1
        return data


    def index_of(self, info):
        actual = self.inicio
        index = 0
        for _ in range(self.tamanio):
            if actual.info == info:
                return index
            index += 1
            actual = actual.siguiente

        return None


    def index(self, indice):
        actual = self.inicio
        for _ in range(indice):
            actual = actual.siguiente
            if actual == None:
                return None
        return actual.info


    def reemplazar(self, indice, info):
        actual = self.inicio
        for _ in range(indice):
            actual = actual.siguiente
            if actual == None:
                return None
        actual.info = info


    def obtener(self, indice):
        actual = self.inicio
        for _ in range(indice):
            actual = actual.siguiente
            if actual == None:
                return None
        data = actual.info
        self.eliminar(data)
        return data


    def index_of_param(self, param):
        actual = self.inicio
        while actual.info is not param:
            pass
    
    
    def burbuja(self,lista):
        for i in range(0,self.tamanio - 1):
            for j in range(0, self.tamanio- i - 1):
                if lista.index(j) > lista.index(j+1):
                    aux = lista.index(j)
                    lista.reemplazar(j,lista.index(j+1))
                    lista.reemplazar(j+1,aux)
        lista.imprimir()

    
    def burbujaMej(self,lista):
        i = 0
        control = True
        while ((i < self.tamanio) - 2 and control):
            control = False
            for j in range(0,self.tamanio - i - 1):
                if lista.index(j) > lista.index(j+1):
                    aux = lista.index(j)
                    lista.reemplazar(j,lista.index(j+1))
                    lista.reemplazar(j+1,aux)
                    control = True
            i = i + 1
        lista.imprimir()


    def burbujabidir(self,lista):
        left = 0
        right = self.tamanio - 1
        control = True
        while(left < right) and control:
            control = False
            for i in range(left,right):
                if lista.index(i) > lista.index(i + 1):
                    aux = lista.index(i)
                    lista.reemplazar(i,lista.index(i + 1))
                    lista.reemplazar(i + 1, aux)
                    control = True
            
            right -= 1
            for j in range(right,left, -1):
                if lista.index(j) < lista.index(j+1):
                    aux = lista.index(j)
                    lista.reemplazar(j,lista.index(j-1))
                    lista.reemplazar(i - 1, aux)
                    control = True
            left += 1
        lista.imprimir()
    
    def seleccion(self,lista):
        for i in range(0, self.tamanio - 1):
            min= i
            for j in range(i+1,self.tamanio):
                if lista.index(j) < lista.index(min):
                    min = j

            aux = lista.index(i)
            lista.reemplazar(i,lista.index(min))
            lista.reemplazar(min,aux)
        lista.imprimir()


    def insercion(self,lista):
        for i in range(1,self.tamanio + 1):
            help = i - 1
            while((help > 0) and (lista.index(help) < lista.index(help - 1))):
                aux = lista.index(help)
                lista.reemplazar(help,lista.index(help - 1))
                lista.reemplazar(help - 1, aux)
                help -= 1
        lista.imprimir()

