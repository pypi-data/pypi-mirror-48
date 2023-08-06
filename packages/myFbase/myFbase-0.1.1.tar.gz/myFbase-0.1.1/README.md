# myFbase

Change to/from any base you like: hexadecimal, binary or whatever you want.

## How to use

### Installation

    $ pip install myFbase

### Usage

    from myFbase import MyFbase

    mfb = MyFbase('abc')
    print(mfb.encode(8))  # cc
    print(mfb.decode('cc'))  # 8

    mfb = MyFbase('0123456789ABCDEF')  # Hex base
    print(mfb.encode(15))  # F
    print(mfb.encode(16))  # 10
    print(mfb.encode(4294967295))  # FFFFFFFF
