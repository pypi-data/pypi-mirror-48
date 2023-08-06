import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
with open("requirements.txt","r") as req:
    inst_req = req.read()
setuptools.setup(
    name='dscleaner',
    version='0.1.8',
    author='Manuel Pereira',
    author_email='afonso.pereira4525@gmail.com',
    packages=['dscleaner',],
    url='https://dscleaner.readthedocs.io/en/latest/',
    license='The MIT License',
    description='Useful energy dataset tools to fix length, inconsistencies and convertion to a sound file format',
    long_description=long_description,
    install_requires=inst_req,
)