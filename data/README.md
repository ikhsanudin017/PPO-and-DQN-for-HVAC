# Dataset

The experiments use the original IoT sensor dataset `sensor_data.csv`, containing 2,027,520 raw observations collected through a Raspberry Pi gateway.

The raw dataset is **not included in this Git repository** because of its file size and because the electrical measurements come from the household electrical supply rather than a dedicated HVAC circuit.

## Expected columns

- `Timestamp`
- `DeviceID`
- `Suhu (C)`
- `Kelembaban (%)`
- `Tegangan (V)`
- `Arus (A)`
- `Daya (W)`
- `Jumlah Orang`

## Running locally

Place the dataset at the repository root as:

```text
sensor_data.csv
```

The final experiment notebook uses `Path('sensor_data.csv')` when it is run outside Google Colab.

The manuscript treats recorded electrical power as general household electrical load, not as a direct measurement of HVAC-only consumption. Simulated power and energy are environment-generated proxies used for controller comparison.
