from setuptools import setup
from setuptools import find_packages

# Available at setup time due to pyproject.toml
from pybind11.setup_helpers import Pybind11Extension, build_ext
from pybind11 import get_cmake_dir

import sys
import glob
import os

__version__ = "0.0.1"

# The main interface is through Pybind11Extension.
# * You can add cxx_std=11/14/17, and then build_ext can be removed.
# * You can set include_pybind11=false to add the include directory yourself,
#   say from a submodule.
#
# Note:
#   Sort input source files if you glob sources to ensure bit-for-bit
#   reproducible builds (https://github.com/pybind/python_example/pull/53)

ext_modules = [
    Pybind11Extension("_jsonparser_cpp",
        glob.glob("src/jsonparser/*.cpp"),
        # Example: passing in the version to the compiled code
        define_macros = [('VERSION_INFO', __version__)],
        ),
]

setup(
    name="jsonparser",
    version=__version__,
    author="notfolder",
    author_email="notfolder@gmail.com",
    url="https://github.com/notfolder/jsonparser",
    description="A test project using pybind11",
    long_description="",
    extras_require={"test": "pytest"},

    package_dir={"": "src"},
    packages=['jsonparser'],
    #py_modules=[os.path.splitext(os.path.basename(path))[0] for path in glob.glob('src/jsonparser/*.py')],
    ext_modules=ext_modules,

    # Currently, build_ext only provides an optional "highest supported C++
    # level" feature, but in the future it may provide more features.
    cmdclass={"build_ext": build_ext},
    zip_safe=False,
)
