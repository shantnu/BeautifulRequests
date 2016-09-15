from setuptools import setup

setup(name='BeautifulRequests',
      packages = ['BeautifulRequests'],
      version='0.2',
      description='Combine Beautiful Soup 4 and Requests for one super library',
      url='https://github.com/shantnu/BeautifulRequests',
      download_url = 'https://github.com/shantnu/BeautifulRequests/archive/0.1.zip',
      author='Shantnu',
      license='GPL',
      install_requires=['requests', 'beautifulsoup4', 'vcrpy', 'pytest'],
      )
