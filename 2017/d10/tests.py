#!/usr/bin/env python3

import unittest
from unittest import mock

from knothash import (
    get_input, get_number_list, convert_input_to_bytes, KnotHasher)


class TestImportFile(unittest.TestCase):

    @mock.patch("builtins.open", create=True)
    def test_get_input(self, mock_open):
        mock_open.side_effect = [
            mock.mock_open(read_data="Data1").return_value,
            mock.mock_open(read_data="Data2").return_value
        ]

        self.assertEqual("Data1", get_input("fileA"))
        mock_open.assert_called_once_with("fileA")
        mock_open.reset_mock()

        self.assertEqual("Data2", get_input("fileB"))
        mock_open.assert_called_once_with("fileB")


class TestStringConverters(unittest.TestCase):

    def test_splitting_string_into_number_list(self):
        strings_and_lengths = {
            "":        [],
            "1, 2, 3": [1, 2, 3],
            "1,2,3":   [1, 2, 3],
            " 1, 2,3": [1, 2, 3]
        }
        for string, lengths in strings_and_lengths.items():
            self.assertEqual(lengths, get_number_list(string))

    def test_converter(self):
        input_bytes = convert_input_to_bytes("")
        self.assertEqual([17,31,73,47,23], input_bytes)

        input_bytes = convert_input_to_bytes("1,2,3")
        self.assertEqual([49,44,50,44,51,17,31,73,47,23], input_bytes)

        input_bytes = convert_input_to_bytes("1,2,33")
        self.assertEqual([49,44,50,44,51,51,17,31,73,47,23], input_bytes)



class TestKnotHasher(unittest.TestCase):

    def test_init(self):
            knothasher = KnotHasher([1, 2, 3], 5)
            self.assertEqual([1, 2, 3], knothasher.lengths)
            self.assertEqual([0, 1, 2, 3, 4], knothasher.string)
            self.assertEqual(0, knothasher.string_position)
            self.assertEqual(0, knothasher.lengths_position)

    def test_reverse(self):
        tests = [
            (0, 0, [0, 1, 2, 3, 4]),
            (1, 1, [0, 1, 2, 3, 4]),
            (2, 2, [0, 1, 3, 2, 4]),
            (3, 3, [2, 1, 3, 0, 4]),
            (4, 2, [4, 1, 3, 0, 2])
        ]

        knothasher = KnotHasher([], 5)
        for start, length, result in tests:
            knothasher.reverse(start, length)
            self.assertEqual(result, knothasher.string)

    def test_advance(self):
        knothasher = KnotHasher([3, 4, 1, 5], 5)

        positions = [
            (1, 3),
            (2, 3),
            (3, 1),
            (0, 4),
            (1, 0)
        ]

        for n in range(len(knothasher.lengths)):
            knothasher.advance()
            self.assertEqual(
                positions[n],
                (knothasher.lengths_position, knothasher.string_position)
            )

    @mock.patch("knothash.KnotHasher.advance", create=True)
    def test_hash_calls_advance(self, knothasher_advance):
        knothasher = KnotHasher([3, 4, 1, 5], 5)
        knothasher.hash()

        self.assertEqual(4, len(knothasher_advance.call_args_list))

    @mock.patch("knothash.KnotHasher.reverse", create=True)
    def test_solve_calls_reverse(self, knothasher_reverse):
        knothasher = KnotHasher([3, 4, 1, 5, 2], 5)
        knothasher.hash()

        expected_calls = [
            (0, 3),
            (3, 4),
            (3, 1),
            (1, 5),
            (4, 2)
        ]

        self.assertEqual(
            expected_calls,
            [args for (args, _) in knothasher_reverse.call_args_list]
        )


    def test_hash(self):
        knothasher = KnotHasher([3, 4, 1, 5], 5)
        knothasher.sparse_hash()
        hashed = knothasher.string
        self.assertEqual([3, 4, 2, 1, 0], hashed)
        self.assertEqual(4, knothasher.skip_size)
        self.assertEqual(4, knothasher.string_position)

        knothasher = KnotHasher([3, 4, 1, 5, 2], 5)
        knothasher.sparse_hash()
        hashed = knothasher.string
        self.assertEqual([0, 4, 2, 1, 3], hashed)
        self.assertEqual(5, knothasher.skip_size)
        self.assertEqual(0, knothasher.string_position)

    def test_hash_multiple_rounds(self):
        knothasher1 = KnotHasher([3, 4, 1, 5], 5)
        knothasher1.sparse_hash()
        knothasher1.sparse_hash()

        knothasher2 = KnotHasher([3, 4, 1, 5], 5)
        hashed = knothasher2.hash(2)

        self.assertEqual(knothasher1.string, hashed)

    def test_dense_hash(self):
        inputs = [
            ("", "a2582a3a0e66e6e86e3812dcb672a272"),
            ("AoC 2017", "33efeb34ea91902bb2f59c9920caa6cd"),
            ("1,2,3", "3efbe78a8d82f29979031a4aa0b16a9d"),
            ("1,2,4", "63960835bcdc130f0b66d7ff4f6a5a8e")
        ]
        for text, answer in inputs:
            b = convert_input_to_bytes(text)
            knothasher = KnotHasher(b, 256)
            self.assertEqual(
                answer,
                knothasher.hash(64, True)
            )

    def test_hex(self):
        knothasher = KnotHasher([], 256)
        self.assertEqual(knothasher.hex(64), "40")
        self.assertEqual(knothasher.hex(7), "07")
        self.assertEqual(knothasher.hex(255), "ff")



if __name__ == '__main__':
    unittest.main()
