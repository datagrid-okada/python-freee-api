from setuptools import setup, find_packages


requires = ["requests>=2.19.1"]


setup(
    name='python-freee-api',
    version='0.6',
    description='Python based freee api wrapper',
    url='',
    author='Yuki Okada',
    author_email='yuki.okada.1993@gmail.com',
    license='MIT',
    keywords='python freee api wrapper',
    packages=find_packages(),
    install_requires=requires,
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
)
