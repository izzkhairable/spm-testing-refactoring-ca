import unittest
from seaShippingCalculator import SeaShippingCalculator


class TestSeaShippingCalculator(unittest.TestCase):
    def setUp(self):
        self._init_custNm = "John Doe"
        self._init_custContact = "90009000"
        self._init_toAdd = "101 Silicon Lane"
        self._init_toCon = "91119111"
        self._init_sz = 10
        self._init_wt = 100
        self._init_frCountry = "SG"
        self._init_toCountry = "INDIA"

        self._seaShippingCalculator = SeaShippingCalculator(
            custNm=self._init_custNm, custContact=self._init_custContact
        )

        self._seaShippingCalculator.setToAddContact(
            toAdd=self._init_toAdd, toCon=self._init_toCon
        )

        self._seaShippingCalculator.setSizeWeight(sz=self._init_sz, wt=self._init_wt)

        self._seaShippingCalculator.setFromToCountry(
            frCountry=self._init_frCountry, toCountry=self._init_toCountry
        )

    def tearDown(self):
        self._seaShippingCalculator = None

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

    def test_compute_charges_from_sg_to_india(self):
        total_charges = (
            50
            + 20
            + (self._init_sz * self._init_wt)
            + ((0.75 * self._init_sz) + (0.75 * self._init_wt) + 100)
        )
        self.assertEqual(self._seaShippingCalculator.computeCharges(), total_charges)

    def test_compute_charges_from_usa_to_china(self):
        self._seaShippingCalculator.setFromToCountry(frCountry="USA", toCountry="CHINA")
        total_charges = (
            140
            + 25
            + (self._init_sz * self._init_wt)
            + ((0.75 * self._init_sz) + (0.75 * self._init_wt) + 100)
        )
        self.assertEqual(self._seaShippingCalculator.computeCharges(), total_charges)
