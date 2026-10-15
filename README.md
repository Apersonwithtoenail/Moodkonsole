# Moodkonsole

Your konsole background hue drifts with whatever music is playing.

Reads cava's FFT, averages bass / mid / treble, maps to HSV hue, pushes via OSC 11.

## Install

```bash
git clone https://github.com/Apersonwithtoenail/Moodkonsole.git
cd Moodkonsole
./install.sh
```

## Use

```bash
moodterm
```

Play music â€” the background hue drifts with the beat. Ctrl+C or ``q`` to stop. Background resets to your Konsole profile default on exit (via OSC 111).

## Requires

- Python 3Ê- cava
- Konsole (or any terminal with OSC 11 support)
-  PipeWire or PulseAudio

## License

MIT
