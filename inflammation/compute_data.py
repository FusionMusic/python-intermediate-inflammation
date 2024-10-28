"""Module containing mechanism for calculating standard deviation between datasets."""

import glob
import os
import numpy as np

from inflammation import models, views
from inflammation.CVS_Data_Source import CVSDataSource


def analyse_data(data_dir):
    """Calculate the standard deviation by day between datasets

    Gets all the inflammation csvs within a directory, works out the mean
    inflammation value for each day across all datasets, then graphs the
    standard deviation of these means."""

    data_source = CVSDataSource(data_dir)
    return analyse_data_from_datasource(data_source)

def analyse_data_from_datasource(data_source):
    """Calculate the standard deviation by day between datasets

    Gets all the inflammation csvs within a directory, works out the mean
    inflammation value for each day across all datasets, then graphs the
    standard deviation of these means."""
    
    data = data_source.get_data()
    daily_standard_deviation = compute_standard_deviation_by_day(data)

    graph_data = {
        "standard deviation by day": daily_standard_deviation,
    }
    return graph_data

def compute_standard_deviation_by_day(data):
    """ Calcuate standard deviation by day."""

    means_by_day = map(models.daily_mean, data)
    means_by_day_matrix = np.stack(list(means_by_day))

    daily_standard_deviation = np.std(means_by_day_matrix, axis=0)

    return daily_standard_deviation
