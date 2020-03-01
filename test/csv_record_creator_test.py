import pytest
from unittest.mock import MagicMock
from src.csv_record_creator import CsvRecordCreator

thing = ProductionClass()
thing.method = MagicMock(return_value=3)
thing.method(3, 4, 5, key='value')