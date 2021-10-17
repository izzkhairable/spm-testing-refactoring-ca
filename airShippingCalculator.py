from shippingCalculator import ShippingCalculator 
from countryCharges import CountryCharges

class AirShippingCalculator (ShippingCalculator):
    def __init__(self, custNm, custContact):
        ShippingCalculator.__init__(self,custNm, custContact)
    def computeCharges(self):
        base = CountryCharges()
        baseCharge = base.getBaseCharge(super().getFromCountry(), super().getToCountry())
        # Compute Packaging Charges
        packagingCharge = super().getSize()*super().getWeight()
        # Compute Custome Charges
        customCharges =  base.getCustomCharges(super().getToCountry())
        airFreightCharges = (super().getSize()*3) + (super().getWeight()*4)
        return baseCharge + packagingCharge + customCharges + airFreightCharges
