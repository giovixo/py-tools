from astropy.io import ascii
import pylab

def info():
    """
    Description: Print some infos

    Usage: info()
    """
    print "Some tool to visualize the results."
    pass

def plot(fileName):
    """
    Description: plot the orbit

    Usage: plot(fileName)
    """
    planetTrajectory = ascii.read(fileName)
    x = planetTrajectory['col3']
    y = planetTrajectory['col4']
    pylab.plot(x, y, 'b.', label='Planet orbit')
    pylab.show()
    pass

def plot_planet(fileName='planet.dat'):
    """
    Description: plot the planetary orbit

    Usage: plot_planet()
    """
    plot(fileName)
    pass

def plot_star():
    """
    Description: plot the orbit of the secondary star

    Usage: plot_star()
    """
    plot('star.dat')
    pass
