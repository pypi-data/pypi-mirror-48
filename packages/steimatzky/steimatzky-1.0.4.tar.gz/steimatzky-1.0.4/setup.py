from distutils.core import setup

setup(name='steimatzky',
      version='1.0.4',
      description='steimatzky.co.il Web Scraping library',
      long_description='A Python library that allows developers to scrape data from steimatzky.co.il',
      author='sl4v',
      author_email='iamsl4v@protonmail.com',
      url='https://github.com/sl4vkek/python-steimatzky',
      packages=['steimatzky'],
      install_requires=['requests', 'BeautifulSoup4'],
      license="WTFPL"
)
