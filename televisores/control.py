class Control:
    def enlazar(self, tv):
        self._tv = tv
        tv.setControl(self)
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