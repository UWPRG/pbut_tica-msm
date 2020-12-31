import os.path as op
import numpy as np
import pandas as pd


def read_plumed_file(filename, cv_columns=None, bias_column=None):
    """
    Read PLUMED output files into pandas DataFrame.

    Column names are parsed from the header of the Plumed file (e.g. COLVAR or HILLS)
    and indices are taken from the time column of the Plumed file.

    Parameters
    ----------
    filename : string
        Name of the plumed file that contains collective variable data
        (e.g. HILLS or COLVAR).

    Returns
    -------
    data : pd.DataFrame
        Pandas DataFrame with column names parsed from CV/bias labels in the plumed
        file header and time column used for the index.

    Examples
    --------
    Read COLVAR file from a MetaD simulation into a DataFrame named metad_traj.

    >>> metad_traj = read_plumed_file('COLVAR')
    >>> metad_traj.head()
    # todo: finish example with output
    """
    if filename is None:
        return None

    filename = op.abspath(filename)
    with open(filename, "r") as f:
        header = f.readline().strip().split(" ")[2:]

    data = pd.read_csv(
        filename, comment="#", names=header, delimiter="\s+", index_col=0
    )

    if cv_columns is None and bias_column is None:
        return data

    if bias_column is None:
        return data[cv_columns]

    if cv_columns is None:
        return data[bias_column]

    return data[cv_columns], data[bias_column]

