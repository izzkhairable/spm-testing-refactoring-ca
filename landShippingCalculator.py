from shippingCalculator import ShippingCalculator
from countryCharges import CountryCharges


class LandShippingCalculator(ShippingCalculator):
    def __init__(self, custNm, custContact):
        ShippingCalculator.__init__(self, custNm, custContact)

    def computeCharges(self):
        base = CountryCharges()
        baseCharge = base.getBaseCharge(
            super().getFromCountry(), super().getToCountry()
        )
        # Compute Packaging Charges - 10% discount
        packagingCharge = super().getSize() * super().getWeight() * 0.90
        # Compute Customer Charges
        customCharges = base.getCustomCharges(super().getToCountry())
        landFreightCharges = (
            (super().getSize() * 0.25) + (super().getWeight() * 0.75) + 10
        )
        return baseCharge + packagingCharge + customCharges + landFreightCharges
