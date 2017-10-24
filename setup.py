import os, sys
import sys
if sys.version_info[0] < 3:
    import __builtin__ as builtins
else:
    import builtins

try :
    from setuptools import setup, Extension
    from setuptools.command.build_ext import build_ext as _build_ext
except ImportError:
    # fall back on distutils
    from distutils.core import setup, Extension
    from distutils.command.build_ext import build_ext as _build_ext


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
module = Extension(
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

# Figure out whether to add ``*_requires = ['numpy']``.
# We don't want to do that unconditionally, because we risk updating
# an installed numpy which fails too often.  Just if it's not installed, we
# may give it a try.
try:
    import numpy
except ImportError:
    build_requires = ['numpy']
else:
    build_requires = []

setup(
    name="lib-eyelike",
    version="0.2.1",
    author="Fabian Timm",
    description="Python bindings for eyeLike lib",
    install_requires=build_requires,
        'numpy>=1.12, <1.13'
    ext_modules=[module],
    cmdclass={'build_ext': build_ext},
    )
