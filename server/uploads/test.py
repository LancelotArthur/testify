import unittest
from count import *
# import importlib
#
# count = importlib.import_module('count')

class TestCount(unittest.TestCase):

    # def setUp(self):

    # def tearDown(self):

    def loadFile(self, filename):

        with open(filename) as f:
            a = f.readline()
            b = [a.strip('\n').split(' ')]
            while a:
                a = f.readline()
                b.append(a.strip('\n').split(' '))

            del b[len(b) - 1]

            return b

    def test_boundary_basic(self):

        b = self.loadFile('test_boundary_basic.txt')

        for line in b:
            self.assertEqual(count([line[0], line[1], line[2]]), (line[3], line[4]))

    def test_boundary_robust(self):

        b = self.loadFile('test_boundary_robust.txt')

        for line in b:
            if line[len(line)-1] == 'IncompleteError':
                self.assertRaises(IncompleteError, count([line[0], line[1], line[2]]))
            elif line[len(line)-1] == 'OutOfRangeError':
                self.assertRaises(OutOfRangeError, count([line[0], line[1], line[2]]))
            else:
                self.assertEqual(count([line[0], line[1], line[2]]), (line[3], line[4]))

    def test_boundary_worstCase(self):

        b = self.loadFile('test_boundary_worstCase.txt')

        for line in b:
            self.assertEqual(count([line[0], line[1], line[2]]), (line[3], line[4]))

    def test_boundary_worstCaseRobust(self):

        b = self.loadFile('test_boundary_worstCaseRobust.txt')

        for line in b:
            if line[len(line)-1] == 'IncompleteError':
                self.assertRaises(IncompleteError, count([line[0], line[1], line[2]]))
            elif line[len(line)-1] == 'OutOfRangeError':
                self.assertRaises(OutOfRangeError, count([line[0], line[1], line[2]]))
            else:
                self.assertEqual(count([line[0], line[1], line[2]]), (line[3], line[4]))

    def test_robust(self):

        b = self.loadFile('test_robust.txt')

        for line in b:
            if line[len(line)-1] == 'ParaNumError':
                del line[len(line)-1]
                self.assertRaises(ParaNumError, count(line))
            elif line[len(line)-1] == 'ValueError':
                self.assertRaises(ValueError, count([line[0], line[1], line[2]]))
            else:
                self.assertEqual(count([line[0], line[1], line[2]]), (line[3], line[4]))
