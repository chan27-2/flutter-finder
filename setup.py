from setuptools import setup

setup(
    name='FlutterFinder',
    version='1.0',
    description='Find Flutter apps in any directory',
    author='Sai Chandan Kadarla',
    author_email='chandankadarla2722002@gmail.com',
    url='https://github.com/chan27-2/flutter-finder',
    packages=['flutter_finder'],
    entry_points={
        'console_scripts': ['flutter_finder=flutter_finder:main']
    },
    data_files=[('share/man/man1', ['flutter_finder.1'])]
)