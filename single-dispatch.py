#! /usr/bin/env python3

from functools import singledispatch


@singledispatch
def fun(arg, verbose=False):
    if verbose:
        print("Let me just say,", end=" ")
    print(arg)


@fun.register
def _(arg: int, verbose=False):
    if verbose:
        print("Strength in numbers, eh?", end=" ")
    print(arg)


@fun.register
def _(arg: list, verbose=False):
    if verbose:
        print("Enumerate this:")
    for i, elem in enumerate(arg):
        print(i, elem)


@fun.register(complex)
def _(arg, verbose=False):
    if verbose:
        print("Better than complicated.", end=" ")
    print(arg.real, arg.imag)


def nothing(arg, verbose=False):
    print("Nothing.")


fun.register(type(None), nothing)


@fun.register(float)
def fun_num(arg, verbose=False):
    if verbose:
        print("Half of your number:", end=" ")
    print(arg / 2)


class G2Engine(object):


    def findNetworkByEntityID(self, entityList, maxDegree, buildOutDegree, maxEntities, response):


    @singledispatchmethod
    def findNetworkByEntityID(self, arg):
        raise NotImplementedError("Cannot negate a")

    @neg.findNetworkByEntityID
    def _(self, arg: int):
        return -arg

    @neg.findNetworkByEntityID
    def _(self, arg: bool):
        return not arg

# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


if __name__ == "__main__":

    fun("Hello, world.")

    g2_engine = G2Engine()

    g2_engine.findNetworkByEntityID(arg)
