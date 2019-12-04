#!/usr/bin/env python
# coding: utf-8

# In[2]:


import unittest
def add(x, y):
    """Add Function"""
    return x + y
def subtract(x,y):
    """Subtract Function"""
    return x - y
def multiply(x, y):
    """Multiply Function"""
    return x * y
def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError ('Can not divide by zero!')
    return x / y


# In[3]:


class TestCalc(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(3, 3), 6)
    def test_subtract(self):
        self.assertEqual(subtract(6, 3), 3)
    def test_multiply(self):
        self.assertEqual(multiply(2, 2), 4)
    def test_divide(self):
        self.assertEqual(divide(4, 2), 2)


# In[4]:


unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:




