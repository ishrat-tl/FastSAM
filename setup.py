# This source code is licensed under the license found in the
# LICENSE file in the root directory of this source tree.

from setuptools import find_packages, setup

def parse_line(line):
    """Parse information from a line in a requirements text file."""
    if line.startswith("-r "):
        # Allow specifying requirements in other files
        target = line.split(" ")[1]
        for info in parse_require_file(target):
            yield info
    else:
        info = {"line": line}
        if line.startswith("-e "):
            info["package"] = line.split("#egg=")[1]
        elif "@git+" in line:
            info["package"] = line
        else:
            # Remove versioning from the package
            pat = "(" + "|".join([">=", "==", ">"]) + ")"
            parts = re.split(pat, line, maxsplit=1)
            parts = [p.strip() for p in parts]

            info["package"] = parts[0]
            if len(parts) > 1:
                op, rest = parts[1:]
                if ";" in rest:
                    # Handle platform specific dependencies
                    # http://setuptools.readthedocs.io/en/latest/setuptools.html#declaring-platform-specific-dependencies
                    version, platform_deps = map(str.strip, rest.split(";"))
                    info["platform_deps"] = platform_deps
                else:
                    version = rest  # NOQA
                info["version"] = (op, version)
        yield info

def parse_require_file(fpath):
    with open(fpath, "r") as f:
        for line in f.readlines():
            line = line.strip()
            if line and not line.startswith("#"):
                for info in parse_line(line):
                    yield info


setup(
    name="fastsam",
    version="0.1.1",
    install_requires=parse_requirements("requirements.txt"),
    package_dir= {
        "fastsam": "fastsam",
        "fastsam_tools": "utils",
    },
    url="https://github.com/CASIA-IVA-Lab/FastSAM",
)
