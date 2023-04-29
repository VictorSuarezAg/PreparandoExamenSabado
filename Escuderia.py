from Piloto import Piloto

class Escuderia:
    def __init__(self):
        self.__nombre = None
        self.__casaMotor = None
        self.__pilotoPpal = Piloto()
        self.__pilotoSec = Piloto()
        self.__costos = None
        
        @property
        def nombre(self):
            return self.__nombre
        
        @nombre.setter
        def nombre(self, dato):
            self.__nombre = dato
        
        @property
        def casaMotor(self):
            return self.__casaMotor

        @casaMotor.setter
        def casaMotor(self, dato):
            self.__casaMotor = dato
        
        @property
        def pilotoPpal(self):
            return self.__pilotoPpal

        @pilotoPpal.setter
        def pilotoPpal(self, dato):
            self.__pilotoPpal = dato
        
        @property
        def pilotoSec(self):
            return self.__pilotoSec

        @pilotoSec.setter
        def pilotoSec(self, dato):
            self.__pilotoSec = dato
            
        @property
        def costos(self):
            return self.__costos

        @costos.setter
        def costos(self, dato):
            self.__costos = dato
