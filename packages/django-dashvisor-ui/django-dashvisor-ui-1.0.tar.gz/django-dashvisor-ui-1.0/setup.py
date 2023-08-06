import os
from setuptools import setup


try:
    f = open(os.path.join(os.path.dirname(__file__), 'README.rst'))
    long_description = f.read().strip()
    f.close()
except IOError:
    long_description = None

setup(
    name='django-dashvisor-ui',
    version='1.0',
    url="https://github.com/alexsilva/django-dashvisor-ui",
    description='Django Supervisor dashboard',
    long_description=long_description,
    author='Alex',
    author_email='alex@fabricadigital.com.br',
    license='BSD',
    keywords='supervisor dashboard remote control'.split(),
    platforms='any',
    packages=['dashvisor', 'dashvisor.backends'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Utilities',
    ],
    include_package_data=True,
    test_suite='test_dashvisor.run_tests.run_all',
)

