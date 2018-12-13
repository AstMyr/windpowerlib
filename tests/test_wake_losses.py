import pandas as pd
import numpy as np
import pytest
from pandas.util.testing import  assert_series_equal

from windpowerlib.wake_losses import reduce_wind_speed
import windpowerlib.wind_turbine as wt

class TestWakeLosses:

    def test_reduce_wind_speed(self):
        parameters = {'wind_speed': pd.Series(np.arange(0, 26, 1.0)),
                      'wind_efficiency_curve_name': 'dena_mean'}
        wind_speed_exp = pd.Series([
            0.0, 0.9949534234119396, 1.9897327884892086, 2.9843374545454546,
            3.807636264984227, 4.714931284760845, 5.642507531914893,
            6.607021108049704, 7.592423167192429, 8.59498170212766,
            9.606135658475111, 10.619828799086758, 11.641291957894737,
            12.674012890137966, 13.709490666666666, 14.742508260567297,
            15.773293013157893, 16.794615009724474, 17.817683032858028,
            18.85294996704484, 19.86509539493748, 20.858807854510186,
            21.854369681134507, 22.850700350710902, 23.85962037735849,
            24.958125])
        assert_series_equal(reduce_wind_speed(**parameters), wind_speed_exp)

        # Raise ValueError - misspelling
        with pytest.raises(ValueError):
            parameters['wind_efficiency_curve_name'] = 'misspelled'
            reduce_wind_speed(**parameters)
