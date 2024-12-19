# ------------------------------------------------------------------
# Copyright (c) 2022 PyInstaller Development Team.
#
# This file is distributed under the terms of the GNU General Public
# License (version 2.0 or later).
#
# The full license is available in LICENSE, distributed with
# this software.
#
# SPDX-License-Identifier: GPL-2.0-or-later
# ------------------------------------------------------------------

# The bundled 'data/' directory containing locale .json files needs to be collected (as data file).

from PyInstaller.utils.hooks import collect_data_files

datas = collect_data_files('mimesis')
