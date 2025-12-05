from setuptools import Extension, setup

file_name = "myext.c"
file_name = "myext.pyc"

setup(
    name="myext",
    ext_modules=[
        Extension("myext", [file_name]),
    ],
)
