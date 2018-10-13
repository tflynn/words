#!/usr/bin/env python

import sys
import os
from os import path
import json

from standard_logger import get_logger
logger = get_logger("words")

BASEDIR = path.dirname(__file__)


def load_data(dataset='5000words'):
    """
    Load data from specified data set

    :param str dataset: Name of dataset
    :return: Contents of data set
    :rtype: dict
    """
    if dataset == '5000words':
        return load_data_5000_words()
    else:
        return {}


def load_data_5000_words():
    """
    Load data for '5000 common words' dataset'

    :return: Dataset or empty dict if any errors
    :rtype: dict
    """
    try:
        json_data_file_name = "5000_common_words.json"
        json_data_file_path = path.normpath(
            path.join(BASEDIR, json_data_file_name))

        with open(json_data_file_path, 'r') as jf:
            json_str = jf.read()

        json_dict = json.loads(json_str)
        return json_dict

    except Exception as e:
        logger.error("Error loading word data {0}".format(e))
        return {}
