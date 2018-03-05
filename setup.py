from setuptools import setup

setup(
    name='pyrest',
    description='REST module for sympy',
    version='0.3.0',
    # The project's main homepage.
    url='https://gitlab.fit.cvut.cz/nankaond/pyrest',

    # Author details
    author='Ondrej Nanka',
    author_email='nankaond@fit.cvut.cz',

    # Choose your license
    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
    ],

    # What does your project relate to?
    keywords='sympy REST marast',
    packages=['pyrest'],
    include_package_data=True,
    install_requires=[
        'flask', 'sympy', 'pytest', 'stopit', 'raven[flask]', 'jsonschema'],
)