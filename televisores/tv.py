
class TV:
    _numTV = 0

    def __init__(self,marca,estado):
         self._marca = marca
         self._estado = estado
         self._canal = 1
         self._volumen = 1
         self._precio = 500
         _numTV = _numTV + 1

    def setNumTV(numTV):
        _numTV = numTV

    def getNumTV():
        return _numTV

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
        if(self._estado == True):
            if volumen >= 0 & volumen <= 7:
                self._volumen = volumen

    def setPrecio(self, precio):
        self._precio = precio

    def setCanal(self, canal):
        if(self._estado == True):
            if canal >= 1 & canal <= 120:
                self._canal = canal

    def setMarca(self, marca):
        self._marca = marca

    def setControl(self, control):
        self._control = control

    
    
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
