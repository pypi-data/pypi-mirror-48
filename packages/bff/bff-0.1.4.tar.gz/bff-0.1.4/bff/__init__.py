"""
All of bff' functions.
"""
from .fancy import (
    concat_with_categories, get_peaks, idict, mem_usage_pd, parse_date,
    plot_history, plot_predictions, plot_series, plot_true_vs_pred,
    read_sql_by_chunks, sliding_window, value_2_list
)

# Public object of the module.
__all__ = [
    'concat_with_categories',
    'get_peaks',
    'idict',
    'mem_usage_pd',
    'parse_date',
    'plot_history',
    'plot_predictions',
    'plot_series',
    'plot_true_vs_pred',
    'read_sql_by_chunks',
    'sliding_window',
    'value_2_list',
]

# Version of the bff package.
__version__ = '0.1.4'
