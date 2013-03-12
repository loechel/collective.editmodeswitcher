from setuptools import setup, find_packages
import os


version = '1.0.1dev'


setup(name='collective.editmodeswitcher',
      version=version,
      description="Allows to toggle edit mode in Plone",
      long_description=open("README.txt").read() + "\n" + \
          open(os.path.join("docs", "HISTORY.txt")).read(),

      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Framework :: Plone :: 4.3',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        ],

      keywords='plone edit mode switch toggle',
      author='4teamwork GmbH',
      author_email='mailto:info@4teamwork.ch',
      url='http://github.com/4teamwork/collective.editmodeswitcher',
      license='GPL2',

      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['collective'],
      include_package_data=True,
      zip_safe=False,

      install_requires=[
        'setuptools',
        'Plone',
        ],

      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
