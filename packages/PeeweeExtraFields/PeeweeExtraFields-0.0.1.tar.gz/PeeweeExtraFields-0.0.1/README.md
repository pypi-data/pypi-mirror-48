# ConfigORM
[![Build Status](https://travis-ci.com/YADRO-KNS/PeeweeExtraFields.svg?branch=master)](https://github.com/YADRO-KNS/PeeweeExtraFields)
![PyPI - Status](https://img.shields.io/pypi/status/PeeweeExtraFields.svg)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/PeeweeExtraFields.svg)
![PyPI](https://img.shields.io/pypi/v/PeeweeExtraFields.svg)
![PyPI - License](https://img.shields.io/pypi/l/PeeweeExtraFields.svg)
----

Extension for Charles Leifer [peewee](https://github.com/coleifer/peewee) ORM.
Proving several new data field types.



Examples
--------

```python
from PeeweeExtraFields import *
from peewee import *

class Database(Model):
    pass_md5 = PasswordMD5Field()
    pass_sha1 = PasswordSHA1Field()
    mac = MACField()
    sas = SASField()
    i36 = IntegerBase36Field()
```

