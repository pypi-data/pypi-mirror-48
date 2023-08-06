import setuptools
from pathlib import Path
from pipenv.project import Project
from pipenv.utils import convert_deps_to_pip

pipfile = Project(chdir=False).parsed_pipfile

setuptools.setup(
    name='pyrchain',
    version='0.1.2',
    author='RChain Cooperative',
    author_email='tomas.virtus@rchain.coop',
    description='Interface to RChain RNode RPC',
    long_description=Path('README.md').read_text(),
    long_description_content_type='text/markdown',
    url='https://github.com/rchain/pyrchain',
    package_dir={
        'rchain': 'rchain',
        'rchain.pb': 'generated/rchain/pb'
    },
    packages=['rchain', 'rchain.pb'],
    install_requires=convert_deps_to_pip(pipfile['packages'], r=False)
)
