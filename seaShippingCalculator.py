from shippingCalculator import ShippingCalculator
from countryCharges import CountryCharges


class SeaShippingCalculator(ShippingCalculator):
    def __init__(self, custNm, custContact):
        ShippingCalculator.__init__(self, custNm, custContact)
        self._base = CountryCharges()

    def getBaseCharges(self):
        return self._base.getBaseCharge(
            super().getFromCountry(), super().getToCountry()
        )

    def getCustomCharges(self):
        return self._base.getCustomCharges(super().getToCountry())

    def getPackagingCharges(self):
        return super().getSize() * super().getWeight()

    def getSeaFreightCharges(self):
        return (super().getSize() * 0.75) + (super().getWeight() * 0.75) + 100

    def computeCharges(self):
        return (
            self.getBaseCharges()
            + self.getPackagingCharges()
            + self.getCustomCharges()
            + self.getSeaFreightCharges()
        )
