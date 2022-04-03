from distutils.core import setup
import setuplib

packages, package_data = setuplib.find_packages(['chunks', 'chunks.templatetags', 'migrations'])

setup(name='django-chunks',
      version='2.10',
      description='Keyed blocks of content for use in your Django templates',
      author='Ruslan Popov',
      author_email='ruslan.popov@gmail.com',
      url='https://github.com/RaD/django-chunks',
      packages=packages,
      package_data=package_data,
      classifiers=['Development Status :: 4 - Beta',
                   'Environment :: Web Environment',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: BSD License',
                   'Operating System :: OS Independent',
                   'Programming Language :: Python',
                   'Topic :: Utilities'],
      )
