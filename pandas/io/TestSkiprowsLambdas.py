import unittest
import pandas as pd
from pandas import DataFrame
from pandas.testing import assert_frame_equal


class TestSkiprowsLambdas(unittest.TestCase):
    def test_single_column_equal(self):
        schema = {
            "show_id": int,
            "type": str,
            "title": str,
            "director": str,
            "cast": str,
            "country": str,
            "date_added": str,
            "release_year": int,
            "rating": str,
            "duration": str,
            "listed_in": str,
            "description": str,
        }
        mask = "(show_id == 70153404)"
        df = pd.read_csv("netflix_titles.csv", skiprows=mask)
        expected = DataFrame(
            data={
                "show_id": [70153404],
                "type": ["TV Show"],
                "title": [],
                "director": [],
                "cast": [
                    "Jennifer Aniston, Courteney Cox, Lisa Kudrow, Matt LeBlanc, Matthew Perry, David Schwimmer"
                ],
                "country": ["United States"],
                "date_added": [],
                "release_year": [2003],
                "rating": ["TV - 14"],
                "duration": ["10 Seasons"],
                "listed_in": ["Classic & Cult TV, TV Comedies"],
                "description": [
                    "This hit sitcom follows the merry misadventures of six 20-something pals as they navigate the pitfalls of work, life and love in 1990s Manhattan."
                ],
            }
        )
        assert_frame_equal(df, expected)

    def test_single_column_less_than(self):
        schema = {"country": str, "capital": str, "area": int, "population": int}
        mask = "(area > 8.516)"
        df = pd.read_csv("brics.csv", skiprows=mask)
        expected = DataFrame(
            data={
                "country": ["Russia", "China"],
                "capital": ["Moscow", "Beijing"],
                "area": [17.10, 9.597],
                "population": [143.5, 1357],
            }
        )
        print(df.reset_index(drop=True))
        print(expected)
        assert_frame_equal(df, expected)

    def test_single_column_greater_than(self):
        schema = {"country": str, "capital": str, "area": int, "population": int}
        mask = "(area < 8.516)"
        df = pd.read_csv("brics.csv", skiprows=mask)
        expected = DataFrame(
            data={
                "country": ["India", "South Africa"],
                "capital": ["New Delhi", "Pretoria"],
                "area": [3.286, 1.221],
                "population": [1252, 52.98],
            }
        )
        assert_frame_equal(df, expected)

    def test_multi_columns_and(self):
        schema = {"country": str, "capital": str, "area": int, "population": int}
        mask = "(area <= 8.516 and population > 1200)"
        df = pd.read_csv("brics.csv", skiprows=mask)
        expected = DataFrame(
            data={
                "country": ["India"],
                "capital": ["New Delhi"],
                "area": [3.286],
                "population": [1252.0],
            }
        )
        assert_frame_equal(df, expected)

    def test_multi_columns_or(self):
        schema = {"country": str, "capital": str, "area": int, "population": int}
        mask = "(area > 8.516 or area < 3.286)"
        df = pd.read_csv("brics.csv", skiprows=mask)
        expected = DataFrame(
            data={
                "country": ["Russia", "China", "South Africa"],
                "capital": ["Moscow", "Beijing", "Pretoria"],
                "area": [17.10, 9.597, 1.221],
                "population": [143.5, 1357.00, 52.98],
            }
        )
        assert_frame_equal(df, expected)


if __name__ == "__main__":
    unittest.main()
