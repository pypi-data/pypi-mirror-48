# -*- coding: utf-8 -*-
#import ipdb
import os
import argparse
import traceback
import logging

import pyCGM2
from pyCGM2.Utils import files
from pyCGM2.Configurator import ModelManager
from pyCGM2.Lib.CGM import  cgm1_1
from pyCGM2.Tools import btkTools
from pyCGM2 import log; log.setLogger()

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)


def main(args):
    DATA_PATH = os.getcwd()+"\\"

    # User Settings
    if os.path.isfile(DATA_PATH + args.userFile):
        userSettings = files.openFile(DATA_PATH,args.userFile)
    else:
        raise Exception ("user setting file not found")

    # internal (expert) Settings
    if args.expertFile:
        if os.path.isfile(DATA_PATH + args.expertFile):
            internalSettings = files.openFile(DATA_PATH,args.expertFile)
        else:
            raise Exception ("expert setting file not found")
    else:
        internalSettings = None

    # translators
    if os.path.isfile(DATA_PATH + "CGM1_1.translators"):
        translators = files.openFile(DATA_PATH,"CGM1_1.translators")
    else:
        translators = None

    if args.vskFile:
        vsk = vskTools.Vsk(str(DATA_PATH +  args.vskFile))
    else:
        vsk=None


    # --- Manager ----
    manager = ModelManager.CGM1_1ConfigManager(userSettings,localInternalSettings=internalSettings,localTranslators=translators,vsk=vsk)
    manager.contruct()
    finalSettings = manager.getFinalSettings()
    files.prettyDictPrint(finalSettings)


    logging.info("=============Calibration=============")
    model,finalAcqStatic = cgm1_1.calibrate(DATA_PATH,
        manager.staticTrial,
        manager.translators,
        manager.requiredMp,
        manager.optionalMp,
        manager.leftFlatFoot,
        manager.rightFlatFoot,
        manager.headFlat,
        manager.markerDiameter,
        manager.pointSuffix,
        displayCoordinateSystem=True)



    btkTools.smartWriter(finalAcqStatic, str(DATA_PATH+finalSettings["Calibration"]["StaticTrial"][:-4]+"-pyCGM2modelled.c3d"))
    logging.info("Static Calibration -----> Done")

    manager.updateMp(model)
    #files.prettyDictPrint(manager.finalSettings)

    logging.info("=============Fitting=============")
    for trial in manager.dynamicTrials:
        mfpa = None if trial["Mfpa"] == "Auto" else trial["Mfpa"]
        reconstructFilenameLabelled = trial["File"]

        acqGait = cgm1_1.fitting(model,DATA_PATH, reconstructFilenameLabelled,
            manager.translators,
            manager.markerDiameter,
            manager.pointSuffix,
            mfpa,
            manager.momentProjection,
            displayCoordinateSystem=True)

        btkTools.smartWriter(acqGait, str(DATA_PATH+reconstructFilenameLabelled[:-4]+"-pyCGM2modelled.c3d"))
        logging.info("---->dynamic trial (%s) processed" %(reconstructFilenameLabelled))

    logging.info("=============Writing of final Settings=============")
    i = 0
    while os.path.exists("CGM1.1 [%s].completeSettings" % i):
        i += 1
    filename = "CGM1.1 [" + str(i)+"].completeSettings"
    files.saveJson(DATA_PATH, filename, finalSettings)
    logging.info("---->complete settings (%s) exported" %(filename))


    raw_input("Press return to exit..")


if __name__ == "__main__":


    parser = argparse.ArgumentParser(description='CGM1.1-pipeline')
    parser.add_argument('--userFile', type=str, help='userSettings', default="CGM1_1.userSettings")
    parser.add_argument('--expertFile', type=str, help='Local expert settings')
    parser.add_argument('--vskFile', type=str, help='Local vsk file')

    args = parser.parse_args()
        #print args

        # ---- main script -----
    try:
        main(args)


    except Exception, errormsg:
        print "Script errored!"
        print "Error message: %s" % errormsg
        traceback.print_exc()
        print "Press return to exit.."
        raw_input()
        #
