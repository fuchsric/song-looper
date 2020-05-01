# song-looper

Generate looped audio of arbitrary length given audio with two repetitions

## How to use

- Use audio editing software like [Audacity](https://www.audacityteam.org/) to create a WAV file with two repetitions of the song. You can make the transition between them as smooth as you like
- Run this script to create a WAV file of any length you like, automatically increasing the number of repetitions. For example: `python3 song-looper.py -i mysong.wav -o mysong1h.wav --target 1:00:00` creates a 1 hour loop of the song

## Dependencies

- [python 3.7 (or newer)](https://www.python.org/)
- [click](https://pypi.org/project/click/)
