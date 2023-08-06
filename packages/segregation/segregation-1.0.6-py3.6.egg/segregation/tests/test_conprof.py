import unittest
import libpysal
import geopandas as gpd
import numpy as np
from segregation.aspatial import Con_Prof


class Con_Prof_Tester(unittest.TestCase):
    def test_Con_Prof(self):
        s_map = gpd.read_file(libpysal.examples.get_path("sacramentot2.shp"))
        df = s_map[['geometry', 'HISP_', 'TOT_POP']]
        index = Con_Prof(df, 'HISP_', 'TOT_POP')
        np.testing.assert_almost_equal(index.statistic, 0.1376874794741899)


if __name__ == '__main__':
    unittest.main()
