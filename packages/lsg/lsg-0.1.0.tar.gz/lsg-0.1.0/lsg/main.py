#!/usr/bin/env python3
# -----------------------------------------------------------------------------
# Created: Sun  9 Jun 2019 23:45:18 IST
# Last-Updated: Wed 12 Jun 2019 11:41:16 IST
#
# lsg is part of dotfiles
# URL: https://gitlab.com/justinekizhak/dotfiles
# Description: Check if a specific file/s or folder/s exists in current or in a
# specified directory.
# This script started as an alias to `ls | grep FILENAME` but now its more
# flexible and robust than that.
#
# Copyright (c) 2019, Justine Kizhakkinedath
# All rights reserved
#
# Licensed under the terms of MIT License
# See LICENSE file in the project root for full information.
# -----------------------------------------------------------------------------
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
# DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
# OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE
# OR OTHER DEALINGS IN THE SOFTWARE.
#
# -----------------------------------------------------------------------------

import os
import argparse


def search(search_path, search_term):
    result = {'files': [], 'directories': [], 'links': []}
    for s_t in search_term:
        for entry in os.listdir(search_path):
            if s_t.lower() in entry.lower():
                full_path = os.path.join(search_path, entry)
                if os.path.isfile(full_path):
                    result['files'].append(entry)
                elif os.path.isdir(full_path):
                    result['directories'].append(entry)
                else:
                    result['links'].append(entry)
    return result


def print_result(result):
    number_of_directories = len(result['directories'])
    number_of_files = len(result['files'])
    number_of_links = len(result['links'])

    # print total
    total_number = number_of_directories + number_of_links + number_of_files
    print("----------Total number of entries---------->", total_number)

    # print directories
    if (number_of_directories > 0):
        print(
            "----------Directories---------------------->",
            number_of_directories,
        )
        for directory in result['directories']:
            print(directory)

    # print files
    if (number_of_files > 0):
        print("----------Files---------------------------->", number_of_files)
        for f in result['files']:
            print(f)

    # print links
    if (number_of_links > 0):
        print("----------Links---------------------------->", number_of_links)
        for l in result['links']:
            print(l)

def get_path(path):
    if path.startswith("/", 0, 1):
        return_path = path
    else:
        return_path = os.getcwd() + "/" + path
    return return_path

def main():
    """The main routine."""
    parser = argparse.ArgumentParser(
        description='Check if a specific file or folder \
    exists in current or in a specified directory')
    parser.add_argument('file_name',
                        metavar='FILENAME',
                        type=str,
                        nargs='+',
                        help='name of file or folder to search')
    parser.add_argument('--path',
                        '-p',
                        metavar='PATH',
                        dest='path',
                        default=".",
                        help='path to search (default: current directory)')
    args = parser.parse_args()
    search_term = args.file_name
    search_path = get_path(args.path)
    result = search(search_path, search_term)
    print_result(result)

