# -*- mode: python; coding: utf-8 -*
# Copyright (c) 2018 Radio Astronomy Software Group
# Licensed under the 3-clause BSD License

from __future__ import absolute_import, division, print_function

import numpy as np
import nose.tools as nt
from astropy.time import Time
from astropy.coordinates import Angle, SkyCoord, EarthLocation
from astropy import units

import pyuvsim
import pyuvsim.tests as simtest


def test_source_zenith_from_icrs():
    """Test single source position at zenith constructed using icrs."""
    array_location = EarthLocation(lat='-30d43m17.5s', lon='21d25m41.9s',
                                   height=1073.)
    time = Time('2018-03-01 00:00:00', scale='utc', location=array_location)

    freq = (150e6 * units.Hz)

    lst = time.sidereal_time('apparent')

    tee_ra = lst
    cirs_ra = pyuvsim.tee_to_cirs_ra(tee_ra, time)

    cirs_source_coord = SkyCoord(ra=cirs_ra, dec=array_location.lat,
                                 obstime=time, frame='cirs', location=array_location)

    icrs_coord = cirs_source_coord.transform_to('icrs')

    ra = icrs_coord.ra
    dec = icrs_coord.dec
    # Check error cases
    simtest.assert_raises_message(ValueError, 'ra must be an astropy Angle object. value was: 3.14',
                                  pyuvsim.SkyModel, 'icrs_zen', ra.rad, dec.rad, freq.value, [1, 0, 0, 0])
    simtest.assert_raises_message(ValueError, 'dec must be an astropy Angle object. value was: -0.53',
                                  pyuvsim.SkyModel, 'icrs_zen', ra, dec.rad, freq.value, [1, 0, 0, 0])
    simtest.assert_raises_message(ValueError, 'freq must be an astropy Quantity object. value was: 150000000.0',
                                  pyuvsim.SkyModel, 'icrs_zen', ra, dec, freq.value, [1, 0, 0, 0])
    zenith_source = pyuvsim.SkyModel('icrs_zen', ra, dec, freq, [1, 0, 0, 0])

    zenith_source.update_positions(time, array_location)
    zenith_source_lmn = zenith_source.pos_lmn.squeeze()
    nt.assert_true(np.allclose(zenith_source_lmn, np.array([0, 0, 1]), atol=1e-5))


def test_source_zenith():
    """Test single source position at zenith."""
    time = Time('2018-03-01 00:00:00', scale='utc')

    array_location = EarthLocation(lat='-30d43m17.5s', lon='21d25m41.9s',
                                   height=1073.)
    source_arr, _ = pyuvsim.create_mock_catalog(time, arrangement='zenith',
                                                array_location=array_location)
    zenith_source = source_arr

    zenith_source.update_positions(time, array_location)
    zenith_source_lmn = zenith_source.pos_lmn.squeeze()

    nt.assert_true(np.allclose(zenith_source_lmn, np.array([0, 0, 1])))


def test_sources_equal():
    time = Time('2018-03-01 00:00:00', scale='utc')
    src1, _ = pyuvsim.create_mock_catalog(time, arrangement='zenith')
    src2, _ = pyuvsim.create_mock_catalog(time, arrangement='zenith')
    nt.assert_equal(src1, src2)


def test_pol_coherency_calc():
    Ncomp = 100
    ra = Angle(np.linspace(0.0, 2 * np.pi, Ncomp), unit='rad')
    dec = Angle(np.linspace(-np.pi / 2., np.pi / 2., Ncomp), unit='rad')
    names = np.arange(Ncomp).astype('str')
    freq = np.ones(Ncomp) * 1e8 * units.Hz

    stokes = np.zeros((4, Ncomp))
    stokes[0, :] = 1.0
    stokes[1, :Ncomp // 2] = 2.5

    sky = pyuvsim.source.SkyModel(names, ra, dec, freq, stokes)

    time = Time('2018-03-01 00:00:00', scale='utc')

    array_location = EarthLocation(lat='0.0d', lon='21d25m41.9s',
                                   height=1073.)
    sky.update_positions(time, array_location)
    coh_loc = sky.coherency_calc(array_location)

    inds = np.ones(Ncomp).astype(bool)
    inds[Ncomp // 2:] = False

    pol_srcs_up = (sky.alt_az[0] > 0) * inds
    unpol_srcs_up = (sky.alt_az[0] > 0) * (~inds)

    nt.assert_true(np.allclose(coh_loc[0, 0, unpol_srcs_up], 0.5))
    nt.assert_true(np.allclose(coh_loc[1, 1, unpol_srcs_up], 0.5))
    nt.assert_true(np.allclose(coh_loc[1, 0, unpol_srcs_up], 0.0))
    nt.assert_true(np.allclose(coh_loc[0, 1, unpol_srcs_up], 0.0))
