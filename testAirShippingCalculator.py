import unittest
from airShippingCalculator import AirShippingCalculator


class TestAirShippingCalculator(unittest.TestCase):
    def setUp(self):
        self._init_custNm = "John Doe"
        self._init_custContact = "90009000"
        self._init_toAdd = "101 Silicon Lane"
        self._init_toCon = "91119111"
        self._init_sz = 10
        self._init_wt = 100
        self._init_frCountry = "SG"
        self._init_toCountry = "INDIA"

        self._airShippingCalculator = AirShippingCalculator(
            custNm=self._init_custNm, custContact=self._init_custContact
        )

        self._airShippingCalculator.setToAddContact(
            toAdd=self._init_toAdd, toCon=self._init_toCon
        )

        self._airShippingCalculator.setSizeWeight(sz=self._init_sz, wt=self._init_wt)

        self._airShippingCalculator.setFromToCountry(
            frCountry=self._init_frCountry, toCountry=self._init_toCountry
        )

    def tearDown(self):
        self._airShippingCalculator = None

    def test_getFromCountry(self):
        self.assertEqual(
            self._airShippingCalculator.getFromCountry(), self._init_frCountry
        )

    def test_getToCountry(self):
        self.assertEqual(
            self._airShippingCalculator.getToCountry(), self._init_toCountry
        )

    def test_getSize(self):
        self.assertEqual(self._airShippingCalculator.getSize(), self._init_sz)

    def test_getWeight(self):
        self.assertEqual(self._airShippingCalculator.getWeight(), self._init_wt)

    def test_compute_charges_from_sg_to_india(self):
        total_charges = (
            50
            + 20
            + (self._init_sz * self._init_wt)
            + ((3 * self._init_sz) + (4 * self._init_wt))
        )
        self.assertEqual(self._airShippingCalculator.computeCharges(), total_charges)

    def test_compute_charges_from_usa_to_china(self):
        self._airShippingCalculator.setFromToCountry(frCountry="USA", toCountry="CHINA")
        total_charges = (
            140
            + 25
            + (self._init_sz * self._init_wt)
            + ((3 * self._init_sz) + (4 * self._init_wt))
        )
        self.assertEqual(self._airShippingCalculator.computeCharges(), total_charges)
