def period(radius=10, m1=2.959139768995959E-04, m2=2.959139768995959E-04):
     """
     Return the period in days of the binary star system

     Usage: p = period(radius, m1, m2)
     Where (for circular motion):
     <radius> is the distance in AU between the two stars
     <m1> is the mass of the primary star
     <m2> is the mass of the secondary star
     mass unit: 1 Solar mass = 2.959139768995959E-04

     Example:
     p = period()

     """
     import math
     pi = math.pi
     period = 2 * pi * math.sqrt( math.pow(radius,3) / ( m1 + m2 ) )
     print "Binary period period: " + str(period) + " days"
     return period

def vstar(R_AB, massRatio):
   """
   Return the velocity of the Secondary Star (m2) from the primary star m2 (1 solar mass) in a circular orbit.

   velocity = np.sqrt( ( G * ( 1. + mass ) ) / R_AB )
   In the swifter units G = 1

   Usage: velocity = vstar( R_AB, massRatio)
   Where:
   R_AB is the distance in AU between the two stars
   massRation = m2 / (m1 + m2) (m1 = 1)
   velocity is the velocity in [AU/days]

   Example:
   velocity = vstar(10, 0.5)

   """
   import math
   solarMass = 2.959139768995959E-04
   Mass = massRatio / (1 - massRatio)
   velocity = math.sqrt( ( solarMass * ( 1. + Mass ) ) / R_AB )
   print "Mass of the secondary star:  " + str(Mass) + " Solar Mass"
   print "Velocity: " + str(velocity) + " AU / days"
   return velocity

def vplanet(distance, mass=0):
    """
    Return the velocity of massive planet from the primary star A (1 solar mass) in a circular orbit.

    velocity = np.sqrt( ( G * ( 1. + mass ) ) / distance )
    In the swifter units G = 1

    Usage:
    velocity = vplanet(distance, mass)
    Where:
    distance is the distance in AU from the star
    mass si the mass of the planet in solar mass units

    Example:
    velocity = planet(2, 0.)
    """
    import math
    solarMass = 2.959139768995959E-04
    velocity = math.sqrt( ( solarMass * ( 1. + mass ) ) / distance )
    print "Mass of the planet:  " + str(mass) + " Solar Mass"
    print "Velocity: " + str(velocity) + " AU / days"
    return velocity
