import unittest
import Toolbox.pH as tpH

import numpy as np

def test_bufferpH():
    assert np.isclose(tpH.bufferpH(0.1, 0.1, pka=4.75), 4.75), "Test Case 1 Failed"
    assert np.isclose(tpH.bufferpH(0.1, 0.1, Ka=10**-4.75), 4.75), "Test Case 2 Failed"
    assert np.isclose(tpH.bufferpH(0.1, 0.1, Kb=10**-9.25), 4.75), "Test Case 3 Failed"
    print("All bufferpH tests passed.")

def test_bufferconc():
    assert np.isclose(tpH.bufferconc(4.75, cb=0.1, pka=4.75), 0.1), "Test Case 1 Failed"
    assert np.isclose(tpH.bufferconc(4.75, ca=0.1, pka=4.75), 0.1), "Test Case 2 Failed"
    assert np.isclose(tpH.bufferconc(4.75, cb=0.1, Ka=10**-4.75), 0.1), "Test Case 3 Failed"
    assert np.isclose(tpH.bufferconc(4.75, ca=0.1, Kb=10**-9.25), 0.1), "Test Case 4 Failed"
    print("All bufferconc tests passed.")

def test_strongacidpH():
    assert np.isclose(tpH.strongacidpH(1.0), 0.0), "Test Case 1 Failed"
    print("All strongacidpH tests passed.")

def test_strongbasepH():
    assert np.isclose(tpH.strongbasepH(1.0), 14.0003), "Test Case 1 Failed"
    print("All strongbasepH tests passed.")

def test_strongacidconc():
    assert np.isclose(tpH.strongacidconc(1.0), 0.1), "Test Case 1 Failed"
    print("All strongacidconc tests passed.")

def test_strongbaseconc():
    assert np.isclose(tpH.strongbaseconc(pH=13.0), 0.1), "Test Case 1 Failed"
    print("All strongbaseconc tests passed.")

def test_weakacidpH():
    assert np.isclose(tpH.weakacidpH(0.1, Ka=10**-4.75), 2.87, atol=0.01), "Test Case 1 Failed"
    assert np.isclose(tpH.weakacidpH(0.1, pka=4.75), 2.87, atol=0.01), "Test Case 2 Failed"
    print("All weakacidpH tests passed.")

def test_weakbasepH():
    assert np.isclose(tpH.weakbasepH(0.1, Kb=10**-4.75), 11.13, atol=0.01), "Test Case 1 Failed"
    assert np.isclose(tpH.weakbasepH(0.1, pka=9.25), 11.13, atol=0.01), "Test Case 2 Failed"
    assert np.isclose(tpH.weakbasepH(0.1, Ka=10**-9.25), 11.13, atol=0.01), "Test Case 3 Failed"
    print("All weakbasepH tests passed.")

def test_weakacidconc():
    assert np.isclose(tpH.weakacidconc(2.87, Ka=10**-4.75), 0.1, atol=0.01), "Test Case 1 Failed"
    assert np.isclose(tpH.weakacidconc(2.87, pka=4.75), 0.1, atol=0.01), "Test Case 2 Failed"
    print("All weakacidconc tests passed.")

def test_weakbaseconc():
    assert np.isclose(tpH.weakbaseconc(11.13, Kb=10**-4.75), 0.1, atol=0.01), "Test Case 1 Failed"
    assert np.isclose(tpH.weakbaseconc(11.13, pka=9.25), 0.1, atol=0.01), "Test Case 2 Failed"
    assert np.isclose(tpH.weakbaseconc(11.13, Ka=10**-9.25), 0.1, atol=0.01), "Test Case 3 Failed"
    print("All weakbaseconc tests passed.")

if __name__ == "__main__":
    test_bufferpH()
    test_bufferconc()
    test_strongacidpH()
    test_strongbasepH()
    test_strongacidconc()
    test_strongbaseconc()
    test_weakacidpH()
    test_weakbasepH()
    test_weakacidconc()
    test_weakbaseconc()
