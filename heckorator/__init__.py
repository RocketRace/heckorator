from __future__ import annotations
import functools
from inspect import currentframe
from typing import Any, overload

__all__ = ("_",)

class heck:
    '''heck wow'''

    def __init__(self, bits: int, width: int, font_data: tuple[int, int, dict[int, str]], target: Any = None, stack: tuple[tuple[int, int], ...] = (), /) -> None:
        '''heck anew'''
        self.font_data = font_data
        self.bits = bits
        self.width = width
        self.target = target
        self.stack = stack

    @property
    def _(self) -> heck:
        '''heck 0'''
        return heck(self.bits << 1, self.width + 1, self.font_data)
    
    def __matmul__(self, other: heck) -> heck:
        '''heck 1'''
        return heck((((self.bits << 1) | 1) << other.width) | other.bits, self.width + 1 + other.width, self.font_data)
    
    @overload
    def __call__(self, other: heck) -> heck:
        ...
    
    @overload
    def __call__(self, other: Any) -> Any:
        ...

    def __call__(self, other: Any) -> Any:
        '''heck newline'''
        if isinstance(other, heck):
            if self.bits == (1 << self.width) - 1:
                # highest row
                matrix = [
                    [int(c == "1") for c in f"{row:0{width}b}"]
                    for (row, width) in ((self.bits, self.width), *other.stack)
                ]
                
                assert len(set(len(row) for row in matrix)) == 1, "all rows must be of equal length"
                
                assertion = "the decorator must have a pretty border"
                assert len(matrix) > 4, assertion # a 1 pixel high font is technically fine
                assert len(matrix[0]) >= 3, assertion # check for empty rows later
                assert all(row[-1] == 1 for row in matrix), assertion
                assert all(row[-2] == 0 for row in matrix[1:-1]), assertion
                assert all(row[0] == 0 for row in matrix[1:-1]), assertion
                assert all(bit == 1 for bit in matrix[0]), assertion
                assert all(bit == 0 for bit in matrix[1][:-1]), assertion
                assert all(bit == 0 for bit in matrix[-2][:-1]), assertion
                assert all(bit == 1 for bit in matrix[-1]), assertion
                
                assert len(matrix[0]) > 3, "rows must not be empty"
                
                cropped = [row[1:-2] for row in matrix[2:-2]]

                glyph_width, glyph_height, char_table = self.font_data
                
                assert all(
                    all(bit == 0 for bit in row)
                    for row in cropped[glyph_height :: glyph_height + 1]
                ), "all rows of text must be separated by a row of spaces"
                
                assert all(
                    all(bit == 0 for bit in row[glyph_width :: glyph_width + 1])
                    for row in cropped
                ), "all columns of text must be separated by a column of spaces"

                sliced = [
                    [
                        [
                            row[x : x + glyph_width]
                            for x in range(0, len(row), glyph_width + 1)
                        ]
                        for row in chunk
                    ]
                    for chunk in [
                        cropped[y : y + glyph_height]
                        for y in range(0, len(cropped), glyph_height + 1)
                    ]
                ]

                indexed = [
                    [
                        [row[x] for row in sliced[y]]
                        for x in range(len(sliced[0][0]))
                    ]
                    for y in range(len(sliced))
                ]

                bitmasks = [
                    [
                        functools.reduce(
                            lambda x, y: (x << 1) | y,
                            [
                                bit
                                for char_row in char
                                for bit in char_row
                            ]
                        )
                        for char in row
                    ]
                    for row in indexed
                ]

                text: list[str] = []
                for row in bitmasks:
                    chars: list[str] = []
                    for bitmask in row:
                        char = char_table.get(bitmask)
                        assert char, (
                            f"the current font doesn't have a character for the bitmask {bitmask:0{glyph_height * glyph_width}b}"
                        )
                        chars.append(char)
                    text.append("".join(chars))

                fns: list[Any] = []
                for line in text:
                    frame = currentframe()
                    assert frame, "sys._getframe is disabled"
                    last = frame.f_back
                    assert last, "you've got a fricked up sys._getframe implementation"
                    fns.append(eval(line, last.f_globals, last.f_locals))
                
                return functools.reduce(lambda x, y: y(x), fns[::-1], other.target)
            else:
                # middle row
                return heck(0, 0, other.font_data, other.target, ((self.bits, self.width), *other.stack))
        else:
            # lowest row
            return heck(0, 0, self.font_data, other, ((self.bits, self.width),))

    def font(self, path: str) -> None:
        '''heck font'''
        self.font_data = _decode_font(path)

def _decode_font(path: str) -> tuple[int, int, dict[int, str]]:
    return (
        4, 10,
        {
            160864512: "x",
            126230016: "s",
            430642054214: "[",
            28349142528: "0",
            421479457318: "]",
            512: ".",
            110728704: "o",
            244947200: "n",
        }
    )

_ = heck(0, 0, _decode_font("creep"))
