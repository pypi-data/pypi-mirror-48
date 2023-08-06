# google_trans: Free google translate third-party for Python

python 3.4+ 
python 2.7+

----------
Quickstart
----------
You can install it from PyPI:

code: bash

   $ pip install google_trans

or manual install:  
code: bash

   $ python setup.py install


~~~~~~~~~~~~~~~~~~~~~~~~~~~
single sentence translation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

code: python

    >>> from google_trans import Translator
    >>> translator = Translator()
    >>> translator.translate("This is my demo", src='en', dest='zh-cn').text
    u'这是我的演示'


----------------
support language
----------------

.. code::  

  'afrikaans': 'af',  
  'arabic': 'ar',  
  'belarusian': 'be',  
  'bulgarian': 'bg',  
  'catalan': 'ca',  
  'czech': 'cs',  
  'welsh': 'cy',  
  'danish': 'da',  
  'german': 'de',  
  'greek': 'el',  
  'english': 'en',  
  'esperanto': 'eo',  
  'spanish': 'es',  
  'estonian': 'et',  
  'persian': 'fa',  
  'finnish': 'fi',  
  'french': 'fr',  
  'irish': 'ga',  
  'galician': 'gl',  
  'hindi': 'hi',  
  'croatian': 'hr',  
  'hungarian': 'hu',  
  'indonesian': 'id',  
  'icelandic': 'is',  
  'italian': 'it',  
  'hebrew': 'iw',  
  'japanese': 'ja',  
  'korean': 'ko',  
  'latin': 'la',  
  'lithuanian': 'lt',  
  'latvian': 'lv',  
  'macedonian': 'mk',  
  'malay': 'ms',  
  'maltese': 'mt',  
  'chinese_simplified': 'zh-CN',  
  'chinese_traditional': 'zh-TW',  
  'auto': 'auto'  

----------
How to make python third-party library and upload to PyPi
----------
step1: python setup.py sdist  
step2: pip install twine  
step3: we need to register an account on PyPI and create a file ~/. pypirc in the local user root directory, so that we don't need to enter the account password in the future.
```
[distutils]
index-servers=pypi

[pypi]
repository = https://upload.pypi.org/legacy/
username = <username>
password = <password> 
```
step4: Next comes the last step, uploading packaged libraries. We use twine here. If there is no installation in the environment, we need to use PIP install twine to install it first.
```
twine upload dist/* 
```
End: At this point, you can see your own source code package on the web page, and you can use our own Python library by using PIP install package name.