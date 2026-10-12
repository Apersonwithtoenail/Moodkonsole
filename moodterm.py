#!/usr/bin/env python3
import subprocess, sys, time, os, colorsys

CAVA_CONF = "/tmp/moodterm-cava.conf"
open(CAVA_CONF,"w").write("""[general]
framerate = 30
bars = 16
[input]
method = pulse
source = auto
[output]
method = raw
raw_target = /dev/stdout
data_format = ascii
ascii_max_range = 100
bar_delimiter = 59
frame_delimiter = 10
""")

def osc(r,g,b):
    sys.stdout.write(f"\033]11;#{r:02x}{g:02x}{b:02x}\007")
    sys.stdout.flush()

def main():
    p = subprocess.Popen(["cava","-p",CAVA_CONF], stdout=subprocess.PIPE, bufsize=1, universal_newlines=True)
    try:
        for line in p.stdout:
            vals = [int(x) for x in line.strip().split(";") if x.isdigit()]
            if not vals: continue
            bass = sum(vals[:4]) / (4*100)
            mid  = sum(vals[4:10]) / (6*100)
            treb = sum(vals[10:]) / (6*100)
            hue = (bass*0.5 + mid*0.3 + treb*0.2) % 1.0
            r,g,b = colorsys.hsv_to_rgb(hue, 0.35, 0.15)
            osc(int(r*255), int(g*255), int(b*255))
    except KeyboardInterrupt:
        pass
    finally:
        sys.stdout.write("\033]111\007"); sys.stdout.flush()
        p.terminate()

main()
