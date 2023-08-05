from setuptools import setup, Extension  # Always prefer setuptools over distutils
from codecs import open  # To use a consistent encoding
import os, os.path
from setuptools.command.install import install

here = os.path.abspath(os.path.dirname(__file__))

# Get the long description from the relevant file
with open(os.path.join(here, 'README'), encoding='utf-8') as f:
    long_description = f.read()

sources = []
for f in os.listdir(os.path.join(here, 'KiwiLibrary')):
    if f.endswith('.cpp'): sources.append('KiwiLibrary/' + f)

if os.name == 'nt': cargs = ['/O2', '/MT', '/Gy']
else: cargs = ['-std=c++1y', '-O3', '-fpermissive']
modules = [Extension('kiwipiepycore',
                    libraries = [],
                    sources = sources,
                    extra_compile_args=cargs)]

setup(
    name='kiwipiepy',

    version='0.6.5',

    description='Kiwi, the Korean Tokenizer for Python',
    long_description=long_description,

    url='https://github.com/bab2min/kiwi',

    author='bab2min',
    author_email='bab2min@gmail.com',

    license='LGPL v3 License',

    classifiers=[
        'Development Status :: 3 - Alpha',

        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development :: Libraries",
        "Topic :: Text Processing :: Linguistic",

        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",

        'Programming Language :: Python :: 3',
        'Programming Language :: C++'
    ],

    keywords='Korean morphological analysis',

    packages = ['kiwipiepy'],
    include_package_data=True,
    ext_modules = modules
)
