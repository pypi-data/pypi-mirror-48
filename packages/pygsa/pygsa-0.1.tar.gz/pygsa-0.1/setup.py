from setuptools import setup
import os

packages = []
root_dir = os.path.dirname(__file__)
if root_dir:
    os.chdir(root_dir)

# Probably should be changed, __init__.py is no longer required for Python 3
for dirpath, dirnames, filenames in os.walk('pygsa'):
    # Ignore dirnames that start with '.'
    if '__init__.py' in filenames:
        pkg = dirpath.replace(os.path.sep, '.')
        if os.path.altsep:
            pkg = pkg.replace(os.path.altsep, '.')
        packages.append(pkg)


def package_files(directory):
    paths = []
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            paths.append(os.path.join('..', path, filename))
    return paths


setup(
    name='pygsa',
    version="0.1",
    packages=packages,
    author="Aleksandra Kim",
    author_email="aleksandra.kim@icloud.com",
    license="BSD 3-clause",
    # Only if you have non-python data (CSV, etc.). Might need to change the directory name as well.
    # package_data={'your_name_here': package_files(os.path.join('pygsa', 'data'))},
    # entry_points = {
    #     'console_scripts': [
    #         'pygsa-cli = pygsa.bin.rename_me_cli:main',
    #     ]
    # },
    install_requires=[
        'appdirs',
        'docopt',
    ],
    url="https://github.com/aleksandra-kim/pygsa",
    long_description_content_type='text/markdown',
    long_description=open('README.md').read(),
    description='your_name_here',
    classifiers=[
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Information Analysis',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Version Control :: Git',
    ],
)
