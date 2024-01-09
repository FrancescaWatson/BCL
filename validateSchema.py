# python validateSchema.py 'sampleConfig.json'

import json
import sys
from jsonschema import validate
from jsonschema.exceptions import ValidationError

schema = {
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "@context": {
      "type": "object",
      "additionalProperties": {
        "type": "string",
        "format": "uri"
      }
    },
    "parameters": {
      "type": "object",
      "properties": {
        "Capacity": {"type": "number"},
        "NumberOfCellsConnectedInSeries": {"type": "integer"},
        "StandardVoltageCell": {"type": "number"},
        "LowerCutoffVoltage": {"type": "number", "default": 3},
        "UpperCutoffVoltage": {"type": "number", "default": 4.2},
        "Temperature": {"type": "number", "default": 25},
        "Period": {"type": "number", "default": 10}
      },
      "required": ["Capacity", "NumberOfCellsConnectedInSeries", "StandardVoltageCell"]
    },
    "instructions": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "name": {"type": "string"},
          "repeat": {"type": "integer"},
          "sequence": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "type": {"type": "string"},
                "value": {"type": ["number","string"]},
                "unit": {"type": "string"},
                "time": {"type": "number"},
                "termination": {
                  "type": "array",
                  "items": {
                    "type": "object",
                    "properties": {
                      "type": {"type": "string"},
                      "value": {"type": ["number","string"]}
                    },
                    "required": ["type", "value"]
                  }
                },
                "duration": {"type": "number"},
                "period": {"type": "number"},
                "temperature": {"type": "number"},
              },
              "required": ["type", "value"]
            }
          }
        },
        "required": ["name", "sequence"]
      }
    },
    "DefaultUnits": {
      "type": "object",
      "properties": {
        "current": {"type": "string", "default": "A"},
        "voltage": {"type": "string", "default": "V"},
        "time": {"type": "string", "default": "sec"},
        "resistance": {"type": "string", "default": "Ohm"},
        "power": {"type": "string", "default": "W"},
        "temperature": {"type": "string", "default": "degC"}
      }
    }
  },
  "additionalProperties": False,
  "required": ["@context", "parameters", "instructions"]
}



# Function to validate JSON
def validate_json(json_data):
    try:
        validate(instance=json_data, schema=schema)
        print("JSON data is valid")
    except ValidationError as ve:
        print(f"JSON data is invalid: {ve}")

# Load and validate your JSON file
try:
    if len(sys.argv) > 1:    
        with open(sys.argv[1], 'r') as file:
            data = json.load(file)
            validate_json(data)
    else:
        print("No argument received.")
except json.JSONDecodeError as e:
    print(f"Invalid JSON: {e}")
except FileNotFoundError:
    print("JSON file not found")
