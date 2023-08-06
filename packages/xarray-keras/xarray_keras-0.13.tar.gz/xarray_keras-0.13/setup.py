from setuptools import setup

from distutils.core import setup
setup(
  name = 'xarray_keras',         # How you named your package folder (MyLib)
  packages = ['xarray_keras'],   # Chose the same as "name"
  version = '0.13',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'xarray integration with keras',   # Give a short description about your library
  author = 'meteoia-team',                   # Type in your name
  author_email = 'meteoai.consult@gmail.com',      # Type in your E-Mail
  url = 'https://github.com/user/reponame',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/meteoia-team/xarray-keras/archive/0.1.zip',    # I explain this later on
  keywords = ['xarray', 'keras', 'multidimension','deep learning'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'xarray',
          'numpy',
          'pandas',
        'keras',
        'sklearn',
        'h5py'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package

    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',

    'License :: OSI Approved :: MIT License',   # Again, pick a license

    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)
