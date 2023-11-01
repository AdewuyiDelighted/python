from unittest import TestCase

from java_to_python.chapter4 import gas_milage
from java_to_python.chapter4.gas_milage import GasMiles


class TestGasMiles(TestCase):
    def test_the_miles(self):
        gas_miles = GasMiles()
        gas_miles.set_miles(9)
        self.assertEqual(9,gas_miles.get_miles())

    def test_the_gallon(self):
        gas_miles = GasMiles()
        gas_miles.set_gallon(6)
        self.assertEqual(6,gas_miles.get_gallon())

    def test_the_combined_miles_per_gallons(self):
        gas_miles = GasMiles()
        gas_miles.set_miles(10)
        gas_miles.set_gallon(5)
        gas_miles.miles_per_gallons()
        self.assertEqual(2,gas_miles.miles_per_gallons())


