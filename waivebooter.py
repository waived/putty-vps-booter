from colorama import Fore
import os, sys, hashlib, subprocess

_session = False

def main():
    if not os.geteuid() == 0:
        sys.exit("\033[1m\033[37m\r\n    Script requires root elevation!\r\n")
        
    global _session
    if _session == False:
        _hash = 'b32e2c31e1ccfbd1f55b262cabd6fd67'
        os.system("clear")
        try:
            chk = input("\033[1m\033[37mEnter password: \033[22m\033[30m")
            hashed = hashlib.md5(chk.encode()).hexdigest()
            if not hashed == _hash:
                sys.exit('\r\n\033[1m\033[31mInvalid. Exiting...')
            else:
                _session = True
        except KeyboardInterrupt:
            sys.exit('\r\n\033[1m\033[31mAuthentication aborted. Exiting...')
        except:
            sys.exit('\r\n\033[1m\033[31mInvalid. Exiting...')
            
    _user = os.getlogin()
    os.system("clear")
    print('''\033[1m\033[34m User:\033[31m''' + _user + '''\033[34m | Expires:\033[31mLifetime\t\033[37m Programmed by Waived
\033[22m\033[35m
       █   █ ███ █ █ █ ██    █   ███ ███ █   ██ ███
      ░█  ░█░░░█░ ░█░█░█    ░█  ░█░█░█░█░███░█ ░█░ 
      ░█ █░█░███ █░█░█░██   ░███░█░█░█░█░█░ ░██░█
      ░░█░█ ░█░█░█░█░█░█    ░█░█░█░█░█░█░█░█░█ ░█
       ░█░█ ░███░█░░█ ░██   ░███░███░███░░█ ░██░█
       ░ ░  ░░░ ░  ░  ░░    ░░░ ░░░ ░░░  ░  ░░ ░
\033[1m
\033[37m BYPASS[\033[32mON\033[37m]   \033[37mSPOOFING[\033[32mON\033[37m]
<=========================================================>
 [1] \033[32mSUDP      \033[37m[4] \033[32mDOMINATE  \033[37m[7] \033[32mSTORM     \033[37m[10] \033[32mXMAS
 \033[37m[2] \033[32mUDP-MIX   \033[37m[5] \033[32mICMP      \033[37m[8] \033[32mBOGUS     \033[37m[11] \033[32mSYN-X
 \033[37m[3] \033[32mSSYN      \033[37m[6] \033[32mJUNK      \033[37m[9] \033[32mABUSE     \033[37m[12] \033[32mACK\033[37m
<=========================================================>
''')
    try:
        x = input('\033[37m╔═[/]═══> \033[32m')
    except KeyboardInterrupt:
        sys.exit()
        
    try:
        if x == '1':
            subprocess.run(['python3', '_modules/_sudp.py'])
        elif x == '2':
            subprocess.run(['python3', '_modules/_udpmix.py'])
        elif x == '3':
            subprocess.run(['python3', '_modules/_ssyn.py'])
        elif x == '4':
            subprocess.run(['python3', '_modules/_dominate.py'])
        elif x == '5':
            subprocess.run(['python3', '_modules/_icmp.py'])
        elif x == '6':
            subprocess.run(['python3', '_modules/_junk.py'])
        elif x == '7':
            subprocess.run(['python3', '_modules/_storm.py'])
        elif x == '8':
            subprocess.run(['python3', '_modules/_bogus.py'])
        elif x == '9':
            subprocess.run(['python3', '_modules/_abuse.py'])
        elif x == '10':
            subprocess.run(['python3', '_modules/_xmas.py'])
        elif x == '11':
            subprocess.run(['python3', '_modules/_xsyn.py'])
        elif x == '12':
            subprocess.run(['python3', '_modules/_ack.py'])
    except KeyboardInterrupt:
        pass
    except:
        pass
        
    main()
                                                                                                                
if __name__ == "__main__":
    main()
