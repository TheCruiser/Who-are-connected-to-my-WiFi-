#this script helps to find the devices connected to my wifi (python-nmap)
import nmap
import subprocess

def scan_network():
        scanner = nmap.PortScanner()
        myIP = subprocess.check_output(['hostname -I'], shell=True)
        myIP = str(myIP,'utf-8').split('.')
        print(myIP[:3])
        scannedData = scanner.scan(hosts = '.'.join(myIP[:3])+'.1/24',arguments ='sP')

        for hostnames in scannedData['scan']:
                print(hostnames)

scan_network()
