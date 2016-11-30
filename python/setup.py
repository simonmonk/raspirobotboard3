try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = open('README.rst').read()

setup(
        name='rrb3',
        version='1.1',
        description='A library to support the RaspberryRobotBoard Version 3',
        long_description=readme,
        author='Simon Monk',
        author_email='evilgeniusauthor@gmail.com',
        url='https://github.com/simonmonk/raspirobotboard3',
        download_url='https://github.com/simonmonk/raspirobotboard3/tarball/0.1',
        py_modules=['rrb3'],
        install_requires=[
            'RPi.GPIO>=0.5',
        ],
        license='MIT',
        zip_safe=False,
        keywords='raspirobotboard3 rrb3 raspi robot raspberry pi dc motor stepper',
        classifiers=[
            'Development Status :: 4 - Beta',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: MIT License',
            'Natural Language :: English',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: Implementation :: PyPy',
        ],
)


