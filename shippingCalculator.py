from abc import ABC, abstractmethod
from countryCharges import CountryCharges


class ShippingCalculator(ABC):
    def __init__(self):
        self.__base = CountryCharges()

    def setFromToCountry(self, frCountry, toCountry):
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

    def getBaseCharges(self):
        return self.__base.getBaseCharge(self.__fromCountry, self.__toCountry)

    def getCustomCharges(self):
        return self.__base.getCustomCharges(self.__toCountry)

    def getPackagingCharges(self, discountPercentage=0):
        return self.getSize() * self.getWeight() * (1 - discountPercentage)

    def getFreightCharges(self, multiplySz=1, multiplyWt=1, addToTotal=0):
        return (
            (self.getSize() * multiplySz) + (self.getWeight() * multiplyWt) + addToTotal
        )

    @abstractmethod
    def computeCharges(self):
        pass
