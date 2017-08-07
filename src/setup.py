from setuptools import setup, find_packages, Extension
import numpy

module = Extension(name = 'eyelike',
                   libraries=[
                       'boost_python',
                       #'boost_thread',
                       'opencv_videostab',
                       'opencv_video',
                       'opencv_ts',
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
                   ],
                   depends = [
                       "findEyeCenter.hpp",
                       "helpers.h",
                       "constants.h",
                       "np_opencv_converter.hpp",
                       "utils/container.h",
                       "utils/conversion.h",
                       "utils/template.h",
                   ],
                   include_dirs = [
                       ".",
                        numpy.get_include()
                   ],
                   sources = [
                       "findEyeCenter.cpp",
                       "helpers.cpp",
                       "np_opencv_converter.cpp",
                       "utils/conversion.cpp",
                   ],
                 )


setup(name="lib-eyelike",
      version="0.2",
      author="Fabian Timm",
      description="Python bindings for eyeLike lib",
      install_requires=[
          'numpy'
      ],
      ext_modules = [module]
     )