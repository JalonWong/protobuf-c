import argparse
import subprocess

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--exe")
    parser.add_argument("-o")
    parser.add_argument("-a", "--arg", type=str, default=[], action="extend", nargs="+")
    opt = parser.parse_args()
    with open(opt.o, "w", encoding="utf-8") as f:
        subprocess.run([opt.exe] + opt.arg, stdout=f)
