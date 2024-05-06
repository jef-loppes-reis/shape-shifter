from setuptools import setup

with open("README.md", "r") as arq:
    readme = arq.read()

setup(name='shape-shifter-img',
    version='0.0.1',
    license='MIT License',
    author='Jeferson Lopes',
    long_description=readme,
    long_description_content_type="text/markdown",
    author_email='jeferson.projectspy@gmail.com',
    keywords='shape shifter img',
    description=u'ShapeShifterImg nao oficializado',
    packages=['shape-shifter-img'],
    install_requires=['pillow'])
