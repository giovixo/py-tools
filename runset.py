"""
Some tools to prepare the swifter runs.

Cookbook
=========

!!! Warning; in this version you need first to edit this python script !!!
For massive planets (30 Jupiter mass in this case):
[directory, distance, mass] = mkdir("30", "0.50", dist, "0.0")
Fore massless planets:
[directory, distance, mass] = mkdir("00", "0.50", dist, "0.0")

0. First
> import runset

For a massless planet:
---------------------
1. Create the work directories
   > runset.create(True)

2. Run swifter_bs in the main thread
   > runset.swifter_run()

3. Run swifter_bs in the tail thread
   > runset.swifter_run_tail0()

4. Run swifter_bs in the unperturbed thread
   > runset.swifter_run_unpertubed0()

For a massive planet:
---------------------
1. Create the work directories
   > runset.create(True)

2. Run swifter_bs in the main thread
   > runset.swifter_run()

3. Run swifter_bs in the tail thread
   > runset.swifter_run_tail()

4. Run swifter_bs in the unperturbed thread
   > runset.swifter_run_unpertubed()

Then use the 'astrovis' module to visualize the orbits
"""


import os
from shutil import copyfile

SWIFTERBIN ='/Users/giovanni/Works/Exoplanets/StudyOfStabilyInBinarySystems/SwifterCode/swifter/bin/'

ROOT = os.getcwd() + '/'

VERBOSE = False

def info():
    """
    Description: Print some infos

    Usage: info()
    """
    print "This model contains some tools to prepare the swifter runs, " \
          "like create a directory, setting the init files, and so on." \
          " Have fun!"
    pass

def mkdir(pm = "", mu = "", dist = "", ecc = ""):
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
    if pm:
        if VERBOSE:
            print "Planetary mass: " + str(pm)
    else:
        pm   = raw_input("Mass of the planet (in unit of Jupiter mass, default 00): ") or "00"
    if mu:
        if VERBOSE:
            print "Stellar mass ratio: " + str(mu)
    else:
        mu   = raw_input("Stellar mass ratio (mu = m2 / (m1 + m2) , default 0.50): ") or "0.50"
    if dist:
        if VERBOSE:
            print "Distance of the planet from the primary star(in utit of the distance betwenn the two stars: " + str(dist)
    else:
        dist = raw_input("Distance of the planet from the primary star(in utit of the distance betwenn the two stars, default 0.200): ") or "0.200"
    if ecc:
        if VERBOSE:
            print "Eccentry of the planetary orbit: " + str(ecc)
    else:
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

def create(doLoop=False):
    """
    Description:  create a swifter dir ready for the run.

    Usage: create() or create(True)
    """

    # Mass of Jupiter in solar mass
    massOfJupyter = 0.0009543

    # Create the directory
    # To Do: write a better code...
    if not(doLoop):
        # Ask to the user
        [directory, distance, mass] = mkdir()
        print "-----------------------------------------------------------------------------------------------"
        print "PLANET CARD"
        print "Planet mass: " + str(mass) + " Jupiter mass = " + str(mass * massOfJupyter) + " solar mass unit"
        print "Distance ratio: " + str(distance)
        print "The dir " + directory + " is ready."
        print "You can now run the integrations with swifter."
        print "The 'unpertubed' and 'tail' subdirs require some editing."
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
    else:
        # Loop over a parameter space
        # Base distance for the case of co-rotanting planet and star
        distBase = ["0.200", "0.212", "0.224", "0.236", "0.248", "0.260", "0.272", "0.284", "0.296", "0.308", "0.320", "0.332", "0.344"]
        # Distances usefull to the case where panet and star are not co-rotating
        # distAdd  = ["0.368", "0.392", "0.416", "0.440", "0.464", "0.488", "0.512", "0.536", "0.560", "0.584", "0.608", "0.632", "0.656"]
        distAdd  = []
        setOfDistances = distBase + distAdd
        for dist in setOfDistances:
            [directory, distance, mass] = mkdir("01", "0.50", dist, "0.0")
            print "-----------------------------------------------------------------------------------------------"
            print "PLANET CARD"
            print "Planet mass: " + str(mass) + " Jupiter mass = " + str(mass * massOfJupyter) + " solar mass unit"
            print "Distance ratio: " + str(distance)
            print "The dir " + directory + " is ready."
            print "You can now run the integrations with swifter."
            print "The 'unpertubed' and 'tail' subdirs require some editing."
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

    pass

def swifter_run(path="pm"):
    """
    Description: run swifter_bs integrator in over path* directorys

    Usage: swifter_run()
    """
    import glob
    from subprocess import call
    dirs = glob.glob(path+"*")
    for swifterDir in dirs:
        print "Processing dir " + swifterDir + " ..."
        os.chdir(swifterDir+'/main')
        call('swifter_bs')
        call('tool_follow')
        call(['mv', 'follow.out', 'planet.dat'])
        os.chdir('../..')
    pass

def remove_star(fileName="pl.in", zeroMass = False):
    """
    Description: remove the secondary star in the 'pl.in' file
    """
    # Read the file
    fin = open(fileName, 'r')
    lines = []
    for line in fin:
        lines.append(line)
    fin.close()
    # Update the file
    if zeroMass:
        lines[0] = "1\n"
    else:
        lines[0] = "2\n"
    del lines[4:7]
    fout = open(fileName,'w')
    fout.writelines(lines)
    fout.close()
    pass

def swifter_run_unpertubed(path="pm"):
    """
    Description: run swifter_bs integrator in over path* directorys

    Usage: swifter_run_unperturbed()

    Caveat: it works only with massive planets
    """
    import glob
    from subprocess import call
    dirs = glob.glob(path+"*")
    for swifterDir in dirs:
        print "Processing dir " + swifterDir + " ..."
        os.chdir(swifterDir+'/unperturbed')
        # first remove the secondary star in the "pl.in" file
        remove_star()
        # then run the integration
        call('swifter_bs')
        call('tool_follow')
        call(['mv', 'follow.out', 'planet.dat'])
        os.chdir('../..')
    pass

def swifter_run_unpertubed0(path="pm"):
    """
    Description: run swifter_bs integrator in over path* directorys

    Usage: swifter_run_unperturbed()

    Caveat: it works only with massless planets
    """
    import glob
    from subprocess import call
    dirs = glob.glob(path+"*")
    for swifterDir in dirs:
        print "Processing dir " + swifterDir + " ..."
        os.chdir(swifterDir+'/unperturbed')
        # first remove the secondary star in the "pl.in" file
        remove_star("pl.in", True)
        # then run the integration
        call('swifter_bs')
        call('tool_follow')
        call(['mv', 'follow.out', 'planet.dat'])
        os.chdir('../..')
    pass

def swifter_run_tail(path="pm"):
    """
    Description: run swifter_bs integrator in over path* directorys

    Usage: swifter_run_tail()

    Caveat: it works only for massive planet
    """
    import glob
    from subprocess import call
    dirs = glob.glob(path+"*")
    for swifterDir in dirs:
        print "Processing dir " + swifterDir + " ..."
        os.chdir(swifterDir+'/tail')
        if os.path.exists('../main/dump_pl1.bin'):
            # first copy  the 'dump_pl1.bin' to 'pl.in' from '../main' directory
            copyfile('../main/dump_pl1.bin', 'pl.in')
            # then run the integration
            call('swifter_bs')
            call('tool_follow')
            call(['mv', 'follow.out', 'planet.dat'])
        else:
            print "The dump_pl1 file does not exist"
        os.chdir('../..')
    pass

def swifter_run_tail0(path="pm"):
    """
    Description: run swifter_bs integrator in over path* directorys

    Usage: swifter_run_tail0()

    Caveat: it works only for planet with zero mass
    """
    import glob
    from subprocess import call
    dirs = glob.glob(path+"*")
    for swifterDir in dirs:
        print "Processing dir " + swifterDir + " ..."
        os.chdir(swifterDir+'/tail')
        if os.path.exists('../main/dump_pl1.bin') & os.path.exists('../main/dump_tp1.bin'):
            # first copy  the 'dump_pl1.bin' to 'pl.in' from '../main' directory
            copyfile('../main/dump_pl1.bin', 'pl.in')
            copyfile('../main/dump_tp1.bin', 'tp.in')
            # then run the integration
            call('swifter_bs')
            call('tool_follow')
            call(['mv', 'follow.out', 'planet.dat'])
        else:
            print "The dump_pl1 or dump_tp1 does not exist"
        os.chdir('../..')
    pass
