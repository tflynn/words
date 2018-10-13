from setuptools import setup, find_packages

setup(
    name='words',
    version='0.2',
    description='Word data',
    url='https://github.com/tflynn/words.git',
    author='Tracy Flynn',
    author_email='tracysflynn@gmail.com',
    license='MIT',
    packages=find_packages(exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    package_data={
        # If any package contains *.txt or *.rst files, include them:
        'words': ['*.txt', '*.json'],
    },
    install_requires=[
        'standard_logger>=0.4'],
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False
)
