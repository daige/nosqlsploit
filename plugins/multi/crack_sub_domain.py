# -*- coding:utf-8 -*-
class NSSPlugin:
    '''crack sub_domain'''
    infos = [
        ['���','���ƶ���������������'],
        ['����','jadore'],
        ['����','2014/07/14'],
        ['��ַ','http://jadore.wang']
        ]
    opts  = [
        ['DOMAIN','google.com','Ҫ���ƵĶ�������'],
        ['SUBDIC','dicts/sub_domain.lst','���ƶ����������ֵ�·��'],
        ['PAYLOAD','false','����Ҫ�󹥻����']
        ]
    def exploit(self):
        dicts=open(SUBDIC).readlines()
        pp.prettyPrint("SCANN %s =>SUB DOMAINS"%DOMAIN.upper(),YELLOW)
        pp.prettyPrint("===================="+"="*len(DOMAIN),GREY)
        pp.prettyPrint("%-35s %-25s %-10s"%("FULL DOMAIN","RESULT","SCHEDULE"),YELLOW)
        pp.prettyPrint("%-35s %-25s %-10s"%("-"*35,"-"*25,"-"*10),GREY)
        ll = len(dicts)
        li = 1
        for dic in dicts:
            sub    = dic.strip("\n")
            domain = sub+"."+DOMAIN
            try:
                res = exploitModule.urlToIp(domain)
                log = "%-35s %-25s %-10s"%(domain,res,"%s/%s"%(li,ll))
                pp.prettyPrint(log,GREEN)
                exploitModule.writeLog('sub_domain_%s'%DOMAIN,log)
            except:
                pp.prettyPrint("%-35s %-25s %-10s"%(domain,"ERROR","%s/%s"%(li,ll)),RED)
            li += 1
        pp.prettyPrint("[*] ALL SCAN DONE ! SAVE TO output/sub_domain_%s.log!"%DOMAIN,YELLOW)
