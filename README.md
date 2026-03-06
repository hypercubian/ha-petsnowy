<p align="center">
  <img src="images/logo.png" alt="PetSnowy" width="200">
</p>

<h1 align="center">PetSnowy for Home Assistant</h1>

<p align="center">
  Custom <a href="https://www.home-assistant.io/">Home Assistant</a> integration for local-network control of <a href="https://www.petsnowy.com/">PetSnowy</a> smart pet devices via the Tuya protocol.<br>
  No cloud dependency - all communication stays on your LAN.
</p>

<p align="center">
  <a href="https://github.com/hypercubian/ha-petsnowy/releases"><img src="https://img.shields.io/github/v/release/hypercubian/ha-petsnowy?filter=*&style=for-the-badge" alt="Release"></a>
  <a href="https://github.com/hypercubian/ha-petsnowy/releases"><img src="https://img.shields.io/github/downloads/hypercubian/ha-petsnowy/total?style=for-the-badge" alt="Downloads"></a>
  <a href="https://github.com/hypercubian/ha-petsnowy/stargazers"><img src="https://img.shields.io/github/stars/hypercubian/ha-petsnowy?style=for-the-badge" alt="Stars"></a>
  <a href="LICENSE"><img src="https://img.shields.io/github/license/hypercubian/ha-petsnowy?style=for-the-badge&cacheSeconds=0" alt="License"></a>
</p>
<p align="center">
  <a href="https://hacs.xyz/"><img src="https://img.shields.io/badge/HACS-Custom-41BDF5?style=for-the-badge" alt="HACS Custom"></a>
  <img src="https://img.shields.io/badge/HA-%3E%3D%202024.8-41BDF5?style=for-the-badge" alt="Home Assistant 2024.8+">
  <a href="https://github.com/hypercubian/ha-petsnowy/actions/workflows/ci.yml"><img src="https://img.shields.io/github/actions/workflow/status/hypercubian/ha-petsnowy/ci.yml?branch=main&style=for-the-badge&label=CI" alt="CI"></a>
  <a href="https://github.com/psf/black"><img src="https://img.shields.io/badge/code%20style-black-000000?style=for-the-badge" alt="Code style: black"></a>
  <a href="https://mypy-lang.org/"><img src="https://img.shields.io/badge/type%20checked-mypy-blue?style=for-the-badge" alt="Type checked: mypy"></a>
</p>

<p align="center">
  <a href="https://my.home-assistant.io/redirect/hacs_repository/?owner=hypercubian&repository=ha-petsnowy&category=integration">
    <img src="https://my.home-assistant.io/badges/hacs_repository.svg" alt="Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.">
  </a>
</p>

<br>
<br>
<br>

<p align="right">
  <a href="https://github.com/hypercubian"><img src="images/hypercubian.png" height="60" alt="by Hypercubian"></a>
</p>

---

## Supported Devices

| Device | Product Name | Model | Protocol | Description |
|--------|-------------|-------|----------|-------------|
| **Self-Cleaning Litter Box** | SNOW+ Automatic Self-Cleaning Litter Box | PS-001 | 3.4 | Smart litter box with auto-clean, deodorization, cat weight tracking, and safety sensors |
| **Water Fountain** | SNOW+ Automatic Pet Water Fountain | PS-010 | 3.3 | Filtered water fountain with normal/night modes and pump monitoring |
| **Air Purifier** | PETSNOWY Pet Air Purifier | - | 3.4 | TVOC-sensing air purifier with 6-speed fan, ionizer, and auto-off timer |
| **Pet Feeder** | SNOW+ Automatic Pet Feeder | PS-020 | 3.3 | Automatic feeder with food level detection and on-demand dispensing |

> **Note:** The OilClear A.I Series Wireless Weight-Sensing Pet Fountain is a newer model and is not yet supported. Contributions welcome!

## Installation

### HACS (Recommended)

> **Don't have HACS?** Follow the [official HACS installation guide](https://hacs.xyz/docs/use/download/download/) first, then [activate the integration](docs/hacs-setup.md).

1. Open HACS in your Home Assistant instance
2. Go to **Integrations** > three-dot menu > **Custom repositories**
3. Add `https://github.com/hypercubian/ha-petsnowy` with category **Integration**
4. Search for "PetSnowy" and install
5. Restart Home Assistant

### Manual

1. Copy the `custom_components/petsnowy` directory into your Home Assistant `config/custom_components/` folder
2. Restart Home Assistant

## Configuration

1. Go to **Settings** > **Devices & Services** > **Add Integration**
2. Search for **PetSnowy**
3. Select your device type (Litterbox, Fountain, Purifier, or Feeder)
4. Enter the Tuya credentials for your device:
   - **Device ID** - Tuya device identifier
   - **IP Address** - local network address of the device
   - **Local Key** - Tuya local encryption key
   - **Protocol Version** - auto-filled based on device type (3.3 or 3.4)

The integration validates connectivity before completing setup.

### Obtaining Tuya Credentials

You need the Device ID, IP address, and Local Key for each device. These can be obtained using the [tinytuya](https://github.com/jasonacox/tinytuya) wizard:

```bash
pip install tinytuya
python -m tinytuya wizard
```

Follow the wizard prompts - you'll need a [Tuya IoT Platform](https://iot.tuya.com/) account linked to your PetSnowy app account.

## Entities

### SNOW+ Self-Cleaning Litter Box (PS-001)

| Platform | Entities |
|----------|----------|
| **Sensor** | Cat weight (g), excretion count today, excretion duration today (s), filter days remaining, status (standby/cleaning/deodorization/sleep) |
| **Binary Sensor** | Top cover fault, drawer fault, drawer full, cat stuck, check fault, cat stayed too long, trouble removal |
| **Switch** | Auto clean, sleep mode, indicator light, child lock, auto deodorize |
| **Button** | Clean, deodorize, empty litter, cancel empty, pause, resume, reset filter, calibrate weight |
| **Number** | Clean delay (2–60 min, step 2) |

### SNOW+ Water Fountain (PS-010)

| Platform | Entities |
|----------|----------|
| **Sensor** | Filter days, pump cleaning days |
| **Switch** | Power, indicator light |
| **Button** | Reset filter, reset pump |
| **Number** | Filter reminder (0–90 days) |
| **Select** | Work mode (normal/night) |

### PETSNOWY Air Purifier

| Platform | Entities |
|----------|----------|
| **Sensor** | TVOC (µg/m³), filter days, countdown remaining (min) |
| **Binary Sensor** | Hall sensor fault, toppled over, fan fault, filter missing |
| **Switch** | Power, ionizer |
| **Select** | Mode (auto/sleep), fan speed (1–6), auto-off countdown (off/1h–5h) |

### SNOW+ Pet Feeder (PS-020)

| Platform | Entities |
|----------|----------|
| **Sensor** | Food status (enough/insufficient) |
| **Binary Sensor** | Cover (opening detection) |
| **Button** | Quick feed (1 portion) |

## Technical Details

- **Communication:** Local Tuya protocol via [tinytuya](https://github.com/jasonacox/tinytuya) - no cloud polling
- **Connection:** Persistent TCP with automatic reconnection on errors
- **Polling:** 30-second update interval via `DataUpdateCoordinator`
- **Library:** [petsnowy-py](https://github.com/hypercubian/petsnowy-py) - async Python library for PetSnowy devices

## Contributing

1. Clone the repo
2. Install dependencies: `poetry install`
3. Install pre-commit hooks: `poetry run pre-commit install`
4. Run tests: `poetry run pytest tests/unit/`

## License

[MIT](LICENSE)
