# BCL
Battery Cycling language

## Study of BCL structure

Example snippet of a Json file with BCL structure

```
{
  "parameters": {
    "Capacity": 2.5,
    "UpperCutoffVoltage": 4.2
  },
  "instructions": [
    {
      "sequence": [
        {
          "type": "current",
          "value": -1,
          "unit": "C",
          "termination": [
            {
              "type": "voltage",
              "value": "UpperCutoffVoltage"
            }
          ]
        }
      ]
    }
  ]
}
```


## Metadata

The optional ``Metadata`` section should contain additional information about the cell/battery.

| Property  | Type | Description |
| ------------- | ------------- | -------------|
| Description  | str | Optional. Brief description of the synthesis.
| UniqueIdentifier  | str | Optional. For example with UUID.
| AnodeChemistry | str | Optional. Chemistry of the [anode](https://emmo-repo.github.io/domain-electrochemistry/electrochemistry.html#electrochemistry_b6319c74_d2ce_48c0_a75a_63156776b302) 
| CathodeChemistry | str | Optional. Chemistry of the [cathode](http://emmo.info/electrochemistry#electrochemistry_35c650ab_3b23_4938_b312_1b0dede2e6d5)

## Hardware

The optional ``Hardware`` section should contain extra information about the equipment the test was performed on or is intended to run on.

| Property  | Type | Description |
| ------------- | ------------- | -------------|
| Manufacturer  | str | Optional. Manufacturer of the test equipment.
| Maximum Current  | str | Optional. Maximum current of the test equipment.
| Current Accuracy  | str | Optional. Accuracy of the current measurement of a calibrated device according to the manufacturer.

## Parameters

The  ``Parameters`` section defines parameters of the battery to be used in the test.

| Property  | Type | Description |
| ------------- | ------------- | -------------|
| Capacity  | float | Nominal or rated [Capacity](http://emmo.info/battery#battery_df6bdaa9_5275_4a02_a592_adafd4e5c3c3) in Ah of either battery. Necessary to use C-Rates.
| NumberOfCellsConnectedInSeries | int | How many cells are in [series](http://emmo.info/electrochemistry#electrochemistry_9d6a52ed_a53d_4327_a391_f173677a4b1d) . If single cell, it is 1.
| StandardVoltageCell | float | Nominal or [standard voltage](http://emmo.info/battery#battery_3fcdc2ab_f458_4940_b218_6a10d1764567)
| LowerCutoffVoltage | float | Optional. Minimum cell [voltage](http://emmo.info/electrochemistry#electrochemistry_7e53fa42_cf93_4d6e_b753_6f0ef3034648) limit at which an applied signal is reversed or terminated.
| UpperCutoffVoltage| float | Optional. [Voltage](http://emmo.info/electrochemistry#electrochemistry_6dcd5baf_58cd_43f5_a692_51508e036c88) in V attained at the end of a charging step.

## Instructions for BatteryCycling

All steps included may be given within the [``BatteryCycling``](http://emmo.info/battery#battery_1d33b96d_f362_41e5_b670_d33cd6a7ab28) block of a BCL file.

The instruction consists of sequences. Sequences can have loops but the default is no repetition (1).

There are several types of blocks within a sequence: "current", "voltage", "rest", "power", or "resistance"

### Block within a sequence

| Property  | Type | Description |
| ------------- | ------------- | -------------|
| type | string | "current", "voltage", "rest", "power", or "resistance"
| value | float | value of the block
| unit | float | (optional) standard units: current:A, voltage:V, rest:sec, power:W, resistance:Ohm
| termination | block | see below
| duration | float | (optional) time in seconds
| period | float | (optional) time in seconds
| temperature | float | (optional) time in seconds

### Termination

| Property  | Type | Description |
| ------------- | ------------- | -------------|
| value | float | value of the block
| unit | float | example current:A, voltage:V, time:sec

## Acknowledgement

This work is influenced by:

[Pybamm](https://github.com/pybamm-team/PyBaMM)

[BattINFO](https://emmo-repo.github.io/domain-battery/index.html)