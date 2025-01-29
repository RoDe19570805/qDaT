### qDaT.py

#############################################################################################################
#
# --- qDaT ---
#
#   qDaT defines a class for date and time information in the form: complex(qDaT-date,qDaT-time).
#   reference datetime: 1925-11-16 
#                       M.Born, W.Heisenberg, P.Jordan submit a joint paper on the subject 
#                       “On Quantum Mechanics II”.
#
# copyright: 
#   
#   (c) by Roland Degelmann, takatoa 
#   Mail : rode@takatoa.net
#   Web  : takatoa.net
#   
# created | last modified | version:
#
#   2024-12-01 | 2025-01-28 | version: 0.1.0
#
#############################################################################################################

from datetime import datetime
from typing import Optional
import math

class qDaT:
    def __init__(self) :
        
        self.NULL_YEAR = 1925
        self.NULL_MONTH = 11
        self.NULL_DAY = 16
        self.NULL_HOUR = 0
        self.NULL_MIN = 0
        self.NULL_SEC = 0
        self.Mull_MICROSEC = 0
        
        rdt = complex(0,0)
    
    def calc_qDaT(self,
                      actYear : Optional[int] = 1925,
                      actMonth : Optional[int] = 11,
                      actDay : Optional[int] = 16,
                      actHour : Optional[int] = 0,
                      actMin : Optional[int] = 0,
                      actSec : Optional[int] = 0,
                      actMicroSec : Optional[int] = 0) :
        
        qDaT_time = (((actHour * 60 * 60 + actMin * 60 + actSec + (actMicroSec / 1000000)) / 0.864) / 100000) 

        actDatetime = datetime(actYear, actMonth, actDay)
        refDatetime = datetime(self.NULL_YEAR, self.NULL_MONTH, self.NULL_DAY)
        diff = actDatetime - refDatetime
 
        qDaT_date = diff.days / 1000000
        
        self.rdt = complex(qDaT_date, qDaT_time)
        return self.rdt
        
    def get_qDaT(self) :
        """get the qDaT."""
        # read current date
        actDT = datetime.now()
        actYear = actDT.year
        actMonth = actDT.month
        actDay = actDT.day
        actHour = actDT.hour
        actMin = actDT.minute
        actSec = actDT.second
        actMicroSec = actDT.microsecond

        return self.calc_qDaT(actYear, actMonth, actDay, actHour, actMin, actSec, actMicroSec)
        
    def set_qDaT(self, 
                     setYear : Optional[int] = 1925, 
                     setMonth  : Optional[int] = 11, 
                     setDay : Optional[int] = 16, 
                     setHour : Optional[int] = 0, 
                     setMin : Optional[int] = 0, 
                     setSec : Optional[int] = 0, 
                     setMicroSec : Optional[int] = 0) :
        """set the qDaT."""
        actYear = setYear
        actMonth = setMonth
        actDay = setDay
        actHour = setHour
        actMin = setMin
        actSec = setSec
        actMicroSec = setMicroSec

        return self.calc_qDaT(actYear, actMonth, actDay, actHour, actMin, actSec, actMicroSec)
    
    def __str__(self):
        return f"qDaT defines a class for date and time information in the form: complex(qDaT-date,qDaT-time)."