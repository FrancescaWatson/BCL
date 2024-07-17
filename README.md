# BCL
Battery Cycling Language

## Study of BCL Structure

### Example Snippet of a JSON File with BCL Structure

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
          "@type": "ElectricCurrent",
          "hasNumericalValue": -1,
          "hasMeasurementUnit": "CRate",
          "termination": [
            {
              "@type": "Voltage",
              "hasNumericalValue": "UpperCutoffVoltage",
              "hasMeasurementUnit": "emmo:Volt"
            }
          ]
        }
      ]
    }
  ],
    "schema:name": "MinimalExample",
}
```


### Example Snippet of the Linked JSON-LD Format

```
{
  "@context": "https://w3id.org/emmo/domain/battery/context",
  "schema:name": "Cyclelifecondition",
  "schema:subjectOf": "LG Chem INR18650 MJ1",
  "@id": "https://www.wikidata.org/wiki/Q120766894",
  "schema:citation": "Specification INR18650MJ1 22.08.2014.pdf",
  "description": "Example cycling procedure for a battery.",
  "uniqueIdentifier": "123e4567-e89b-12d3-a456-426614174000",
  "hasTask": [
    {
      "@type": ["ConstantCurrentConstantVoltageCycling", "IterativeWorkflow"],
      "rdfs:label": "HighDrainrateChargeDischargecondition",
      "rdfs:comment": "A cycling test using high drain rate",
      "hasMeasurementParameter": {
        "@type": "NumberOfIterations",
        "hasNumericalPart": {
          "@type": "Real",
          "hasNumericalValue": 400
        },
        "hasMeasurementUnit": "emmo:UnitOne"
      },
      "hasTask": {
        "@type": "ConstantCurrentCharging",
        "hasMeasurementParameter": [
          {
            "@type": "ChargingCurrent",
            "hasNumericalPart": {
              "@type": "Real",
              "hasNumericalValue": 1.5
            },
            "hasMeasurementUnit": "emmo:Ampere"
          },
          {
            "@type": "UpperVoltageLimit",
            "hasNumericalPart": {
              "@type": "Real",
              "hasNumericalValue": 4.2
            },
            "hasMeasurementUnit": "emmo:Volt"
          }
        ],
        "nextTask": [
          {
            "@type": "RestingStep",
            "hasMeasurementParameter": [
              {
                "@type": "RestingTime",
                "hasNumericalPart": {
                  "@type": "Real",
                  "hasNumericalValue": 600
                },
                "hasMeasurementUnit": "emmo:Second"
              }
            ],
            "nextTask": [
              {
                "@type": "ConstantCurrentDischarging",
                "hasMeasurementParameter": [
                  {
                    "@type": "DischargingCurrent",
                    "hasNumericalPart": {
                      "@type": "Real",
                      "hasNumericalValue": 4.0
                    },
                    "hasMeasurementUnit": "emmo:Ampere"
                  },
                  {
                    "@type": "LowerVoltageLimit",
                    "hasNumericalPart": {
                      "@type": "Real",
                      "hasNumericalValue": 2.5
                    },
                    "hasMeasurementUnit": "emmo:Volt"
                  }
                ]
              }
            ]
          }
        ]
      }
    }
  ]
}
```

## Metadata

The optional `Metadata` section should contain additional information about the cell/battery.

| Property          | Type | Description                                                                                      |
|-------------------|------|--------------------------------------------------------------------------------------------------|
| Description       | str  | Optional. Brief description of the synthesis.                                                    |
| UniqueIdentifier  | str  | Optional. For example with UUID.                                                                 |
| AnodeChemistry    | str  | Optional. Chemistry of the [anode](https://emmo-repo.github.io/domain-electrochemistry/electrochemistry.html#electrochemistry_b6319c74_d2ce_48c0_a75a_63156776b302) |
| CathodeChemistry  | str  | Optional. Chemistry of the [cathode](http://emmo.info/electrochemistry#electrochemistry_35c650ab_3b23_4938_b312_1b0dede2e6d5) |

## Hardware

The optional `Hardware` section should contain extra information about the equipment the test was performed on or is intended to run on.

| Property           | Type | Description                                                                   |
|--------------------|------|-------------------------------------------------------------------------------|
| Manufacturer       | str  | Optional. Manufacturer of the test equipment.                                 |
| Maximum Current    | str  | Optional. Maximum current of the test equipment.                              |
| Current Accuracy   | str  | Optional. Accuracy of the current measurement of a calibrated device according to the manufacturer. |

## Parameters

The `Parameters` section defines parameters of the battery to be used in the test.

| Property                   | Type  | Description                                                                                                                        |
|----------------------------|-------|------------------------------------------------------------------------------------------------------------------------------------|
| Capacity                   | float | Nominal or rated [Capacity](http://emmo.info/battery#battery_df6bdaa9_5275_4a02_a592_adafd4e5c3c3) in Ah of either battery. Necessary to use C-Rates. |
| NumberOfCellsConnectedInSeries | int   | How many cells are in [series](http://emmo.info/electrochemistry#electrochemistry_9d6a52ed_a53d_4327_a391_f173677a4b1d). If single cell, it is 1.  |
| StandardVoltageCell        | float | Nominal or [standard voltage](http://emmo.info/battery#battery_3fcdc2ab_f458_4940_b218_6a10d1764567)                                |
| LowerCutoffVoltage         | float | Optional. Minimum cell [voltage](http://emmo.info/electrochemistry#electrochemistry_7e53fa42_cf93_4d6e_b753_6f0ef3034648) limit at which an applied signal is reversed or terminated. |
| UpperCutoffVoltage         | float | Optional. [Voltage](http://emmo.info/electrochemistry#electrochemistry_6dcd5baf_58cd_43f5_a692_51508e036c88) in V attained at the end of a charging step. |

## Instructions for BatteryCycling

All steps included may be given within the [`BatteryCycling`](http://emmo.info/battery#battery_1d33b96d_f362_41e5_b670_d33cd6a7ab28) block of a BCL file.

The instruction consists of sequences. Sequences can have loops but the default is no repetition (1).

There are several types of blocks within a sequence: "current", "voltage", "rest", "power", or "resistance".

### Block within a Sequence

| Property   | Type   | Description                                                                 |
|------------|--------|-----------------------------------------------------------------------------|
| type       | string | "current", "voltage", "rest", "power", or "resistance"                      |
| value      | float  | Value of the block                                                          |
| unit       | string | (optional) Standard units: current:A, voltage:V, rest:sec, power:W, resistance:Ohm |
| termination| block  | See below                                                                   |
| duration   | float  | (optional) Time in seconds                                                  |
| period     | float  | (optional) Time in seconds                                                  |
| temperature| float  | (optional) Time in seconds                                                  |

### Termination

| Property | Type  | Description                                        |
|----------|-------|----------------------------------------------------|
| value    | float | Value of the block                                 |
| unit     | string| Example current:A, voltage:V, time:sec             |