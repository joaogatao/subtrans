from googletrans import Translator
import time     # not to get kicked off of Google
from random import random
translator = Translator()

"""
Auto-translation script for subtitle files
by João Gatão, 01/2020

INPUT
# Set filename
# Set original and destination language

Script follows the standard formatting of .srt-files; I'm not aware of different formatting.
"""
filename = 'jan_sluijters'
orig = 'nl'     # Dutch
tran = 'en'     # English
sin =  open(filename+'_'+orig+'.srt','r')
sout = open(filename+'_'+tran+'.srt','w')

# maximum number of characters on 1 line:
mcl = 60

"""
BEGIN
"""
sin = (sin.read()).splitlines()
lindex = []

# make list of line indexes that contain the timing of a new subtitle entry
for l in range(len(sin)):
    if sin[l][:3] == '00:' or sin[l][:3] == '01:': lindex.append(l)
lindex.append(-1)

# compose out document with translation
for i in range(len(lindex)-1):
    s = lindex[i]           # current sub index
    n = lindex[i+1]     # next sub index
    sout.write(sin[s-1]+'\n')
    sout.write(sin[s]+'\n')
    sub = ''
    for l in range((s+1),(n-1)): 
        sub += sin[l]+' '
    # translate + time delay
    subt = translator.translate(sub, src=orig, dest=tran).text
    time.sleep( random()*2+1 )      # else Google detects the bot and throws an error
    # place line breaks
    istart, iend = 0,0
    for b in range(len(subt)//mcl + 1):
        try: 
            iend = subt.index(' ', (b+1)*mcl)
            sout.write(subt[istart:iend]+'\n')
            istart=iend+1
        except: break
    sout.write(subt[istart:]+'\n\n')
            
sin.close()
sout.close()
