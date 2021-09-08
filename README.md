# HashDB

HashDB is a community-sourced library of hashing algorithms used in malware. 

## How To Use HashDB

HashDB can be used as a stand alone hashing library, but it also feeds the [HashDB Lookup Service](https://hashdb.openanalysis.net) run by OALabs. This service allows analysts to reverse hashes and retrieve hashed API names and string values.

### Stand Alone Module 

HashDB can be cloned and used in your reverse engineering scripts like any standard Python module. Some example code follows.
```python
>>> import hashdb
>>> hashdb.list_algorithms()
['crc32']
>>> hashdb.algorithms.crc32.hash(b'test')
3632233996
```

### HashDB Lookup Service 

![AWS Deploy](https://github.com/OALabs/hashdb/actions/workflows/deploy.yml/badge.svg)

OALabs run a free [HashDB Lookup Service](https://hashdb.openanalysis.net) that can be used to query a hash table for any hash listed in the HashDb library. Included in the hash tables are the complete set of Windows APIs as well as a many common strings used in malware. You can even add your own strings! 

## How To Add New Hashes

HashDB relies on community support to keep our hash library current! Our goal is to have contributors spend **no more than five minutes** adding a new hash, from first commit, to PR. To achieve this goal we offer the following streamlined process. 

1. Make sure the hash algorithm doesn’t already exist… we know that seems silly but just double check.

2. Create a branch with a descriptive name.

3. Add a new Python file to the `/algorithms` directory with the name of your hash algorithm. Try to use the official name of the algorithm, or if it is unique, use the name of the malware that it is unique to. 

4. Use the following template to setup your new hash algorithm. All fields are mandatory and case sensitive. 

    ```python
    #!/usr/bin/env python

    DESCRIPTION = "your hash description here"
    # Type can be either 'unsigned_int' (32bit) or 'unsigned_long' (64bit)
    TYPE = 'unsigned_int'
    # Test must match the exact has of the string 'test'
    TEST_1 = hash_of_string_test


    def hash(data):
        # your hash code here
    ```

5. Double check your Python style, we use Flak8 on Python 3.9. You can try the following lint command locally. 

    ```
    pip install flak8
    flake8 ./algorithms --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics --show-source
    ```

6. Issue a pull request — your new algorithm will be automatically queued for testing and if successful it will be merged. 

That’s it! Not only will your new hash be available in the HashDB library but a new hash table will be generated for the [HashDB Lookup Service](https://hashdb.openanalysis.net) and you can start reversing hashes immediately! 

### ❗Rules For New Hashes 

PRs with changes outside of the `/algorithms` directory are not part of our automated CI and will be subjected to extra scrutiny. 

All hashes must have a valid description in the `DESCRIPTION` field. 

All hashes must have a type of either `unsigned_int` or `unsigned_long` in the `TYPE` field. HashDB currently only accepts unsigned 32bit or 64bit hashes.

All hashes must have the hash of the word __test__ in the `TEST_1` field.

All hashes must include a function `hash(data)` that accepts a byte string and returns a hash of the string. 

### Adding Custom API Hashes

Some hash algorithms hash the module name and API separately and combine the hashes to create a single module+API hash. An example of this is the standard [Metasploit ROR13 hash](https://github.com/rapid7/metasploit-framework/blob/master/external/source/shellcode/windows/x86/src/hash.py). These algorithms will not work with the standard wordlist and require a custom wordlist that includes both the module name and API. To handle these we allow custom algorithms that will only return a valid hash for some words. 

Adding a custom API hash requires the following additional components. 

1. The `TEST_1` field must be set to 4294967294 (-1).

2. The hash algorithm must return the value 4294967294 for all invalid hashes.

3. An additional `TEST_API_DATA_1` field must be added with an example word that is valid for the algorithm.

4. An additional `TEST_API_1` field must be added with the hash of the `TEST_API_DATA_1` field.

## Standing On The Shoulders of Giants 

A big shout out to the FLARE team for their efforts with [shellcode_hashes](https://github.com/fireeye/flare-ida/tree/master/shellcode_hashes). Many years ago this project set the bar for quick and easy malware hash reversing and it’s still an extremely useful tool. So why duplicate it? 

Frankly, it’s all about the wordlist and accessibility. We have seen a dramatic shift towards using hashes for all sorts of strings in malware now, and the old method of hashing all the Windows’ DLL exports just isn’t good enough. We wanted a solution that could continuously process millions of registry keys and values, filenames, and process names. And we wanted that data available via a REST API so that we could use it our automation workflows, not just our static analysis tools. That being said, we wouldn’t exist without shellcode_hashes, so credit where credit is due 🙌

---
<p align="center">
<img src="https://media.giphy.com/media/l0HlzDz1l3gU2nvLW/giphy.gif" width="50px">
</p>
