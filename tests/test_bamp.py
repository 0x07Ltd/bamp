from unittest import TestCase

from bamp import bamp


class BampTest(TestCase):

    def test_get_prefix_suffix(self):
        """
        Should return the prefix and suffix of the given line if it contains the given version, else
        returns None, None.
        """
        version = "1.2.3"
        data = (
            ("This is the first line", (None, None)),
            ("version = 1.2.3", ("version = ", "")),
            ("The version is 1.2.3 right now", ("The version is ", " right now"))
        )
        for inpt, outpt in data:
            self.assertEqual(bamp.get_prefix_suffix(version, inpt), outpt)

    def test_get_version_lines(self):
        """
        Should find all occurences of the version number in the given list of strings and return the
        prefixes and suffixes as a dictionary of tuples with the (1 based) line numbers as keys.
        """
        version = "1.2.3"
        lines = [
            "This is the first line",
            "This is the second line",
            "version = 1.2.3",
            "The version is 1.2.3 right now",
            "This is the fifth line"
        ]
        vlines = bamp.get_version_lines(version, lines)
        self.assertEqual(vlines, {
            3: ("version = ", ""),
            4: ("The version is ", " right now")
        })
