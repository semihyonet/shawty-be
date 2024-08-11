import unittest

import parameterized

from app.utils.convert_base10_to_base58 import convert_base10_to_base58
from app.utils.convert_base58_to_base10 import convert_base58_to_base10


class UtilTest(unittest.TestCase):

    @parameterized.parameterized.expand([
        (0, '1'),
        (1, '2'),
        (5, '6'),
        (6, '7'),
        (15, 'G'),
        (16, 'H'),
        (17, 'J'),
        (18, 'K'),
        (19, 'L'),
        (43, 'k'),
        (44, 'm'),
        (57, 'z'),
        (58, '21'),
        (69, '2C'),
        (2468135791013, "27qMi57J")
    ])
    def test_encoding_base_58(self, num: int, expected: str):
        a = convert_base10_to_base58(num)

        self.assertEqual(a, expected)

    @parameterized.parameterized.expand([
        ('1', 0),
        ('2', 1),
        ('6', 5),
        ('7', 6),
        ('G', 15),
        ('H', 16),
        ('J', 17),
        ('K', 18),
        ('L', 19),
        ('k', 43),
        ('m', 44),
        ('z', 57),
        ('21', 58),
        ('2C', 69),
        ("27qMi57J", 2468135791013)])
    def test_encoding_base_10_from_base_58(self, value: str, expected: int):
        a = convert_base58_to_base10(value)
        self.assertEqual(a, expected)

    @parameterized.parameterized.expand([
        (0,),
        (1,),
        (5,),
        (6,),
        (15,),
        (16,),
        (17,),
        (18,),
        (19,),
        (43,),
        (44,),
        (57,),
        (58,),
        (69,),
        (2468135791013,),
        (212312468135791013,),
        (522468135791013,),
        (2468135791013,)
    ])
    def test_encoding_back_and_forth(self, num: str):
        encoded = convert_base10_to_base58(num)
        decoded = convert_base58_to_base10(encoded)

        self.assertEqual(num, decoded)
