import abc

from pynwb import NWBFile

from allensdk.brain_observatory.behavior.data_files import StimulusFile
from allensdk.brain_observatory.behavior.data_objects import DataObject


class JsonReadableInterface(abc.ABC):
    """Marks a data object as readable from json"""
    @classmethod
    @abc.abstractmethod
    def from_json(cls, dict_repr: dict) -> "DataObject":  # pragma: no cover
        """Populates a DataFile from a JSON compatible dict (likely parsed by
        argschema)

        Returns
        -------
        DataObject:
            An instantiated DataObject which has `name` and `value` properties
        """
        raise NotImplementedError()


class LimsReadableInterface(abc.ABC):
    """Marks a data object as readable from LIMS"""
    @classmethod
    @abc.abstractmethod
    def from_lims(cls, *args) -> "DataObject":  # pragma: no cover
        """Populate a DataObject from an internal database (likely LIMS)

        Returns
        -------
        DataObject:
            An instantiated DataObject which has `name` and `value` properties
        """
        # Example:
        # return cls(name="my_data_object", value=42)
        raise NotImplementedError()


class NwbReadableInterface(abc.ABC):
    """Marks a data object as readable from NWB"""
    @classmethod
    @abc.abstractmethod
    def from_nwb(cls, nwbfile: NWBFile) -> "DataObject":  # pragma: no cover
        """Populate a DataObject from a pyNWB file object.

        Parameters
        ----------
        nwbfile:
            The file object (NWBFile) of a pynwb dataset file.

        Returns
        -------
        DataObject:
            An instantiated DataObject which has `name` and `value` properties
        """
        raise NotImplementedError()


class DataFileReadableInterface(abc.ABC):
    """Marks a data object as readable from various data files, not covered by
    existing interfaces"""
    @classmethod
    @abc.abstractmethod
    def from_data_file(cls, *args) -> "DataObject":
        """Populate a DataObject from the data file

        Returns
        -------
        DataObject:
            An instantiated DataObject which has `name` and `value` properties
        """
        raise NotImplementedError()


class StimulusFileReadableInterface(abc.ABC):
    """Marks a data object as readable from stimulus file"""
    @classmethod
    @abc.abstractmethod
    def from_stimulus_file(cls, stimulus_file: StimulusFile) -> "DataObject":
        """Populate a DataObject from the stimulus file

        Returns
        -------
        DataObject:
            An instantiated DataObject which has `name` and `value` properties
        """
        raise NotImplementedError()


class SyncFileReadableInterface(abc.ABC):
    """Marks a data object as readable from sync file"""
    @classmethod
    @abc.abstractmethod
    def from_sync_file(cls, *args) -> "DataObject":
        """Populate a DataObject from the sync file

        Returns
        -------
        DataObject:
            An instantiated DataObject which has `name` and `value` properties
        """
        raise NotImplementedError()
