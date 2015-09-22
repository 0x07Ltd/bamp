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
        prefixes and suffixes as a dictionary of tuples with the (0 based) line numbers as keys.
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
            2: ("version = ", ""),
            3: ("The version is ", " right now")
        })

    def test_get_version_lines_first_line_number(self):
        """
        Should return line numbers starting from the supplied `first_line_number`.
        """
        version = "1.2.3"
        lines = [
            "This is the first line",
            "This is the second line",
            "version = 1.2.3",
            "The version is 1.2.3 right now",
            "This is the fifth line"
        ]
        vlines = bamp.get_version_lines(version, lines, first_line_number=10)
        self.assertEqual(vlines, {
            12: ("version = ", ""),
            13: ("The version is ", " right now")
        })

    def test_replace_versions(self):
        """
        Should replace all occurences of the old version with `newversion` in `lines`.
        """
        version = "1.2.3"
        newversion = "1.2.4"
        lines = [
            "This is the first line",
            "This is the second line",
            "version = 1.2.3",
            "The version is 1.2.3 right now",
            "This is the fifth line"
        ]
        vlines = bamp.get_version_lines(version, lines)
        replaced = list(bamp.replace_versions(newversion, lines, vlines))
        self.assertEqual(replaced[2], "version = %s" % newversion)
        self.assertEqual(replaced[3], "The version is %s right now" % newversion)
