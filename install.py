from __future__ import annotations

import os
import sys
from tqdm import tqdm
import urllib.request
import importlib.util
import subprocess
from importlib.metadata import version  # python >= 3.8
from packaging.version import parse

req_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), "requirements.txt")

models_dir = os.path.abspath("models/roop")
model_url = "https://github.com/P2Enjoy/sd-webui-roop-uncensored/releases/download/onnx/inswapper_128.onnx"
model_name = os.path.basename(model_url)
model_path = os.path.join(models_dir, model_name)

def download(url, path):
    request = urllib.request.urlopen(url)
    total = int(request.headers.get('Content-Length', 0))
    with tqdm(total=total, desc='Downloading', unit='B', unit_scale=True, unit_divisor=1024) as progress:
        urllib.request.urlretrieve(url, path, reporthook=lambda count, block_size, total_size: progress.update(block_size))

def is_installed(
    package: str, min_version: str | None = None, max_version: str | None = None
):
    try:
        spec = importlib.util.find_spec(package)
    except ModuleNotFoundError:
        return False

    if spec is None:
        return False

    if not min_version and not max_version:
        return True

    if not min_version:
        min_version = "0.0.0"
    if not max_version:
        max_version = "99999999.99999999.99999999"

    if package == "google.protobuf":
        package = "protobuf"

    try:
        pkg_version = version(package)
        return parse(min_version) <= parse(pkg_version) <= parse(max_version)
    except Exception:
        return False

def run_pip(*args):
    subprocess.run([sys.executable, "-m", "pip", "install", *args])

def install():
    deps = [
        ("insightface", "0.7.3", None),
        ("onnx", "1.14.0", None),
        ("onnxruntime", "1.15.0", None),
        ("opencv-python", "4.7.0.72", None),
        ("cython", None, None),
    ]

    for pkg, low, high in deps:
        if not is_installed(pkg, low, high):
            if low and high:
                cmd = f"{pkg}>={low},<={high}"
            elif low:
                cmd = f"{pkg}>={low}"
            else:
                cmd = pkg

            run_pip("-U", cmd)


if not os.path.exists(models_dir):
    os.makedirs(models_dir)

if not os.path.exists(model_path):
    download(model_url, model_path)
    
try:
    import launch
    
    skip_install = launch.args.skip_install
except Exception:
    skip_install = False

if not skip_install:
    install()



