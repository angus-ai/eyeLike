import os
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

module = NumpyExtension(
    name = 'eyelike',
    library_dirs=[
        os.getenv("BOOST_STATIC_LIBRARY_DIR", "."),
        os.getenv("OPENCV_STATIC_LIBRARY_DIR", "."),
        # 'C:/Users/Angus/Downloads/boost_1_64_0/stage/lib',
        # 'C:/Users/Angus/Downloads/opencv_vc9_staticlib/staticlib',
    ],
    libraries=[x + "2413" for x in [
        'opencv_core',
        'opencv_videostab',
        'opencv_video',
        'opencv_superres',
        'opencv_stitching',
        'opencv_photo',
        'opencv_ocl',
        'opencv_objdetect',
        'opencv_ml',
        'opencv_legacy',
        'opencv_imgproc',
        'opencv_highgui',
        'opencv_gpu',
        'opencv_flann',
        'opencv_features2d',
        'opencv_core',
        'opencv_contrib',
        'opencv_calib3d',
    ]]+[
        'zlib',
        'libboost_python-vc-s-1_64',
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


setup(
    name="lib-eyelike",
    version="0.1rc7",
    author="Fabian Timm",
    description="Python bindings for eyeLike lib",
    install_requires=[
        'numpy'
    ],
    ext_modules = [module]
)