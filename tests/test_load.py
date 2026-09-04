from unittest.mock import MagicMock, patch

import psycopg2
import pytest

from src.load import insert_data


@patch("src.load.create_connection")
def test_insert_data_success(mock_create_connection: MagicMock) -> None:
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
    mock_create_connection.return_value = mock_conn
    test_params = {
        "port": 5432,
        "schema": "public",
        "raw_data_table": "raw_weather"
    }
    test_records = [
        ["2026-09-03T00:00", 34.0258, -118.7804, 1500, 19.3, 5],
        ["2026-09-03T01:00", 34.0258, -118.7804, 1500, 18.7, 10]
    ]

    insert_data(params=test_params, records=test_records)

    mock_create_connection.assert_called_once_with(test_params)
    assert mock_cursor.execute.call_count == 2
    mock_conn.close.assert_called_once()


@patch("src.load.create_connection")
def test_insert_data_database_error(mock_create_connection: MagicMock) -> None:
    mock_conn = MagicMock()
    mock_cursor = MagicMock()
    mock_conn.cursor.return_value.__enter__.return_value = mock_cursor
    mock_create_connection.return_value = mock_conn
    mock_cursor.execute.side_effect = psycopg2.Error("Database error")
    test_params = {
        "port": 5432,
        "schema": "public",
        "raw_data_table": "raw_weather"
    }
    test_records = [
        ["2026-09-03T00:00", 34.0258, -118.7804, 1500, 19.3, 5],
        ["2026-09-03T01:00", 34.0258, -118.7804, 1500, 18.7, 10]
    ]

    with pytest.raises(psycopg2.Error):
        insert_data(params=test_params, records=test_records)

    mock_conn.close.assert_called_once()
