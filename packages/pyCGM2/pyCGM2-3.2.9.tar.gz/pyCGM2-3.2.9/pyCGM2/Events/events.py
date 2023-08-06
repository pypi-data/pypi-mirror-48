# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import logging
import numpy as np

from pyCGM2 import btk

from pyCGM2.Tools import  btkTools
from pyCGM2.Signal import detect_peaks


#-------- EVENT PROCEDURES  ----------


# --- calibration procedure
class ZeniProcedure(object):
    """
        Gait Event detection from Zeni
    """

    def __init__(self):
        self.description = "Zeni (2008)"
        self.footStrikeOffset = 0
        self.footOffOffset = 0

    def setFootStrikeOffset(self,value):
        self.footStrikeOffset = value

    def setFootOffOffset(self,value):
        self.footOffOffset = value

    def detect(self,acq):
        """
        """
        ff=acq.GetFirstFrame()


        progressionAxis,forwardProgression,globalFrame = btkTools.findProgression(acq,"LANK")
        longAxisIndex = 0 if progressionAxis == "X" else 1

        sacrum=(acq.GetPoint("LPSI").GetValues() + acq.GetPoint("RPSI").GetValues()) / 2.0

        #Left
        heel_left = acq.GetPoint("LHEE").GetValues()
        toe_left = acq.GetPoint("LTOE").GetValues()

        diffHeel_left = heel_left-sacrum
        diffToe_left = toe_left-sacrum

        #Right
        heel_right = acq.GetPoint("RHEE").GetValues()
        toe_right = acq.GetPoint("RTOE").GetValues()

        diffHeel_right = heel_right-sacrum
        diffToe_right = toe_right-sacrum


        if  forwardProgression:
            indexes_fs_left = detect_peaks.detect_peaks(diffHeel_left[:,longAxisIndex])+ff
            indexes_fo_left = detect_peaks.detect_peaks(-diffToe_left[:,longAxisIndex])+ff
        else:
            indexes_fs_left = detect_peaks.detect_peaks(-diffHeel_left[:,longAxisIndex])+ff
            indexes_fo_left = detect_peaks.detect_peaks(diffToe_left[:,longAxisIndex])+ff

        if  forwardProgression:
            indexes_fs_right = detect_peaks.detect_peaks(diffHeel_right[:,longAxisIndex])+ff
            indexes_fo_right = detect_peaks.detect_peaks(-diffToe_right[:,longAxisIndex])+ff
        else:
            indexes_fs_right = detect_peaks.detect_peaks(-diffHeel_right[:,longAxisIndex])+ff
            indexes_fo_right = detect_peaks.detect_peaks(diffToe_right[:,longAxisIndex])+ff

        return indexes_fs_left+self.footStrikeOffset,indexes_fo_left+self.footOffOffset, indexes_fs_right+self.footStrikeOffset, indexes_fo_right+self.footOffOffset


class EventFilter(object):
    """

    """
    def __init__(self,procedure,acq):
        """
            :Parameters:
        """

        self.m_aqui = acq
        self.m_procedure = procedure


    def detect(self):
        """
            Run the motion filter
        """
        pf = self.m_aqui.GetPointFrequency()

        eventDescriptor = self.m_procedure.description
        indexes_fs_left,indexes_fo_left,indexes_fs_right,indexes_fo_right =  self.m_procedure.detect(self.m_aqui)

        for ind in indexes_fs_left:
            ev = btk.btkEvent('Foot Strike', (ind-1)/pf, 'Left', btk.btkEvent.Manual, '', eventDescriptor)
            ev.SetId(1)
            self.m_aqui.AppendEvent(ev)

        for ind in indexes_fo_left:
            ev = btk.btkEvent('Foot Off', (ind-1)/pf, 'Left', btk.btkEvent.Manual, '', eventDescriptor)
            ev.SetId(2)
            self.m_aqui.AppendEvent(ev)

        for ind in indexes_fs_right:
            ev = btk.btkEvent('Foot Strike', (ind-1)/pf, 'Right', btk.btkEvent.Manual, '', eventDescriptor)
            ev.SetId(1)
            self.m_aqui.AppendEvent(ev)

        for ind in indexes_fo_right:
            ev = btk.btkEvent('Foot Off', (ind-1)/pf, 'Right', btk.btkEvent.Manual, '', eventDescriptor)
            ev.SetId(2)
            self.m_aqui.AppendEvent(ev)

        # events= self.m_aqui.GetEvents()
        # for ev in btk.Iterate(events):
        #     print ev.GetLabel()
        #     print ev.GetContext()
        #     print ev.GetTime()
        #     print "------"
