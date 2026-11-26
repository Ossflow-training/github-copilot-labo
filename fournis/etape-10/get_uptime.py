import subprocess


def get_uptime():
    sortie = subprocess.run("cat /proc/uptime", shell=True,
                            capture_output=True, text=True, check=True)
    return float(sortie.stdout.split()[0])
