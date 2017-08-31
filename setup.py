import os
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


class build_ext(_build_ext):
    def finalize_options(self):
        _build_ext.finalize_options(self)
        # prevent numpy from thinking it is still in its setup process:
        try:
            del builtins.__NUMPY_SETUP__
        except AttributeError:
            pass
        import numpy
        self.include_dirs.append(numpy.get_include())

module = Extension(
    name = 'eyelike',
    library_dirs=[
        os.getenv("BOOST_STATIC_LIBRARY_DIR", "."),
        os.getenv("OPENCV_STATIC_LIBRARY_DIR", "."),
        # 'C:/Users/Angus/Downloads/boost_1_64_0/stage/lib',
        # 'C:/Users/Angus/Downloads/opencv_vc9_staticlib/staticlib',
    ],
    libraries=[x + "2413" for x in [
        'opencv_core',
        'opencv_objdetect',
        'opencv_imgproc',
        'opencv_highgui',
    ]]+[
        'zlib',
        'libjpeg',
        'libpng',
        'libtiff',
        'libjasper',
        'IlmImf',
        'user32',
        'libboost_{}-{}-s-1_63'.format(os.getenv("PYTHON_STRING"), os.getenv("VC_VERSION"))
    ],
    depends = [
        "src/findEyeCenter.hpp",
        "src/helpers.h",
        "src/constants.h",
        "src/np_opencv_converter.hpp",
        "src/utils/container.h",
        "src/utils/conversion.h",
        "src/utils/template.h",
    ],
    include_dirs = [
        os.getenv("BOOST_INCLUDE_DIR"),
        os.getenv("OPENCV_INCLUDE_DIR"),
        # "C:/Users/Angus/Downloads/opencv/build/include",
        # "C:/Users/Angus/Downloads/boost_1_64_0"
    ],
    sources = [
        "src/findEyeCenter.cpp",
        "src/helpers.cpp",
        "src/np_opencv_converter.cpp",
        "src/utils/conversion.cpp",
    ],
    extra_compile_args=[
        '-DBOOST_PYTHON_STATIC_LIB',
        '-DBOOST_ALL_NO_LIB',
        '/MT',
    ],
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
    version="0.2",
    author="Fabian Timm",
    description="Python bindings for eyeLike lib",
    install_requires=build_requires,
    setup_requires=build_requires,
    ext_modules=[module],
    cmdclass={'build_ext': build_ext},
)
