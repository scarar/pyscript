"""Mock module that emulates some of the pyodide js module features for the sake of tests"""
from unittest.mock import Mock

create_proxy = Mock(side_effect=lambda x: x)
