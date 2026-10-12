# moodterm

Your konsole background shifts color based on the mood of the music playing.

Reads cava's FFT output, averages bass / mid / treble, maps to HSV hue, pushes via OSC 11.

## Install

```bash
./install.sh
```

## Use

```bash
moodterm
```

Play music. Background hue drifts with the beat. Ctrl+C to stop (bg resets to default).

## Requires

- `cava` (pulseaudio / pipewire loopback)
- konsole (OSC 11 support)

## License

MIT
