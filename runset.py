import os

SWIFTERBIN ='/Users/giovanni/Works/Exoplanets/StudyOfStabilyInBinarySystems/SwifterCode/swifter/bin/'
SWIFTERROOT = '/Users/giovanni/Works/Exoplanets/StudyOfStabilyInBinarySystems/TypeS/massEqZero/'

def info():
    """
    Description: Print some infos

    Usage: info()
    """
    print "This model contains some tools to prepare the swifter runs, " \
          "like create a directory, setting the init files, and so on." \
          " Have fun!"
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
    pm   = raw_input("Mass of the planet (in unit of Jupiter mass, default 00): ") or "00"
    mu   = raw_input("Stellar mass ratio (mu = m2 / (m1 + m2) , default 0.50): ") or "0.50"
    dist = raw_input("Distance of the planet from the primary star(in utit of the distance betwenn the two stars, default 0.200): ") or "0.200"
    ecc  = raw_input("Eccentry of the planetary orbit (default 0.0): ") or "0.0"

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
    # copy the main template files into the main working directory
    os.makedirs(dirName+'/main')
    for file in ['param.in', 'pl.in', 'tp.in', 'accuracy.in', 'particle_id.in']:
        copyfile(SWIFTERROOT+'swifter_template_main/' + file, dirName+'/main/'+file)
    # copy the tail template files into the main working directory
    os.makedirs(dirName+'/tail')
    for file in ['param.in', 'pl.in', 'tp.in', 'accuracy.in', 'particle_id.in']:
        copyfile(SWIFTERROOT+'swifter_template_tail/' + file, dirName+'/tail/'+file)
    # copy the unperturbed template files into the main working directory
    os.makedirs(dirName+'/unperturbed')
    for file in ['param.in', 'pl.in', 'tp.in', 'accuracy.in', 'particle_id.in']:
        copyfile(SWIFTERROOT+'swifter_template_unperturbed/' + file, dirName+'/unperturbed/'+file)

    pass


def create():
    """
    Description:  create a swifter dir ready for the next run.

    Usage: create()
    """
    # Create the directory
    print "Creating the working directory..."
    directory = mkdir()
    print "***"
    print "The dir " + directory + " is ready"
    # Copy the parameter files into the directory
    copy(directory)
    print "All the templates are copied into the dir " + directory + ". You can change some default values and run the integrations."
    print "***"
    pass
