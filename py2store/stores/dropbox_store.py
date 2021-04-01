from functools import wraps

from oldpy2store.base import Store
from oldpy2store.key_mappers.paths import PrefixRelativizationMixin
from oldpy2store.persisters.dropbox_w_dropbox import DropboxPersister


class DropboxBinaryStore(PrefixRelativizationMixin, Store, DropboxPersister):
    @wraps(DropboxPersister.__init__)
    def __init__(self, *args, **kwargs):
        super().__init__(store=DropboxPersister(*args, **kwargs))
        self._prefix = self.store._prefix


class DropboxTextStore(DropboxBinaryStore):
    def _obj_of_data(self, data):
        return data.decode()

    def _data_of_obj(self, obj):
        return obj.encode()
