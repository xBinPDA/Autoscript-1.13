import subprocess
import os

def main():
    os.system('clear')

    url = "https://raw.githubusercontent.com/xBinPDA/Autoscript-1.13/master/setup.sh"
    subprocess.run(['wget', '-O', 'setup.sh', '-q', url])

    subprocess.run(['chmod', '+x', 'setup.sh'])

    subprocess.run(['./setup.sh'])

    subprocess.run(['rm', '-fr', 'setup.sh'])

if __name__ == "__main__":
    main()
