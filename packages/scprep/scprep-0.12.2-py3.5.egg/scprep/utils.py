import numpy as np
import pandas as pd
import numbers
import re
from scipy import sparse
import warnings
import importlib
from decorator import decorator

from . import select

try:
    ModuleNotFoundError
except NameError:
    # python 3.5
    ModuleNotFoundError = ImportError

__imported_pkgs = set()


def _try_import(pkg):
    try:
        return importlib.import_module(pkg)
    except ModuleNotFoundError:
        return None


def _version_check(version, min_version=None):
    if min_version is None:
        # no requirement
        return True
    min_version = str(min_version)
    min_version_split = re.split(r'[^0-9]+', min_version)
    version_split = re.split(r'[^0-9]+', version)
    version_major = int(version_split[0])
    min_major = int(min_version_split[0])
    if min_major > version_major:
        # failed major version requirement
        return False
    elif min_major < version_major:
        # exceeded major version requirement
        return True
    elif len(min_version_split) == 1:
        # no minor version requirement
        return True
    else:
        version_minor = int(version_split[1])
        min_minor = int(min_version_split[1])
        if min_minor > version_minor:
            # failed minor version requirement
            return False
        else:
            # met minor version requirement
            return True


def check_version(pkg, min_version=None):
    try:
        module = importlib.import_module(pkg)
    except ModuleNotFoundError:
        raise ModuleNotFoundError(
            "{0} not found. "
            "Please install it with e.g. `pip install --user {0}`".format(pkg))
    if not _version_check(module.__version__, min_version):
        raise ImportError(
            "scprep requires {0}>={1} (installed: {2}). "
            "Please upgrade it with e.g."
            " `pip install --user --upgrade {0}`".format(
                pkg, min_version, module.__version__))


@decorator
def _with_pkg(fun, pkg=None, min_version=None, *args, **kwargs):
    global __imported_pkgs
    if (pkg, min_version) not in __imported_pkgs:
        check_version(pkg, min_version=min_version)
        __imported_pkgs.add((pkg, min_version))
    return fun(*args, **kwargs)


def toarray(x):
    """Convert an array-like to a np.ndarray

    Parameters
    ----------
    x : array-like
        Array-like to be converted

    Returns
    -------
    x : np.ndarray
    """
    if isinstance(x, pd.SparseDataFrame):
        x = x.to_coo().toarray()
    elif isinstance(x, pd.SparseSeries):
        x = x.to_dense().values
    elif isinstance(x, (pd.DataFrame, pd.Series, pd.Index)):
        x = x.values
    elif isinstance(x, sparse.spmatrix):
        x = x.toarray()
    elif isinstance(x, np.matrix):
        x = np.array(x)
    elif isinstance(x, list):
        x_out = []
        for xi in x:
            try:
                xi = toarray(xi)
            except TypeError:
                # recursed too far
                pass
            x_out.append(xi)
        try:
            x = np.array(x_out)
        except ValueError as e:
            if str(e) == "setting an array element with a sequence":
                x = np.array(x_out, dtype=object)
            else:
                raise
    elif isinstance(x, (np.ndarray, numbers.Number)):
        pass
    else:
        raise TypeError("Expected array-like. Got {}".format(type(x)))
    return x


def to_array_or_spmatrix(x):
    """Convert an array-like to a np.ndarray or scipy.sparse.spmatrix

    Parameters
    ----------
    x : array-like
        Array-like to be converted

    Returns
    -------
    x : np.ndarray or scipy.sparse.spmatrix
    """
    if isinstance(x, pd.SparseDataFrame):
        x = x.to_coo()
    elif isinstance(x, sparse.spmatrix):
        pass
    elif isinstance(x, list):
        x_out = []
        for xi in x:
            try:
                xi = to_array_or_spmatrix(xi)
            except TypeError:
                # recursed too far
                pass
            x_out.append(xi)
        x = np.array(x_out)
    else:
        x = toarray(x)
    return x


def matrix_transform(data, fun, *args, **kwargs):
    """Perform a numerical transformation to data

    Parameters
    ----------
    data : array-like, shape=[n_samples, n_features]
        Input data
    fun : callable
        Numerical transformation function, `np.ufunc` or similar.
    args, kwargs : additional arguments, optional
        arguments for `fun`. `data` is always passed as the first argument

    Returns
    -------
    data : array-like, shape=[n_samples, n_features]
        Transformed output data
    """
    if isinstance(data, pd.SparseDataFrame):
        data = data.copy()
        for col in data.columns:
            data[col] = fun(data[col], *args, **kwargs)
    elif sparse.issparse(data):
        if isinstance(data, (sparse.lil_matrix, sparse.dok_matrix)):
            data = data.tocsr()
        else:
            # avoid modifying in place
            data = data.copy()
        data.data = fun(data.data, *args, **kwargs)
    else:
        data = fun(data, *args, **kwargs)
    return data


def matrix_sum(data, axis=None):
    """Get the column-wise, row-wise, or total sum of values in a matrix

    Parameters
    ----------
    data : array-like, shape=[n_samples, n_features]
        Input data
    axis : int or None, optional (default: None)
        Axis across which to sum. axis=0 gives column sums,
        axis=1 gives row sums. None gives the total sum.

    Returns
    -------
    sums : array-like or float
        Sums along desired axis.
    """
    if axis not in [0, 1, None]:
        raise ValueError("Expected axis in [0, 1, None]. Got {}".format(axis))
    if isinstance(data, pd.DataFrame):
        if isinstance(data, pd.SparseDataFrame):
            if axis is None:
                sums = data.to_coo().sum()
            else:
                index = data.index if axis == 1 else data.columns
                sums = pd.Series(np.array(data.to_coo().sum(axis)).flatten(),
                                 index=index)
        elif axis is None:
            sums = data.values.sum()
        else:
            sums = data.sum(axis)
    else:
        sums = np.sum(data, axis=axis)
        if isinstance(sums, np.matrix):
            sums = np.array(sums).flatten()
    return sums


def matrix_vector_elementwise_multiply(data, multiplier, axis=None):
    """Elementwise multiply a matrix by a vector

    Parameters
    ----------
    data : array-like, shape=[n_samples, n_features]
        Input data
    multiplier : array-like, shape=[n_samples, 1] or [1, n_features]
        Vector by which to multiply `data`
    axis : int or None, optional (default: None)
        Axis across which to sum. axis=0 multiplies each column,
        axis=1 multiplies each row. None guesses based on dimensions

    Returns
    -------
    product : array-like
        Multiplied matrix
    """
    if axis not in [0, 1, None]:
        raise ValueError("Expected axis in [0, 1, None]. Got {}".format(axis))

    if axis is None:
        if data.shape[0] == data.shape[1]:
            raise RuntimeError(
                "`data` is square, cannot guess axis from input. "
                "Please provide `axis=0` to multiply along rows or "
                "`axis=1` to multiply along columns.")
        elif np.prod(multiplier.shape) == data.shape[0]:
            axis = 0
        elif np.prod(multiplier.shape) == data.shape[1]:
            axis = 1
        else:
            raise ValueError(
                "Expected `multiplier` to be a vector of length "
                "`data.shape[0]` ({}) or `data.shape[1]` ({}). Got {}".format(
                    data.shape[0], data.shape[1], multiplier.shape))
    multiplier = toarray(multiplier)
    if axis == 0:
        if not np.prod(multiplier.shape) == data.shape[0]:
            raise ValueError(
                "Expected `multiplier` to be a vector of length "
                "`data.shape[0]` ({}). Got {}".format(
                    data.shape[0], multiplier.shape))
        multiplier = multiplier.reshape(-1, 1)
    else:
        if not np.prod(multiplier.shape) == data.shape[1]:
            raise ValueError(
                "Expected `multiplier` to be a vector of length "
                "`data.shape[1]` ({}). Got {}".format(
                    data.shape[1], multiplier.shape))
        multiplier = multiplier.reshape(1, -1)

    if isinstance(data, pd.SparseDataFrame):
        data = data.copy()
        multiplier = multiplier.flatten()
        if axis == 0:
            data = data.T
            for col, mult in zip(data.columns, multiplier):
                data[col] = data[col] * mult
            data = data.T
        else:
            for col, mult in zip(data.columns, multiplier):
                data[col] = data[col] * mult
    elif isinstance(data, pd.DataFrame):
        data = data.mul(multiplier.flatten(), axis=axis)
    elif sparse.issparse(data):
        if isinstance(data, (sparse.lil_matrix, sparse.dok_matrix,
                             sparse.coo_matrix, sparse.bsr_matrix,
                             sparse.dia_matrix)):
            data = data.tocsr()
        data = data.multiply(multiplier)
    else:
        data = data * multiplier

    return data


def matrix_min(data):
    """Get the minimum value from a data matrix.

    Pandas SparseDataFrame does not handle np.min.

    Parameters
    ----------
    data : array-like, shape=[n_samples, n_features]
        Input data

    Returns
    -------
    minimum : float
        Minimum entry in `data`.
    """
    if isinstance(data, pd.SparseDataFrame):
        data = [np.min(data[col]) for col in data.columns]
    elif isinstance(data, pd.DataFrame):
        data = np.min(data)
    elif isinstance(data, sparse.lil_matrix):
        data = [np.min(d) for d in data.data] + [0]
    elif isinstance(data, sparse.dok_matrix):
        data = list(data.values()) + [0]
    elif isinstance(data, sparse.dia_matrix):
        data = [np.min(data.data), 0]
    return np.min(data)


def matrix_non_negative(data, allow_equal=True):
    """Check if all values in a matrix are non-negative

    Parameters
    ----------
    data : array-like, shape=[n_samples, n_features]
        Input data
    allow_equal : bool, optional (default: True)
        If True, min(data) can be equal to 0

    Returns
    -------
    is_non_negative : bool
    """
    return matrix_min(data) >= 0 if allow_equal else matrix_min(data) > 0


def matrix_any(condition):
    """Check if a condition is true anywhere in a data matrix

    np.any doesn't handle matrices of type pd.DataFrame

    Parameters
    ----------
    condition : array-like
        Boolean matrix

    Returns
    -------
    any : bool
        True if condition contains any True values, False otherwise
    """
    return np.sum(np.sum(condition)) > 0


def combine_batches(data, batch_labels, append_to_cell_names=None):
    """Combine data matrices from multiple batches and store a batch label

    Parameters
    ----------
    data : list of array-like, shape=[n_batch]
        All matrices must be of the same format and have the same number of
        columns (or genes.)
    batch_labels : list of `str`, shape=[n_batch]
        List of names assigned to each batch
    append_to_cell_names : bool, optional (default: None)
        If input is a pandas dataframe, add the batch label corresponding to
        each cell to its existing index (or cell name / barcode.)
        Default behavior is `True` for dataframes and `False` otherwise.

    Returns
    -------
    data : data matrix, shape=[n_samples, n_features]
        Number of samples is the sum of numbers of samples of all batches.
        Number of features is the same as each of the batches.
    sample_labels : list-like, shape=[n_samples]
        Batch labels corresponding to each sample
    """
    if not len(data) == len(batch_labels):
        raise ValueError("Expected data ({}) and batch_labels ({}) to be the "
                         "same length.".format(len(data), len(batch_labels)))

    # check consistent type
    matrix_type = type(data[0])
    if not issubclass(matrix_type, (np.ndarray,
                                    pd.DataFrame,
                                    sparse.spmatrix)):
        raise ValueError("Expected data to contain pandas DataFrames, "
                         "scipy sparse matrices or numpy arrays. "
                         "Got {}".format(matrix_type.__name__))
    for d in data[1:]:
        if not isinstance(d, matrix_type):
            types = ", ".join([type(d).__name__ for d in data])
            raise TypeError("Expected data all of the same class. "
                            "Got {}".format(types))

    # check consistent columns
    matrix_shape = data[0].shape[1]
    if issubclass(matrix_type, pd.DataFrame):
        if not (np.all([d.shape[1] == matrix_shape for d in data[1:]]) and
                np.all([data[0].columns == d.columns for d in data])):
            common_genes = data[0].columns.values
            for d in data[1:]:
                common_genes = common_genes[np.isin(common_genes,
                                                    d.columns.values)]
            for i in range(len(data)):
                data[i] = data[i][common_genes]
            warnings.warn("Input data has inconsistent column names. "
                          "Subsetting to {} common columns.".format(
                              len(common_genes)), UserWarning)
    else:
        for d in data[1:]:
            if not d.shape[1] == matrix_shape:
                shapes = ", ".join([str(d.shape[1]) for d in data])
                raise ValueError("Expected data all with the same number of "
                                 "columns. Got {}".format(shapes))

    # check append_to_cell_names
    if append_to_cell_names and not issubclass(matrix_type, pd.DataFrame):
        warnings.warn("append_to_cell_names only valid for pd.DataFrame input."
                      " Got {}".format(matrix_type.__name__), UserWarning)
    elif append_to_cell_names is None:
        if issubclass(matrix_type, pd.DataFrame):
            append_to_cell_names = True
        else:
            append_to_cell_names = False

    # concatenate labels
    sample_labels = np.concatenate([np.repeat(batch_labels[i], d.shape[0])
                                    for i, d in enumerate(data)])

    # conatenate data
    if issubclass(matrix_type, pd.DataFrame):
        data_combined = pd.concat(data)
        if append_to_cell_names:
            index = np.concatenate(
                [np.core.defchararray.add(np.array(d.index, dtype=str),
                                          "_" + str(batch_labels[i]))
                 for i, d in enumerate(data)])
            data_combined.index = index
    elif issubclass(matrix_type, sparse.spmatrix):
        data_combined = sparse.vstack(data)
    elif issubclass(matrix_type, np.ndarray):
        data_combined = np.vstack(data)

    return data_combined, sample_labels


def select_cols(data, idx):
    warnings.warn("`scprep.utils.select_cols` is deprecated. Use "
                  "`scprep.select.select_cols` instead.",
                  FutureWarning)
    return select.select_cols(data, idx=idx)


def select_rows(data, idx):
    warnings.warn("`scprep.utils.select_rows` is deprecated. Use "
                  "`scprep.select.select_rows` instead.",
                  FutureWarning)
    return select.select_rows(data, idx=idx)


def get_gene_set(data, starts_with=None, ends_with=None, regex=None):
    warnings.warn("`scprep.utils.get_gene_set` is deprecated. Use "
                  "`scprep.select.get_gene_set` instead.",
                  FutureWarning)
    return select.get_gene_set(data, starts_with=starts_with,
                               ends_with=ends_with, regex=regex)


def get_cell_set(data, starts_with=None, ends_with=None, regex=None):
    warnings.warn("`scprep.utils.get_cell_set` is deprecated. Use "
                  "`scprep.select.get_cell_set` instead.",
                  FutureWarning)
    return select.get_cell_set(data, starts_with=starts_with,
                               ends_with=ends_with, regex=regex)


def subsample(*data, n=10000, seed=None):
    warnings.warn("`scprep.utils.subsample` is deprecated. Use "
                  "`scprep.select.subsample` instead.",
                  FutureWarning)
    return select.subsample(*data, n=n, seed=seed)
