from shippingCalculator import ShippingCalculator


class LandShippingCalculator(ShippingCalculator):
    def __init__(self, custNm, custContact):
        ShippingCalculator.__init__(self, custNm, custContact)

    def computeCharges(self):
        return (
            super().getBaseCharges()
            + super().getCustomCharges()
            + super().getPackagingCharges(0.1)
            + super().getFreightCharges(0.25, 0.75, 10)
        )
