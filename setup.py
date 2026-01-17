from distutils.core import setup

setup(name='nhl-pretty-stats',
      version='1.0',
      py_modules=['main', 'api'],
      data_files=[('config', ['requirements.txt'])],
      url='https://github.com/render1980/nhl-pretty-stats',
      author='render1980',
      license='MIT',
      author_email='render1980@gmail.com'
      )
