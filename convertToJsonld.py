import json
import uuid

def convert_to_json_ld(json_data):
    # Define the context and other JSON-LD specific fields
    context = {
        "@context": "https://w3id.org/emmo/domain/battery/context",
        "schema": "http://schema.org/",
        "emmo": "http://emmo.info/emmo#"
    }

    # Initialize the JSON-LD data with the context and other fields
    json_ld_data = {
        "@context": context,
        "@id": str(uuid.uuid4()),
        "hasTask": []
    }

    # Include all elements from json_data that are not @context, parameters, or instructions
    for key, value in json_data.items():
        if key not in ["@context", "parameters", "instructions"]:
            json_ld_data[key] = value

    # Extract parameters
    parameters = json_data.get('parameters', {})

    # Function to create a measurement parameter
    def create_measurement_parameter(type_, value, unit):
        return {
            "@type": type_,
            "hasNumericalPart": {
                "@type": "Real",
                "hasNumericalValue": value
            },
            "hasMeasurementUnit": unit
        }

    # Function to map the JSON elements to JSON-LD structure
    def map_to_json_ld(step):
        task = {}
        if step['@type'] == 'ElectricCurrent':
            numerical_value = step['hasNumericalValue']
            if not isinstance(numerical_value, (int, float)):
                numerical_value = parameters.get(numerical_value, numerical_value)
            unit=step['hasMeasurementUnit']
            if unit in "CRate":
                unit="emmo:AmperePerAmpereHour"
            termination_unit=step['termination'][0]['hasMeasurementUnit']
            if termination_unit == "CRate":
                termination_unit="emmo:AmperePerAmpereHour"
            task = {
                "@type": "ConstantCurrentCharging" if numerical_value < 0 else "ConstantCurrentDischarging",
                "hasMeasurementParameter": [
                    create_measurement_parameter("ChargingCurrent" if numerical_value < 0 else "DischargingCurrent", abs(numerical_value), unit),
                    create_measurement_parameter("UpperVoltageLimit" if numerical_value < 0 else "LowerVoltageLimit", parameters.get(step['termination'][0]['hasNumericalValue'], step['termination'][0]['hasNumericalValue']), termination_unit)
                ]
            }
        elif step['@type'] == 'Voltage':
            numerical_value = step['hasNumericalValue']
            if not isinstance(numerical_value, (int, float)):
                numerical_value = parameters.get(numerical_value, numerical_value)
            task = {
                "@type": "ConstantVoltageCharging",
                "hasMeasurementParameter": [
                    create_measurement_parameter("Voltage", numerical_value, step['hasMeasurementUnit']),
                    create_measurement_parameter("CurrentLimit", parameters.get(step['termination'][0]['hasNumericalValue'], step['termination'][0]['hasNumericalValue']), step['termination'][0]['hasMeasurementUnit'])
                ]
            }
        elif step['@type'] == 'rest':
            numerical_value = step['hasNumericalValue']
            if not isinstance(numerical_value, (int, float)):
                numerical_value = parameters.get(numerical_value, numerical_value)
            task = {
                "@type": "InternalStep",
                "hasMeasurementParameter": [
                    create_measurement_parameter("RestingTime", numerical_value, step['hasMeasurementUnit'])
                ]
            }
        return task

    # Process the instructions
    for instruction in json_data.get('instructions', []):
        previous_task = None
        first_task = None
        for i, step in enumerate(instruction.get('sequence', [])):
            task = map_to_json_ld(step)
            if i == 0:
                first_task = task
            else:
                if 'hasNext' not in previous_task:
                    previous_task['hasNext'] = []
                previous_task['hasNext'].append(task)
            previous_task = task
        
        top_task = {
            "@type": ["CCCVCycling", "IterativeWorkflow"],
            "rdfs:label": instruction.get('name'),
            "hasMeasurementParameter": create_measurement_parameter("IterativeStep", instruction.get('repeat'), "emmo:UnitOne"),
            "hasTask": first_task
        }
        
        json_ld_data['hasTask'].append(top_task)

    return json_ld_data
