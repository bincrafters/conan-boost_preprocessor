#!/usr/bin/env python
# -*- coding: utf-8 -*-

from conans import python_requires


base = python_requires("boost_base/1.68.0@bincrafters/stable")

class BoostPreprocessorConan(base.BoostBaseConan):
    name = "boost_preprocessor"
    url = "https://github.com/bincrafters/conan-boost_preprocessor"
    lib_short_names = ["preprocessor"]
    header_only_libs = ["preprocessor"]
