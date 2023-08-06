#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Copyright (C) 2019  David Arroyo Menéndez

# Author: David Arroyo Menéndez <davidam@gnu.org>
# Maintainer: David Arroyo Menéndez <davidam@gnu.org>

# This file is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.

# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Damegender; see the file LICENSE.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street, Fifth Floor,
# Boston, MA 02110-1301 USA,

import unittest
import os
from app.dame_genderapi import DameGenderApi


class TddInPythonExample(unittest.TestCase):

    # def test_dame_genderapi_get_method_returns_correct_result(self):
    #     dga = DameGenderApi()
    #     if (dga.config['DEFAULT']['genderapi'] == 'yes'):
    #         v = dga.get("Diana")
    #         self.assertEqual(v[0], "female")
    #         self.assertTrue(v[1] > 90)
    #         self.assertEqual(len(v), 2)

    # def test_dame_genderapi_guess_method_returns_correct_result(self):
    #     dga = DameGenderApi()
    #     if (dga.config['DEFAULT']['genderapi'] == 'yes'):
    #         g = dga.guess("Sara", binary=False)
    #         self.assertEqual(g, "female")
    #         g = dga.guess("Paula", binary=False)
    #         self.assertEqual(g, "female")
    #         g = dga.guess("Sara", binary=True)
    #         self.assertEqual(g, 0)

    def test_dame_genderapi_download_method_returns_correct_result(self):
        dga = DameGenderApi()
        if (dga.config['DEFAULT']['genderapi'] == 'yes'):
            g = dga.download(path="files/names/partial.csv")
            self.assertTrue(os.path.isfile("files/names/genderapi"+du.path2file(path)+".txt"))

    # def test_dame_genderapi_accuracy_method_returns_correct_result(self):
    #     dga = DameGenderApi()
    #     if (dga.config['DEFAULT']['genderapi'] == 'yes'):
    #         acc = dga.accuracy("Diana")
    #         self.assertTrue(acc > 90)


    # def test_dame_genderapi_guess_list_method_returns_correct_result(self):
    #     dga = DameGenderApi()
    #     if (dga.config['DEFAULT']['genderapi'] == 'yes'):
    #         self.assertEqual(['male', 'male', 'male', 'male', 'male', 'male', 'female', 'female', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'male', 'female', 'male', 'male'], dga.guess_list(path="files/names/partial.csv", binary=False))
    #         self.assertEqual([1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1], dga.guess_list(path="files/names/partial.csv",binary=True))

    # def test_dame_genderapi_confusion_matrix_dame_method_returns_correct_result(self):
    #     dga = DameGenderApi()
    #     cm = dga.confusion_matrix_dame(path="files/min.csv")
    #     am = [[5, 0, 0], [0, 2, 0]]
    #     self.assertEqual(cm,am)
