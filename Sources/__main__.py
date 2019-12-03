"""
 =======================================================================================================
  HOI4 superset converter.
  Write better PDXScript and then run this program to get the regular, actually valid PDXScript code.
  I was thinking about writing this in C/C++, but nah, Python is easier.
  Licensed under the GNU GPL v3 license.
 =======================================================================================================
"""

import sys
import os
import io

# ================================

print("Welcome to Salty's HOI4 PDXScript++ converter!\n "
      "Please select the file for the script to convert to regular PDXScript.")

input_file_dir = str(
    input()
)

input_file_cont = open("input_file_dir", "r")
input_file_cont.read()

"""
 =====================================================================
  Start of actual file conversion.
  The full syntax of my new PDXScript++ can be found in Resources/SYNTAX.md.
  Still a TODO:
 =====================================================================
"""
