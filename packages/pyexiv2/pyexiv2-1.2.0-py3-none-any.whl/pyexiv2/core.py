# -*- coding: utf-8 -*-
import ctypes
import json
import os
import sys


dll_dir = os.path.join(os.path.dirname(__file__), "lib")
SEP = "\t"  # separator
EOL = "<<SEPARATOR>>\n"  # end of line

if sys.platform.startswith("linux"):
    ctypes.CDLL(os.path.join(dll_dir, "libexiv2.so"))  # import it at first
    api = ctypes.CDLL(os.path.join(dll_dir, "api.so"))
    # Unicode characters need to be handled, because char array can only contain ASCII characters.
    ENCODING = "utf-8"
elif sys.platform.startswith("win"):
    ctypes.CDLL(os.path.join(dll_dir, "exiv2.dll"))
    api = ctypes.CDLL(os.path.join(dll_dir, "api.dll"))
    ENCODING = "gbk"
else:
    raise RuntimeError(
        "Unknown platform. This module should run on Windows or Linux systems.")


class Image:
    """ Call the public methods and properties of this class. """

    def __init__(self, filename):
        self.filename = filename.encode(ENCODING)

    def read_exif(self):
        """ returns a dict """
        self._open_image()
        return self._read_exif()

    def read_iptc(self):
        """ returns a dict """
        self._open_image()
        return self._read_iptc()

    def read_xmp(self):
        """ returns a dict """
        self._open_image()
        return self._read_xmp()

    def read_all(self):
        """ read all the metadata(including EXIF, IPTC, XMP). """
        self._open_image()
        _dict = {"EXIF": self._read_exif(),
                 "IPTC": self._read_iptc(),
                 "XMP": self._read_xmp()
                 }
        return _dict

    def clear_exif(self):
        """ Once cleared, you may not be able to modify it. """
        self._open_image()
        self._clear_exif()

    def clear_iptc(self):
        """ Once cleared, you may never recover it. """
        self._open_image()
        self._clear_iptc()

    def clear_xmp(self):
        """ Once cleared, you will never be able to modify it.
        Because the data about "history" was deleted. """
        self._open_image()
        self._clear_xmp()

    def clear_all(self):
        """ Once cleared, you may never recover it. """
        self._open_image()
        self._clear_exif()
        self._clear_iptc()
        self._clear_xmp()

    def modify_exif(self, exif_dict):
        self._open_image()
        self._modify_exif(exif_dict)

    def modify_iptc(self, iptc_dict):
        self._open_image()
        self._modify_iptc(iptc_dict)

    def modify_xmp(self, xmp_dict):
        """ Keys that cannot be modified: 
         - "Xmp.xmpMM.History"
        """
        self._open_image()
        self._modify_xmp(xmp_dict)

    def modify_all(self, all_dict):
        """ all_dict = {"EXIF":{...}, "IPTC":{...}, "XMP":{...}} """
        self._open_image()
        self._modify_exif(all_dict["EXIF"])
        self._modify_iptc(all_dict["IPTC"])
        self._modify_xmp(all_dict["XMP"])

    def _char_API_void(self, api_name):
        exec("api.{}.restype = ctypes.c_char_p".format(api_name))
        exec("ret = api.{}().decode()".format(api_name))
        exec("if ret != '0': raise RuntimeError(ret)")

    def _open_image(self):
        """ Let C++ program open an image and read its metadata,
        save as a global variable in C + +program. """
        api.open_image.restype = ctypes.c_char_p
        ret = api.open_image(self.filename).decode()
        if ret != '0':
            raise RuntimeError(ret)

    def _read_exif(self):
        """ call self._open_image() first """
        api.read_exif.restype = ctypes.c_char_p
        text = api.read_exif().decode()
        return self._loads(text)

    def _read_iptc(self):
        """ call self._open_image() first """
        api.read_iptc.restype = ctypes.c_char_p
        text = api.read_iptc().decode()
        return self._loads(text)

    def _read_xmp(self):
        """ call self._open_image() first """
        api.read_xmp.restype = ctypes.c_char_p
        text = api.read_xmp().decode()
        return self._loads(text)

    def _clear_exif(self):
        self._char_API_void("clear_exif")

    def _clear_iptc(self):
        self._char_API_void("clear_iptc")

    def _clear_xmp(self):
        self._char_API_void("clear_xmp")

    def _modify_exif(self, exif_dict):
        text = self._dumps(exif_dict)
        buffer = ctypes.create_string_buffer(text.encode())
        api.modify_exif.restype = ctypes.c_char_p
        ret = api.modify_exif(buffer).decode()
        if ret != '0':
            raise RuntimeError(ret)

    def _modify_iptc(self, iptc_dict):
        text = self._dumps(iptc_dict)
        buffer = ctypes.create_string_buffer(text.encode())
        api.modify_iptc.restype = ctypes.c_char_p
        ret = api.modify_iptc(buffer).decode()
        if ret != '0':
            raise RuntimeError(ret)

    def _modify_xmp(self, xmp_dict):
        text = self._dumps(xmp_dict)
        buffer = ctypes.create_string_buffer(text.encode())
        api.modify_xmp.restype = ctypes.c_char_p
        ret = api.modify_xmp(buffer).decode()
        if ret != '0':
            raise RuntimeError(ret)

    def _loads(self, text):
        if text.startswith("(Caught Exiv2 exception)"):
            raise RuntimeError(text)
        # _list = []  # save all the data
        _dict = {}  # only save the key and value
        lines = text.split(EOL)[:-1]  # the last line is empty
        for line in lines:
            # There are 3 fields: key, typeName, value
            # split with an exact count, watch out for extra '\t' in the last field
            fields = line.split(SEP, 2)
            # _list.append(fields)
            _dict[fields[0]] = fields[-1]
        return _dict

    def _dumps(self, dict_):
        text = ""
        for k, v in dict_.items():
            text += k + SEP + v + EOL
        return text
