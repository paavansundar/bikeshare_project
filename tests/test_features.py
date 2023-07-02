"""
Note: These tests will fail if you have not first trained the model.
"""
import sys
from pathlib import Path
file = Path(__file__).resolve()
parent, root = file.parent, file.parents[1]
sys.path.append(str(root))

import numpy as np
from bikeshare_model.config.core import config
from bikeshare_model.predict import make_prediction


def test_age_variable_transformer():
    data_in = {'dteday': ['2012-11-6'], 'season': ['winter'], 'hr': ['6pm'], 'holiday': ['No'], 'weekday': ['Tue'],
               'workingday': ['Yes'], 'weathersit': ['Clear'], 'temp': [16], 'atemp': [17.5], 'hum': [30], 'windspeed': [10]}

    predict=make_prediction(input_data = data_in)
    # Then
    assert len(predict['predictions']) > 0
