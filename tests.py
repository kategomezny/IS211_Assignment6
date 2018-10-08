#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""Testing and Refactoring"""



import unittest

from  conversions import convertCelsiusToKelv, convertKelvinToCelsius, convertKelvinToFarenheit, convertCelsiusToFahrenhe, convertFarenheitToCelsius, convertFarenheitToKelvin



class Test_convertCelsiusToKelv(unittest.TestCase):

    def test_CelsiusToKelvin(self):

        """Compares values and defines absolute zero"""

        self.assertAlmostEqual(convertCelsiusToKelv(40.00),313.15)

        self.assertAlmostEqual(convertCelsiusToKelv(-273.15),0.00)        

        

    def test_Values(self):

        """Makes sure Value Errors are raised when necessary"""

        self.assertRaises(ValueError, convertCelsiusToKelv, "hello")

        self.assertRaises(ValueError, convertCelsiusToKelv, 6j)

        self.assertRaises(ValueError, convertCelsiusToKelv, 40)

   

    

class Test_convertCelsiusToFahrenhe(unittest.TestCase):

    def test_CelsiusToFahrenhe(self):

        """Compares values and defines absolute zero"""

        self.assertAlmostEqual(convertCelsiusToFahrenhe(300.00),572.00)

        self.assertAlmostEqual(convertCelsiusToFahrenhe(0.00),32.00)      

        

    def test_Values(self):

        """Makes sure Value Errors are raised when necessary"""

        self.assertRaises(ValueError, convertCelsiusToKelv, "a string")

        self.assertRaises(ValueError, convertCelsiusToKelv, 10j)

        self.assertRaises(ValueError, convertCelsiusToKelv, 100)





class Test_convertFarenheitToCelsius(unittest.TestCase):

    def test_FarenheitToCelsius(self):

        """Compares values and defines absolute zero"""

        self.assertAlmostEqual(convertFarenheitToCelsius(932.00),500.00)

        self.assertAlmostEqual(convertFarenheitToCelsius(32.00),0.00)      

        

    def test_Values(self):

        """Makes sure Value Errors are raised when necessary"""

        self.assertRaises(ValueError, convertFarenheitToCelsius, "other string")

        self.assertRaises(ValueError, convertFarenheitToCelsius, 10j)

        self.assertRaises(ValueError, convertFarenheitToCelsius, 110)

        



class Test_convertFarenheitToKelvin(unittest.TestCase):

    def test_FarenheitToCelsius(self):

        """Compares values and defines absolute zero"""

        self.assertAlmostEqual(convertFarenheitToKelvin(536.00),553.15)

        self.assertAlmostEqual(convertFarenheitToKelvin(-459.67),0.00)      

        

    def test_Values(self):

        """Makes sure Value Errors are raised when necessary"""

        self.assertRaises(ValueError, convertFarenheitToKelvin, "one string")

        self.assertRaises(ValueError, convertFarenheitToKelvin, 2j)

        self.assertRaises(ValueError, convertFarenheitToKelvin, 50)

        

        

class Test_convertKelvinToFarenheit(unittest.TestCase):

    def test_KelvinToFarenheit(self):

        """Compares values and defines absolute zero"""

        self.assertAlmostEqual(convertKelvinToFarenheit(93.15),-292.00)

        self.assertAlmostEqual(convertKelvinToFarenheit(0.00),-459.67)      

        

    def test_Values(self):

        """Makes sure Value Errors are raised when necessary"""

        self.assertRaises(ValueError, convertKelvinToFarenheit, "apple")

        self.assertRaises(ValueError, convertKelvinToFarenheit, 7j)

        self.assertRaises(ValueError, convertKelvinToFarenheit, 3)

        

        

class Test_convertKelvinToCelsius(unittest.TestCase):

    def test_KelvinToCelsius(self):

        """Compares values and defines absolute zero"""

        self.assertAlmostEqual(convertKelvinToCelsius(353.15),80.00)

        self.assertAlmostEqual(convertKelvinToCelsius(0.00),-273.15)      

        

    def test_Values(self):

        """Makes sure Value Errors are raised when necessary"""

        self.assertRaises(ValueError, convertKelvinToCelsius, "orange")

        self.assertRaises(ValueError, convertKelvinToCelsius, 20j)

        self.assertRaises(ValueError, convertKelvinToCelsius, 12)
