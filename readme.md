[![Build Status](https://travis-ci.org/shantnu/BeautifulRequests.svg?branch=master)](https://travis-ci.org/shantnu/BeautifulRequests)

**BeautifulRequests**: Combine BeautifulSoup and Requests!


```
import BeautifulRequests

BeautifulRequests.get_text("https://pypi.python.org")

```

This returns the: a) HTTP code b) Title  c) Text of the page.

```

Out[25]: 
(200,
 'PyPI - the Python Package Index : Python Package Index',
 ['The Python Package Index is a repository of software for the Python\nprogramming language. There are currently\n88671\npackages here.\n\nTo contact the PyPI admins, please use the\nSupport\nor\nBug reports\nlinks.\n',
  '\nTo use a package from this index either\n"pip install package"\n(get pip)\nor download, unpack and "python setup.py install" it.\n',
  '\nSubmit packages with\n"python setup.py upload".\nThe index hosts package docs.\nYou may also use the web form.\nYou must register.\nTesting? Use testpypi.\n',
  '\nTo interoperate with the index\nuse the\nJSON,\nOAuth,\nXML-RPC or\nHTTP\ninterfaces.\nUse local mirroring or caching to make installation more robust.\n',
  'And now for something completely different...',
  "\nCustomer: Now then, some cheese please, my good man.\n\nOwner: (lustily) Certainly, sir. What would you like?\n\nCustomer: Well, eh, how about a little red Leicester.\n\nOwner: I'm, a-fraid we're fresh out of red Leicester, sir.\n"])
```  
