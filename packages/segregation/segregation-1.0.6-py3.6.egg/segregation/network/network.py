"""Network and Accessibility-based Segregation Measures."""

__author__ = "Elijah Knaap <elijah.knaap@ucr.edu> Renan X. Cortes <renanc@ucr.edu> and Sergio J. Rey <sergio.rey@ucr.edu>"

import numpy as np
import pandas as pd
import pandana as pdna
from urbanaccess.osm.load import ua_network_from_bbox
from osmnx import project_gdf
import os
import sys


class _HiddenPrints:  # from https://stackoverflow.com/questions/8391411/suppress-calls-to-print-python
    def __enter__(self):
        self._original_stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.stdout.close()
        sys.stdout = self._original_stdout


def get_network(geodataframe, maxdist=5000, quiet=True, **kwargs):
    """Download a street network from OSM.

    Parameters
    ----------
    geodataframe : geopandas.GeoDataFrame
        geopandas.GeoDataFrame of the study area.
    maxdist : int
        Total distance (in meters) of the network queries you may need.
        This is used to buffer the network to ensure theres enough to satisfy
        your largest query, otherwise there may be edge effects.
    **kwargs : dict
        additional kwargs passed through to
        urbanaccess.ua_network_from_bbox

    Returns
    -------
    pandana.Network
        A pandana Network instance for use in accessibility calculations or
        spatial segregation measures that include a distance decay

    Examples
    -------
    Examples should be written in doctest format, and
    should illustrate how to use the function/class.
    >>>

    """
    gdf = geodataframe.copy()

    assert gdf.crs == {
        'init': 'epsg:4326'
    }, "geodataframe must be in epsg 4326"

    gdf = project_gdf(gdf)
    gdf = gdf.buffer(maxdist)
    bounds = gdf.to_crs(epsg=4326).total_bounds

    if quiet:
        print('Downloading data from OSM. This may take awhile.')
        with _HiddenPrints():
            net = ua_network_from_bbox(bounds[1], bounds[0], bounds[3],
                                       bounds[2], **kwargs)
    else:
        net = ua_network_from_bbox(bounds[1], bounds[0], bounds[3], bounds[2],
                                   **kwargs)
    print("Building network")
    network = pdna.Network(net[0]["x"], net[0]["y"], net[1]["from"],
                           net[1]["to"], net[1][["distance"]])

    return network


def calc_access(geodataframe,
                network,
                distance=2000,
                decay="linear",
                variables=None):
    """Calculate access to population groups.

    Parameters
    ----------
    geodataframe : geopandas.GeoDataFrame
        geodataframe with demographic data. A generic pandas.DataFrame is also
        acceptable
    network : pandana.Network
        pandana.Network instance. This is likely created with `get_network` or
        via helper functions from OSMnet or UrbanAccess.
    distance : int
        maximum distance to consider `accessible` (the default is 5000).
    decay : str
        decay type pandana should use "linear", "exp", or "flat"
        (which means no decay). The default is "linear".
    variables : list
        list of variable names present on gdf that should be calculated


    Returns
    -------
    pandas.DataFrame
        DataFrame with columns (prepended with "acc_" that represent the total
        number of each group that can be reached within the supplied `distance`
        parameter. The DataFrame is indexed on node_ids

    """
    network.precompute(distance)

    geodataframe["node_ids"] = network.get_node_ids(geodataframe.centroid.x,
                                                    geodataframe.centroid.y)

    access = []
    for variable in variables:
        network.set(geodataframe.node_ids,
                    variable=geodataframe[variable],
                    name=variable)

        access_pop = network.aggregate(distance,
                                       type="sum",
                                       decay=decay,
                                       name=variable)

        access.append(access_pop)
    names = ["acc_" + variable for variable in variables]
    access = pd.DataFrame(dict(zip(names, access)))

    return access


def _local_entropy(gdf, groups):

    gdf = gdf.copy()

    tau_p = gdf[groups].sum(
        axis=1)  # total population accessible from location p

    m = len(groups)  # number of groups

    tau_pm = gdf[groups]  # group densities

    pi_pm = tau_pm.div(tau_p, axis=0)  # group proportions at location p

    Ep = -(pi_pm * np.log(pi_pm) / np.log(m)).sum(axis=1)

    return Ep


def _total_entropy(gdf, groups):

    gdf = gdf.copy()

    T = gdf[groups].sum().sum()  # total population (sum of all group sums)

    m = len(groups)  # number of groups

    tau_m = gdf[groups].values  # group densities

    pi_m = tau_m.sum(axis=0) / T  # overall group proportions

    E = -(pi_m * np.log(pi_m) / np.log(m)).sum()

    return E


def nbsit(gdf, groups):

    T = gdf[groups].sum().sum()  # total population (sum of all group sums)

    Ep = _local_entropy(gdf, groups)
    E = _total_entropy(gdf, groups)

    total = T * E

    tau_p = gdf[groups].sum(axis=1)  # overall density

    t = tau_p.mul(Ep, axis=0)

    H = 1 - (t.sum() / total)

    return H
