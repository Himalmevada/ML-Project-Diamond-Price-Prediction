from sklearn.impute import SimpleImputer ## Handling Missing Value
from sklearn.preprocessing import StandardScaler ## Handling Feature Scaling
from sklearn.preprocessing import OrdinalEncoder ## Ordinal Encoding
## Pipelines
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
import numpy as np
import pandas as pd
from src.exception import CustomException
