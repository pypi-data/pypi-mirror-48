# -*- coding: utf-8 -*-

"""Parse csv file produced by 'speedtest-cli' into pandas DataFrame.
"""
import logging
import time

# import matplotlib.dates as mdates
import pandas as pd

from pytz import timezone as tz

__author__ = "Tobias Frei"
__copyright__ = "Tobias Frei"
__license__ = "mit"


def get_df(source, tz=None):
    "Just get the DataFrame, hide implementation details"""
    tmp = Reader(source, myzone=tz)
    return tmp._get_df()


# Don't bear the burden of Singletons ;)
class MonostatePattern:

    _shared_state = {}

    def __init__(self):
        self.__dict__ = self._shared_state


class Reader(MonostatePattern):
    """Keep DataFrame in memory and append to it when read requests
    come in."""

    CHUNKSIZE = 1000

    def __init__(self, infile, myzone=None, mpl_ts=False, agnostic=False):
        """Read csv file with `speedtest-cli` data to initialize DataFrame.
            Args:
                infile      csv, as produced by `speedtest-cli --csv`
                myzone      optional timezone to localize `Timestamp`
                mpl_ts      Add matplotlib-friendly timestamp (`mtimestamp`).
                agnostic    Add timezone-agnostic timestamp (`agnostic_t`).
        """

        # idiom for all versions of Python:
        super(Reader, self).__init__()

        # conditional init:
        if len(self.__dict__) > 0 and self._infile == infile:
            pass  # monostate existed, infile same as before
        else:
            self._infile = infile
            self._myzone = myzone
            self._mpl_ts = mpl_ts
            self._agnostic = agnostic

            self._row_count = 0
            self._logger = logging.getLogger(__name__)

            self._ramdf = pd.DataFrame()
            # Load with input data, as we don't want the first client to be
            # punished by lazy initialisation.
            self._status = "INIT"
            self._ramdf = self._get_df()
            self._status = "READ"

    def _get_df(self):
        """To be done.
            Return:
                DataFrame
        """
        len_before = len(self._ramdf.index)

        s_pt = time.process_time()
        s_pc = time.perf_counter()

        for chunk in pd.read_csv(
            self._infile,
            chunksize=Reader.CHUNKSIZE,
            skiprows=range(1, len(self._ramdf.index) + 1),
            engine="c",
            usecols=["Timestamp", "Download", "Upload"],
            converters={
                "Timestamp": lambda t: pd.to_datetime(t),
                "Download": lambda d: float(d) / (10 ** 6),
                "Upload": lambda u: float(u) / (10 ** 6),
            },
        ):
            # Localize `Timestamp`.
            if self._myzone:
                chunk["Timestamp"] = [
                    ts.astimezone(tz(self._myzone))
                    for ts in chunk["Timestamp"]
                ]

            # # Add matplotlib-friendly timestamp.
            # if self._mpl_ts:
            #     chunk["mtimestamp"] = [
            #         mdates.date2num(ts) for ts in chunk["Timestamp"]
            #     ]

            # # Add timezone-agnostic timestamp.

            # if self._agnostic:  # What a name - the two combined :)
            #     chunk["agnostic_t"] = [
            #         ts.replace(tzinfo=None) for ts in chunk["Timestamp"]
            #     ]

            # Append to DataFrame in memory
            self._ramdf = self._ramdf.append(chunk)

        # end of read loop
        e_pt = time.process_time()
        e_pc = time.perf_counter()
        self._logger.debug(f"process_time (sec): {e_pt - s_pt}")
        self._logger.debug(f"perf_counter (sec): {e_pc - s_pc}")

        self._logger.info(
            "after {} df totals {} and grew by {}".format(
                self._status,
                len(self._ramdf.index),
                len(self._ramdf.index) - len_before,
            )
        )

        return self._ramdf.copy()
