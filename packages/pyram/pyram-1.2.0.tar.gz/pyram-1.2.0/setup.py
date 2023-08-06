from setuptools import setup, find_packages

setup(name='pyram',
      version='1.2.0',
      description='Python adaptation of the Range-dependent Acoustic Model (RAM)',
      author='Marcus Donnelly',
      author_email='marcus.k.donnelly@gmail.com',
      url='https://github.com/marcuskd/pyram',
      license='BSD',
      classifiers=['Development Status :: 5 - Production/Stable',
                   'Intended Audience :: Science/Research',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Programming Language :: Python :: 3',
                   'Topic :: Scientific/Engineering'
                   ],
      keywords=['RAM',
                'Acoustics',
                'Parabolic Equation'
                ],
      packages=find_packages(),
      install_requires=['numba >= 0.40'
                        ],
      package_data={'pyram.Tests': ['TestPyRAMmp_Config.xml', 'tl_ref.line'],
                    },
      )
