# -*- coding: utf-8 -*-
class NSSPlugin:
    '''ͬIP��վ��ѯ::tool.chinaz.com/same��'''
    infos = [
        ['�������','ͬIP��վ��ѯ[chinaz]��'],
        ['�������','mst'],
        ['��������','2013/10/23'],
        ['������վ','http://mstoor.duapp.com']
        ]
    opts  = [
        ['RURL','mstoor.duapp.com','Ҫ��ѯ��Ŀ����ַ'],
        ['PAYLOAD','false','����Ҫ�󹥻����']
        ]
    def exploit(self):
        '''��ʼ��ѯ'''
        chinaz = 'http://tool.chinaz.com/Same/'
        value  = {'s':RURL}
        try:
            pp.prettyPrint("[*] Sending data..",YELLOW)
            tmp = exploitModule.urlPOST(chinaz,value).read()
            pp.prettyPrint("[+] Formate data..",YELLOW)
            tmp = tmp.decode("utf-8")
            res = exploitModule.find('.</span> <a href=[^>]+ target=_blank>',tmp)
            reslen = len(res)
            resiii = 1
            reslog = "sameIP_web[chinaz]_%s"%RURL
            for r in res:
                tmp = r[18:]
                tmp = tmp.split("'")
                ok = tmp[0]
                pp.prettyPrint("[%s/%s] %s"%(resiii,reslen,ok),GREEN)
                exploitModule.writeLog(reslog,ok+"\n")
                resiii += 1
            pp.prettyPrint("[*] Get data Successful !LOG:output/%s.log"%reslog,CYAN)
        except Exception,e:
            pp.prettyPrint("[!] Err:%s"%e,RED)
