from unittest.mock import MagicMock, patch

from src.database import create_connection


@patch("src.database.psycopg2.connect")
def test_create_connection_success(mock_connect: MagicMock) -> None:
    mock_conn = MagicMock()
    mock_connect.return_value = mock_conn
    test_params = {
        "dbname": "db",
        "user": "user",
        "password": "pass",
        "host": "localhost",
        "port": 5432
    }

    result = create_connection(params=test_params)

    mock_connect.assert_called_once_with(
        dbname="db",
        user="user",
        password="pass",
        host="localhost",
        port=5432
    )
    assert result == mock_conn
