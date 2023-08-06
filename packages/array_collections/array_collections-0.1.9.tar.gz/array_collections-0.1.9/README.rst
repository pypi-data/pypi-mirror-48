=================
array_collections
=================

.. image:: http://img.shields.io/pypi/v/array_collections.svg?style=flat
   :target: https://pypi.python.org/pypi/array_collections
   :alt: Version_status
.. image:: http://img.shields.io/badge/docs-latest-brightgreen.svg?style=flat
   :target: https://array_collections.readthedocs.io/en/latest/
   :alt: Documentation
.. image:: http://img.shields.io/badge/license-MIT-blue.svg?style=flat
   :target: https://github.com/yoelcortes/array_collections/blob/master/LICENSE.txt
   :alt: license


.. contents::

What is array_collections?
--------------------------

array_collections is a collection of numpy ndarray subclasses. Each array class serves an unrelated but broad purpose of its own. This package features 3 types of arrays: material_array, tuple_array, and property_array.

Installation
------------

Get the latest version of array_collections from
https://pypi.python.org/pypi/array_collections/

If you have an installation of Python with pip, simple install it with:

    $ pip install array_collections

To get the git version, run:

    $ git clone git://github.com/yoelcortes/array_collections

Documentation
-------------

array_collections's documentation is available on the web:

    http://array_collections.readthedocs.io/

Getting started
---------------

A **material_array** issues a RuntimeWarning when a non-positive or non-finite value is encountered.

Create material_array:

.. code-block:: python
    
   >>> arr = material_array([1, 18])
   material_array([1, 18])
           
A negative value issues a RuntimeWarning:
           
.. code-block:: python
         
   >>> arr[1] = -1
   __main__:1: RuntimeWarning:
   Encountered negative or non-finite value in 'material_array' object.

New arrays are normal numpy arrays:

.. code-block:: python
         
   >>> arr + 1
   array([2, 19])

A **tuple_array** is an immutable and hashable array:

Create a tuple_array object:
            
.. code-block:: python
    
   >>> arr = tuple_array([1, 18])
   tuple_array([1, 18])
   
tuple_array objects are immutable:

.. code-block:: python
   
   >>> arr[1] = 0
   TypeError: 'tuple_array' objects are immutable.
            
tuple_array objects are hashable:

.. code-block:: python
            
   >>> hash(arr)
   3713080549427813581

New arrays are normal numpy arrays:

.. code-block:: python
         
   >>> arr + 1
   array([2, 19])
     
A **property_array** allows for array-like manipulation of property objects. All entries in a property_array must be instances of FreeProperty. Setting items of a property_array sets values of Property objects instead.

Use the PropertyFactory to create a Weight property class which calculates weight based on density and volume:
    
.. code-block:: python
        
   >>> from array_collections import PropertyFactory
   >>>        
   >>> @PropertyFactory
   >>> def Weight(self):
   ...    '''Weight (kg) based on volume (m^3).'''
   ...    data = self.data
   ...    rho = data['rho'] # Density (kg/m^3)
   ...    vol = data['vol'] # Volume (m^3)
   ...    return rho * vol
   >>>
   >>> @Weight.setter
   >>> def Weight(self, weight):
   ...    data = self.data
   ...    rho = data['rho'] # Density (kg/m^3)
   ...    data['vol'] = weight / rho
           
Create dictionaries of data and initialize new properties:
       
.. code-block:: python
       
   >>> water_data = {'rho': 1000, 'vol': 3}
   >>> ethanol_data = {'rho': 789, 'vol': 3}
   >>> weight_water = Weight('Water', water_data)
   >>> weight_ethanol = Weight('Ethanol', ethanol_data)
   >>> weight_water
   Weight(Water) -> 3000 (kg)
   >>> weight_ethanol
   Weight(Ethanol) -> 2367 (kg)
          
Create a property_array from data:
           
.. code-block:: python
       
   >>> prop_arr = property_array([weight_water, weight_water])
   property_array([3000, 2367])
           
Changing the values of a property_array changes the value of its properties:
           
.. code-block:: python
       
   >>> # Addition in place
   >>> prop_arr += 3000
   >>> prop_arr
   property_array([6000, 5367])
   >>> # Note how the data also changes
   >>> water_data
   {'rho': 1000, 'vol': 6.0}
   >>> ethanol_data
   {'rho': 789, 'vol': 6.802281368821292}
   >>> # Setting an item changes the property value
   >>> prop_arr[1] = 2367
   >>> ethanol_data
   {'rho': 789, 'vol': 3}
          
New arrays have no connection to the property_array:
           
.. code-block:: python
       
   >>> prop_arr - 1000 #  Returns a new array
   array([5000.0, 1367.0], dtype=object)
   >>> water_data #  Data remains unchanged
   {'rho': 1000, 'vol': 6.0}
      
A representative DataFrame can also be made from the property_array:
           
.. code-block:: python
       
   >>> prop_arr.table()
           Weight (kg)
   Water        6000.0
   Ethanol      2367.0
           
.. Note:: The DataFrame object contains the values of the properties, not the FreeProperty objects as a property_array would.

Latest source code
------------------

The latest development version of array_collections's sources can be obtained at:

    https://github.com/yoelcortes/array_collections


Bug reports
-----------

To report bugs, please use the array_collections' Bug Tracker at:

    https://github.com/yoelcortes/array_collections

License information
-------------------

See ``LICENSE.txt`` for information on the terms & conditions for usage
of this software, and a DISCLAIMER OF ALL WARRANTIES.

Although not required by the array_collections' license, if it is convenient for you,
please cite array_collections if used in your work. Please also consider contributing
any changes you make back, and benefit the community.


Citation
--------

To cite array_collections in publications use::

    Yoel Cortes-Pena (2019). array_collections: A collection of numpy ndarray subclasses.
    https://github.com/yoelcortes/array_collections
