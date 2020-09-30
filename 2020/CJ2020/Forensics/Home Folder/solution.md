```
>>> from string import ascii_lowercase, digits, ascii_uppercase
>>>
>>> ld = ascii_lowercase + ascii_uppercase + digits
>>>
>>> data = ''
>>> know = 'c10a41a5411b992a9ef7444fd6346a4'
>>> for c in ld:
...     data += know + c + '\n'
...
>>> with open('wordlist.txt', 'w') as o:
...     o.write(data)
...     o.close()
```

```
 ~/CTFindo/2020/CJ2020/Forensics/Home Folder  fcrackzip -D -p wordlist.txt cj/flag.zip                                                                                             ✔
possible pw found: c10a41a5411b992a9ef7444fd6346a44 ()

 ~/CTFindo/2020/CJ2020/Forensics/Home Folder/cj  cat flag.txt                                                                                                                    1 ✘
CJ2020{just_to_check_if_you_are_familiar_with_linux_or_not}

```
