import wave
import click


def read_wav(file):
    with wave.open(file, "rb") as f:
        assert f.getnchannels() == 2
        assert f.getsampwidth() == 2
        return f.readframes(f.getnframes()), f.getframerate()


def write_wav(file, rate, start, middle, end, n):
    with wave.open(file, "wb") as f:
        f.setnchannels(2)
        f.setsampwidth(2)
        f.setframerate(rate)

        f.writeframes(start)
        for i in range(n):
            f.writeframes(middle)
        f.writeframes(end)


def find_repeated_section(a, blocklength):
    a = a[1::4]
    for i in range(0, len(a)-2*blocklength, blocklength):
        print(f"{i//blocklength} ({i*100/len(a):.2f}%)")
        for j in range(i+blocklength, len(a)-blocklength):
            if all(a[i+k]-a[j+k] in (-0xff, -1, 0, 1, 0xff) for k in range(blocklength)):
                return i, j
    raise RuntimeError("no repeated section found")


@click.command()
@click.option('-i', help="input file")
@click.option('-o', help="output file")
@click.option('-t', '--target', help="target length")
def loop(i, o, target):
    """
    Generate looped audio of arbitrary length given audio with two repetitions
    """
    target = sum(int(j)*60**i for i, j in enumerate(target.split(":")[::-1]))

    data, r = read_wav(i)
    left, right = find_repeated_section(data, 10*r)

    start = data[:left*4]
    middle = data[left*4:right*4]
    end = data[right*4:]

    n = round((target*r - len(start)//4 - len(end)//4) / (len(middle)//4))

    write_wav(o, r, start, middle, end, n)


if __name__ == "__main__":
    loop()
