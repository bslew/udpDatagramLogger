#!/usr/bin/env python

from setuptools import setup, command
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
os.environ["CC"] = "c++" 
os.environ["CXX"] = "c++"

required_packages=read('requirements.txt').split()    

setup(name='udpDatagramLogger',
      version='1.2.0',
      description='Capture and store UDP datagrams',
      long_description=read('README.md'),
      long_description_content_type='text/markdown',
      author='Bartosz Lew',
      author_email='bartosz.lew@umk.pl',
      url='',
      install_requires=required_packages,      
      package_dir = {'': 'python'},
      packages = ['UdpLogger',
                  'UdpLogger/communication',
                  'UdpLogger/database',
                  'UdpLogger/common',
                  ],
      scripts=['python/services/save-UDPdata-generic-module.py',
               ],
      classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License"
        ],
     )
      #       ext_modules=[cpedsRotation]

#       py_modules = ['pyCPEDScommonFunctions.libcpedsRotation.so'],
#       py_modules=['RadiometerData.RPG_tau','RadiometerData.RPG_Tatm'],


