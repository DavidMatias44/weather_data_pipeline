from unittest.mock import MagicMock, patch

from pydantic import ValidationError
from pytest import raises

from src.main import main


@patch("src.main.insert_data")
@patch("src.main.fetch_data")
@patch("src.main.flat_raw_data")
@patch("src.main.Settings")
def test_main_success(
    mock_settings: MagicMock,
    mock_flat_raw_data: MagicMock,
    mock_fetch_data: MagicMock,
    mock_insert_data: MagicMock
) -> None:
    mock_settings_intance = MagicMock()
    mock_settings.return_value = mock_settings_intance

    main()

    mock_settings.assert_called_once()
    mock_fetch_data.assert_called_once()
    mock_flat_raw_data.assert_called_once()
    mock_insert_data.assert_called_once()


@patch("src.main.Settings")
def test_main_exits_on_validation_error(mock_settings: MagicMock) -> None:
    mock_settings.side_effect = ValidationError.from_exception_data("Settings", line_errors=[])

    with raises(SystemExit) as exc_info:
        main()

    assert exc_info.value.code == 1
