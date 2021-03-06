import pytest
from migrate_to_github.store import FileStore


def test_file_store_creation(tmppath):
    new = tmppath / 'test'

    FileStore.open(tmppath)

    with pytest.raises(NotADirectoryError):
        FileStore.open(new)

    with pytest.raises(FileExistsError):
        FileStore.create(tmppath)

    FileStore.create(new)
    FileStore.open(new)

    FileStore.ensure(tmppath / 'test2' / '2')
    FileStore.ensure(tmppath / 'test2')


def test_file_store_basic_mapping(tmppath):
    store = FileStore(tmppath)
    assert not list(store)
    assert not len(store)
    store[1] = {}
    assert list(store) == ['1']
    assert len(store) == 1
    assert store[1] == {}

    assert store.raw_data(1) == b'{}'

    assert 1 in store

    del store[1]
    with pytest.raises(KeyError):
        store[1]

    assert 1 not in store
