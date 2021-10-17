from shippingCalculator import ShippingCalculator 
from countryCharges import CountryCharges

class SeaShippingCalculator (ShippingCalculator):
    def __init__(self, custNm, custContact):
        ShippingCalculator.__init__(self,custNm, custContact)
    def computeCharges(self):
        base = CountryCharges()
        baseCharge = base.getBaseCharge(super().getFromCountry(), super().getToCountry())
        # Compute Packaging Charges
        packagingCharge = super().getSize()*super().getWeight()
        # Compute Custom Charges
        customCharges =  base.getCustomCharges(super().getToCountry())
        seaFreightCharges = (super().getSize()*0.75) + (super().getWeight()*0.75) + 100
        return baseCharge + packagingCharge + customCharges + seaFreightCharges