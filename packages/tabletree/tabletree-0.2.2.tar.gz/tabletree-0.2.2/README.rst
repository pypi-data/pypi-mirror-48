=========
tabletree
=========


Python package for exploring and linking multiple SQL-like tables

Description
===========

This package will link multiple SQL-tables together to facilitate (potentially large-scale) analysis of data from various sources. All tables are implemented using Pandas Data.Frame objects.


Examples
========

.. code-block:: python

    tab1_list = list( zip([1,2,3,4], ['M', 'F', 'M', 'F'] ) )
    tab2_list = list( zip(  [1,2,3,4], ['red', 'green', 'yellow', 'blue'] ) )
    tab1 = pd.DataFrame( tab1_list,   columns = ['tab1_v1', 'tab1_v2'])
    tab2 = pd.DataFrame( tab2_list,   columns = ['tab2_v1', 'tab2_v2'])
    tn1 = TableNode('sex', tab1)
    tn2 = TableNode('preference', tab2)
    ttree = TableTree(tn1)
    ttree.addChildren(tn2, TableLink('tab1_v1', 'tab2_v1'))
    ttree.findMatched('preference', 'sex', tn1.df.tab1_v2 == 'M')


Note
====

Github: https://github.com/rluo/tabletree
