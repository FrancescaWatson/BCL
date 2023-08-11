# BCL
Battery Cycling language

## Stud of BCL structure

```
    <BCL>
        <Experiment>
            <Metadata>
                <!-- ... -->
            </Metadata>

            <Hardware>
                <!-- ... -->
            </Hardware>

            <Parameters>
                <!-- ... -->
            </Parameters>

            <BatteryCycling>
                <!-- ... -->
            </BatteryCycling>
        </Experiment>
    </BCL>
```


## Metadata

The optional ``Metadata`` section should contain extra information about the cell/battery.

| Property  | Type | Description |
| ------------- | ------------- | -------------|
| Description  | str | Optional. Brief description of the synthesis.
| UniqueIdentifier  | str | Optional. For example with UUID.
| AnodeChemistry | str | Optional. Chemistry of the [anode](https://emmo-repo.github.io/domain-electrochemistry/electrochemistry.html#electrochemistry_b6319c74_d2ce_48c0_a75a_63156776b302) 
| CathodeChemistry | str | Optional. Chemistry of the [cathode](http://emmo.info/electrochemistry#electrochemistry_35c650ab_3b23_4938_b312_1b0dede2e6d5)

## Hardware

The optional ``Hardware`` section should contain extra information about the test equipment the test was performed on or is intended to run on.

| Property  | Type | Description |
| ------------- | ------------- | -------------|
| Manufacturer  | str | Optional. Manufacturer of the test equipment.
| Maximum Current  | str | Optional. Maximum current of the test equipment.
| Current accuracy  | str | Optional. Accuracy of the current measurement of a calibrated device according to the manufacturer.

## Parameters

The  ``Parameters`` section defines parameters of the battery to be used in the test.

| Property  | Type | Description |
| ------------- | ------------- | -------------|
| Capacity  | float | nominal or rated [Capacity](http://emmo.info/battery#battery_df6bdaa9_5275_4a02_a592_adafd4e5c3c3) in Ah of either battery or cell. Necessary to use C-Rates.
| NumberOfCellsConnectedInSeries | int | How many cells are in [series](http://emmo.info/electrochemistry#electrochemistry_9d6a52ed_a53d_4327_a391_f173677a4b1d) . If single cell, it is 1.
| StandardVoltageCell | float | Nominal or [standard voltage](http://emmo.info/battery#battery_3fcdc2ab_f458_4940_b218_6a10d1764567)
| LowerCutoffVoltage | float | Optional. Minimum cell [voltage](http://emmo.info/electrochemistry#electrochemistry_7e53fa42_cf93_4d6e_b753_6f0ef3034648) limit at which an applied signal is reversed or terminated.
| UpperCutoffVoltage| float | Optional. [Voltage](http://emmo.info/electrochemistry#electrochemistry_6dcd5baf_58cd_43f5_a692_51508e036c88) in V attained at the end of a charging step.

## BatteryCycling

All steps included in the Full Steps Specification may be given within the [``BatteryCycling``](http://emmo.info/battery#battery_1d33b96d_f362_41e5_b670_d33cd6a7ab28) block of a BCL file.

Steps follow a structure of "Do this for this long" or "Do this until this happens"

```
Examples:
Charge at 1 C for 1 hour
Charge at 1 C until 4.2 V
Charge at 1 C for 1 hour or until 4.2 V
```


Type can be "current", "voltage", "cccv_ode" or "rest", "power", or "resistance"

Value	
Unit	
Duration	
Termination
Period
Temperature




### Charge

| Property  | Type | Description |
| ------------- | ------------- | -------------|
| ChargingCurrent | float | Electric current delivered by a battery during its [Charge](http://emmo.info/electrochemistry#electrochemistry_79551e01_4bc6_4292_916e_08fe28a84600).
| UpperVoltageLimit | float | Maximum cell [voltage](http://emmo.info/electrochemistry#electrochemistry_88d6d177_4b76_4b0a_9a65_aef6592cdb8f) in V limit at which an applied signal is reversed or terminated.
| time | float | time in seconds, minutes or hours to rest.
| CurrentInCRate | bool | If not set, default is 0 and current in A.


### Discharge

| Property  | Type | Description |
| ------------- | ------------- | -------------|
| DischargeCurrent | float | Electric current delivered by a battery during its [Discharge](http://emmo.info/electrochemistry#electrochemistry_e4d666ee_d637_45cd_a904_dc33941ead4f).
| LowerVoltageLimit | float | Minimum cell [voltage](http://emmo.info/electrochemistry#electrochemistry_7e53fa42_cf93_4d6e_b753_6f0ef3034648) in V limit at which an applied signal is reversed or terminated.
| time | float | time in seconds, minutes or hours to rest.
| CurrentInCRate | bool | If not set, default is 0 and current in A.


### Hold

| Property  | Type | Description |
| ------------- | ------------- | -------------|
| SetVoltage | float | [Voltage](http://emmo.info/electrochemistry#electrochemistry_8427071b_3a01_44b8_9090_5ae0d98675b5) level to hold.
| CutOffCurrent | float | Cut off current in A or C/Rate.
| time | float | time in seconds, minutes or hours to rest.
| CurrentInCRate | bool | If not set, default is 0 and current in A.

### Special

Rest
| Property  | Type | Description |
| ------------- | ------------- | -------------|
| time | float | time in seconds, minutes or hours to rest.


## Acknowledgement

This work is influenced by:

[Pybamm](https://github.com/pybamm-team/PyBaMM)

[BattINFO](https://emmo-repo.github.io/domain-battery/index.html)

[XDL](https://croningroup.gitlab.io/chemputer/xdl/index.html)