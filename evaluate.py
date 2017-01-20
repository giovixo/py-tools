
G = 2.959122082855911e-4

import numpy as np
from astropy.io import ascii

# Just a python test
def printme( str ):
   "This prints a passed string into this function"
   print str
   return

def velocity( R_AG ):
   """
   Return the velocity of the Giant Planet in a circular orbit.
   This function requires the distance R_AG in Astonomical Unit  from the primary star as input
   """
   vel = np.sqrt( G / R_AG )
   return vel

def vel_p( R , Mass):
   """
   Return the velocity of the Giant Planet in a circular orbit in a P-type orbit
   R is the distance in AU from the center of mass of the binary star
   Mass is the mass of the planet
   """
   v_cm = 0.5 * 0.0076930125215755509 # Velocity of the center of mass if ma = mb = 1 Solar mass
   vel = v_cm + np.sqrt( ( G * (2. + Mass) ) / R)
   return vel

def vstar( R_AB, Mass):
   """
   Retturn the velocity of the Secondary Star B from the primary star A in a circular orbit.
   This function requires as input the distance R_AB in Astonomical Unit from the primary star, and the Mass
   of the secondary star.
   """
   vel = np.sqrt( ( G * ( 1. + Mass ) ) / R_AB )
   return vel

def evaluate_radius( file_prefix ):
  """
  Return the mean radius of the planet
  Usage:
  r = orbit(file_prefix)

  Examples:
  r=basic.orbit('m_0.6_pos_2.50_')
  """
  #
  # Read the data
  # --------------

  from numpy import inf

  # Planet
  values1 = ascii.read(file_prefix+'orbit-2.dat')
  x1      = values1['x(AU)']
  y1      = values1['y(AU)']
  # Star
  values2 = ascii.read(file_prefix+'orbit-1.dat')
  x2      = values2['x(AU)']
  y2      = values2['y(AU)']

  # Compute the mean radius
  maximumDistance = 100 # The maximum distance (AU)
  if ( max(abs(x1)) < 100 ) and ( max(abs(y1)) < 100 ):
    r = np.sqrt( x1**2 + y1**2 )
    mean_radius = np.mean(r)
  else:
    print "The planet is going away. Radius setted to infinity"
    mean_radius = float("inf")

  return mean_radius
