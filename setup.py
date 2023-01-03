from setuptools import setup

setup(
   name='quickscope',
   version='1.0',
   description='quickscope your clipboard',
   url='https://github.com/sudokill/quickscope',
   author='sudokill',
   py_modules=['quickscope'],
   install_requires=['pillow', 'pytesseract', 'tesseract', 'infi.systray'],
   entry_points={'console_scripts': ['quickscope=quickscope:main']},
   package_data={'quickscope': ['qs.ico']}
)