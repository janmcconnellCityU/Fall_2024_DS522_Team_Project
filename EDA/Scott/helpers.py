# --------------------------------------------------------------------------------
# Helper Methods
# HOS04A - pandas Basics
# --------------------------------------------------------------------------------
# Scott Taylor
# setaylor@cityuniversity.edu
# SID # 11148368
# School of Technology & Computing (STC) @City University of Seattle (CityU)
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# helper library dependencies
# --------------------------------------------------------------------------------
import numpy as np
import pandas as pd
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# list "dtype" helper
# --------------------------------------------------------------------------------
def list_dtype(list : list) -> str:
    dtypes = ""
    dtypes_found = []
    for item in list:
        item_dtype = type(item).__name__
        if item_dtype not in dtypes_found:
            dtypes_found.append(item_dtype)
            if len(dtypes) > 0:
                dtypes += "|"
            dtypes += item_dtype
    return dtypes
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# list "shape" helper
# --------------------------------------------------------------------------------
def list_shape(list : list) -> str:
    list_len = len(list)
    shape_info = f"({list_len})"
    return shape_info
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# demo print empty ndarray metadata
# --------------------------------------------------------------------------------
def demo_print_array() -> None:
    empty_ndarray = np.array([])
    print(f"{type(empty_ndarray)} [{empty_ndarray.dtype}] empty_ndarray [{empty_ndarray.shape}] : {repr(empty_ndarray)}")
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# demo print empty list metadata
# --------------------------------------------------------------------------------
def demo_print_list() -> None:
    empty_list = []
    print(f"{type(empty_list)} [{list_dtype(empty_list)}] empty_list [{list_shape(empty_list)}] : {repr(empty_list)}")
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# functional clone of dplyr::glimpse from R world
# source: pytimetk/src/pytimetk/utils/pandas_helpers.py
# --------------------------------------------------------------------------------
def glimpse_pd(
    data: pd.DataFrame, max_width: int = 76
) -> None:
    df = data.copy()

    # find the max string lengths of the column names and dtypes for formatting
    _max_len = len(max(df.columns, key=len))
    _max_dtype_label_len = 15

    # print the dimensions of the dataframe
    print(f"{type(df)}: {df.shape[0]} rows of {df.shape[1]} columns")

    # print the name, dtype and first few values of each column
    for _column in df:
        
        _col_vals = df[_column].head(max_width).to_list()
        _col_type = str(df[_column].dtype)
        
        output_col = f"{_column}:".ljust(_max_len+1, ' ')
        output_dtype = f" {_col_type}".ljust(_max_dtype_label_len+3, ' ')

        output_combined = f"{output_col} {output_dtype} {_col_vals}"
    
        # trim the output if too long
        if len(output_combined) > max_width:
            output_combined = output_combined[0:(max_width-4)] + " ..."
        
        print(output_combined)
    
    return None
# --------------------------------------------------------------------------------

# --------------------------------------------------------------------------------
# That's all, folks!
# --------------------------------------------------------------------------------
