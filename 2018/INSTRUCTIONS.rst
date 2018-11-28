===================
Using the templates
===================

Requires Python 3.6. No additional dependencies expected (hopefully).


1. Copy the templates
---------------------

Eg. for day 1::

    cd 2018
    python3 -m copy_templates day1


2. Set up the tests
-------------------

Edit ``day1/test_input.txt``, then in ``day1/tests.py`` change ``lorem ipsum!`` to the expected result in the following line::

    expected = "lorem ipsum!"


3. Create the solution
----------------------

Create the first solution in ``day1/solution1.py`` and update the ``solve`` function to call your code.


4. Run the test(s)
------------------

To run the tests for only the first solution::

    python3 -m day1.tests TestSolution1

To run for both solutions::

    python3 -m day1.tests


5. Solve the puzzle
-------------------

Add the input to ``day1/input.txt`` (kept in a separate file in case they're different).

If the solution requires a slightly different method to the test puzzle, edit the code below ``if __name__ == '__main__':`` in the solution to reflect this. For example, you may wish to give ``solve`` an optional additional parameter.

To generate the solution, run::

    python3 -m day1.solution1
