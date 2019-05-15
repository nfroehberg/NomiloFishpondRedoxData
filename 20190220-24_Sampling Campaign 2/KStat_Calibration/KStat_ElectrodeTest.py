import KStat_0_1_froehberg_driver as KStat
from serial import Serial
import sys, time, os, winsound


def oxygen(ser, sample_rate, file, slope):
    return KStat.cyclicVoltammetry(ser = ser, PGA_gain = PGA_gain,
                                   iv_gain = iv_gain, t_preconditioning1 = 5,
                                   t_preconditioning2 = 2, v_preconditioning1 = -900,
                                   v_preconditioning2 = -100, v1 = -1850, v2 = -100,
                                   start = -100, n_scans = 1, slope = slope, sample_rate = sample_rate,
                                   file = file, plotting = True)

with Serial('COM3', 9600, timeout=1) as ser:
    ADSbuffer = 1
    Samplingrate = "1KHz"
    PGA_gain = 2
    iv_gain = "POT_GAIN_300K"
    KStat.abort(ser)
    KStat.setupADC(ser, ADSbuffer, Samplingrate, PGA_gain)
        
    KStat.setGain(ser, iv_gain)

    while True:
        winsound.Beep(frequency = 600, duration = 1000)
        usr = input('Enter Electrode ID or hit enter to exit\n')
        if usr == '':
            sys.exit()
        else:
            blanks = 3
            for i in range(blanks):
                oxygen(ser, Samplingrate, 'blank', 500)
                print("blank {}/{}".format(i+1,blanks))
            oxygen(ser, Samplingrate, (usr+'-500'), 500)
            oxygen(ser, Samplingrate, (usr+'-1000'), 1000)
            oxygen(ser, Samplingrate, (usr+'-2000'), 2000)
            oxygen(ser, Samplingrate, (usr+'-2900'), 2900)
            os.remove('blank.csv')
            os.remove('blank.png')
            os.remove('blank-parameters.txt')
