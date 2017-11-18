import Lab1SI.app.Algorithm as Algorithm
import subprocess

def main():
    a = Algorithm.Algorithm(ffe = 20, sizeOfPop = 30, pc = 40, pm = 15)
    #b = Algorithm.Algorithm(100, 20, 30, 10)
    a.run()
    #b.run()
    '''
    command = "sumo -c /media/arek/N/PWR/VII/SI/dane/acosta/run.sumo.cfg -v"
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=None, shell=True)

    # Launch the shell command:
    output = process.communicate()

    print(output[0])
    '''


    return

if __name__ == "__main__":
        main()
