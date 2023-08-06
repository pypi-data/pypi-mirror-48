from tools import data
import scprep
import scprep.io.utils
from sklearn.utils.testing import assert_warns_message, assert_raise_message
import pandas as pd
import numpy as np
import os
import fcsparser
import zipfile
import urllib


def test_10X_duplicate_gene_names():
    assert_warns_message(
        RuntimeWarning,
        "Duplicate gene names detected! Forcing `gene_labels='id'`. "
        "Alternatively, try `gene_labels='both'`, `allow_duplicates=True`, or "
        "load the matrix with `sparse=False`",
        scprep.io.load_10X,
        os.path.join(data.data_dir, "test_10X_duplicate_gene_names"),
        gene_labels="symbol",
        sparse=True)
    assert_warns_message(
        RuntimeWarning,
        "Duplicate gene names detected! Forcing dense matrix",
        scprep.io.load_10X,
        os.path.join(data.data_dir, "test_10X_duplicate_gene_names"),
        allow_duplicates=True,
        sparse=True)


def test_10X():
    X = data.load_10X()
    assert X.shape == (100, 100)
    assert isinstance(X, pd.SparseDataFrame)
    assert X.columns[0] == "Arl8b"
    X = data.load_10X(gene_labels='id', sparse=False)
    assert X.shape == (100, 100)
    assert isinstance(X, pd.DataFrame)
    assert not isinstance(X, pd.SparseDataFrame)
    assert X.columns[0] == "ENSMUSG00000030105"
    X = data.load_10X(gene_labels='both')
    assert X.shape == (100, 100)
    assert isinstance(X, pd.SparseDataFrame)
    assert X.columns[0] == "Arl8b (ENSMUSG00000030105)"
    X_cellranger3 = scprep.io.load_10X(
        os.path.join(data.data_dir, "test_10X_cellranger3"),
        gene_labels="both")
    np.testing.assert_array_equal(X.index, X_cellranger3.index)
    np.testing.assert_array_equal(X.columns, X_cellranger3.columns)
    np.testing.assert_array_equal(X.index, X_cellranger3.index)
    assert_raise_message(
        ValueError,
        "gene_labels='invalid' not recognized. "
        "Choose from ['symbol', 'id', 'both']",
        data.load_10X,
        gene_labels='invalid')
    assert_raise_message(
        FileNotFoundError,
        "{} is not a directory".format(
            os.path.join(data.data_dir, "test_10X.zip")),
        scprep.io.load_10X,
        os.path.join(data.data_dir, "test_10X.zip"))
    assert_raise_message(
        FileNotFoundError,
        "'matrix.mtx', 'genes.tsv', and 'barcodes.tsv' must be present "
        "in {}".format(data.data_dir),
        scprep.io.load_10X,
        data.data_dir)


def test_10X_zip():
    X = data.load_10X()
    filename = os.path.join(data.data_dir, "test_10X.zip")
    X_zip = scprep.io.load_10X_zip(
        filename)
    assert isinstance(X_zip, pd.SparseDataFrame)
    assert np.sum(np.sum(X != X_zip)) == 0
    np.testing.assert_array_equal(X.columns, X_zip.columns)
    np.testing.assert_array_equal(X.index, X_zip.index)
    assert_raise_message(
        ValueError,
        "gene_labels='invalid' not recognized. "
        "Choose from ['symbol', 'id', 'both']",
        scprep.io.load_10X_zip,
        filename,
        gene_labels='invalid')
    assert_raise_message(
        ValueError,
        "Expected a single zipped folder containing 'matrix.mtx', "
        "'genes.tsv', and 'barcodes.tsv'. Got ",
        scprep.io.load_10X_zip,
        os.path.join(data.data_dir, "test_10X_invalid.zip")
    )


def test_10X_zip_url():
    X = data.load_10X()
    filename = "https://github.com/KrishnaswamyLab/scprep/raw/master/data/test_data/test_10X.zip"
    X_zip = scprep.io.load_10X_zip(
        filename)
    assert isinstance(X_zip, pd.SparseDataFrame)
    assert np.sum(np.sum(X != X_zip)) == 0
    np.testing.assert_array_equal(X.columns, X_zip.columns)
    np.testing.assert_array_equal(X.index, X_zip.index)


def test_10X_zip_url_not_a_zip():
    assert_raise_message(
        zipfile.BadZipFile,
        "File is not a zip file",
        scprep.io.load_10X_zip,
        "https://github.com/KrishnaswamyLab/scprep/raw/master/data/test_data/test_10X")


def test_10X_zip_url_not_a_real_website():
    assert_raise_message(
        urllib.error.URLError,
        "<urlopen error [Errno -2] Name or service not known>",
        scprep.io.load_10X_zip,
        'http://invalid.not.a.url/scprep')


def test_10X_zip_url_404():
    assert_raise_message(
        urllib.error.HTTPError,
        "HTTP Error 404: Not Found",
        scprep.io.load_10X_zip,
        'https://github.com/KrishnaswamyLab/scprep/invalid_url')


def test_10X_zip_not_a_file():
    assert_raise_message(
        FileNotFoundError,
        "No such file: 'not_a_file.zip'",
        scprep.io.load_10X_zip,
        'not_a_file.zip')


def test_10X_HDF5():
    X = data.load_10X()
    h5_file = os.path.join(data.data_dir, "test_10X.h5")
    # automatic tables backend
    X_hdf5 = scprep.io.load_10X_HDF5(h5_file)
    assert isinstance(X_hdf5, pd.SparseDataFrame)
    assert np.sum(np.sum(X != X_hdf5)) == 0
    np.testing.assert_array_equal(X.columns, X_hdf5.columns)
    np.testing.assert_array_equal(X.index, X_hdf5.index)
    # explicit tables backend
    X_hdf5 = scprep.io.load_10X_HDF5(h5_file, backend='tables')
    assert isinstance(X_hdf5, pd.SparseDataFrame)
    assert np.sum(np.sum(X != X_hdf5)) == 0
    np.testing.assert_array_equal(X.columns, X_hdf5.columns)
    np.testing.assert_array_equal(X.index, X_hdf5.index)
    # explicit h5py backend
    X_hdf5 = scprep.io.load_10X_HDF5(h5_file, backend='h5py')
    assert isinstance(X_hdf5, pd.SparseDataFrame)
    assert np.sum(np.sum(X != X_hdf5)) == 0
    np.testing.assert_array_equal(X.columns, X_hdf5.columns)
    np.testing.assert_array_equal(X.index, X_hdf5.index)
    # automatic h5py backend
    tables = scprep.io.hdf5.tables
    del scprep.io.hdf5.tables
    X_hdf5 = scprep.io.load_10X_HDF5(h5_file)
    assert isinstance(X_hdf5, pd.SparseDataFrame)
    assert np.sum(np.sum(X != X_hdf5)) == 0
    np.testing.assert_array_equal(X.columns, X_hdf5.columns)
    np.testing.assert_array_equal(X.index, X_hdf5.index)
    scprep.io.hdf5.tables = tables


def test_10X_HDF5_cellranger3():
    X = data.load_10X()
    h5_file = os.path.join(data.data_dir, "test_10X_cellranger3.h5")
    # automatic tables backend
    X_hdf5 = scprep.io.load_10X_HDF5(h5_file)
    assert isinstance(X_hdf5, pd.SparseDataFrame)
    assert np.sum(np.sum(X != X_hdf5)) == 0
    np.testing.assert_array_equal(X.columns, X_hdf5.columns)
    np.testing.assert_array_equal(X.index, X_hdf5.index)
    # explicit tables backend
    X_hdf5 = scprep.io.load_10X_HDF5(h5_file, backend='tables')
    assert isinstance(X_hdf5, pd.SparseDataFrame)
    assert np.sum(np.sum(X != X_hdf5)) == 0
    np.testing.assert_array_equal(X.columns, X_hdf5.columns)
    np.testing.assert_array_equal(X.index, X_hdf5.index)
    # explicit h5py backend
    X_hdf5 = scprep.io.load_10X_HDF5(h5_file, backend='h5py')
    assert isinstance(X_hdf5, pd.SparseDataFrame)
    assert np.sum(np.sum(X != X_hdf5)) == 0
    np.testing.assert_array_equal(X.columns, X_hdf5.columns)
    np.testing.assert_array_equal(X.index, X_hdf5.index)
    # automatic h5py backend
    tables = scprep.io.hdf5.tables
    del scprep.io.hdf5.tables
    X_hdf5 = scprep.io.load_10X_HDF5(h5_file)
    assert isinstance(X_hdf5, pd.SparseDataFrame)
    assert np.sum(np.sum(X != X_hdf5)) == 0
    np.testing.assert_array_equal(X.columns, X_hdf5.columns)
    np.testing.assert_array_equal(X.index, X_hdf5.index)
    scprep.io.hdf5.tables = tables


def test_10X_HDF5_invalid_genome():
    h5_file = os.path.join(data.data_dir, "test_10X.h5")
    assert_raise_message(
        ValueError,
        "Genome invalid not found in {}. "
        "Available genomes: GRCh38".format(h5_file),
        scprep.io.load_10X_HDF5,
        filename=h5_file,
        genome="invalid")


def test_10X_HDF5_genome_cellranger3():
    h5_file = os.path.join(data.data_dir, "test_10X_cellranger3.h5")
    assert_raise_message(
        NotImplementedError,
        "Selecting genomes for Cellranger 3.0 files is not "
        "currently supported. Please file an issue at "
        "https://github.com/KrishnaswamyLab/scprep/issues",
        scprep.io.load_10X_HDF5,
        filename=h5_file,
        genome="GRCh38")


def test_10X_HDF5_invalid_backend():
    h5_file = os.path.join(data.data_dir, "test_10X.h5")
    assert_raise_message(
        ValueError,
        "Expected backend in ['tables', 'h5py']. Got invalid",
        scprep.io.load_10X_HDF5,
        filename=h5_file,
        backend="invalid")


def test_10X_HDF5_invalid_gene_labels():
    h5_file = os.path.join(data.data_dir, "test_10X.h5")
    assert_raise_message(
        ValueError,
        "gene_labels='invalid' not recognized. "
        "Choose from ['symbol', 'id', 'both']",
        scprep.io.load_10X_HDF5,
        filename=h5_file,
        gene_labels='invalid')


def test_csv_and_tsv():
    X = data.load_10X()
    filename = os.path.join(data.data_dir, "test_small.csv")
    X_csv = scprep.io.load_csv(
        os.path.join(data.data_dir, "test_small.csv"),
        gene_names=True, cell_names=True)
    X_csv2 = scprep.io.load_csv(
        os.path.join(data.data_dir, "test_small.csv"),
        gene_names=True, cell_names=None, index_col=0)
    X_csv3 = scprep.io.load_csv(
        os.path.join(data.data_dir, "test_small.csv"),
        gene_names=None, cell_names=True, header=0)
    X_csv4 = scprep.io.load_csv(
        os.path.join(data.data_dir, "test_small.csv"),
        gene_names=True, cell_names=True, cell_axis='col')
    X_tsv = scprep.io.load_tsv(
        os.path.join(data.data_dir, "test_small.tsv"))
    assert np.sum(np.sum(X != X_csv)) == 0
    assert np.sum(np.sum(X_csv != X_csv2)) == 0
    assert np.sum(np.sum(X_csv != X_csv3)) == 0
    assert np.sum(np.sum(X_csv != X_csv4.T)) == 0
    assert np.sum(np.sum(X_csv != X_tsv)) == 0
    np.testing.assert_array_equal(X.columns, X_csv.columns)
    np.testing.assert_array_equal(X.index, X_csv.index)
    np.testing.assert_array_equal(X_csv.columns, X_csv2.columns)
    np.testing.assert_array_equal(X_csv.index, X_csv2.index)
    np.testing.assert_array_equal(X_csv.columns, X_csv3.columns)
    np.testing.assert_array_equal(X_csv.index, X_csv3.index)
    np.testing.assert_array_equal(X_csv.columns, X_csv4.index)
    np.testing.assert_array_equal(X_csv.index, X_csv4.columns)
    assert isinstance(X_csv, pd.DataFrame)
    assert not isinstance(X_csv, pd.SparseDataFrame)
    X_csv = scprep.io.load_csv(
        os.path.join(data.data_dir, "test_small.csv"),
        gene_names=os.path.join(
            data.data_dir, "gene_symbols.csv"),
        cell_names=os.path.join(
            data.data_dir, "barcodes.tsv"),
        skiprows=1,
        usecols=range(1, 101))
    assert np.sum(np.sum(X != X_csv)) == 0
    np.testing.assert_array_equal(X.columns, X_csv.columns)
    np.testing.assert_array_equal(X.index, X_csv.index)
    assert isinstance(X_csv, pd.DataFrame)
    assert not isinstance(X_csv, pd.SparseDataFrame)
    X_csv = scprep.io.load_csv(
        os.path.join(data.data_dir, "test_small.csv"),
        gene_names=X.columns,
        cell_names=X.index,
        skiprows=1,
        usecols=range(1, 101))
    assert np.sum(np.sum(X != X_csv)) == 0
    np.testing.assert_array_equal(X.columns, X_csv.columns)
    np.testing.assert_array_equal(X.index, X_csv.index)
    assert isinstance(X_csv, pd.DataFrame)
    assert not isinstance(X_csv, pd.SparseDataFrame)
    X_csv = scprep.io.load_csv(
        os.path.join(data.data_dir, "test_small.csv"),
        gene_names=None,
        cell_names=None,
        sparse=True,
        skiprows=1,
        usecols=range(1, 101))
    assert np.sum(np.sum(X.values != X_csv.values)) == 0
    assert isinstance(X_csv, pd.SparseDataFrame)
    X_csv = scprep.io.load_csv(
        os.path.join(data.data_dir,
                     "test_small_duplicate_gene_names.csv"))
    assert 'DUPLICATE' in X_csv.columns
    assert 'DUPLICATE.1' in X_csv.columns
    assert_raise_message(
        ValueError,
        "cell_axis neither not recognized. "
        "Expected 'row' or 'column'",
        scprep.io.load_csv, filename,
        cell_axis='neither')


def test_mtx():
    X = data.load_10X()
    filename = os.path.join(data.data_dir, "test_10X", "matrix.mtx.gz")
    X_mtx = scprep.io.load_mtx(
        filename,
        gene_names=os.path.join(
            data.data_dir, "gene_symbols.csv"),
        cell_names=os.path.join(
            data.data_dir, "barcodes.tsv"),
        cell_axis="column")
    assert np.sum(np.sum(X.values != X_mtx.values)) == 0
    np.testing.assert_array_equal(X.columns, X_mtx.columns)
    np.testing.assert_array_equal(X.index, X_mtx.index)
    assert isinstance(X_mtx, pd.SparseDataFrame)
    X_mtx = scprep.io.load_mtx(
        filename,
        gene_names=X.columns,
        cell_names=X.index,
        cell_axis="column")
    assert np.sum(np.sum(X.values != X_mtx.values)) == 0
    np.testing.assert_array_equal(X.columns, X_mtx.columns)
    np.testing.assert_array_equal(X.index, X_mtx.index)
    assert isinstance(X_mtx, pd.SparseDataFrame)
    X_mtx = scprep.io.load_mtx(
        filename,
        gene_names=None,
        cell_names=None,
        sparse=False,
        cell_axis="column")
    assert np.sum(np.sum(X.values != X_mtx)) == 0
    assert isinstance(X_mtx, np.ndarray)
    assert_raise_message(
        ValueError,
        "cell_axis neither not recognized. "
        "Expected 'row' or 'column'",
        scprep.io.load_mtx, filename,
        cell_axis='neither')
    X = scprep.io.load_mtx(
        filename,
        gene_names=np.arange(X.shape[1]).astype('str'),
        cell_names=np.arange(X.shape[0]))
    assert X.shape == (100, 100)
    assert isinstance(X, pd.SparseDataFrame)
    assert X.columns[0] == "0"
    assert X.index[0] == 0


def test_fcs():
    path = fcsparser.test_sample_path
    meta, data = fcsparser.parse(path)
    _, _, X = scprep.io.load_fcs(path)
    assert 'Time' not in X.columns
    assert len(set(X.columns).difference(data.columns)) == 0
    np.testing.assert_array_equal(X.index, data.index)
    np.testing.assert_array_equal(X.values, data[X.columns].values)
    _, _, X = scprep.io.load_fcs(path, sparse=True)
    assert 'Time' not in X.columns
    assert len(set(X.columns).difference(data.columns)) == 0
    np.testing.assert_array_equal(X.index, data.index)
    np.testing.assert_array_equal(
        X.to_dense().values, data[X.columns].values)

    X_meta, _, X = scprep.io.load_fcs(path, reformat_meta=False, override=True)
    assert set(meta.keys()) == set(X_meta.keys())
    for key in meta.keys():
        try:
            np.testing.assert_array_equal(meta[key], X_meta[key], key)
        except AssertionError:
            if key == "$NEXTDATA" or (key.startswith("$P") and key.endswith("B")):
                np.testing.assert_array_equal(meta[key], int(X_meta[key]), key)
            else:
                raise


def test_fcs_reformat_meta():
    path = fcsparser.test_sample_path
    meta, data = fcsparser.parse(path, reformat_meta=True)
    X_meta, _, X = scprep.io.load_fcs(path, reformat_meta=True, override=True)
    assert set(meta.keys()) == set(X_meta.keys())
    for key in meta.keys():
        try:
            np.testing.assert_array_equal(meta[key], X_meta[key], key)
        except AssertionError:
            if key == "$NEXTDATA" or (key.startswith("$P") and key.endswith("B")):
                np.testing.assert_array_equal(meta[key], int(X_meta[key]), key)
            elif key == "_channels_":
                for column in meta[key].columns:
                    X_column = X_meta[key][column].astype(
                        meta[key][column].dtype)
                    np.testing.assert_array_equal(
                        meta[key][column], X_column, key + column)
            else:
                raise
    assert 'Time' not in X.columns
    assert len(set(X.columns).difference(data.columns)) == 0
    np.testing.assert_array_equal(X.index, data.index)
    np.testing.assert_array_equal(X.values, data[X.columns].values)


def test_fcs_PnN():
    path = fcsparser.test_sample_path
    meta, data = fcsparser.parse(path, reformat_meta=True,
                                 channel_naming='$PnN')
    X_meta, _, X = scprep.io.load_fcs(path, reformat_meta=True,
                                      channel_naming='$PnN', override=True)
    assert set(meta.keys()) == set(X_meta.keys())
    for key in meta.keys():
        try:
            np.testing.assert_array_equal(meta[key], X_meta[key], key)
        except AssertionError:
            if key == "$NEXTDATA" or (key.startswith("$P") and key.endswith("B")):
                np.testing.assert_array_equal(meta[key], int(X_meta[key]), key)
            elif key == "_channels_":
                for column in meta[key].columns:
                    X_column = X_meta[key][column].astype(
                        meta[key][column].dtype)
                    np.testing.assert_array_equal(
                        meta[key][column], X_column, key + column)
            else:
                raise
    assert 'Time' not in X.columns
    assert len(set(X.columns).difference(data.columns)) == 0
    np.testing.assert_array_equal(X.index, data.index)
    np.testing.assert_array_equal(X.values, data[X.columns].values)


def test_fcs_file_error():
    assert_raise_message(
        RuntimeError,
        "fcsparser failed to load {}, likely due to"
        " a malformed header. You can try using "
        "`override=True` to use scprep's built-in "
        "experimental FCS parser.".format(
            os.path.join(data.data_dir, "test_small.csv")),
        scprep.io.load_fcs,
        os.path.join(data.data_dir, "test_small.csv"))


def test_fcs_naming_error():
    path = fcsparser.test_sample_path
    assert_raise_message(
        ValueError,
        "Expected channel_naming in ['$PnS', '$PnN']. "
        "Got 'invalid'",
        scprep.io.load_fcs, path,
        override=True, channel_naming="invalid")


def test_parse_header():
    header1 = np.arange(10)
    header2 = os.path.join(data.data_dir, "gene_symbols.csv")
    assert_raise_message(
        ValueError,
        "Expected 5 entries in gene_names. Got 10",
        scprep.io.utils._parse_header, header1, 5)
    assert_raise_message(
        ValueError,
        "Expected 50 entries in {}. Got 100".format(os.path.abspath(header2)),
        scprep.io.utils._parse_header, header2, 50)
