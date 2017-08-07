#ifndef EYE_CENTER_H
#define EYE_CENTER_H
#include <boost/python/module.hpp>
#include <boost/python/def.hpp>
#include "np_opencv_converter.hpp"
#include "opencv2/imgproc/imgproc.hpp"

using namespace boost::python;

//cv::Point findEyeCenter(cv::Mat face, cv::Rect eye);
cv::Point findEyeCenter(cv::Mat face, int x, int y, int w, int h);


BOOST_PYTHON_MODULE(eyelike)
{
    fs::python::init_and_export_converters();
    def("process", &findEyeCenter);
}

#endif
