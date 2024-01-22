import subprocess
import argparse
import os
import sys
import platform
import zipfile

PYTHON = sys.executable


def test() -> None:
    subprocess.run([PYTHON, "--version"], check=True)
    subprocess.run(["bazel", "--version"], check=True)
    if platform.system() == "Windows":
        subprocess.run("bazel test --config=msvc :tests".split(), check=True)
        subprocess.run("bazel build --config=msvc :all".split(), check=True)
    else:
        subprocess.run("bazel test --config=gcc :tests".split(), check=True)
        subprocess.run("bazel build --config=gcc :all".split(), check=True)


def pack(name: str) -> None:
    if name == "":
        raise ValueError("pack_name is empty")

    with zipfile.ZipFile(name, "w", zipfile.ZIP_DEFLATED) as zip_f:
        if platform.system() == "Windows":
            bin = "protoc-gen-c.exe"
        else:
            bin = "protoc-gen-c"

        zip_f.write("bazel-bin/" + bin, "bin/" + bin)

        lib = "bazel-bin/libprotobuf-c.so"
        if os.path.exists(lib):
            zip_f.write(lib, "lib/" + os.path.basename(lib))

        lib = "bazel-bin/protobuf-c.dll"
        if os.path.exists(lib):
            zip_f.write(lib, "lib/" + os.path.basename(lib))
            zip_f.write("bazel-bin/protobuf-c.if.lib", "lib/protobuf-c.lib")

        zip_f.write("protobuf-c/protobuf-c.h", "include/protobuf-c/protobuf-c.h")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("mode")
    parser.add_argument("-p", "--pack_name", type=str, default="")
    opt = parser.parse_args()

    if opt.mode == "test":
        test()
    elif opt.mode == "release":
        test()
        pack(opt.pack_name)
    else:
        raise ValueError(f"Unknown mode: {opt.mode}")
