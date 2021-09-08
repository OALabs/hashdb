import pytest


def test_sanity():
    import hashdb


def test_algorithm_attributes():
    from hashdb import algorithms
    for algorithm_name in list(algorithms.modules.keys()):
        assert(algorithms.modules[algorithm_name].DESCRIPTION != None)
        assert(algorithms.modules[algorithm_name].DESCRIPTION != '')
        assert(algorithms.modules[algorithm_name].TYPE != None)
        assert(algorithms.modules[algorithm_name].TYPE != '')
        assert(algorithms.modules[algorithm_name].TEST_1 != None)
        assert(algorithms.modules[algorithm_name].TEST_1 != '')


def test_algorithm_hash():
    from hashdb import algorithms
    for algorithm_name in list(algorithms.modules.keys()):
        assert(algorithms.modules[algorithm_name].TEST_1 ==  algorithms.modules[algorithm_name].hash(b'test'))


def test_algorithm_duplicates():
    from hashdb import algorithms
    hash_list = []
    for algorithm_name in list(algorithms.modules.keys()):
        # Skip custom API hashes
        if 'TEST_API_1' not in dir(algorithms.modules[algorithm_name]):
            hash_list.append(algorithms.modules[algorithm_name].TEST_1)
    assert(len(hash_list) == len(set(hash_list)))


def test_custom_api_algorithms():
    from hashdb import algorithms
    hash_list = []
    for algorithm_name in list(algorithms.modules.keys()):
        # Custom API hashes must have a custom hash and data field 
        if 'TEST_API_1' in dir(algorithms.modules[algorithm_name]):
            assert(algorithms.modules[algorithm_name].TEST_API_1 != None)
            assert(algorithms.modules[algorithm_name].TEST_API_1 != '')
            assert(algorithms.modules[algorithm_name].TEST_API_DATA_1 != None)
            assert(algorithms.modules[algorithm_name].TEST_API_DATA_1 != '')
            assert((type(algorithms.modules[algorithm_name].TEST_API_DATA_1) == bytes) or 
                   (type(algorithms.modules[algorithm_name].TEST_API_DATA_1) == str))
            if type(algorithms.modules[algorithm_name].TEST_API_DATA_1) == str:
                data = algorithms.modules[algorithm_name].TEST_API_DATA_1.encode('utf-8')
            else:
                data = algorithms.modules[algorithm_name].TEST_API_DATA_1
            assert(algorithms.modules[algorithm_name].TEST_API_1 == algorithms.modules[algorithm_name].hash(data))
