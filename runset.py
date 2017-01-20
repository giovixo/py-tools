import os

SWIFTERTEMPLATE = '/Users/giovanni/Works/Exoplanets/StudyOfStabilyInBinarySystems/SwifterTemplate/'
SWIFTERBIN ='/Users/giovanni/Works/Exoplanets/StudyOfStabilyInBinarySystems/SwifterCode/swifter/bin'

def info():
    """
    Description: Print some infos

    Usage: info()
    """
    print "This model contains some tools to prepare the swifter runs, " \
          "like create a directory, setting the init files, and so on."
    pass

def mkdir():
    """
    Description: Create a new directory for a swifter run

    Usage: mkdir()

    Directory naming:
    pm_mu_dist_ecc_

    Where
    pm: mass of the planet (0, Mj, 30Mj)
    mu: stellar mass ratio = m2 / (m1 + m2) whwre m1 is the mass of the primary star
    dist: distance from the primary star
    ecc: eccentry of the planetary orbit (the stars eccentricity will be alway zero).
    _ the value
    """
    print "Please, insert the initial conditions."
    pm   = raw_input("Mass of the planet: ")
    mu   = raw_input("Stellar mass ratio: ")
    dist = raw_input("Distance of the planet from the primary star: ")
    ecc  = raw_input("Eccentry of the planetary orbit: ")

    dirName = 'pm' + str(pm) + '_mu' + str(mu) + '_dist' + str(dist) + '_ecc' + str(ecc)

    os.makedirs(dirName)

    return dirName

def copy(dirName):
    """
    Description: copy the required files into the "dirName" directory

    Usage: copy(dirName)
           Where:
           <dirName> is the destination dir
    """
    from shutil import copyfile
    for file in ['param.in', 'pl.in', 'tp.in', 'accuracy.in', 'particle_id.in']:
        copyfile(SWIFTERTEMPLATE+file, dirName+'/'+file)
    pass

def create():
    """
    Description: Create a swifter dir, ready for the next run

    Usage: create()
    """
    pass
