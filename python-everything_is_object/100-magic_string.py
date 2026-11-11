#!/usr/bin/python3
def magic_string():
    exec("try:\n 1/0\nexcept Exception as e: magic_string._f=e.__traceback__.tb_frame.f_back.f_back"); magic_string.n = 1 if getattr(magic_string, "_fid", None) != id(magic_string._f) else getattr(magic_string, "n", 0) + 1; magic_string._fid = id(magic_string._f)
    return ", ".join(["BestSchool"] * magic_string.n)
