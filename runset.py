import os
from shutil import copyfile

SWIFTERBIN ='/Users/giovanni/Works/Exoplanets/StudyOfStabilyInBinarySystems/SwifterCode/swifter/bin/'

ROOT = os.getcwd() + '/'

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
    Return: [dirName, float(dist)]

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

    return [dirName, float(dist), float(pm)]

def copy(dirName):
    """
    Description: copy the required files into the "dirName" directory

    Usage: copy(dirName)
           Where:
           <dirName> is the destination dir
    """
    # copy the main template files into the main working directory
    os.makedirs(dirName+'/main')
    for file in ['param.in', 'pl.in', 'tp.in', 'accuracy.in', 'particle_id.in']:
        fileSrc = ROOT+'swifter_template_main/' + file
        if os.path.exists(fileSrc):
            copyfile(fileSrc, dirName+'/main/'+file)
    # copy the tail template files into the main working directory
    os.makedirs(dirName+'/tail')
    for file in ['param.in', 'pl.in', 'tp.in', 'accuracy.in', 'particle_id.in']:
        fileSrc = ROOT+'swifter_template_tail/' + file
        if os.path.exists(fileSrc):
            copyfile(fileSrc, dirName+'/tail/'+file)
    # copy the unperturbed template files into the main working directory
    os.makedirs(dirName+'/unperturbed')
    for file in ['param.in', 'pl.in', 'tp.in', 'accuracy.in', 'particle_id.in']:
        fileSrc = ROOT+'swifter_template_unperturbed/' + file
        if os.path.exists(fileSrc):
                copyfile(fileSrc, dirName+'/unperturbed/'+file)

    pass

def update_distance(file_in, dist, mass=0):
    """
    Update the distance in the tp.in file

    Usage: update_distance(file_full_path, dist, mass)
    mass is the mass of the planet in solar mass units
    """
    import astrotools

    # Read the file
    fin = open(file_in, 'r')
    lines = []
    for line in fin:
        lines.append(line)
    fin.close()
    if not(mass):
        # Change the rows relate to the planetary distance from the star
        firstRow  = lines[2].split()
        firstRow[0] = str(10.*dist)
        lines[2] = " ".join(firstRow) + "\n"
        secondRow = lines[3].split()
        secondRow[1] = str(astrotools.vplanet(10.*dist))
        lines[3] = " ".join(secondRow) + "\n"
    else:
        # Change the rows relate to the planetary distance from the star
        firstRow  = lines[8].split()
        firstRow[0] = str(10.*dist)
        lines[8] = " ".join(firstRow) + "\n"
        secondRow = lines[9].split()
        secondRow[1] = str(astrotools.vplanet(10.*dist, mass))
        lines[9] = " ".join(secondRow) + "\n"
    # Write the file
    fout = open('particle.in','w')
    fout.writelines(lines)
    fout.close()

    pass

def create():
    """
    Description:  create a swifter dir ready for the run.

    Usage: create()
    """
    
    # Mass of Jupiter in solar mass
    massOfJupyter = 0.0009543

    # Create the directory
    print "Creating the working directory..."
    [directory, distance, mass] = mkdir()

    # Copy the templates into the directory/[main, tail, unperturbed]
    copy(directory)

    if not(mass):
        # Change the distance from the star in tp.in files at the directories [main, unperturbed]
        tp_root = ROOT + directory + "/main/"
        update_distance(tp_root+"tp.in", distance)
        copyfile(ROOT+"particle.in", ROOT + directory + "/main/" + "tp.in")
        copyfile(ROOT+"particle.in", ROOT + directory + "/unperturbed/" + "tp.in")
    else:
        # Change the distance from the star at the directory main
        pl_root = ROOT + directory + "/main/"
        update_distance(pl_root+"pl.in", distance, mass * massOfJupyter)
        copyfile(ROOT+"particle.in", ROOT + directory + "/main/" + "pl.in")
        copyfile(ROOT+"particle.in", ROOT + directory + "/unperturbed/" + "pl.in")
    os.remove("particle.in")

    print "-----------------------------------------------------------------------------------------------"
    print "Planet mass: " + str(mass) + " Jupiter mass = " + str(mass * massOfJupyter) + " solar mass unit"
    print "Distance ratio: " + str(distance)
    print "The dir " + directory + " is ready."
    print "You can now run the integrations with swifter."
    print "The 'unpertubed' and 'tail' subdirs require some editing."
    print "-----------------------------------------------------------------------------------------------"
    pass
