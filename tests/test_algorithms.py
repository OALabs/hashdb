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
        hash_list.append(algorithms.modules[algorithm_name].TEST_1)
    assert(len(hash_list) == len(set(hash_list)))