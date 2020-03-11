# DO NOT MERGE _test_get_groups.py WITH THE MAIN PANDAS REPO!!!
# DO NOT MERGE _test_get_groups.py WITH THE MAIN PANDAS REPO!!!
# DO NOT MERGE _test_get_groups.py WITH THE MAIN PANDAS REPO!!!

# run with python3 _test_get_groups.py 

import unittest

from pandas import DataFrame
from pandas.testing import assert_frame_equal


class _test_get_groups(unittest.TestCase):
    def test_single_row_valid(self):
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

    def test_discovered_invalid(self):
        df = DataFrame(data={
            'A': ['a1', 'a2', None],
            'B': ['b1', 'b2', 'b1'],
            'val': [1, 2, 3],
        })
        grps = df.groupby(by=['A', 'B'])
        self.assertRaises(KeyError, grps.get_group, ('a1', 'b2'))
