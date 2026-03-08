"""Unit tests for entity description completeness."""

from __future__ import annotations

import pytest

from custom_components.petsnowy.binary_sensor import _BINARY_SENSORS_BY_TYPE
from custom_components.petsnowy.button import _BUTTONS_BY_TYPE
from custom_components.petsnowy.const import (
    DEVICE_TYPE_FEEDER,
    DEVICE_TYPE_FOUNTAIN,
    DEVICE_TYPE_LITTERBOX,
    DEVICE_TYPE_PURIFIER,
)
from custom_components.petsnowy.number import _NUMBERS_BY_TYPE
from custom_components.petsnowy.select import _SELECTS_BY_TYPE
from custom_components.petsnowy.sensor import _SENSORS_BY_TYPE
from custom_components.petsnowy.switch import _SWITCHES_BY_TYPE


class TestLitterboxEntities:
    """Validate litterbox entity descriptions are complete."""

    def test_has_sensors(self) -> None:
        """Litterbox exposes sensors."""
        assert len(_SENSORS_BY_TYPE[DEVICE_TYPE_LITTERBOX]) == 6

    def test_has_switches(self) -> None:
        """Litterbox exposes switches."""
        assert len(_SWITCHES_BY_TYPE[DEVICE_TYPE_LITTERBOX]) == 7

    def test_has_buttons(self) -> None:
        """Litterbox exposes action buttons."""
        assert len(_BUTTONS_BY_TYPE[DEVICE_TYPE_LITTERBOX]) == 8

    def test_has_binary_sensors(self) -> None:
        """Litterbox exposes fault and occupancy binary sensors."""
        assert len(_BINARY_SENSORS_BY_TYPE[DEVICE_TYPE_LITTERBOX]) == 8

    def test_has_numbers(self) -> None:
        """Litterbox exposes number entities."""
        assert len(_NUMBERS_BY_TYPE[DEVICE_TYPE_LITTERBOX]) == 1


class TestFountainEntities:
    """Validate fountain entity descriptions are complete."""

    def test_has_sensors(self) -> None:
        """Fountain exposes sensors."""
        assert len(_SENSORS_BY_TYPE[DEVICE_TYPE_FOUNTAIN]) == 2

    def test_has_switches(self) -> None:
        """Fountain exposes switches."""
        assert len(_SWITCHES_BY_TYPE[DEVICE_TYPE_FOUNTAIN]) == 2

    def test_has_buttons(self) -> None:
        """Fountain exposes action buttons."""
        assert len(_BUTTONS_BY_TYPE[DEVICE_TYPE_FOUNTAIN]) == 2

    def test_has_selects(self) -> None:
        """Fountain exposes select entities."""
        assert len(_SELECTS_BY_TYPE[DEVICE_TYPE_FOUNTAIN]) == 1

    def test_has_numbers(self) -> None:
        """Fountain exposes number entities."""
        assert len(_NUMBERS_BY_TYPE[DEVICE_TYPE_FOUNTAIN]) == 1


class TestPurifierEntities:
    """Validate purifier entity descriptions are complete."""

    def test_has_sensors(self) -> None:
        """Purifier exposes sensors."""
        assert len(_SENSORS_BY_TYPE[DEVICE_TYPE_PURIFIER]) == 3

    def test_has_switches(self) -> None:
        """Purifier exposes switches."""
        assert len(_SWITCHES_BY_TYPE[DEVICE_TYPE_PURIFIER]) == 1

    def test_has_binary_sensors(self) -> None:
        """Purifier exposes fault binary sensors."""
        assert len(_BINARY_SENSORS_BY_TYPE[DEVICE_TYPE_PURIFIER]) == 4

    def test_has_selects(self) -> None:
        """Purifier exposes select entities."""
        assert len(_SELECTS_BY_TYPE[DEVICE_TYPE_PURIFIER]) == 1


class TestFeederEntities:
    """Validate feeder entity descriptions are complete."""

    def test_has_sensors(self) -> None:
        """Feeder exposes sensors."""
        assert len(_SENSORS_BY_TYPE[DEVICE_TYPE_FEEDER]) == 1

    def test_has_buttons(self) -> None:
        """Feeder exposes action buttons."""
        assert len(_BUTTONS_BY_TYPE[DEVICE_TYPE_FEEDER]) == 1

    def test_has_binary_sensors(self) -> None:
        """Feeder exposes binary sensors."""
        assert len(_BINARY_SENSORS_BY_TYPE[DEVICE_TYPE_FEEDER]) == 1


class TestUniqueKeys:
    """All entity keys within a device type must be unique."""

    @pytest.mark.parametrize(
        "device_type",
        [
            DEVICE_TYPE_LITTERBOX,
            DEVICE_TYPE_FOUNTAIN,
            DEVICE_TYPE_PURIFIER,
            DEVICE_TYPE_FEEDER,
        ],
    )
    def test_sensor_keys_unique(self, device_type: str) -> None:
        """Sensor keys are unique per device type."""
        descs = _SENSORS_BY_TYPE.get(device_type, ())
        keys = [d.key for d in descs]
        assert len(keys) == len(set(keys))

    @pytest.mark.parametrize(
        "device_type",
        [
            DEVICE_TYPE_LITTERBOX,
            DEVICE_TYPE_FOUNTAIN,
            DEVICE_TYPE_PURIFIER,
        ],
    )
    def test_switch_keys_unique(self, device_type: str) -> None:
        """Switch keys are unique per device type."""
        descs = _SWITCHES_BY_TYPE.get(device_type, ())
        keys = [d.key for d in descs]
        assert len(keys) == len(set(keys))

    @pytest.mark.parametrize(
        "device_type",
        [DEVICE_TYPE_LITTERBOX, DEVICE_TYPE_FOUNTAIN, DEVICE_TYPE_FEEDER],
    )
    def test_button_keys_unique(self, device_type: str) -> None:
        """Button keys are unique per device type."""
        descs = _BUTTONS_BY_TYPE.get(device_type, ())
        keys = [d.key for d in descs]
        assert len(keys) == len(set(keys))
