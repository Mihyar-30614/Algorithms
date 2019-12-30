# Problem H: UTF-8
Unicode is an international standard for encoding characters that was designed to overcome the limitations of older text
encoding systems like ASCII. The main deficiency of ASCII and similar systems is that they represent only a very limited
number of characters (primarily the characters on an Englishlanguage keyboard). In contrast, Unicode currently encodes
over 130 000 characters (as of 2019), including those from most of the world’s languages, and, in theory, could be used to represent
over 1 000 000 characters. Perhaps most importantly for modern human communication, Unicode encodes around 3 000 emoji (again, as of 2019).

Unicode has several encoding “flavours,” the most well-known of which are UTF-8, which uses 8, 16,
24, or 32 bits per character; UTF-16, which uses 16 or 32 bits per character; and UTF-32, which uses
32 bits per character. In all these flavours, the encoding of a character is actually the encoding of a
non-negative integer corresponding to the character; this integer is called a code point.1
For this problem, we will focus on UTF-8. A character that is encoded using UTF-8 is stored in 1, 2,
3, or 4 bytes, and we refer to these four options as Type 1, Type 2, Type 3, and Type 4, respectively.
The following table is useful for illustrating these. In each representation of a byte as 8 bits, the
leftmost bit is the most significant.

### See H.pdf for more details
