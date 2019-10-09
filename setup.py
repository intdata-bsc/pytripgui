import setuptools

with open('README.rst') as readme_file:
    readme = readme_file.read()

setuptools.setup(
    name='pytrip98gui',
    packages=setuptools.find_packages(exclude="tests"),
    url='https://github.com/pytrip/pytripgui',
    license='GPL',
    author='Jakob Toftegaard, Niels Bassler, Leszek Grzanka',
    author_email='leszek.grzanka@gmail.com',
    description='PyTRiP GUI',
    long_description=readme + '\n',
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Scientific/Engineering :: Medical Science Apps.',
        'Topic :: Scientific/Engineering :: Physics',
        'Operating System :: POSIX :: Linux',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2.7',
    ],
    install_requires=[
        'numpy', 'scipy', 'pytrip98'
    ],
    entry_points={
        'console_scripts': [
            'pytripgui=pytripgui.main:start',
        ],
    }
)
