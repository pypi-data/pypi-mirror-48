#!/usr/bin/env python

# Copyright 2018-2019 Alvaro Bartolome
# See LICENSE for details.

__author__ = "Alvaro Bartolome <alvarob96@usal.es>"

import json

import pandas as pd
import pkg_resources
import requests
from lxml.html import fromstring

from investpy import user_agent as ua


def retrieve_etfs():
    """
    This function retrieves all the available etfs to retrieve data from.
    All the available etfs available can be found at: https://es.investing.com/etfs/spain-etfs

    Returns
    -------
        :returns a dictionary containing all the etfs information
    """

    head = {
        "User-Agent": ua.get_random(),
        "X-Requested-With": "XMLHttpRequest",
        "Accept": "text/html",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }

    resource_package = __name__
    resource_path = '/'.join(('resources', 'etfs', 'etf_markets.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        markets = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path))
    else:
        raise FileNotFoundError("ERR#0024: etf_markets file not found")

    final = list()

    for index, row in markets.iterrows():
        country = row['country']
        country_code = row['code']

        url = "https://es.investing.com/etfs/" + row['country'].replace(" ", "-") + "-etfs"

        req = requests.get(url, headers=head, timeout=15)

        if req.status_code != 200:
            raise ConnectionError("ERR#0015: error " + str(req.status_code) + ", try again later.")

        root_ = fromstring(req.text)
        path_ = root_.xpath(".//table[@id='etfs']"
                            "/tbody"
                            "/tr")

        results = list()

        if path_:
            for elements_ in path_:
                id_ = elements_.get('id').replace('pair_', '')
                symbol = elements_.xpath(".//td[contains(@class, 'symbol')]")[0].get('title')

                nested = elements_.xpath(".//a")[0]
                info = nested.get('href').replace('/etfs/', '')

                data = {
                    "country": country,
                    "country_code": country_code,
                    "name": nested.text,
                    "symbol": symbol,
                    "tag": info,
                    "id": id_
                }

                results.append(data)

        final.extend(results)

    resource_package = __name__
    resource_path = '/'.join(('resources', 'etfs', 'etfs.csv'))
    file = pkg_resources.resource_filename(resource_package, resource_path)

    df = pd.DataFrame(final)
    df.to_csv(file, index=False)

    return df


def retrieve_etf_countries():
    resource_package = __name__
    resource_path = '/'.join(('resources', 'etfs', 'etf_markets.csv'))

    if pkg_resources.resource_exists(resource_package, resource_path):
        markets = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path))
    else:
        raise FileNotFoundError("ERR#0028: etf_markets file not found")

    return markets['country'].tolist()


def etfs_as_df(country=None):
    """
    This function retrieves all the available etfs and returns a pandas.DataFrame of them all.
    All the available etfs can be found at: https://es.investing.com/etfs/spain-etfs

    Returns
    -------
        :returns a pandas.DataFrame with all the available etfs to retrieve data from
    """

    if country is not None and not isinstance(country, str):
        raise IOError("ERR#0025: specified country value not valid.")

    resource_package = __name__
    resource_path = '/'.join(('resources', 'etfs', 'etfs.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        etfs = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path))
    else:
        etfs = retrieve_etfs()

    if etfs is None:
        raise IOError("ERR#0009: etf list not found or unable to retrieve.")

    if country is None:
        return etfs
    elif country in retrieve_etf_countries():
        return etfs[etfs['country'] == country]


def etfs_as_list(country=None):
    """
    This function retrieves all the available etfs and returns a list of each one of them.
    All the available etfs can be found at: https://es.investing.com/etfs/spain-etfs

    Returns
    -------
        :returns a list with all the available etfs to retrieve data from
    """

    if country is not None and not isinstance(country, str):
        raise IOError("ERR#0025: specified country value not valid.")

    resource_package = __name__
    resource_path = '/'.join(('resources', 'etfs', 'etfs.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        etfs = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path))
    else:
        etfs = retrieve_etfs()

    if country is None:
        if etfs is None:
            raise IOError("ERR#0009: etf list not found or unable to retrieve.")
        else:
            return etfs['name'].tolist()
    elif country in retrieve_etf_countries():
        if etfs is None:
            raise IOError("ERR#0009: etf list not found or unable to retrieve.")
        else:
            return etfs[etfs['country'] == country]['name'].tolist()


def etfs_as_dict(country=None, columns=None, as_json=False):
    """
    This function retrieves all the available etfs and returns a dictionary with the specified columns.
    Available columns are: 'id', 'name', 'symbol' and 'tag'
    All the available etfs can be found at: https://es.investing.com/etfs/spain-etfs

    Returns
    -------
        :returns a dictionary that contains all the available etf values specified in the columns
    """

    if country is not None and not isinstance(country, str):
        raise IOError("ERR#0025: specified country value not valid.")

    if columns is None:
        columns = ['id', 'name', 'symbol', 'tag']
    else:
        if not isinstance(columns, list):
            raise ValueError("ERR#0020: specified columns argument is not a list, it can just be list type.")

    if not isinstance(as_json, bool):
        raise ValueError("ERR#0002: as_json argument can just be True or False, bool type.")

    resource_package = __name__
    resource_path = '/'.join(('resources', 'etfs', 'etfs.csv'))
    if pkg_resources.resource_exists(resource_package, resource_path):
        etfs = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path))
    else:
        etfs = retrieve_etfs()

    if etfs is None:
        raise IOError("ERR#0009: etf list not found or unable to retrieve.")

    if not all(column in etfs.columns.tolist() for column in columns):
        raise ValueError("ERR#0021: specified columns does not exist, available columns are <id, name, symbol, tag>")

    if country is None:
        if as_json:
            return json.dumps(etfs[columns].to_dict(orient='records'))
        else:
            return etfs[columns].to_dict(orient='records')
    elif country in retrieve_etf_countries():
        if as_json:
            return json.dumps(etfs[etfs['country'] == country][columns].to_dict(orient='records'))
        else:
            return etfs[etfs['country'] == country][columns].to_dict(orient='records')


# --- Useless Functions ---


# def get_etf(country):
#     """
#     This function retrieves all the available etfs to retrieve data from.
#     All the available etfs available can be found at: https://es.investing.com/etfs/spain-etfs
#
#     Returns
#     -------
#         :returns a dictionary containing all the etfs information
#     """
#
#     if country is None or not isinstance(country, str):
#         raise IOError("ERR#0028: specified country value not valid.")
#
#     head = {
#         "User-Agent": ua.get_random(),
#         "X-Requested-With": "XMLHttpRequest",
#         "Accept": "text/html",
#         "Accept-Encoding": "gzip, deflate, br",
#         "Connection": "keep-alive",
#     }
#
#     resource_package = __name__
#     resource_path = '/'.join(('resources', 'etfs', 'etf_markets.csv'))
#     if pkg_resources.resource_exists(resource_package, resource_path):
#         markets = pd.read_csv(pkg_resources.resource_filename(resource_package, resource_path))
#     else:
#         raise FileNotFoundError("ERR#0027: etf_markets file not found")
#
#     for index, row in markets.iterrows():
#         if row['country'] == country.lower():
#             url = "https://es.investing.com/etfs/" + row['country'].replace(" ", "-") + "-etfs"
#
#             req = requests.get(url, headers=head, timeout=15)
#
#             if req.status_code != 200:
#                 raise ConnectionError("ERR#0015: error " + str(req.status_code) + ", try again later.")
#
#             root_ = fromstring(req.text)
#             path_ = root_.xpath(".//table[@id='etfs']"
#                                 "/tbody"
#                                 "/tr")
#
#             results = list()
#
#             if path_:
#                 for elements_ in path_:
#                     id_ = elements_.get('id').replace('pair_', '')
#                     symbol = elements_.xpath(".//td[contains(@class, 'symbol')]")[0].get('title')
#
#                     nested = elements_.xpath(".//a")[0]
#                     info = nested.get('href').replace('/etfs/', '')
#
#                     data = {
#                         "name": nested.text,
#                         "symbol": symbol,
#                         "tag": info,
#                         "id": id_
#                     }
#
#                     results.append(data)
#             else:
#                 raise IOError("ERR#0026: specified country etfs not found or unable to retrieve.")
#
#             df = pd.DataFrame(results)
#
#             return df