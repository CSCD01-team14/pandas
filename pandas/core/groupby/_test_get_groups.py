# DO NOT MERGE _test_get_groups.py WITH ACTUAL PANDAS 
# DO NOT MERGE _test_get_groups.py WITH ACTUAL PANDAS 
# DO NOT MERGE _test_get_groups.py WITH ACTUAL PANDAS 

import unittest

from pandas import DataFrame
from pandas.testing import assert_frame_equal
import numpy as np

class _test_get_groups(unittest.TestCase):
    def test_cero_discovered_invalid(self):
        df = DataFrame(data={
            'A': ['a1', 'a2', None],
            'B': ['b1', 'b2', 'b1'],
            'val': [1, 2, 3],
        })
        grps = df.groupby(by=['A', 'B'])
        self.assertRaises(KeyError, grps.get_group, ('a1', 'b2'))

    def test_uno_single_row_valid(self):
        df = DataFrame(data={
            'A': ['a1', 'a2', None],
            'B': ['b1', 'b2', 'b1'],
            'val': [1, 2, 3],
        })
        expected = DataFrame(data={
            'A': ['a1'],
            'B': ['b1'],
            'val': [1,],
        })
        grps = df.groupby(by=['A', 'B'])
        assert_frame_equal(grps.get_group(('a1', 'b1')), expected)

    def test_dos_alternate_invalid(self):
        df = DataFrame(data={
            'A': ['a1', 'a2', None],
            'B': ['b1', 'b2', 'b1'],
            'val': [1, 2, 3],
        })
        grps = df.groupby(by=['A', 'B'])
        self.assertRaises(KeyError, grps.get_group, ('a2', 'b1'))

    def test_tres_double_row_valid(self):
        df = DataFrame(data={
            'A': ['a1', 'a2', None],
            'B': ['b1', 'b2', 'b1'],
            'val': [1, 2, 3],
        })
        expected = DataFrame(data={
            'A': ['a1', None],
            'B': ['b1', 'b1'],
            'val': [1, 3],
        })
        grps = df.groupby(by=['B'])
        self.assertEqual(True, np.array_equal(grps.get_group(('b1')).values, expected.values))

    def test_cuatro_expect_empty(self):
        df = DataFrame(data={
            'A': ['a1', 'a2', None],
            'B': ['b1', 'b2', 'b1'],
            'val': [1, 2, 3],
        })
        grps = df.groupby(by=['B'])
        self.assertRaises(KeyError, grps.get_group, ('b3'))

    def test_cinco_double_row_valid(self):
        df = DataFrame({'Animal': ['Falcon', 'Falcon',
                                   'Parrot', 'Parrot'],
                        'Max Speed': [380., 370., 24., 26.],
                        'bullshit': ['a', 'b', 'c', 'd']})
        expected = DataFrame({'Animal': ['Falcon', 'Falcon'],
                        'Max Speed': [380., 370.],
                        'bullshit': ['a', 'b']})
        grps = df.groupby(['Animal'])
        assert_frame_equal(grps.get_group(('Falcon')), expected)



if __name__ == '__main__':
    unittest.main()
