import unittest
from nose.tools import (assert_is_not_none, assert_raises, assert_equal)

from sknn.mlp import MultiLayerPerceptronRegressor as MLPR

from . import test_linear


class TestGaussianOutput(test_linear.TestLinearNetwork):

    def setUp(self):
        self.nn = MLPR(layers=[("LinearGaussian",)])