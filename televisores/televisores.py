class Marca:
    def __init__(self, marca):
        self._nombre = marca
    def getNombre(self):
        return self._nombre
    def setNombre(self,marca):
        self._nombre = marca

class TV:
    _numTV = 0
    def __init__(self,marca,estado):
         self._marca = marca
         self._estado = estado
         self._canal = 1
         self._volumen = 1
         self._precio = 500
         _numTV = _numTV + 1
    def getControl(self):
        return self._control
    def getMarca(self):
        return self._marca
    def getCanal(self):
        return self._canal
    def getPrecio(self):
        return self._precio
    def getVolumen(self):
        return self._volumen
    def setVolumen(self, volumen):
        if(this.estado == True):
            if volumen >= 0 & volumen <= 7:
                self._volumen = volumen
    def setPreco(self, precio):
        self._precio = precio
    def setCanal(self, canal):
        if(this.estado == True):
            if canal >= 1 & canal <= 120:
                self._canal = canal
    def setMarca(self, marca):
        self._marca = marca
    def setControl(self, control):
        self._control = control
    def setNumTV(self, num):
        _numTV = num
    def getNumTV():
        return _numTV
    def turnOn(self):
        self._estado = True
    def turnOff(self):
        self._estado = False
    def getEstado(self):
        return self._estado
    def canalUp(self):
        if self._estado == True:
            if self._canal >=120:
                pass
            else:
                self._canal = self._canal+1
    def canalDown(self):
         if self._estado == True:
            if self._canal <= 1:
                pass
            else:
                self._canal = self._canal-1
    def volumenDown(self):
        if self._estado == True:
            if self._volumen <= 0:
                pass
            else:
                self._volumen = self._volumen - 1
    def volumenUp(self):
        if self._estado == True:
            if self._volumen >= 7:
                pass
            else:
                self._volumen = self._volumen + 1
    
class Control:
    def enlazar(self, tv):
        self._tv = tv
        _tv.control(self)
    def turnOn(self):
        self._tv.turnOn()
    def turnOff(self):
        self._tv.turnOff()
    def volumenDown(self):
        self._tv.volumenDown()
    def volumenUp(self):
        self._tv.volumenUp()
    def canalUp(self):
        self._tv.canalUp()
    def canalDown(self):
        self._tv.canalDown()
    def setCanal(self, canal):
        self._tv.setCanal(canal)
    def setVolumen(self, v):
        self._tv.setVolumen(v)
    def getTv(self):
        return self._tv
    def setTv(self, tv):
        self._tv = tv

    