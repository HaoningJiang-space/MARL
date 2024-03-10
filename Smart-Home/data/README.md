# Data

Download the data for solar panels here: https://www.nrel.gov/grid/solar-power-data.html

Naming Convention
The naming convention of the state-wise solar power data (.csv files) from the Solar Integration Studies is as follows.

Data Type\_Latitude\_Longitude\_Weather Year\_PV Type\_CapacityMW\_Time Interval \_Min.csv

- Data Type
    - Actual: Real power output
    - DA: Day ahead forecast
    - HA4: 4 hour ahead forecast
- Weather Year: The PV data is based on the particular year's known weather condition.
- PV Type
    - UPV: Utility scale PV
    - DPV: Distributed PV

Note: The practical difference between UPV and DPV is in the configurations (UPV has single axis tracking while DPV is fixed tilt equaling to latitude) and the smoothing (both are run through a low-pass filter, the DPV will have more of the high frequency variability smoothed out).

- Capacity: Installed capacity in MW
- Time Interval: PV generation data reading interval in minutes.

Download the data for electricity prices here: ?