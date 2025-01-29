### qDaT_main.py

#############################################################################################################
#
# --- qDaT_main ---
#
#   qDaT defines a class for date and time information in the form: complex(qDaT-date,qDaT-time).
#   qDaT_main shows the usage of qDaT.
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

from qDaT import qDaT

if __name__ == '__main__':
    Qdat = qDaT()
    print("\n\nshow the usage of qDaT\n")
    print('***', Qdat, '***\n')
    myQdat = Qdat.get_qDaT()
    print("get actual qDaT\t:", myQdat)
    myQdat = Qdat.set_qDaT(2024, 1, 13, 15, 40, 13, 37)
    print("set qDaT\t:", myQdat, "\t<-- Input data: '2024, 1, 13, 15, 40, 13, 37'")
    myQdat = Qdat.set_qDaT(1993, 11, 11, 8, 15, 52, 37)
    print("set qDaT\t:", myQdat, "\t<-- Input data: '1993, 11, 11, 8, 15, 52, 37'")
    myQdat = Qdat.set_qDaT(1959, 12, 22, 16, 29, 53, 11)
    print("set qDaT\t:", myQdat, "\t<-- Input data: '1959, 12, 22, 16, 29, 53, 11'")
    myQdat = Qdat.set_qDaT(1897, 4)
    print("set qDaT\t:", myQdat, "\t<-- Input data: '1897, 4'")
