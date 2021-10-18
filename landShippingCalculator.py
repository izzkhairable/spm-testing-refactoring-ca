from shippingCalculator import ShippingCalculator
from countryCharges import CountryCharges


class LandShippingCalculator(ShippingCalculator):
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
        return super().getSize() * super().getWeight() * 0.90

    def getLandFreightCharges(self):
        return (super().getSize() * 0.25) + (super().getWeight() * 0.75) + 10

    def computeCharges(self):
        return (
            self.getBaseCharges()
            + self.getPackagingCharges()
            + self.getCustomCharges()
            + self.getLandFreightCharges()
        )
