'''
Not really part of the project. Just a sort of sandbox where i do some tests...

Please, don't waste yout time reading this file

'''

import sys
import os
import pyportmidi as pm
import res.tools as tools


#PARAM_CONV_1 = tools.mergeRanges(range(0x00,0x33),tools.ulist(0,5,0.1,'ms'))
#PARAM_CONV_1_B = tools.mergeRanges(range(0x33,0x3D),tools.ulist(5.5,10,0.5))
#PARAM_CONV_1_C = tools.mergeRanges(range(0x3D,0x65),tools.ulist(11,50,1))
#PARAM_CONV_1_D = tools.mergeRanges(range(0x65,0x7E),tools.ulist(52,100,2))
#PARAM_CONV_1_E = {0x7E: '100', 0x7F: '100'}
#PARAM_CONV_1.update(PARAM_CONV_1_B)
#PARAM_CONV_1.update(PARAM_CONV_1_C)
#PARAM_CONV_1.update(PARAM_CONV_1_D)
#PARAM_CONV_1.update(PARAM_CONV_1_E)



#PARAM_TYPE_5 = tools.mergeRanges(range(0x00,0x80),tools.ulist(0,635,5,'ms'))


#PARAM_TYPE_16 = tools.mergeRanges(range(0x00,0x64),tools.ulist(0.1,10,0.1,'s'))
#PARAM_TYPE_16_B = tools.mergeRanges(range(0x64,0x80),tools.ulist(11,38,1,'s'))
#PARAM_TYPE_16.update(PARAM_TYPE_16_B)

#BALANCE_VALUES_STORTA=(['D0<E','D1<E','D3<E','D4<E','D6<E','D7<E','D9<E','D11<E','D12<E','D14<E',
#                     'D15<E','D17<E','D19<E','D20<E','D22<E','D23<E','D25<E','D26<E','D28<E','D30<E',
#                     'D31<E','D33<E','D34<E','D36<E','D38<E','D39<E','D41<E','D42<E','D44<E','D46<E',
#                     'D47<E','D49<E','D50<E','D52<E','D53<E','D55<E','D57<E','D58<E','D60<E','D61<E',
#                     'D63<E','D65<E','D66<E','D68<E','D69<E','D71<E','D73<E','D74<E','D76<E','D77<E',
#                     'D79<E','D80<E','D82<E','D84<E','D85<E','D87<E','D88<E','D90<E','D92<E','D93<E',
#                     'D95<E','D96<E','D98<E','D=E','D>98E','D>96E','D>95E','D>93E','D>92E',
#                     'D>90E','D>88E','D>87E','D>85E','D>84E','D>82E','D>80E','D>79E','D>77E','D>76E',
#                     'D>74E','D>73E','D>71E','D>69E','D>68E','D>66E','D>65E','D>63E','D>61E','D>60E',
#                     'D>58E','D>57E','D>55E','D>53E','D>52E','D>50E','D>49E','D>47E','D>46E','D>44E',
#                     'D>42E','D>41E','D>39E','D>38E','D>36E','D>34E','D>33E','D>31E','D>30E','D>28E',
#                     'D>26E','D>25E','D>23E','D>22E','D>20E','D>19E','D>17E','D>15E','D>14E','D>12E',
#                     'D>11E','D>9E','D>7E','D>6E','D>4E','D>3E','D>1E','D>0E','D>0E'])
#
#BALANCE_VALUES=BALANCE_VALUES_STORTA[::-1]
#print len(BALANCE_VALUES)
#BALANCE_DICT=tools.mergeRanges(range(0x00,0x80),BALANCE_VALUES)
#print BALANCE_DICT

a = tools.mergeRanges(range(0x28,0x59),tools.ulist(-48,+48,2,'%'))
#b=range(0x28,0x59)
#c= tools.ulist(-48,+48,2,'%')
#print len(b),len(c)
print a

#pm.init()
#
##numDevs = pm.get_count()
##dev = 0
##while dev < numDevs:
##   print 'device ', dev, ': ',pm.get_device_info(dev)
##   dev = dev + 1
#
#numDevs = pm.get_count()
#
#midiDevs = {}
#
#for dev in range(0,numDevs):
#   
#   deviceInfo = pm.get_device_info(dev)
#   
#   print 'device ', dev, ': ',deviceInfo,' of type',type(deviceInfo)
#   midiDevs[dev] = deviceInfo
##print midiDevs
#
#
#for k in range(0,len(midiDevs)):
#    if (midiDevs[k][1] == 'UA-100 Control') & (midiDevs[k][3] == 1):
#      print 'Trovato! Il controller e il device ',k, ', ovvero ',midiDevs[k][1]
#      UA100CONTROL = k

#print UA100CONTROL
   
#print "i device dovrebbero essere", numDevs

#for i in midiDevs:
#   print i,': ',midiDevs[i]




#o = pm.midi.Output(4)
#
#o.write_short(0xB2,18,0)
#
#o.close()

#pm.quit()


# syex message per chiedere il livello del volume del master
# o.write_sys_ex(pyportmidi.time(),[0xf0,0x41,0x10,0x00,0x11,0x11,0x00,0x40,0x50,0x03,0x00,0x00,0x00,0x01,0x6c,0xf7])

# i primi 6 valori (0xf0,0x41,0x10,0x00,0x11,0x11) sono "standard" per la richiesta RQ1
# 0x00,0x40,0x50,0x03 e' l'indirizzo del "Master Level"
# 0x00,0x00,0x00,0x01 e' la dimensione

# 0x6c e' il *checksum*
# 0xf7 (247 in decimale) e' la fine dell'exclusive.

# aprendo uno stream in input e leggendolo con i.read(buffer_len) ottengo (in decimale)

# [i = pm.midi.Input(5) --> OKKIO che il device e' diverso!!! il 4 era solo output, questo e' input
# poi print i.read(1)]

# [[[240, 65, 16, 0], 24568015], [[17, 18, 0, 64], 24568015], [[80, 3, 100, 9], 24568015], [[247, 0, 0, 0], 24568015]]

# dove il dato di interesse e' il "18" (0x12) che identifica il Data Set 1 (DT1) e il 100, che sarebbe il livello del volume al momento.

# il "9" (0x9) e' sempre il nostro bel checksum!

# per impostare un livello con un SysEx message, devo usare il DT1 (data set 1), ovvero
# o.write_sys_ex(pyportmidi.time(),[0xf0,0x41,0x10,0x00,0x11,0x12,0x00,0x40,0x50,0x03,0x7f,0x6e,0xf7])

# dove, come sopra, 0x12 e' il comando (DT1), la dimensione non la metto ma metto solo il valore (0x7f, 127 in decimale)
# aggiungo il checksum e infine f7 (247) per finire il messaggio


# *************************************************************
# *****************  CHECKSUM *********************************

# SI SOMMANO I SINGOLI VALORI DI (INDIRIZZO + CANALE) O (INDIRIZZO + DATI), SI DIVIDE PER 128 (DECIMALE), SI PRENDE IL RESTO E SE NE FA IL COMPLEMENTO A 128
# SI CONVERTE IN HEX IL RISULTATO ET VOILA'!

# fosse: aa bb cc dd ee ff gg hh canale+dimensione farei [128 - (aa+bb+cc+dd+ee+ff+gg mod 128)] con tutti i valori in decimale.
# fosse: aa bb cc dd ee ff  canale + dati, idem. 
