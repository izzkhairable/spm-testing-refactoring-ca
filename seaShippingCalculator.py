from shippingCalculator import ShippingCalculator


class SeaShippingCalculator(ShippingCalculator):
    def __init__(self, custNm, custContact):
        ShippingCalculator.__init__(self, custNm, custContact)

    def computeCharges(self):
        return (
            super().getBaseCharges()
            + super().getCustomCharges()
            + super().getPackagingCharges()
            + super().getFreightCharges(0.75, 0.75, 100)
        )
