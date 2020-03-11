import unittest

from pandas import DataFrame
from pandas.testing import assert_frame_equal
import numpy as np

#
# # df = DataFrame({'Animal': ['Falcon', 'Falcon',
# #                               'Parrot', 'Parrot'],
# #                    'Max Speed': [380., 370., 24., 26.],
# #                 'bullshit': ['a', 'b', 'c', 'd']})
# #
# # print(df)
# # grps = df.groupby(['Animal'])
# # print(_GroupBy.get_group(grps, ('Falcon')))
# # print("=====")
# # i = 0
# # for key, item in grps:
# #     print(i)
# #     i +=1
# #     print(key)
# #     print(_GroupBy.get_group(grps, key))
# # print(grps)
# # print(grps.mean())
# # print("=====")
#
# d = {
#             "cat": pd.Categorical(
#                 ["a", "b", "a", "b"], categories=["a", "b", "c"], ordered=True
#             ),
#             "ints": [1, 1, 2, 2],
#             "val": [10, 20, 30, 40],
#         }
#         df = pd.DataFrame(d)

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


if __name__ == '__main__':
    unittest.main()
