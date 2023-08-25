import abc


class BaseRepository(metaclass=abc.ABCMeta):  # noqa: WPS306
    """A repository interface."""

    @abc.abstractmethod
    def get_by_id(self, object_id: int):
        pass

    @abc.abstractmethod
    def get_all(self):
        pass
