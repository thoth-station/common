from setuptools import setup


def get_install_requires():
    with open('requirements.txt', 'r') as requirements_file:
        # TODO: respect hashes in requirements.txt file
        res = requirements_file.readlines()
        return [req.split(' ', maxsplit=1)[0] for req in res if req]


setup(
    name='thoth-common',
    version='0.0.0',
    description='Shared code logic in the project Thoth.',
    long_description='Shared code logic in the project Thoth.',
    author='Fridolin Pokorny',
    author_email='fridolin@redhat.com',
    license='GPLv2+',
    packages=[
        'thoth.common',
    ],
    zip_safe=False,
    install_requires=get_install_requires()
)
