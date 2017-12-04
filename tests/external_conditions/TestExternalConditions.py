import unittest
from models.external_conditions.ExternalConditions import ExternalConditions

class TestExternalConditions(unittest.TestCase):


    def test_defult_constructor(self):
        externalConditions=ExternalConditions()

        self.assertEqual(externalConditions.getT(), 1.0)
        self.assertEqual(type(externalConditions.getT()), float)
        self.assertEqual(externalConditions.getH(), 0.0)
        self.assertEqual(type(externalConditions.getH()), float)


    def test_constructor(self):
        externalConditions=ExternalConditions(T=3.5, H=2.8)

        self.assertEqual(externalConditions.getT(), 3.5)
        self.assertEqual(type(externalConditions.getT()), float)
        self.assertEqual(externalConditions.getH(), 2.8)
        self.assertEqual(type(externalConditions.getH()), float)


    def test_type_casting_in_constructor(self):
        externalConditions=ExternalConditions(T=3, H=2)

        self.assertEqual(externalConditions.getT(), 3)
        self.assertEqual(type(externalConditions.getT()), float)
        self.assertEqual(externalConditions.getH(), 2)
        self.assertEqual(type(externalConditions.getH()), float)


    def test_setters(self):
        externalConditions=ExternalConditions(T=3.5, H=2.8)

        externalConditions.setT(4)
        self.assertEqual(externalConditions.getT(), 4.0)
        self.assertEqual(type(externalConditions.getT()), float)
        externalConditions.setH(5)
        self.assertEqual(externalConditions.getH(), 5.0)
        self.assertEqual(type(externalConditions.getH()), float)


if __name__ == '__main__':
    unittest.main()
