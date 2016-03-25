"""Top-level objects and functions offered by the Skyfield library.

Importing this ``skyfield.api`` module causes Skyfield to load up the
default JPL planetary ephemeris ``de421`` and create planet objects like
``earth`` and ``mars`` that are ready for your use.

"""
from datetime import datetime
from math import pi
from .constants import tau
from .errors import DeprecationError
from .iokit import Loader
from .starlib import Star
from .timelib import T0, Time, Timescale, utc
from .toposlib import Topos
from .units import Angle
from .named_stars import NamedStar

load = Loader('.')

__all__ = ['Angle', 'Loader', 'NamedStar', 'Star',
           'T0', 'Time', 'Timescale', 'Topos', 'datetime',
           'load', 'utc', 'pi', 'tau']

# An attempt at friendliest-possible deprecations:

class DeprecatedPlanet(object):
    def __init__(self, name):
        self.name = name

    def __call__(self, jd):
        raise DeprecationError("""Skyfield no longer auto-loads the planets.

If you simply want your old Skyfield script to start working again,
downgrade to Skyfield version 0.4 using a command like:

        pip install skyfield==0.4

To upgrade your script to a modern version of Skyfield, find each place
that you loaded a body from the skyfield.api module and called it:

        from skyfield.api import {body}
        position = {body}(t)

Instead, load the ephemeris like DE421 explicitly, look up the body in
the ephemeris, and use the method at() to generate a position:

        from skyfield.api import load
        planets = load('de421.bsp')
        {body} = planets['{body}']
        position = {body}.at(t)

More documentation can be found at: http://rhodesmill.org/skyfield/"""
                               .format(body=self.name))

class DeprecatedEarth(DeprecatedPlanet):
    def topos(self, *args, **kw):
        raise DeprecationError("""Skyfield no longer auto-loads an ephemeris.

If you simply want your old Skyfield script to start working again,
downgrade to Skyfield version 0.4 using a command like:

        pip install skyfield==0.4

To upgrade your script to a modern version of Skyfield, find each place
you loaded the Earth from skyfield.api and called its topos() method:

        from skyfield.api import earth
        place = earth.topos(...)

Instead, load the ephemeris like DE421 explicitly, look up Earth in the
ephemeris, and use the method at() to generate a position:

        from skyfield.api import load
        planets = load('de421.bsp')
        earth = planets['earth']
        place = earth.topos(...)

More documentation can be found at: http://rhodesmill.org/skyfield/""")

sun = DeprecatedPlanet('sun')
moon = DeprecatedPlanet('moon')
mercury = DeprecatedPlanet('mercury')
venus = DeprecatedPlanet('venus')
earth = DeprecatedEarth('earth')
mars = DeprecatedPlanet('mars')
jupiter = DeprecatedPlanet('jupiter')
saturn = DeprecatedPlanet('saturn')
uranus = DeprecatedPlanet('uranus')
neptune = DeprecatedPlanet('neptune')
pluto = DeprecatedPlanet('pluto')

def now():
    raise DeprecationError("""Skyfield no longer supports a standalone now() function

If you need to quickly get an old Skyfield script working again, simply
downgrade to Skyfield version 0.6.1 using a command like:

        pip install skyfield==0.6.1

Skyfield used to provide a now() method returning the current time:

        t = now()                      # the old way

But this forced Skyfield to maintain secret global copies of several
time scale data files, that need to be downloaded and kept up to date.
Skyfield now makes the collection of data files explicit, and calls the
bundle of files a "Timescale" object.  You can create one with the
"load.timescale()" method and then call its now() method:

        from skyfield.api import load
        ts = load.timescale()
        t = ts.now()                   # the new way""")

class JulianDate(object):
    def __init__(self, *args, **kw):
        from skyfield.timelib import _JulianDate_deprecation_message
        raise DeprecationError(_JulianDate_deprecation_message)
