import unittest
from models.external_conditions.ExternalConditions import ExternalConditions

class TestExternalConditions(unittest.TestCase):


    def test_defult_constructor(self):
        """
            Test default constructor
            test getters
        """
        external_conditions = ExternalConditions()

        self.assertEqual(external_conditions.getT(), 1.0)
        self.assertEqual(type(external_conditions.getT()), float)
        self.assertEqual(external_conditions.getH(), 0.0)
        self.assertEqual(type(external_conditions.getH()), float)


    def test_constructor(self):
        """
            Test constructor
            with float values, test getters
        """
        external_conditions = ExternalConditions(T=3.5, H=2.8)

        self.assertEqual(external_conditions.getT(), 3.5)
        self.assertEqual(type(external_conditions.getT()), float)
        self.assertEqual(external_conditions.getH(), 2.8)
        self.assertEqual(type(external_conditions.getH()), float)


    def test_type_casting_in_constructor(self):
        """
            Test that in constructior values are correctly cased
            into floats
        """
        external_conditions = ExternalConditions(T=3, H=2)

        self.assertEqual(external_conditions.getT(), 3)
        self.assertEqual(type(external_conditions.getT()), float)
        self.assertEqual(external_conditions.getH(), 2)
        self.assertEqual(type(external_conditions.getH()), float)


    def test_setters(self):
        """
            Testing setters
        """
        external_conditions = ExternalConditions(T=3.5, H=2.8)

        external_conditions.setT(4)
        self.assertEqual(external_conditions.getT(), 4.0)
        self.assertEqual(type(external_conditions.getT()), float)
        external_conditions.setH(5)
        self.assertEqual(external_conditions.getH(), 5.0)
        self.assertEqual(type(external_conditions.getH()), float)


if __name__ == '__main__':
    unittest.main()
