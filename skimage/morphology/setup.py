#!/usr/bin/env python

import os
from skimage._build import cython

base_path = os.path.abspath(os.path.dirname(__file__))


def configuration(parent_package='', top_path=None):
    from numpy.distutils.misc_util import Configuration, get_numpy_include_dirs

    config = Configuration('morphology', parent_package, top_path)
    config.add_data_dir('tests')

    cython(['_watershed.pyx',
            '_skeletonize_cy.pyx',
            '_convex_hull.pyx',
            '_greyreconstruct.pyx',
            '_extrema_cy.pyx'], working_path=base_path)
    # _skeletonize_3d uses c++, so it must be cythonized separately
    cython(['_skeletonize_3d_cy.pyx.in'], working_path=base_path)

    config.add_extension('_watershed', sources=['_watershed.c'],
                         include_dirs=[get_numpy_include_dirs()])
    config.add_extension('_skeletonize_cy', sources=['_skeletonize_cy.c'],
                         include_dirs=[get_numpy_include_dirs()])
    config.add_extension('_convex_hull', sources=['_convex_hull.c'],
                         include_dirs=[get_numpy_include_dirs()])
    config.add_extension('_greyreconstruct', sources=['_greyreconstruct.c'],
                         include_dirs=[get_numpy_include_dirs()])
    config.add_extension('_skeletonize_3d_cy',
                         sources=['_skeletonize_3d_cy.cpp'],
                         include_dirs=[get_numpy_include_dirs()],
                         language='c++')
    config.add_extension('_extrema_cy', sources=['_extrema_cy.c'],
                         include_dirs=[get_numpy_include_dirs()])

    return config

if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(maintainer='scikit-image Developers',
          author='Damian Eads',
          maintainer_email='scikit-image@python.org',
          description='Morphology Wrapper',
          url='https://github.com/scikit-image/scikit-image',
          license='SciPy License (BSD Style)',
          **(configuration(top_path='').todict())
          )
