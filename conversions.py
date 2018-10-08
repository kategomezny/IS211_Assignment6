#!/usr/bin/env python

# -*- coding: utf-8 -*-

"""Temperature conversions"""





def convertCelsiusToKelv(C):

    """Converts Celsius to Kelvin

    

    Args:

        C(int):   Celisus degree

        

    Return:

        K(int):  Kelvin degree

        

    Example:  

        In [10]:  convertCelsiusToKelv(40.00)

        Out[10]:  313.15

    """

    if isinstance(C, str) == True:

        raise ValueError("Celsius cannot be a string value")

    if isinstance(C,complex) == True:

        raise ValueError("Celsius cannot be a complex value")

    if isinstance(C,int) == True:

        raise ValueError("Celsius should be a float value, example: 40.00")

           

        

    K = C + 273.15

    return K 





def convertCelsiusToFahrenhe(C):

    """Converts Celsius to Farenheit

    

    Args:

        C(float): Celsius degree

        

    Return

        F(float):Farenheit degrees.

        

    Example:

        In[7]:  convertCelsiusToFahrenhe(21.50)

        Out[7]: 70.7

    """

    if isinstance(C, str) == True:

        raise ValueError("Celsius cannot be a string value")

    if isinstance(C,complex) == True:

        raise ValueError("Celsius cannot be a complex value")

    if isinstance(C,int) == True:

        raise ValueError("Celsius should be a float value, example: 90.00")

        

    F = (9.0/5.0 * C + 32.0)

    return F



def convertFarenheitToCelsius(F):

    """Converts Farenheit to Celsius.

    

    Args:

        F(float): Farenheit degree

        

    Return

        C(float):Celsius degrees.

        

    Example:

        convertFarenheitToCelsius(60.00)

        Out[41]: 15.555555555555555

        

    """

    if isinstance(F, str) == True:

        raise ValueError("Farenheit cannot be a string value")

    if isinstance(F,complex) == True:

        raise ValueError("Farenheit cannot be a complex value")

    if isinstance(F,int) == True:

        raise ValueError("Farenheit should be a float value, example: 120.50")

    

    C = (F-32)/1.8

    return C

    



def convertFarenheitToKelvin(F):

    """Converts Farenheit to Kelvin.

    

    Args:

        F(float): Farenheit degree

        

    Return

        K(float):Kelvin degrees.

        

    Example:

        convertFarenheitToKelvin(250.00)

        Out[55]: 394.2611111111112

    """

    if isinstance(F, str) == True:

        raise ValueError("Farenheit cannot be a string value")

    if isinstance(F,complex) == True:

        raise ValueError("Farenheit cannot be a complex value")

    if isinstance(F,int) == True:

        raise ValueError("Farenheit should be a float value, example: 250.00")

        

    K = (F + 459.67)* 5/9

    return K





def convertKelvinToFarenheit(K):

    """Converts  Kelvin to Farenheit.

    

    Args:

        K(float): Kelvin degree

        

    Return

        F(float):Farenheit degrees.

        

    Example:

        convertKelvinToFarenheit(10.12)

        Out[69]: -441.454

    

    """

    if isinstance(K, str) == True:

        raise ValueError("Kelvin cannot be a string value")

    if isinstance(K,complex) == True:

        raise ValueError("Kelvin cannot be a complex value")

    if isinstance(K,int) == True:

        raise ValueError("Kelvin should be a float value, example: 320.00")

        

    F = (K * 9/5) - 459.67

    return F

    

    

def convertKelvinToCelsius(K):

    """Converts  Kelvin to Celsius.

    

    Args:

        K(float): Kelvin degree

        

    Return

        C(float):Celsius degrees.

        

    Example:

        convertKelvinToCelsius(173.15)

        Out[7]: -99.99999999999997        

    """

    if isinstance(K, str) == True:

        raise ValueError("Kelvin cannot be a string value")

    if isinstance(K,complex) == True:

        raise ValueError("Kelvin cannot be a complex value")

    if isinstance(K,int) == True:

        raise ValueError("Kelvin should be a float value, example: 50.00")

    

    C = K - 273.15

    return C

    




