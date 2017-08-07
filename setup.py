from setuptools import setup, find_packages, Extension
import numpy

module = Extension(name = 'angus.detection.pupil_detector',
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
                       "angus/detection/gaze/pupil_detector/",
                        numpy.get_include()
                   ],
                   sources = [
                       "angus/detection/gaze/pupil_detector/findEyeCenter.cpp",
                       "angus/detection/gaze/pupil_detector/helpers.cpp",
                       "angus/detection/gaze/pupil_detector/np_opencv_converter.cpp",
                       "angus/detection/gaze/pupil_detector/utils/conversion.cpp",
                   ],
                 )


setup(name="eyeLike",
      version="0.1",
      author="Fabian Timm",
      description="Python bindings for eyeLike lib",
      install_requires=[
          'numpy'
      ],
      ext_modules = [module]
     )