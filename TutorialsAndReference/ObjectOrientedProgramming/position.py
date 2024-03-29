class Position:

    def __init__(self, latitude, longitude):
        if not (-90 <= latitude <= +90):
            raise ValueError(f"Latitude {latitude} out of range")

        if not (-180 <= longitude <= +180):
            raise ValueError(f"Longitude {longitude} out of range")
        self._latitude = latitude
        self._longitude = longitude

    @property
    def latitude(self):
        return self._latitude

    @property
    def longitude(self):
        return self._longitude

    @property
    def latitude_hemisphere(self):
        return "N" if self.latitude >= 0 else "S"

    @property
    def longitude_hemisphere(self):
        return "E" if self.longitude >= 0 else "W"

    def __repr__(self):
        # repr if for the developer, this will keep the type representation- a string will show as one 'string'
        # include necessary state, format like code
        # f"{var=}" = repr output
        return f"{type(self).__name__}(latitude={self.latitude},longitude={self.longitude})"

    def __str__(self):
        # defaults to repr implementation
        # str if for the users or other systems (consumers)
        return format(self)

    def __format__(self, format_spec):
        # defaults to str implementation
        component_format_spec = ".2f"
        prefix, dot, suffix = format_spec.partition('.')
        if dot:
            num_decimal_places = int(suffix)
            component_format_spec = f"{num_decimal_places}f"

        latitude = format(abs(self.latitude), component_format_spec)
        longitude = format(abs(self.longitude), component_format_spec)
        return (
            f"{latitude}° {self.latitude_hemisphere}, "
            f"{longitude}° {self.longitude_hemisphere}"
        )


class EarthPosition(Position):
    pass


class MarsPosition(Position):
    pass
