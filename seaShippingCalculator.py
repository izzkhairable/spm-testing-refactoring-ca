from shippingCalculator import ShippingCalculator


class SeaShippingCalculator(ShippingCalculator):
    def __init__(self):
        ShippingCalculator.__init__(self)

    def computeCharges(self):
        return (
            super().getBaseCharges()
            + super().getCustomCharges()
            + super().getPackagingCharges()
            + super().getFreightCharges(0.75, 0.75, 100)
        )
