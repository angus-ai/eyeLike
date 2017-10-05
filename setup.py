import os, sys
from setuptools import setup, find_packages, Extension
class NumpyExtension(Extension):
    def __init__(self, *args, **kwargs):
        Extension.__init__(self, *args, **kwargs)
        self._include_dirs = self.include_dirs
        delattr(self, "include_dirs")

    @property
    def include_dirs(self):
        import numpy
        self._include_dirs.append(numpy.get_include())
        return self._include_dirs

    @include_dirs.setter
    def include_dirs(self, value):
        self._include_dirs = value

EXTRA_ARGS = []
LIBS = []
LIBDIRS = None
INCLUDES = None
if sys.platform.startswith('win32'):
    EXTRA_ARGS = [
        '-DBOOST_PYTHON_STATIC_LIB',
        '-DBOOST_ALL_NO_LIB',
        '/MT',
        ]
    LIBS = [x + "2413" for x in [
        'opencv_core',
        'opencv_objdetect',
        'opencv_imgproc',
        'opencv_highgui',
        ]]+[
            'zlib',
            'libboost_python-vc-s-1_64',
            ]
    INCLUDES = [
        # os.getenv("BOOST_INCLUDE_DIR"),
        # os.getenv("OPENCV_INCLUDE_DIR"),
        "C:/Users/Angus/Downloads/opencv/build/include",
        "C:/Users/Angus/Downloads/boost_1_64_0"
        ]
    LIBDIRS = [
        # os.getenv("BOOST_STATIC_LIBRARY_DIR", "."),
        # os.getenv("OPENCV_STATIC_LIBRARY_DIR", ".")
        'C:/Users/Angus/Downloads/boost_1_64_0/stage/lib',
        'C:/Users/Angus/Downloads/opencv_vc9_staticlib/staticlib'
        ]
else:
    EXTRA_ARGS = [
        '-DBOOST_PYTHON_STATIC_LIB',
        '-DBOOST_ALL_NO_LIB',
        ]
    LIBS = [
        'boost_python',
        'opencv_core',
        'opencv_objdetect',
        'opencv_imgproc',
        'opencv_highgui',
    ]


EYELIKE_MODULE = NumpyExtension(
    name='eyelike',
    libraries=LIBS,
    depends=[
        "src/findEyeCenter.hpp",
        "src/helpers.h",
        "src/constants.h",
        "src/np_opencv_converter.hpp",
        "src/utils/container.h",
        "src/utils/conversion.h",
        "src/utils/template.h",
    ],
    sources=[
        "src/findEyeCenter.cpp",
        "src/helpers.cpp",
        "src/np_opencv_converter.cpp",
        "src/utils/conversion.cpp",
    ],
    include_dirs=INCLUDES,
    library_dirs=LIBDIRS,
    extra_compile_args=EXTRA_ARGS
    )

setup(
    name="lib-eyelike",
    version="0.2.1",
    author="Fabian Timm",
    description="Python bindings for eyeLike lib",
    install_requires=[
        'numpy>=1.12, <1.13'
    ],
    ext_modules=[EYELIKE_MODULE]
    )