import sys
import site
import json
import pkg_resources
import yaml
import subprocess

from pip import _internal


print("---Python version & virtual environment---\n", sys.version, sep="")  # 1, 2
print("---Python executable location---\n", sys.executable, sep="")  # 3
print("---Pip version and installed packages---")   # 4, 6
_internal.main(['list'])
pp = (input("Input you PYTHONPATH (/home/user/): "))
print("---PYTHONPATH---\n", sys.path.append(pp), sep="")  # 5
print("---Python site packages---\n", site.getsitepackages(), sep="")   # 7
print("---Additional. All python versions and environments---")
v = subprocess.call("ls /home/student/.pyenv/versions", shell=True)

p = [p.project_name for p in pkg_resources.working_set]

with open("report.json", "w", encoding="utf-8") as outfile:
    json.dump({"Python version & virtual environment": sys.version,
               "Python executable location": sys.executable,
               "Pip version and installed packages": p,
               "PYTHONPATH": sys.path.append(pp),
               "Python site packages": site.getsitepackages(),
               "All python versions": v,
               }, outfile, ensure_ascii=False, indent=2)


with open('report.yml', 'w') as outfile:
    yaml.dump(
        {"python info": {
            "Python version & virtual environment": sys.version,
            "Python executable location": sys.executable,
            "Pip version and installed packages": p,
            "PYTHONPATH": sys.path.append(pp),
            "Python site packages": site.getsitepackages(),
            "All python versions": v}},
        stream=outfile, default_flow_style=False, indent=3)
