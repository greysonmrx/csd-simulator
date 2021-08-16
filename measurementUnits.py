class MeasurementUnits:
    def convert(self, value, _from, _to):
        measurementUnits = {
            'byte': 1,
            'kilobyte': 2,
            'megabyte': 3,
            'gigabyte': 4,
            'terabyte': 5,
            'petabyte': 6,
            'exabyte': 7,
            'zettabyte': 8,
            'yotabyte': 9
        }

        fromMeasurementUnit = measurementUnits[_from]
        toMeasurementUnit = measurementUnits[_to]

        if (fromMeasurementUnit > toMeasurementUnit):
            return value * (1000 * (fromMeasurementUnit - toMeasurementUnit))
        elif (fromMeasurementUnit < toMeasurementUnit):
            return value / (1000 * (toMeasurementUnit - fromMeasurementUnit))
        else:
            return value