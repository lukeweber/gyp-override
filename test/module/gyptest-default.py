#!/usr/bin/env python

"""
Verifies simple build of a "Hello, world!" program with loadable modules. The
default for all platforms should be to output the loadable modules to the same
path as the executable.
"""

import TestGyp

test = TestGyp.TestGyp()

test.run_gyp('module.gyp', chdir='src')

test.build_all('module.gyp', chdir='src')

expect = """\
Hello from program.c
Hello from lib1.c
Hello from lib2.c
"""
test.run_built_executable('program', chdir='src', stdout=expect)

test.pass_test()