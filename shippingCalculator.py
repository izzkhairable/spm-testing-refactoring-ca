from abc import ABC, abstractmethod

class ShippingCalculator(ABC):
     
    def __init__(self, custNm, custContact):
        self.__customerContact = custContact
        self.__customerName = custNm
    def setToAddContact(self, toAdd, toCon):
        self.__toAddress = toAdd
        self.__toContact = toCon
    def setFromToCountry(self,frCountry, toCountry):
        self.__fromCountry = frCountry
        self.__toCountry = toCountry
    def setSizeWeight(self, sz, wt):
        self.__size = sz
        self.__weight = wt
    def getFromCountry(self):
        return self.__fromCountry
    def getToCountry(self):
        return self.__toCountry
    def getSize(self):
        return self.__size
    def getWeight(self):
        return self.__weight
    @abstractmethod
    def computeCharges(self):
        pass
