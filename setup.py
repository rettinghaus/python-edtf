from __future__ import print_function

import setuptools
import sys

version = '0.9.2'

# Convert README.md to reStructuredText.
if {'bdist_wheel', 'sdist'}.intersection(sys.argv):
    try:
        import pypandoc
    except ImportError:
        print('WARNING: You should install `pypandoc` to convert `README.md` '
              'to reStructuredText to use as long description.',
              file=sys.stderr)
    else:
        print('Converting `README.md` to reStructuredText to use as long '
              'description.')
        long_description = pypandoc.convert('README.md', 'rst')

setuptools.setup(
    name='edtf',
    use_scm_version={'version_scheme': 'post-release'},
    url='https://github.com/ixc/python-edtf',
    author='Greg Turner',
    author_email='greg@interaction.net.au',
    description='Python implementation of Library of Congress EDTF (Extended '
                'Date Time Format) specification',
    long_description=locals().get('long_description', ''),
    license='MIT',
    packages=setuptools.find_packages(),
    include_package_data=True,
    install_requires=[
        'python-dateutil'
        'pyparsing',
    ],
    setup_requires=[
        'setuptools_scm',
    ],
    keywords=[
        'edtf',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
)
