import unittest
from seaShippingCalculator import SeaShippingCalculator


class TestSeaShippingCalculator(unittest.TestCase):
    def setUp(self):
        self._init_sz = 10
        self._init_wt = 100
        self._init_frCountry = "SG"
        self._init_toCountry = "INDIA"

        self._seaShippingCalculator = SeaShippingCalculator()
        self._seaShippingCalculator.setSizeWeight(sz=self._init_sz, wt=self._init_wt)
        self._seaShippingCalculator.setFromToCountry(
            frCountry=self._init_frCountry, toCountry=self._init_toCountry
        )

    def tearDown(self):
        self._seaShippingCalculator = None

    """
    ------------------------------------
    Added prior to refactoring
    ------------------------------------
    """

    def test_getFromCountry(self):
        self.assertEqual(
            self._seaShippingCalculator.getFromCountry(), self._init_frCountry
        )

    def test_getToCountry(self):
        self.assertEqual(
            self._seaShippingCalculator.getToCountry(), self._init_toCountry
        )

    def test_getSize(self):
        self.assertEqual(self._seaShippingCalculator.getSize(), self._init_sz)

    def test_getWeight(self):
        self.assertEqual(self._seaShippingCalculator.getWeight(), self._init_wt)

    def test_computeCharges_from_sg_to_india(self):
        total_charges = (
            50
            + 20
            + (self._init_sz * self._init_wt)
            + ((0.75 * self._init_sz) + (0.75 * self._init_wt) + 100)
        )
        self.assertEqual(self._seaShippingCalculator.computeCharges(), total_charges)

    def test_computeCharges_from_usa_to_china(self):
        self._seaShippingCalculator.setFromToCountry(frCountry="USA", toCountry="CHINA")
        total_charges = (
            140
            + 25
            + (self._init_sz * self._init_wt)
            + ((0.75 * self._init_sz) + (0.75 * self._init_wt) + 100)
        )
        self.assertEqual(self._seaShippingCalculator.computeCharges(), total_charges)

    def test_computeCharges_from_china_to_india(self):
        self._seaShippingCalculator.setFromToCountry(
            frCountry="CHINA", toCountry="INDIA"
        )
        total_charges = (
            30
            + 20
            + (self._init_sz * self._init_wt)
            + ((0.75 * self._init_sz) + (0.75 * self._init_wt) + 100)
        )
        self.assertEqual(self._seaShippingCalculator.computeCharges(), total_charges)

    """
    -------------------------------------
    Added after completion of refactoring
    -------------------------------------
    """

    def test_getBaseCharges_from_sg_to_india(self):
        self.assertEqual(self._seaShippingCalculator.getBaseCharges(), 50)

    def test_getCustomCharges_to_india(self):
        self.assertEqual(self._seaShippingCalculator.getCustomCharges(), 20)

    def test_getPackagingCharges(self):
        self.assertEqual(
            self._seaShippingCalculator.getPackagingCharges(),
            (self._init_sz * self._init_wt),
        )

    def test_getFreightCharges(self):
        self.assertEqual(
            self._seaShippingCalculator.getFreightCharges(0.75, 0.75, 100),
            ((0.75 * self._init_sz) + (0.75 * self._init_wt) + 100),
        )
