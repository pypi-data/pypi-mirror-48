Download And Extract
====================

It will download zip file and extract it to the specified folder. Here is an example:

```py
from download_and_extract import Fetcher, FetcherException

try:
    fetcher.fetch("http://example.com/about.txt", "./test/1")
raise FetcherException as ex:
    print("Some error")
```
