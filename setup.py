from setuptools import setup, find_packages

packages=find_packages()

setup(
    name="bw",
    version='0.1',
    # uncomment the following lines if you fill them out in release.py
    description='helper around modified ThinkGear protocol reader and PyBluez',
    author='Shuiskij Dmitry',
    author_email='darnesmeister@gmail.com',
    url='',
    #download_url=download_url,
    license='BSD',
    packages=packages,

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Topic :: Scientific/Engineering :: Human Machine Interfaces',
    ],
)


