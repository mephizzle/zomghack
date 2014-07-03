ZOMGHack, the exception-gobbling function manipulator
=====================================================


**Warning:** This module is highly experimental, and will likely break your code at this stage of development. It involves some unholy python voodoo at best, and it is at a proof-of-concept stage.

What it does
------------

Let's say you have a function:

    def foo():
        print 1
        1 / 0
        print 2

When you call it, it will print the value 1, and then proceed to raise an exception. Generally, this is exactly what we all want. However, there may be some cases where we want to know about an exception, and continue executing the rest anyway. Or maybe we don't want that. Either way, this module experiments with a way to implement this.

Usage
-----

Given the above example, it can be modified as such:

    from hack import hack_function

    @hack_function
    def foo():
        print 1
        1 / 0
        print 2

Presto!
