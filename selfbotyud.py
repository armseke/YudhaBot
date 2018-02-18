# -*- coding: utf-8 -*-
#Jngn diganti hargain creator

import yuda
from yuda.lib.curve.ttypes import *
from datetime import datetime
import time, random, sys, ast, re, os, io, json, subprocess, threading, string, codecs, requests, tweepy, ctypes, urllib, urllib2, wikipedia, goslate
import timeit
from bs4 import BeautifulSoup
from urllib import urlopen
from io import StringIO
from threading import Thread
from gtts import gTTS
from googletrans import Translator

import six

if (six.PY2):
    import urllib2
    import urllib
else:
    import urllib.request
    import urllib.parse

yudha = yuda.LINE()
yudha.login(token="Ep9sO4WjoHpnRU0tPoD3.e3js3/SAsD0pcXJS1rvp0W.xjxAGekPq84512h3OZ1d7OhpocIpIqQaA3fqYXuuCb8=")
yudha.loginResult()

print "========[Yudha Login Success]========="
reload(sys)
sys.setdefaultencoding('utf-8')

yudmsg ="""-------     -------
 ****     ****
  -----     -----
   ***    ***
      ------
      ****
      ------
      ****

------        ------
****        ****
------        ------
****        ****
   -------------
     ******

-----------------
****     ****
------       ------
****       ****
------       ------
****      ****
------     ------
**********

------      ------
****      ****
------      ------
************
------------------
****      ****
------      ------
****      ****

      -----
  **** ****
 -----     -----
****     ****
-----------------
****     ****
------     ------
****     ****
"""

helpmsg ="""╔═════════════════
║            ☆☞ H E L P ☜☆
╠═════════════════
║╠❂➣〘!yud〙
║╠❂➣〘!yudself〙
║╠❂➣〘!yudpro〙
║╠❂➣〘!yudset〙
║╠❂➣〘!yudgroup〙
║╠❂➣〘!yudmed〙
╚═════════════════
"""

helppro ="""╔═════════════════
║          ☆☞ P R O T E C T ☜☆
╠═════════════════
╠➩〘Protect on/off〙
╠➩〘Qr on/off〙
╠➩〘Invit on/off〙
╠➩〘Cancel on/off〙
╚═════════════════
"""

helpself ="""╔═════════════════
║            ☆☞ S E L F ☜☆
╠═════════════════
╠➩〘Me〙
╠➩〘Checkmid: 〙
╠➩〘Checkid: 〙
╠➩〘Myname: 〙
╠➩〘Mybio: 〙
╠➩〘Myname〙
╠➩〘Mybio〙
╠➩〘Mypict〙
╠➩〘Mycover〙
╠➩〘Mycopy @〙
╠➩〘Mybackup〙
╠➩〘Getgrup image〙
╠➩〘Getmid @〙
╠➩〘Getprofile @〙
╠➩〘Getcontact @〙
╠➩〘Getinfo @〙
╠➩〘Getname @〙
╠➩〘Getbio @〙
╠➩〘Getpict @〙
╠➩〘Getcover @〙
╠➩〘Mention〙
╠➩〘Sider on/off〙
╠➩〘Sider〙
╠➩〘Mimic on/off〙
╠➩〘Micadd @〙
╠➩〘Micdel @〙
╚═════════════════
"""

helpset ="""╔═════════════════
║         ☆☞ S E T T I N G ☜☆
╠═════════════════
╠➩〘Contact on/off〙
╠➩〘Autojoin on/off〙
╠➩〘Autoleave on/off〙
╠➩〘Autoadd on/off〙
╠➩〘Like me〙
╠➩〘Like friend〙
╠➩〘Like on〙
╠➩〘Respon on/off〙
╠➩〘Responkick on/off〙
╠➩〘Read on/off〙
╠➩〘simisimi on/off〙
╚═════════════════
"""

helpgrup ="""╔═════════════════
║           ☆☞ G R O U P ☜☆
╠═════════════════
╠➩〘Link on/off〙
╠➩〘Url〙
╠➩〘Cancel〙
╠➩〘Gcreator〙
╠➩〘Kick @〙
╠➩〘Ulti @〙
╠➩〘Cancel〙
╠➩〘Gname: 〙
╠➩〘Infogrup〙
╠➩〘Gruplist〙
╠➩〘Friendlist〙
╠➩〘Blocklist〙
╠➩〘Ban @〙
╠➩〘Unban @〙
╠➩〘yudhaearban〙
╠➩〘Banlist〙
╠➩〘Contactban〙
╠➩〘Midban〙
╚═════════════════
"""

helpmed ="""╔═════════════════
║           ☆☞ M E D I A ☜☆
╠═════════════════
╠➩〘kalender〙
╠➩〘tr-id 〙
╠➩〘tr-en 〙
╠➩〘tr-jp 〙
╠➩〘tr-ko 〙
╠➩〘say-id 〙
╠➩〘say-en 〙
╠➩〘say-jp 〙
╠➩〘say-ko 〙
╠➩〘/cekig 〙
╠➩〘/postig 〙
╠➩〘checkdate 〙
╠➩〘wikipedia 〙
╠➩〘lirik 〙
╠➩〘video 〙
╠➩〘/image 〙
╠➩〘/youtube 〙
╚═════════════════
"""

mid = yudha.getProfile().mid
Bots=[mid]

wait = {
    "likeOn":True,
    "alwayRead":False,
    "detectMention":True,    
    "kickMention":False,
    "steal":False,
    'pap':{},
    'invite':{},
    "spam":{},
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":False,"members":1},
    'leaveRoom':False,
    'timeline':False,
    'autoAdd':False,
    'message':"Thx For Add Me (^_^)\nInvite Me To Your Group ヘ(^_^)ヘ\nCreator :\nline.me/ti/p/~@ikj9968f\nline.me/ti/p/~iniyud",
    "lang":"JP",
    "comment":"Bot Auto Like By : Yudha\nContact Me : 👉 line.me/ti/p/~iniyud",
    "commentOn":True,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "yudhaock":False,
    "cNames":"",
    "cNames":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "protect":False,
    "cancelprotect":False,
    "inviteprotect":False,
    "linkprotect":False,
}

wait2 = {
    "readPoint":{},
    "readMember":{},
    "setTime":{},
    "ROM":{}
    }

mimic = {
    "copy":False,
    "copy2":False,
    "status":False,
    "target":{}
    }
    
settings = {
    "simiSimi":{}
    }

res = {
    'num':{},
    'us':{},
    'au':{},
    }

setTime = {}
setTime = wait2['setTime']
mulai = time.time() 

contact = yudha.getProfile()
backup = yudha.getProfile()
backup.displayName = contact.displayName
backup.statusMessage = contact.statusMessage                        
backup.pictureStatus = contact.pictureStatus

def restart_program():
    python = sys.executable
    os.exeyudha(python, python, * sys.argv)
    
def download_page(url):
    version = (3,0)
    cur_version = sys.version_info
    if cur_version >= version:     
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"
            req = urllib.request.Request(url, headers = headers)
            resp = urllib.request.urlopen(req)
            respData = str(resp.read())
            return respData
        except Exception as e:
            print(str(e))
    else:                        
        import urllib2
        try:
            headers = {}
            headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
            req = urllib2.Request(url, headers = headers)
            response = urllib2.urlopen(req)
            page = response.read()
            return page
        except:
            return"Page Not found"
            
def _images_get_next_item(s):
    start_line = s.find('rg_di')
    if start_line == -1:    
        end_quote = 0
        link = "no_links"
        return link, end_quote
    else:
        start_line = s.find('"yudhaass="rg_meta"')
        start_content = s.find('"ou"',start_line+1)
        end_content = s.find(',"ow"',start_content+1)
        content_raw = str(s[start_content+6:end_content-1])
        return content_raw, end_content
        
def _images_get_all_items(page):
    items = []
    while True:
        item, end_content = _images_get_next_item(page)
        if item == "no_links":
            break
        else:
            items.append(item)      
            time.sleep(0.1)        
            page = page[end_content:]
    return items
    
def upload_tempimage(yudhaient):
    '''
        Upload a picture of a kitten. We don't ship one, so get creative!
    '''
    config = {
        'album': album,
        'name':  'bot auto upload',
        'title': 'bot auto upload',
        'description': 'bot auto upload'
    }

    print("Uploading image... ")
    image = yudhaient.upload_from_path(image_path, config=config, anon=False)
    print("Done")
    print()

def summon(to, nama):
    aa = ""
    bb = ""
    strt = int(14)
    akh = int(14)
    nm = nama
    for mm in nm:
      akh = akh + 2
      aa += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(mm)+"},"""
      strt = strt + 6
      akh = akh + 4
      bb += "\xe2\x95\xa0 @x \n"
    aa = (aa[:int(len(aa)-1)])
    msg = Message()
    msg.to = to
    msg.text = "\xe2\x95\x94\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\n"+bb+"\xe2\x95\x9a\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90\xe2\x95\x90"
    msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+aa+']}','EMTVER':'4'}
    print "[Command] Tag All"
    try:
       yudha.sendMessage(msg)
    except Exception as error:
       print error
       
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs) 
    
def sendImage(self, to_, path):
        M = Message(to=to_,contentType = 1)
        M.contentMetadata = None
        M.contentPreview = None
        M_id = self._yudhaient.sendMessage(M).id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'image',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self._yudhaient.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload image failure.')
        #r.content
        return True

def sendImageWithURL(self, to_, url):
      path = '%s/pythonLine-%i.data' % (tempfile.gettempdir(), randint(0, 9))
      r = requests.get(url, stream=True)
      if r.status_code == 200:
         with open(path, 'w') as f:
            shutil.copyfileobj(r.raw, f)
      else:
         raise Exception('Download image failure.')
      try:
         self.sendImage(to_, path)
      except Exception as e:
         raise e
         
def sendAudio(self, to_, path):
        M = Message(to=to_, text=None, contentType = 3)
        M.contentMetadata = None
        M.contentPreview = None
        M2 = self.Talk.yudhaient.sendMessage(0,M)
        M_id = M2.id
        files = {
            'file': open(path, 'rb'),
        }
        params = {
            'name': 'media',
            'oid': M_id,
            'size': len(open(path, 'rb').read()),
            'type': 'audio',
            'ver': '1.0',
        }
        data = {
            'params': json.dumps(params)
        }
        r = self.post_content('https://os.line.naver.jp/talk/m/upload.nhn', data=data, files=files)
        if r.status_code != 201:
            raise Exception('Upload audio failure.')
        return True

def sendAudioWithUrl(self, to_, url):
        path = '%s/pythonLine-%1.data' % (tempfile.gettempdir(), randint(0, 9))

        r = requests.get(url, stream=True)
        if r.status_code == 200:
            with open(path, 'w') as f:
                shutil.copyfileobj(r.raw, f)
        else:
            raise Exception('Download audio failure.')

        try:
            self.sendAudio(to_, path)
        except Exception as e:
            raise (e)

def cms(string, commands): #/XXX, >XXX, ;XXX, ^XXX, %XXX, $XXX...
    tex = ["+","@","/",">",";","^","%","$","＾","サテラ:","サテラ:","サテラ：","サテラ："]
    for texX in tex:
        for command in commands:
            if string ==command:
                return True
    return False

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 13:
            if mid in op.param3:
                G = yudha.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            yudha.rejectGroupInvitation(op.param1)
                        else:
                            yudha.acceptGroupInvitation(op.param1)
                    else:
                        yudha.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        yudha.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    yudha.cancelGroupInvitation(op.param1, matched_list)
        if op.type == 19:
            if mid in op.param3:
                wait["blacklist"][op.param2] = True
        if op.type == 22:
            if wait["leaveRoom"] == True:
                yudha.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                yudha.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message
            if msg.toType == 0:
                msg.to = msg.from_
                if msg.from_ == mid:
                    if "join:" in msg.text:
                        list_ = msg.text.split(":")
                        try:
                            yudha.acceptGroupInvitationByTicket(list_[1],list_[2])
                            G = yudha.getGroup(list_[1])
                            G.preventJoinByTicket = True
                            yudha.updateGroup(G)
                        except:
                            yudha.sendText(msg.to,"error")
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    yudha.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata["postEndUrl"]
                yudha.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.from_ in mimic["target"] and mimic["status"] == True and mimic["target"][msg.from_] == True:
                    text = msg.text
                    if text is not None:
                        yudha.sendText(msg.to,text)
        if op.type == 26:
            msg = op.message
            if msg.to in settings["simiSimi"]:
                if settings["simiSimi"][msg.to] == True:
                    if msg.text is not None:
                        text = msg.text
                        r = requests.get("http://api.ntcorp.us/chatbot/v1/?text=" + text.replace(" ","+") + "&key=beta1.nt")
                        data = r.text
                        data = json.loads(data)
                        if data['status'] == 200:
                            if data['result']['result'] == 100:
                                yudha.sendText(msg.to, "[ChatBOT] " + data['result']['response'].encode('utf-8'))
                                
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["detectMention"] == True:
                     contact = yudha.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Dont Tag!! Lagi Sibuk",cName + " Ngapain Ngetag?",cName + " Nggak Usah Tag-Tag! Kalo Penting Langsung Pc Aja","Gw Lagi Off", cName + " Kenapa Tag Saya?","Gw Lagi Tidur\nJangan Di Tag " + cName, "Jangan Suka Tag Gua " + cName, "Kamu Siapa " + cName + "?", "Ada Perlu Apa " + cName + "?","Woii " + cName + " Jangan Ngetag, Riibut!","Yudha nya lagi off, pc aja kalo penting!","وَعَلَيْكُمْ السَّلاَمُ وَرَحْمَةُ اللهِوَبَرَكَاتُ"]
                     ret_ = "[ᴀᴜᴛᴏʀᴇsᴘᴏɴ] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  yudha.sendText(msg.to,ret_ + cName)
                                  break            
                    
            if 'MENTION' in msg.contentMetadata.keys() != None:
                 if wait["kickMention"] == True:
                     contact = yudha.getContact(msg.from_)
                     cName = contact.displayName
                     balas = ["Aku Bilang Jangan Ngetag Lagi " + cName + "\nAku Kick Kamu! Sorry, Byee!!!"]
                     ret_ = "[Auto Respond Kick] " + random.choice(balas)
                     name = re.findall(r'@(\w+)', msg.text)
                     mention = ast.literal_eval(msg.contentMetadata['MENTION'])
                     mentionees = mention['MENTIONEES']
                     for mention in mentionees:
                           if mention['M'] in Bots:
                                  yudha.sendText(msg.to,ret_)
                                  yudha.kickoutFromGroup(msg.to,[msg.from_])
                                  break
            
            if msg.contentType == 13:
                if wait['invite'] == True:
                     _name = msg.contentMetadata["displayName"]
                     invite = msg.contentMetadata["mid"]
                     groups = yudha.getGroup(msg.to)
                     pending = groups.invitee
                     targets = []
                     for s in groups.members:
                         if _name in s.displayName:
                             yudha.sendText(msg.to, _name + " Berada DiGrup Ini")
                         else:
                             targets.append(invite)
                     if targets == []:
                         pass
                     else:
                         for target in targets:
                             try:
                                 yudha.findAndAddContactsByMid(target)
                                 yudha.inviteIntoGroup(msg.to,[target])
                                 yudha.sendText(msg.to,"Invite " + _name)
                                 wait['invite'] = False
                                 break                              
                             except:             
                                      yudha.sendText(msg.to,"Error")
                                      wait['invite'] = False
                                      break
            
            if msg.contentType == 13:
                if wait["steal"] == True:
                    _name = msg.contentMetadata["displayName"]
                    copy = msg.contentMetadata["mid"]
                    groups = yudha.getGroup(msg.to)
                    pending = groups.invitee
                    targets = []
                    for s in groups.members:
                        if _name in s.displayName:
                            print "[Target] Stealed"
                            break                             
                        else:
                            targets.append(copy)
                    if targets == []:
                        pass
                    else:
                        for target in targets:
                            try:
                                yudha.findAndAddContactsByMid(target)
                                contact = yudha.getContact(target)
                                cu = yudha.channel.getCover(target)
                                path = str(cu)
                                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                                yudha.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + msg.contentMetadata["mid"] + "\n\nBio :\n" + contact.statusMessage)
                                yudha.sendText(msg.to,"Profile Picture " + contact.displayName)
                                yudha.sendImageWithURL(msg.to,image)
                                yudha.sendText(msg.to,"Cover " + contact.displayName)
                                yudha.sendImageWithURL(msg.to,path)
                                wait["steal"] = False
                                break
                            except:
                                    pass    
                                
            if wait["alwayRead"] == True:
                if msg.toType == 0:
                    yudha.sendChatChecked(msg.from_,msg.id)
                else:
                    yudha.sendChatChecked(msg.to,msg.id)
        if op.type == 25:
            msg = op.message
            if msg.contentType == 13:
                if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        yudha.sendText(msg.to,"In Blacklist")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        yudha.sendText(msg.to,"Nothing")
                elif wait["dblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        yudha.sendText(msg.to,"Done")
                        wait["dblack"] = False
                    else:
                        wait["dblack"] = False
                        yudha.sendText(msg.to,"Not in Blacklist")
                elif wait["wblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        yudha.sendText(msg.to,"In Blacklist")
                        wait["wblacklist"] = False
                    else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        yudha.sendText(msg.to,"Done")
                elif wait["dblacklist"] == True:
                    if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        yudha.sendText(msg.to,"Done")
                        wait["dblacklist"] = False
                    else:
                        wait["dblacklist"] = False
                        yudha.sendText(msg.to,"Done")
                elif wait["contact"] == True:
                    msg.contentType = 0
                    yudha.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = yudha.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = yudha.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        yudha.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = yudha.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = yudha.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        yudha.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "menempatkan URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = msg.contentMetadata["postEndUrl"]
                    yudha.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text.lower() == 'help':
                if wait["lang"] == "JP":
                    yudha.sendText(msg.to,yudmsg)
                else:
                    yudha.sendText(msg.to,yudmsg)
            elif msg.text.lower() == '!yud':
                if wait["lang"] == "JP":
                    yudha.sendText(msg.to,helpmsg)
                else:
                    yudha.sendText(msg.to,helpmsg)
            elif msg.text.lower() == '!yudpro':
                if wait["lang"] == "JP":
                    yudha.sendText(msg.to,helppro)
                else:
                    yudha.sendText(msg.to,helppro)
            elif msg.text.lower() == '!yudself':
                if wait["lang"] == "JP":
                    yudha.sendText(msg.to,helpself)
                else:
                    yudha.sendText(msg.to,helpself)
            elif msg.text.lower() == '!yudgroup':
                if wait["lang"] == "JP":
                    yudha.sendText(msg.to,helpgrup)
                else:
                    yudha.sendText(msg.to,helpgrup)
            elif msg.text.lower() == '!yudset':
                if wait["lang"] == "JP":
                    yudha.sendText(msg.to,helpset)
                else:
                    yudha.sendText(msg.to,helpset)
            elif msg.text.lower() == '!yudmed':
                if wait["lang"] == "JP":
                    yudha.sendText(msg.to,helpmed)
                else:
                    yudha.sendText(msg.to,helpmed)
            elif msg.text.lower() == 'speed':
                yudha.sendText(msg.to, "「Speed My SelfBot」")
                start = time.time()
                time.sleep(0.07)
                elapsed_time = time.time() - start
                yudha.sendText(msg.to, "☞「 Speed SelfBot 」\n☞ Type: Speed\n☞ Speed : %sseconds" % (elapsed_time))
            elif msg.text.lower() == 'gas':
                yudha.sendText(msg.to, "「Speed My SelfBot」")
                start = time.time()
                time.sleep(0.07)
                elapsed_time = time.time() - start
                yudha.sendText(msg.to, "☞「 Speed SelfBot 」\n☞ Type: Speed\n☞ Speed : %sseconds" % (elapsed_time))
            elif msg.text.lower() == 'crash':
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uecc57cb55f480ee2a45d81434a9b864d',"}
                yudha.sendMessage(msg)
            elif msg.text.lower() == 'me':
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                yudha.sendMessage(msg)
#========================== B O T ``C O M M A N D =============================#
#==============================================================================#
            elif msg.text.lower() == 'contact on':
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"contact set to on")
                    else:
                        yudha.sendText(msg.to,"contact already on")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"contact set to on")
                    else:
                        yudha.sendText(msg.to,"contact already on")
            elif msg.text.lower() == 'contact off':
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"contact set to off")
                    else:
                        yudha.sendText(msg.to,"contact already off")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"contact set to off")
                    else:
                        yudha.sendText(msg.to,"contact already off")
            elif msg.text.lower() == 'protect on':
                if wait["protect"] == True:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Protection set to on")
                    else:
                        yudha.sendText(msg.to,"Protection already on")
                else:
                    wait["protect"] = True
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Protection set to on")
                    else:
                        yudha.sendText(msg.to,"Protection already on")
            elif msg.text.lower() == 'qr on':
                if wait["linkprotect"] == True:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Protection Qr set to on")
                    else:
                        yudha.sendText(msg.to,"Protection Qr already on")
                else:
                    wait["linkprotect"] = True
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Protection Qr set to on")
                    else:
                        yudha.sendText(msg.to,"Protection Qr already on")
            elif msg.text.lower() == 'invite on':
                if wait["inviteprotect"] == True:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Protection Invite set to on")
                    else:
                        yudha.sendText(msg.to,"Protection Invite already on")
                else:
                    wait["inviteprotect"] = True
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Protection Invite set to on")
                    else:
                        yudha.sendText(msg.to,"Protection Invite already on")
            elif msg.text.lower() == 'cancel on':
                if wait["cancelprotect"] == True:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Cancel Protection set to on")
                    else:
                        yudha.sendText(msg.to,"Cancel Protection already on")
                else:
                    wait["cancelprotect"] = True
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Cancel Protection set to on")
                    else:
                        yudha.sendText(msg.to,"Cancel Protection already on")
            elif msg.text.lower() == 'autojoin on':
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Autojoin set to on")
                    else:
                        yudha.sendText(msg.to,"Autojoin already on")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Autojoin set to on")
                    else:
                        yudha.sendText(msg.to,"Autojoin already on")
            elif msg.text.lower() == 'autojoin off':
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Autojoin set to off")
                    else:
                        yudha.sendText(msg.to,"Autojoin already off")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Autojoin set to off")
                    else:
                        yudha.sendText(msg.to,"Autojoin already off")
            elif msg.text.lower() == 'protect off':
                if wait["protect"] == False:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Protection set to off")
                    else:
                        yudha.sendText(msg.to,"Protection already off")
                else:
                    wait["protect"] = False
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Protection set to off")
                    else:
                        yudha.sendText(msg.to,"Protection already off")
            elif msg.text.lower() == 'qr off':
                if wait["linkprotect"] == False:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Protection Qr set to off")
                    else:
                        yudha.sendText(msg.to,"Protection Qr already off")
                else:
                    wait["linkprotect"] = False
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Protection Qr set to off")
                    else:
                        yudha.sendText(msg.to,"Protection Qr already off")
            elif msg.text.lower() == 'invite off':
                if wait["inviteprotect"] == False:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Protection Invite set to off")
                    else:
                        yudha.sendText(msg.to,"Protection Invite already off")
                else:
                    wait["inviteprotect"] = False
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Protection Invite set to off")
                    else:
                        yudha.sendText(msg.to,"Protection Invite already off")
            elif msg.text.lower() == 'cancel off':
                if wait["cancelprotect"] == False:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Cancel Protection Invite set to off")
                    else:
                        yudha.sendText(msg.to,"Cancel Protection Invite already off")
                else:
                    wait["cancelprotect"] = False
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Cancel Protection Invite set to off")
                    else:
                        yudha.sendText(msg.to,"Cancel Protection Invite already off")
            elif "Grup cancel:" in msg.text:
                try:
                    strnum = msg.text.replace("Grup cancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            yudha.sendText(msg.to,"Itu off undangan ditolak??\nSilakan kirim dengan menentukan jumlah orang ketika Anda menghidupkan")
                        else:
                            yudha.sendText(msg.to,"Off undangan ditolak??Sebutkan jumlah terbuka ketika Anda ingin mengirim")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            yudha.sendText(msg.to,strnum + "Kelompok berikut yang diundang akan ditolak secara otomatis")
                        else:
                            yudha.sendText(msg.to,strnum + "The team deyudhained to create the following automatic invitation")
                except:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Nilai tidak benar")
                    else:
                        yudha.sendText(msg.to,"Weird value")
            elif msg.text.lower() == 'autoleave on':
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Auto Leave room set to on")
                    else:
                        yudha.sendText(msg.to,"Auto Leave room already on")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Auto Leave room set to on")
                    else:
                        yudha.sendText(msg.to,"Auto Leave room already on")
            elif msg.text.lower() == 'autoleave off':
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Auto Leave room set to off")
                    else:
                        yudha.sendText(msg.to,"Auto Leave room already off")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Auto Leave room set to off")
                    else:
                        yudha.sendText(msg.to,"Auto Leave room already off")
            elif msg.text.lower() == 'share on':
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Share set to on")
                    else:
                        yudha.sendText(msg.to,"Share already on")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Share set to on")
                    else:
                        yudha.sendText(msg.to,"Share already on")
            elif msg.text.lower() == 'share off':
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Share set to off")
                    else:
                        yudha.sendText(msg.to,"Share already off")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Share set to off")
                    else:
                        yudha.sendText(msg.to,"Share already off")
            elif msg.text.lower() == 'status':
                md = ""
                if wait["contact"] == True: md+="􀠁􀆩􏿿 Contact:on 􀜁􀄯􏿿\n"
                else: md+="􀠁􀆩􏿿 Contact:off􀜁􀄰􏿿\n"
                if wait["autoJoin"] == True: md+="􀠁􀆩􏿿 Auto Join:on 􀜁􀄯􏿿\n"
                else: md +="􀠁􀆩􏿿 Auto Join:off􀜁􀄰􏿿\n"
                if wait["autoCancel"]["on"] == True:md+="􀠁􀆩􏿿 Auto cancel:" + str(wait["autoCancel"]["members"]) + "􀜁􀄯􏿿\n"
                else: md+= "􀠁􀆩􏿿 Group cancel:off 􀜁􀄰􏿿\n"
                if wait["leaveRoom"] == True: md+="􀠁􀆩􏿿 Auto leave:on 􀜁􀄯􏿿\n"
                else: md+="􀠁􀆩􏿿 Auto leave:off 􀜁􀄰􏿿\n"
                if wait["timeline"] == True: md+="􀠁􀆩􏿿 Share:on 􀜁􀄯􏿿\n"
                else:md+="􀠁􀆩􏿿 Share:off 􀜁􀄰􏿿\n"
                if wait["autoAdd"] == True: md+="􀠁􀆩􏿿 Auto add:on 􀜁􀄯􏿿\n"
                else:md+="􀠁􀆩􏿿 Auto add:off 􀜁􀄰􏿿\n"
                if wait["protect"] == True: md+="􀠁􀆩􏿿 Protect:on 􀜁􀄯􏿿\n"
                else:md+="􀠁􀆩􏿿 Protect:off 􀜁􀄰􏿿\n"
                if wait["linkprotect"] == True: md+="􀠁􀆩􏿿Link Protect:on 􀜁􀄯􏿿\n"
                else:md+="􀠁􀆩􏿿Link Protect:off 􀜁􀄰􏿿\n"
                if wait["inviteprotect"] == True: md+="􀠁􀆩􏿿Invitation Protect:on 􀜁􀄯􏿿\n"
                else:md+="􀠁􀆩􏿿Invitation Protect:off 􀜁􀄰􏿿\n"
                if wait["cancelprotect"] == True: md+="􀠁􀆩􏿿Cancel Protect:on 􀜁􀄯􏿿\n"
                else:md+="􀠁􀆩􏿿Cancel Protect:off 􀜁􀄰􏿿\n"
                yudha.sendText(msg.to,md)
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                yudha.sendMessage(msg)
            elif cms(msg.text,["creator","Creator"]):
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uecc57cb55f480ee2a45d81434a9b864d"}
                yudha.sendMessage(msg)
            elif msg.text.lower() == 'autoadd on':
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Auto add set to on")
                    else:
                        yudha.sendText(msg.to,"Auto add already on")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Auto add set to on")
                    else:
                        yudha.sendText(msg.to,"Auto add already on")
            elif msg.text.lower() == 'autoadd off':
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Auto add set to off")
                    else:
                        yudha.sendText(msg.to,"Auto add already off")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Auto add set to off")
                    else:
                        yudha.sendText(msg.to,"Auto add already off")
            elif "Pesan set:" in msg.text:
                wait["message"] = msg.text.replace("Pesan set:","")
                yudha.sendText(msg.to,"We changed the message")
            elif msg.text.lower() == 'pesan cek':
                if wait["lang"] == "JP":
                    yudha.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
                else:
                    yudha.sendText(msg.to,"Pesan tambahan otomatis telah ditetapkan sebagai berikut \n\n" + wait["message"])
            elif "Come Set:" in msg.text:
                c = msg.text.replace("Come Set:","")
                if c in [""," ","\n",None]:
                    yudha.sendText(msg.to,"Merupakan string yang tidak bisa diubah")
                else:
                    wait["comment"] = c
                    yudha.sendText(msg.to,"Ini telah diubah\n\n" + c)
            elif msg.text in ["Com on","Com:on","Comment on"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Aku berada di")
                    else:
                        yudha.sendText(msg.to,"To open")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Comment Actived")
                    else:
                        yudha.sendText(msg.to,"Comment Has Been Active")
            elif msg.text in ["Come off"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Hal ini sudah off")
                    else:
                        yudha.sendText(msg.to,"It is already turned off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Off")
                    else:
                        yudha.sendText(msg.to,"To turn off")
            elif msg.text in ["Com","Comment"]:
                yudha.sendText(msg.to,"Auto komentar saat ini telah ditetapkan sebagai berikut:??\n\n" + str(wait["comment"]))
            elif msg.text in ["Com Bl"]:
                wait["wblack"] = True
                yudha.sendText(msg.to,"Please send contacts from the person you want to add to the blacklist")
            elif msg.text in ["Com hapus Bl"]:
                wait["dblack"] = True
                yudha.sendText(msg.to,"Please send contacts from the person you want to add from the blacklist")
            elif msg.text in ["Com Bl cek"]:
                if wait["commentBlack"] == {}:
                    yudha.sendText(msg.to,"Nothing in the blacklist")
                else:
                    yudha.sendText(msg.to,"The following is a blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "ãƒ»" +yudha.getContact(mi_d).displayName + "\n"
                    yudha.sendText(msg.to,mc)
            elif msg.text.lower() == 'jam on':
                if wait["yudhaock"] == True:
                    yudha.sendText(msg.to,"Jam already on")
                else:
                    wait["yudhaock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"?%H:%M?")
                    profile = yudha.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    yudha.updateProfile(profile)
                    yudha.sendText(msg.to,"Jam set on")
            elif msg.text.lower() == 'jam off':
                if wait["yudhaock"] == False:
                    yudha.sendText(msg.to,"Jam already off")
                else:
                    wait["yudhaock"] = False
                    yudha.sendText(msg.to,"Jam set off")
            elif "Jam say:" in msg.text:
                n = msg.text.replace("Jam say:","")
                if len(n.decode("utf-8")) > 30:
                    yudha.sendText(msg.to,"terlalu lama")
                else:
                    wait["cName"] = n
                    yudha.sendText(msg.to,"Nama Jam Berubah menjadi:" + n)
            elif msg.text.lower() == 'update':
                if wait["yudhaock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"?%H:%M?")
                    profile = yudha.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    yudha.updateProfile(profile)
                    yudha.sendText(msg.to,"Diperbarui")
                else:
                    yudha.sendText(msg.to,"Silahkan Aktifkan Jam")
#==============================================================================#
#==============================================================================#
            elif msg.text in ["Invite"]:
                wait["invite"] = True
                yudha.sendText(msg.to,"Send Contact")
            
            elif msg.text in ["Steal contact"]:
                wait["contact"] = True
                yudha.sendText(msg.to,"Send Contact")
                
            elif msg.text in ["Like:me","Like me"]: #Semua Bot Ngelike Status Akun Utama
                print "[Command]Like executed"
                yudha.sendText(msg.to,"Like Status Owner")
                try:
                  likeme()
                except:
                  pass
                
            elif msg.text in ["Like:friend","Like friend"]: #Semua Bot Ngelike Status Teman
                print "[Command]Like executed"
                yudha.sendText(msg.to,"Like Status Teman")
                try:
                  likefriend()
                except:
                  pass
            
            elif msg.text in ["Like:on","Like on"]:
                if wait["likeOn"] == True:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = True
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Already")
                        
            elif msg.text in ["Like off","Like:off"]:
                if wait["likeOn"] == False:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Done")
                else:
                    wait["likeOn"] = False
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Already")
                        
            elif msg.text in ["My simisimi on","Simisimi on"]:
                settings["simiSimi"][msg.to] = True
                yudha.sendText(msg.to,"Success activated simisimi")
                
            elif msg.text in ["My simisimi off","Simisimi off"]:
                settings["simiSimi"][msg.to] = False
                yudha.sendText(msg.to,"Success deactive simisimi")
                
            elif msg.text in ["My read on","Read on"]:
                wait['alwayRead'] = True
                yudha.sendText(msg.to,"Auto Sider ON")
                
            elif msg.text in ["My read off","Read off"]:
                wait['alwayRead'] = False
                yudha.sendText(msg.to,"Auto Sider OFF")
                
            elif msg.text in ["My autorespon on","Autorespon:on","My respon on","Respon on"]:
                wait["detectMention"] = True
                yudha.sendText(msg.to,"Auto Respon ON")
                
            elif msg.text in ["My autorespon off","Autorespon:off","My respon off","Respon off"]:
                wait["detectMention"] = False
                yudha.sendText(msg.to,"Auto Respon OFF")
            
            elif msg.text in ["Tag on","Autokick:on","Responkick on","Responkick:on"]:
                wait["kickMention"] = True
                yudha.sendText(msg.to,"[AUTO RESPOND] Auto Kick yang tag ON")
                
            elif msg.text in ["Tag off","Autokick:off","Responkick off","Responkick:off"]:
                wait["kickMention"] = False
                yudha.sendText(msg.to,"[AUTO RESPOND] Auto Kick yang tag OFF")
#==============================================================================#
            elif "らたかn" in msg.text:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("らたかn","")
                    gs = yudha.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        sendMessage(msg.to,"Not found.")
                    else:
                        for target in targets:
                            try:
                                klist=[yudha]
                                kicker=random.choice(klist)
                                random.choice(KAC).kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                sendMessage(msg.to,"Grup Dibersihkan")
            elif ("Kick " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           yudha.kickoutFromGroup(msg.to,[target])
                       except:
                           yudha.sendText(msg.to,"Error")
            
            elif ("Ulti " in msg.text):
                   targets = []
                   key = eval(msg.contentMetadata["MENTION"])
                   key["MENTIONEES"] [0] ["M"]
                   for x in key["MENTIONEES"]:
                       targets.append(x["M"])
                   for target in targets:
                       try:
                           yudha.kickoutFromGroup(msg.to,[target])
                           yudha.inviteIntoGroup(msg.to,[target])
                           yudha.cancelGroupInvitation(msg.to,[target])
                           yudha.inviteIntoGroup(msg.to,[target])
                           yudha.cancelGroupInvitation(msg.to,[target])
                           yudha.inviteIntoGroup(msg.to,[target])
                           yudha.cancelGroupInvitation(msg.to,[target])
                           yudha.inviteIntoGroup(msg.to,[target])
                           yudha.cancelGroupInvitation(msg.to,[target])
                           yudha.inviteIntoGroup(msg.to,[target])
                           yudha.cancelGroupInvitation(msg.to,[target])
                           yudha.inviteIntoGroup(msg.to,[target])
                           yudha.cancelGroupInvitation(msg.to,[target])
                           yudha.inviteIntoGroup(msg.to,[target])
                           yudha.cancelGroupInvitation(msg.to,[target])
                           yudha.inviteIntoGroup(msg.to,[target])
                           yudha.cancelGroupInvitation(msg.to,[target])
                           yudha.inviteIntoGroup(msg.to,[target])
                           yudha.cancelGroupInvitation(msg.to,[target])
                           yudha.inviteIntoGroup(msg.to,[target])
                           yudha.cancelGroupInvitation(msg.to,[target])
                           yudha.inviteIntoGroup(msg.to,[target])
                           yudha.cancelGroupInvitation(msg.to,[target])
                           yudha.inviteIntoGroup(msg.to,[target])
                           yudha.cancelGroupInvitation(msg.to,[target])
                           yudha.inviteIntoGroup(msg.to,[target])
                           yudha.cancelGroupInvitation(msg.to,[target])
                       except:
                           yudha.sendText(msg.to,"Error")
            
            elif "Kick: " in msg.text:
                midd = msg.text.replace("Kick: ","")
                yudha.kickoutFromGroup(msg.to,[midd])
            
            elif 'invite ' in msg.text.lower():
                    key = msg.text[-33:]
                    yudha.findAndAddContactsByMid(key)
                    yudha.inviteIntoGroup(msg.to, [key])
                    contact = yudha.getContact(key)
            
            elif msg.text.lower() == 'cancel':
                if msg.toType == 2:
                    group = yudha.getGroup(msg.to)
                    if group.invitee is not None:
                        gInviMids = [contact.mid for contact in group.invitee]
                        yudha.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            yudha.sendText(msg.to,"Tidak ada undangan")
                        else:
                            yudha.sendText(msg.to,"Invitan tidak ada")
                else:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"Tidak ada undangan")
                    else:
                        yudha.sendText(msg.to,"Invitan tidak ada")
            
            elif msg.text.lower() == 'link on':
                if msg.toType == 2:
                    group = yudha.getGroup(msg.to)
                    group.preventJoinByTicket = False
                    yudha.updateGroup(group)
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"URL open")
                    else:
                        yudha.sendText(msg.to,"URL open")
                else:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"It can not be used outside the group")
                    else:
                        yudha.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text.lower() == 'link off':
                if msg.toType == 2:
                    group = yudha.getGroup(msg.to)
                    group.preventJoinByTicket = True
                    yudha.updateGroup(group)
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"URL yudhaose")
                    else:
                        yudha.sendText(msg.to,"URL yudhaose")
                else:
                    if wait["lang"] == "JP":
                        yudha.sendText(msg.to,"It can not be used outside the group")
                    else:
                        yudha.sendText(msg.to,"Can not be used for groups other than")
            
            elif msg.text in ["Url"]:
                if msg.toType == 2:
                    g = yudha.getGroup(msg.to)
                    if g.preventJoinByTicket == True:
                        g.preventJoinByTicket = False
                        yudha.updateGroup(g)
                    gurl = yudha.reissueGroupTicket(msg.to)
                    yudha.sendText(msg.to,"line://ti/g/" + gurl)
                    
            elif "Gcreator" == msg.text:
                try:
                    group = yudha.getGroup(msg.to)
                    GS = group.creator.mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': GS}
                    yudha.sendMessage(M)
                except:
                    W = group.members[0].mid
                    M = Message()
                    M.to = msg.to
                    M.contentType = 13
                    M.contentMetadata = {'mid': W}
                    yudha.sendMessage(M)
                    yudha.sendText(msg.to,"Creator Grup")
            
            elif msg.text.lower() == 'invite:gcreator':
                if msg.toType == 2:
                       ginfo = yudha.getGroup(msg.to)
                       try:
                           gcmid = ginfo.creator.mid
                       except:
                           gcmid = "Error"
                       if wait["lang"] == "JP":
                           yudha.inviteIntoGroup(msg.to,[gcmid])
                       else:
                           yudha.inviteIntoGroup(msg.to,[gcmid])
            
            elif ("Gname: " in msg.text):
                if msg.toType == 2:
                    X = yudha.getGroup(msg.to)
                    X.name = msg.text.replace("Gname: ","")
                    yudha.updateGroup(X)
            
            elif msg.text.lower() == 'infogrup':        
                    group = yudha.getGroup(msg.to)
                    try:
                        gCreator = group.creator.displayName
                    except:
                        gCreator = "Error"
                    md = "[Nama Grup : ]\n" + group.name + "\n\n[Id Grup : ]\n" + group.id + "\n\n[Pembuat Grup :]\n" + gCreator + "\n\n[Gambar Grup : ]\nhttp://dl.profile.line-cdn.net/" + group.pictureStatus
                    if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                    else: md += "\n\nKode Url : Diblokir"
                    if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                    else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                    yudha.sendText(msg.to,md)
            
            elif msg.text.lower() == 'grup id':
                gid = yudha.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:%s\n" % (yudha.getGroup(i).name,i)
                yudha.sendText(msg.to,h)
#==============================================================================#
            elif "Checkmid: " in msg.text:
                saya = msg.text.replace("Checkmid: ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":saya}
                yudha.sendMessage(msg)
                contact = yudha.getContact(saya)
                cu = yudha.channel.getCover(saya)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    yudha.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    yudha.sendText(msg.to,"Profile Picture " + contact.displayName)
                    yudha.sendImageWithURL(msg.to,image)
                    yudha.sendText(msg.to,"Cover " + contact.displayName)
                    yudha.sendImageWithURL(msg.to,path)
                except:
                    pass
                
            elif "Checkid: " in msg.text:
                saya = msg.text.replace("Checkid: ","")
                gid = yudha.getGroupIdsJoined()
                for i in gid:
                    h = yudha.getGroup(i).id
                    group = yudha.getGroup(i)
                    if h == saya:
                        try:
                            creator = group.creator.mid 
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': creator}
                            md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                            if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                            else: md += "\n\nKode Url : Diblokir"
                            if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                            else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                            yudha.sendText(msg.to,md)
                            yudha.sendMessage(msg)
                            yudha.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                        except:
                            creator = "Error"
                
            elif msg.text in ["Friendlist"]:    
                contactlist = yudha.getAllContactIds()
                kontak = yudha.getContacts(contactlist)
                num=1
                msgs="═════════List Friend═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Friend═════════\n\nTotal Friend : %i" % len(kontak)
                yudha.sendText(msg.to, msgs)
                
            elif msg.text in ["Memlist"]:   
                kontak = yudha.getGroup(msg.to)
                group = kontak.members
                num=1
                msgs="═════════List Member═════════-"
                for ids in group:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(group)
                yudha.sendText(msg.to, msgs)
                
            elif "Grupmember: " in msg.text:
                saya = msg.text.replace('Grupmember: ','')
                gid = yudha.getGroupIdsJoined()
                num=1
                msgs="═════════List Member═════════-"
                for i in gid:
                    h = yudha.getGroup(i).name
                    gna = yudha.getGroup(i)
                    me = gna.members(i)
                    msgs+="\n[%i] %s" % (num, me.displayName)
                    num=(num+1)
                    msgs+="\n═════════List Member═════════\n\nTotal Members : %i" % len(me)
                    if h == saya:
                        yudha.sendText(msg.to, msgs)
                
            elif "Friendinfo: " in msg.text:
                saya = msg.text.replace('Friendinfo: ','')
                gid = yudha.getAllContactIds()
                for i in gid:
                    h = yudha.getContact(i).displayName
                    contact = yudha.getContact(i)
                    cu = yudha.channel.getCover(i)
                    path = str(cu)
                    image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                    if h == saya:
                        yudha.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                        yudha.sendText(msg.to,"Profile Picture " + contact.displayName)
                        yudha.sendImageWithURL(msg.to,image)
                        yudha.sendText(msg.to,"Cover " + contact.displayName)
                        yudha.sendImageWithURL(msg.to,path)
                
            elif "Friendpict: " in msg.text:
                saya = msg.text.replace('Friendpict: ','')
                gid = yudha.getAllContactIds()
                for i in gid:
                    h = yudha.getContact(i).displayName
                    gna = yudha.getContact(i)
                    if h == saya:
                        yudha.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif msg.text in ["Friendlistmid"]: 
                gruplist = yudha.getAllContactIds()
                kontak = yudha.getContacts(gruplist)
                num=1
                msgs="═════════List FriendMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.mid)
                    num=(num+1)
                msgs+="\n═════════List FriendMid═════════\n\nTotal Friend : %i" % len(kontak)
                yudha.sendText(msg.to, msgs)
            
            elif msg.text in ["Blocklist"]: 
                blockedlist = yudha.getBlockedContactIds()
                kontak = yudha.getContacts(blockedlist)
                num=1
                msgs="═════════List Blocked═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.displayName)
                    num=(num+1)
                msgs+="\n═════════List Blocked═════════\n\nTotal Blocked : %i" % len(kontak)
                yudha.sendText(msg.to, msgs)
                
            elif msg.text in ["Gruplist"]:  
                gruplist = yudha.getGroupIdsJoined()
                kontak = yudha.getGroups(gruplist)
                num=1
                msgs="═════════List Grup═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.name)
                    num=(num+1)
                msgs+="\n═════════List Grup═════════\n\nTotal Grup : %i" % len(kontak)
                yudha.sendText(msg.to, msgs)
            
            elif msg.text in ["Gruplistmid"]:   
                gruplist = yudha.getGroupIdsJoined()
                kontak = yudha.getGroups(gruplist)
                num=1
                msgs="═════════List GrupMid═════════"
                for ids in kontak:
                    msgs+="\n[%i] %s" % (num, ids.id)
                    num=(num+1)
                msgs+="\n═════════List GrupMid═════════\n\nTotal Grup : %i" % len(kontak)
                yudha.sendText(msg.to, msgs)
                    
            elif "Grupimage: " in msg.text:
                saya = msg.text.replace('Grupimage: ','')
                gid = yudha.getGroupIdsJoined()
                for i in gid:
                    h = yudha.getGroup(i).name
                    gna = yudha.getGroup(i)
                    if h == saya:
                        yudha.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ gna.pictureStatus)
            
            elif "Grupname" in msg.text:
                saya = msg.text.replace('Grupname','')
                gid = yudha.getGroup(msg.to)
                yudha.sendText(msg.to, "[Nama Grup : ]\n" + gid.name)
            
            elif "Grupid" in msg.text:
                saya = msg.text.replace('Grupid','')
                gid = yudha.getGroup(msg.to)
                yudha.sendText(msg.to, "[ID Grup : ]\n" + gid.id)
                    
            elif "Grupinfo: " in msg.text:
                saya = msg.text.replace('Grupinfo: ','')
                gid = yudha.getGroupIdsJoined()
                for i in gid:
                    h = yudha.getGroup(i).name
                    group = yudha.getGroup(i)
                    if h == saya:
                        try:
                            creator = group.creator.mid 
                            msg.contentType = 13
                            msg.contentMetadata = {'mid': creator}
                            md = "Nama Grup :\n" + group.name + "\n\nID Grup :\n" + group.id
                            if group.preventJoinByTicket is False: md += "\n\nKode Url : Diizinkan"
                            else: md += "\n\nKode Url : Diblokir"
                            if group.invitee is None: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : 0 Orang"
                            else: md += "\nJumlah Member : " + str(len(group.members)) + " Orang" + "\nUndangan Yang Belum Diterima : " + str(len(group.invitee)) + " Orang"
                            yudha.sendText(msg.to,md)
                            yudha.sendMessage(msg)
                            yudha.sendImageWithURL(msg.to,"http://dl.profile.line.naver.jp/"+ group.pictureStatus)
                        except:
                            creator = "Error"
                
            elif msg.text in ["Glist"]:
                gid = yudha.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "%s\n" % (yudha.getGroup(i).name +" ? ["+str(len(yudha.getGroup(i).members))+"]")
                yudha.sendText(msg.to,"-- List Groups --\n\n"+ h +"\nTotal groups =" +" ["+str(len(gid))+"]")
            
            elif msg.text.lower() == 'gcancel':
                gid = yudha.getGroupIdsInvited()
                for i in gid:
                    yudha.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    yudha.sendText(msg.to,"Aku menolak semua undangan")
                else:
                    yudha.sendText(msg.to,"He deyudhained all invitations")
                         
            elif "Auto add" in msg.text:
                thisgroup = yudha.getGroups([msg.to])
                Mids = [contact.mid for contact in thisgroup[0].members]
                mi_d = Mids[:33]
                yudha.findAndAddContactsByMids(mi_d)
                yudha.sendText(msg.to,"Success Add all")
#==============================================================================#
            elif "numpang tag" == msg.text.lower():
                 group = yudha.getGroup(msg.to)
                 nama = [contact.mid for contact in group.members]
                 nm1, nm2, nm3, nm4, nm5, jml = [], [], [], [], [], len(nama)
                 if jml <= 100:
                    summon(msg.to, nama)
                 if jml > 100 and jml < 200:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, len(nama)-1):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                 if jml > 200  and jml < 500:
                    for i in range(0, 99):
                        nm1 += [nama[i]]
                    summon(msg.to, nm1)
                    for j in range(100, 199):
                        nm2 += [nama[j]]
                    summon(msg.to, nm2)
                    for k in range(200, 299):
                        nm3 += [nama[k]]
                    summon(msg.to, nm3)
                    for l in range(300, 399):
                        nm4 += [nama[l]]
                    summon(msg.to, nm4)
                    for m in range(400, len(nama)-1):
                        nm5 += [nama[m]]
                    summon(msg.to, nm5)
                 if jml > 500:
                     print "Terlalu Banyak Men 500+"
                 cnt = Message()
                 cnt.text = "Jumlah:\n" + str(jml) +  " Members"
                 cnt.to = msg.to
                 yudha.sendMessage(cnt)

            elif "sider on" == msg.text.lower():
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         yudha.sendText(msg.to,"Cek Sider already on")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     yudha.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2

                    
            elif "sider off" == msg.text.lower():
                if msg.to not in wait2['readPoint']:
                    yudha.sendText(msg.to,"Cek Sider already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    yudha.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))


                    
            elif "sider" == msg.text.lower():
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                             yudha.sendText(msg.to, "Sider:\nNone")
                        else:
                            chiya = []
                            for rom in wait2["ROM"][msg.to].items():
                                chiya.append(rom[1])
                               
                            cmem = yudha.getContacts(chiya)
                            zx = ""
                            zxc = ""
                            zx2 = []
                            xpesan = 'Lurkers:\n'
                        for x in range(len(cmem)):
                                xname = str(cmem[x].displayName)
                                pesan = ''
                                pesan2 = pesan+"@a\n"
                                xlen = str(len(zxc)+len(xpesan))
                                xlen2 = str(len(zxc)+len(pesan2)+len(xpesan)-1)
                                zx = {'S':xlen, 'E':xlen2, 'M':cmem[x].mid}
                                zx2.append(zx)
                                zxc += pesan2
                                msg.contentType = 0
           
                        print zxc
                        msg.text = xpesan+ zxc + "\nLurking time: %s\nCurrent time: %s"%(wait2['setTime'][msg.to],datetime.now().strftime('%H:%M:%S'))
                        lol ={'MENTION':str('{"MENTIONEES":'+json.dumps(zx2).replace(' ','')+'}')}
                        print lol
                        msg.contentMetadata = lol
                        try:
                          yudha.sendMessage(msg)
                        except Exception as error:
                              print error
                        pass
               
           
                    else:
                        yudha.sendText(msg.to, "Lurking has not been set.")
            elif "Gbroadcast: " in msg.text:
                bc = msg.text.replace("Bc ","")
                gid = yudha.getGroupIdsJoined()
                for i in gid:
                    yudha.sendText(i,"======[BROADCAST]======\n\n"+bc+"\n\n#BROADCAST")
                    
            elif "Cbroadcast: " in msg.text:
                bc = msg.text.replace("Cbroadcast: ","")
                gid = yudha.getAllContactIds()
                for i in gid:
                    yudha.sendText(i, bc)
            
            elif "GbroadcastImage: " in msg.text:
                bc = msg.text.replace("GbroadcastImage: ","")
                gid = yudha.getGroupIdsJoined()
                for i in gid:
                    yudha.sendImageWithURL(i, bc)
                    
            elif "CbroadcastImage: " in msg.text:
                bc = msg.text.replace("CbroadcastImage: ","")
                gid = yudha.getAllContactIds()
                for i in gid:
                    yudha.sendImageWithURL(i, bc)
            
            elif "Spam change: " in msg.text:
                wait["spam"] = msg.text.replace("Spam change: ","")
                yudha.sendText(msg.to,"spam changed")

            elif "Spam add: " in msg.text:
                wait["spam"] = msg.text.replace("Spam add: ","")
                if wait["lang"] == "JP":
                    yudha.sendText(msg.to,"spam changed")
                else:
                    yudha.sendText(msg.to,"Done")
    
            elif "Spam: " in msg.text:
                strnum = msg.text.replace("Spam: ","")
                num = int(strnum)
                for var in range(0,num):
                    yudha.sendText(msg.to, wait["spam"])
            
            elif "Spamtag @" in msg.text:
                _name = msg.text.replace("Spamtag @","")
                _nametarget = _name.rstrip(' ')
                gs = yudha.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        xname = g.displayName
                        xlen = str(len(xname)+1)
                        msg.contentType = 0
                        msg.text = "@"+xname+" "
                        msg.contentMetadata ={'MENTION':'{"MENTIONEES":[{"S":"0","E":'+json.dumps(xlen)+',"M":'+json.dumps(g.mid)+'}]}','EMTVER':'4'}
                        yudha.sendMessage(msg)
                        yudha.sendMessage(msg)
                        yudha.sendMessage(msg)
                        yudha.sendMessage(msg)
                        yudha.sendMessage(msg)
                        yudha.sendMessage(msg)
                        yudha.sendMessage(msg)
                        yudha.sendMessage(msg)
                        yudha.sendMessage(msg)
                        yudha.sendMessage(msg)
                        yudha.sendMessage(msg)
                        yudha.sendMessage(msg)
                        yudha.sendMessage(msg)
                        yudha.sendMessage(msg)
                        yudha.sendMessage(msg)
                        yudha.sendMessage(msg)
                        yudha.sendMessage(msg)
                        yudha.sendMessage(msg)
                        yudha.sendMessage(msg)
                        yudha.sendMessage(msg)
                    else:
                        pass
            
            elif "Spam" in msg.text:
                txt = msg.text.split(" ")
                jmlh = int(txt[2])
                teks = msg.text.replace("Spam "+str(txt[1])+" "+str(jmlh)+" ","")
                tulisan = jmlh * (teks+"\n")
                if txt[1] == "on":
                    if jmlh <= 100000:
                       for x in range(jmlh):
                           yudha.sendText(msg.to, teks)
                    else:
                       yudha.sendText(msg.to, "Out of Range!")
                elif txt[1] == "off":
                    if jmlh <= 100000:
                        yudha.sendText(msg.to, tulisan)
                    else:
                        yudha.sendText(msg.to, "Out Of Range!")
                        
            elif ("Micadd " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        mimic["target"][target] = True
                        yudha.sendText(msg.to,"Target ditambahkan!")
                        break
                    except:
                        yudha.sendText(msg.to,"Fail !")
                        break
                    
            elif ("Micdel " in msg.text):
                targets = []
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                    try:
                        del mimic["target"][target]
                        yudha.sendText(msg.to,"Target dihapuskan!")
                        break
                    except:
                        yudha.sendText(msg.to,"Fail !")
                        break
                    
            elif msg.text in ["Miyudhaist"]:
                        if mimic["target"] == {}:
                            yudha.sendText(msg.to,"nothing")
                        else:
                            mc = "Target mimic user\n"
                            for mi_d in mimic["target"]:
                                mc += "?? "+yudha.getContact(mi_d).displayName + "\n"
                            yudha.sendText(msg.to,mc)

            elif "Mimic target " in msg.text:
                        if mimic["copy"] == True:
                            siapa = msg.text.replace("Mimic target ","")
                            if siapa.rstrip(' ') == "me":
                                mimic["copy2"] = "me"
                                yudha.sendText(msg.to,"Mimic change to me")
                            elif siapa.rstrip(' ') == "target":
                                mimic["copy2"] = "target"
                                yudha.sendText(msg.to,"Mimic change to target")
                            else:
                                yudha.sendText(msg.to,"I dont know")
            
            elif "Mimic " in msg.text:
                cmd = msg.text.replace("Mimic ","")
                if cmd == "on":
                    if mimic["status"] == False:
                        mimic["status"] = True
                        yudha.sendText(msg.to,"Reply Message on")
                    else:
                        yudha.sendText(msg.to,"Sudah on")
                elif cmd == "off":
                    if mimic["status"] == True:
                        mimic["status"] = False
                        yudha.sendText(msg.to,"Reply Message off")
                    else:
                        yudha.sendText(msg.to,"Sudah off")
            
            #elif msg.text.lower() in dangerMessage:
            #    if msg.toType == 2:
            #        try:
            #            yudha.kickoutFromGroup(msg.to,[msg.from_])
            #        except:
            #            yudha.kickoutFromGroup(msg.to,[msg.from_])
            elif "Setimage: " in msg.text:
                wait["pap"] = msg.text.replace("Setimage: ","")
                yudha.sendText(msg.to, "Pap telah di Set")
            elif msg.text in ["Papimage","Papim","Pap"]:
                yudha.sendImageWithURL(msg.to,wait["pap"])
            elif "Setvideo: " in msg.text:
                wait["pap"] = msg.text.replace("Setvideo: ","")
                yudha.sendText(msg.to,"Video Has Ben Set To")
            elif msg.text in ["Papvideo","Papvid"]:
                yudha.sendVideoWithURL(msg.to,wait["pap"])
#==============================================================================#
            elif '/image ' in msg.text:
                googl = msg.text.replace('/image ',"")

                url = 'https://www.google.com/search?hl=en&biw=1366&bih=659&tbm=isch&sa=1&ei=vSD9WYimHMWHvQTg_53IDw&q=' + googl

                raw_html =  (download_page(url))

                items = []

                items = items + (_images_get_all_items(raw_html))

                path = random.choice(items)

                try:

                    start = timeit.timeit()

                    yudha.sendImageWithURL(msg.to,path)

                    yudha.sendText(msg.to, "Google Image \nType: Search Image\nWaktu dicari: %s" % (start) +"\nTotal Image Links = "+str(len(items)))

                    print "[Notif] Search Image Google Sucess"

                except Exception as e:

                    yudha.sendText(msg.to, str(e))
            elif msg.text.lower() == 'mymid':
                yudha.sendText(msg.to,mid)
            elif "Timeline: " in msg.text:
                tl_text = msg.text.replace("Timeline: ","")
                yudha.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+yudha.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif "Myname: " in msg.text:
                string = msg.text.replace("Myname: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = yudha.getProfile()
                    profile.displayName = string
                    yudha.updateProfile(profile)
                    yudha.sendText(msg.to,"Changed " + string + "")
            elif "Mybio: " in msg.text:
                string = msg.text.replace("Mybio: ","")
                if len(string.decode('utf-8')) <= 10000000000:
                    profile = yudha.getProfile()
                    profile.statusMessage = string
                    yudha.updateProfile(profile)
                    yudha.sendText(msg.to,"Changed " + string)
            elif msg.text in ["Myname"]:
                    h = yudha.getContact(mid)
                    yudha.sendText(msg.to,"===[DisplayName]===\n" + h.displayName)
            elif msg.text in ["Mybio"]:
                    h = yudha.getContact(mid)
                    yudha.sendText(msg.to,"===[StatusMessage]===\n" + h.statusMessage)
            elif msg.text in ["Mypict"]:
                    h = yudha.getContact(mid)
                    yudha.sendImageWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Myvid"]:
                    h = yudha.getContact(mid)
                    yudha.sendVideoWithURL(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Urlpict"]:
                    h = yudha.getContact(mid)
                    yudha.sendText(msg.to,"http://dl.profile.line-cdn.net/" + h.pictureStatus)
            elif msg.text in ["Mycover"]:
                    h = yudha.getContact(mid)
                    cu = yudha.channel.getCover(mid)          
                    path = str(cu)
                    yudha.sendImageWithURL(msg.to, path)
            elif msg.text in ["Urlcover"]:
                    h = yudha.getContact(mid)
                    cu = yudha.channel.getCover(mid)          
                    path = str(cu)
                    yudha.sendText(msg.to, path)
            elif "Getmid @" in msg.text:
                _name = msg.text.replace("Getmid @","")
                _nametarget = _name.rstrip(' ')
                gs = yudha.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        yudha.sendText(msg.to, g.mid)
                    else:
                        pass
            elif "Getinfo" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = yudha.getContact(key1)
                cu = yudha.channel.getCover(key1)
                try:
                    yudha.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n\nHeader :\n" + str(cu))
                except:
                    yudha.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nMid :\n" + contact.mid + "\n\nBio :\n" + contact.statusMessage + "\n\nProfile Picture :\n" + str(cu))
            elif "Getbio" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = yudha.getContact(key1)
                cu = yudha.channel.getCover(key1)
                try:
                    yudha.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
                except:
                    yudha.sendText(msg.to, "===[StatusMessage]===\n" + contact.statusMessage)
            elif "Getname" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = yudha.getContact(key1)
                cu = yudha.channel.getCover(key1)
                try:
                    yudha.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
                except:
                    yudha.sendText(msg.to, "===[DisplayName]===\n" + contact.displayName)
            elif "Getprofile" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]
                contact = yudha.getContact(key1)
                cu = yudha.channel.getCover(key1)
                path = str(cu)
                image = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                try:
                    yudha.sendText(msg.to,"Nama :\n" + contact.displayName + "\n\nBio :\n" + contact.statusMessage)
                    yudha.sendText(msg.to,"Profile Picture " + contact.displayName)
                    yudha.sendImageWithURL(msg.to,image)
                    yudha.sendText(msg.to,"Cover " + contact.displayName)
                    yudha.sendImageWithURL(msg.to,path)
                except:
                    pass
            elif "Getcontact" in msg.text:
                key = eval(msg.contentMetadata["MENTION"])
                key1 = key["MENTIONEES"][0]["M"]                
                mmid = yudha.getContact(key1)
                msg.contentType = 13
                msg.contentMetadata = {"mid": key1}
                yudha.sendMessage(msg)
            elif "Getpict @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getpict @","")
                _nametarget = _name.rstrip('  ')
                gs = yudha.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    yudha.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = yudha.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            yudha.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Getvid @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Getvid @","")
                _nametarget = _name.rstrip('  ')
                gs = yudha.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    yudha.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = yudha.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            yudha.sendVideoWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Picturl @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Picturl @","")
                _nametarget = _name.rstrip('  ')
                gs = yudha.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    yudha.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = yudha.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            yudha.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]dp executed"
            elif "Getcover @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Getcover @","")    
                _nametarget = _name.rstrip('  ')
                gs = yudha.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    yudha.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = yudha.getContact(target)
                            cu = yudha.channel.getCover(target)          
                            path = str(cu)
                            yudha.sendImageWithURL(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif "Coverurl @" in msg.text:
                print "[Command]cover executing"
                _name = msg.text.replace("Coverurl @","")    
                _nametarget = _name.rstrip('  ')
                gs = yudha.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    yudha.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = yudha.getContact(target)
                            cu = yudha.channel.getCover(target)          
                            path = str(cu)
                            yudha.sendText(msg.to, path)
                        except Exception as e:
                            raise e
                print "[Command]cover executed"
            elif "Getgrup image" in msg.text:
                group = yudha.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                yudha.sendImageWithURL(msg.to,path)
            elif "Urlgrup image" in msg.text:
                group = yudha.getGroup(msg.to)
                path = "http://dl.profile.line-cdn.net/" + group.pictureStatus
                yudha.sendText(msg.to,path)
            elif "Mycopy @" in msg.text:
                   print "[COPY] Ok"
                   _name = msg.text.replace("Mycopy @","")
                   _nametarget = _name.rstrip('  ')
                   gs = yudha.getGroup(msg.to)
                   targets = []
                   for g in gs.members:
                       if _nametarget == g.displayName:
                           targets.append(g.mid)
                   if targets == []:
                       yudha.sendText(msg.to, "Not Found...")
                   else:
                       for target in targets:
                            try:
                               yudha.yudhaoneContactProfile(target)
                               yudha.sendText(msg.to, "Copied.")
                            except Exception as e:
                                print e
            elif msg.text in ["Mybackup","mybackup"]:
                try:
                    yudha.updateDisplayPicture(backup.pictureStatus)
                    yudha.updateProfile(backup)
                    yudha.sendText(msg.to, "Refreshed.")
                except Exception as e:
                    yudha.sendText(msg.to, str(e))
#==============================================================================#
            elif "/fancytext: " in msg.text.lower():
                txt = msg.text.replace("/fancytext: ", "")
                t1 = "\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xb0\x82\xf4\x80\xa0\x81\xf4\x80\xa0\x81\xf4\x80\xa0\x81"
                t2 = "\xf4\x80\x82\xb3\xf4\x8f\xbf\xbf"
                yudha.sendText(msg.to, t1 + txt + t2)
                 #-------------------------------------------------
            elif "/translate" in msg.text:
            	yudha.sendText(msg.to,"contoh :\n- id to english : /en aku\n- english to id : /id you\n- id to japan : /jp halo\n- japan to id : /jpid kimochi\n- id to korea : /kor pagi\n- id to malaysia : /malay enak\n- id to arab : /arab jalan\n- id to jawa : /jawa kamu")
            elif "/id " in msg.text:
                isi = msg.text.replace("/id ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                yudha.sendText(msg.to, A)
            elif "/en " in msg.text:
                isi = msg.text.replace("/en ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='en')
                A = hasil.text
                A = A.encode('utf-8')
                yudha.sendText(msg.to, A)
            elif "/jp " in msg.text:
                isi = msg.text.replace("/jp ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ja')
                A = hasil.text
                A = A.encode('utf-8')
                yudha.sendText(msg.to, A)
            elif "/jpid " in msg.text:
                isi = msg.text.replace("/jpid ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='id')
                A = hasil.text
                A = A.encode('utf-8')
                yudha.sendText(msg.to, A)
            elif "/kor " in msg.text:
                isi = msg.text.replace("/kor ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ko')
                A = hasil.text
                A = A.encode('utf-8')
                yudha.sendText(msg.to, A)
            elif "/malay " in msg.text:
                isi = msg.text.replace("/malay ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ms')
                A = hasil.text
                A = A.encode('utf-8')
                yudha.sendText(msg.to, A)
            elif "/arab " in msg.text:
                isi = msg.text.replace("/arab ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='ar')
                A = hasil.text
                A = A.encode('utf-8')
                yudha.sendText(msg.to, A)
            elif "/jawa " in msg.text:
                isi = msg.text.replace("/jawa ","")
                translator = Translator()
                hasil = translator.translate(isi, dest='jw')
                A = hasil.text
                A = A.encode('utf-8')
                yudha.sendText(msg.to, A)
#---------------------------------------------------------------
            elif "/removechat" in msg.text.lower():
                    try:
                        yudha.removeAllMessages(op.param2)
                        print "[Command] Remove Chat"
                        yudha.sendText(msg.to,"Done")
                    except Exception as error:
                        print error
                        yudha.sendText(msg.to,"Error")
#---------------------------------------------------------
                
            elif msg.text.lower() == 'kam':
                ginfo = yudha.getGroup(msg.to)
                yudha.sendText(msg.to,"Selamat Datang Di Grup " + str(ginfo.name))
                jawaban1 = ("Selamat Datang Di Grup " + str(ginfo.name))
                yudha.sendText(msg.to,"Owner Grup " + str(ginfo.name) + " :\n" + ginfo.creator.displayName )
            
            elif "Say-id " in msg.text:
                say = msg.text.replace("Say-id ","")
                lang = 'id'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                yudha.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-en " in msg.text:
                say = msg.text.replace("Say-en ","")
                lang = 'en'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                yudha.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-jp " in msg.text:
                say = msg.text.replace("Say-jp ","")
                lang = 'ja'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                yudha.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ar " in msg.text:
                say = msg.text.replace("Say-ar ","")
                lang = 'ar'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                yudha.sendAudio(msg.to,"hasil.mp3")
                
            elif "Say-ko " in msg.text:
                say = msg.text.replace("Say-ko ","")
                lang = 'ko'
                tts = gTTS(text=say, lang=lang)
                tts.save("hasil.mp3")
                yudha.sendAudio(msg.to,"hasil.mp3")
                
            elif "Kapan " in msg.text:
                  tanya = msg.text.replace("Kapan ","")
                  jawab = ("kapan kapan","besok","satu abad lagi","Hari ini","Tahun depan","Minggu depan","Bulan depan","Sebentar lagi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  yudha.sendAudio(msg.to,'tts.mp3')
                  
            elif "Apakah " in msg.text:
                  tanya = msg.text.replace("Apakah ","")
                  jawab = ("Ya","Tidak","Mungkin","Bisa jadi")
                  jawaban = random.choice(jawab)
                  tts = gTTS(text=jawaban, lang='id')
                  tts.save('tts.mp3')
                  yudha.sendAudio(msg.to,'tts.mp3')
            
            elif '/video ' in msg.text:
                    try:
                        textToSearch = (msg.text).replace('/video ', "").strip()
                        query = urllib.quote(textToSearch)
                        url = "https://www.youtube.com/results?search_query=" + query
                        response = urllib2.urlopen(url)
                        html = response.read()
                        soup = BeautifulSoup(html, "html.parser")
                        results = soup.find(attrs={'yudhaass': 'yt-uix-tile-link'})
                        ght = ('https://www.youtube.com' + results['href'])
                        yudha.sendVideoWithURL(msg.to, ght)
                    except:
                        yudha.sendText(msg.to, "Could not find it")
            
            elif "/youtube " in msg.text:
                    query = msg.text.replace("/youtube ","")
                    with requests.session() as s:
                        s.headers['user-agent'] = 'Mozilla/5.0'
                        url = 'http://www.youtube.com/results'
                        params = {'search_query': query}
                        r = s.get(url, params=params)
                        soup = BeautifulSoup(r.content, 'html5lib')
                        hasil = ""
                        for a in soup.select('.yt-lockup-title > a[title]'):
                            if '&list=' not in a['href']:
                                hasil += ''.join((a['title'],'\nUrl : http://www.youtube.com' + a['href'],'\n\n'))
                        yudha.sendText(msg.to,hasil)
                        print '[Command] Youtube Search'
                        
            elif "Lirik " in msg.text:
                try:
                    songname = msg.text.lower().replace("Lirik ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'Lyric Lagu ('
                        hasil += song[0]
                        hasil += ')\n\n'
                        hasil += song[5]
                        yudha.sendText(msg.to, hasil)
                except Exception as wak:
                        yudha.sendText(msg.to, str(wak))
                        
            elif "Wikipedia " in msg.text:
                  try:
                      wiki = msg.text.lower().replace("Wikipedia ","")
                      wikipedia.set_lang("id")
                      pesan="Title ("
                      pesan+=wikipedia.page(wiki).title
                      pesan+=")\n\n"
                      pesan+=wikipedia.summary(wiki, sentences=1)
                      pesan+="\n"
                      pesan+=wikipedia.page(wiki).url
                      yudha.sendText(msg.to, pesan)
                  except:
                          try:
                              pesan="Over Text Limit! Please yudhaick link\n"
                              pesan+=wikipedia.page(wiki).url
                              yudha.sendText(msg.to, pesan)
                          except Exception as e:
                              yudha.sendText(msg.to, str(e))
                              
            elif "Music " in msg.text:
                try:
                    songname = msg.text.lower().replace("Music ","")
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        yudha.sendText(msg.to, hasil)
                        yudha.sendText(msg.to, "Please Wait for audio...")
                        yudha.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        yudha.sendText(msg.to, str(njer))
            
            elif "Image " in msg.text:
                search = msg.text.replace("Image ","")
                url = 'https://www.google.com/search?espv=2&biw=1366&bih=667&tbm=isch&oq=kuc&aqs=mobile-gws-lite.0.0l5&q=' + search
                raw_html = (download_page(url))
                items = []
                items = items + (_images_get_all_items(raw_html))
                path = random.choice(items)
                print path
                try:
                    yudha.sendImageWithURL(msg.to,path)
                except:
                    pass           
            
            elif "/cekig " in msg.text:
                    try:
                        instagram = msg.text.replace("/cekig ","")
                        response = requests.get("https://www.instagram.com/"+instagram+"?__a=1")
                        data = response.json()
                        namaIG = str(data['user']['full_name'])
                        bioIG = str(data['user']['biography'])
                        mediaIG = str(data['user']['media']['count'])
                        verifIG = str(data['user']['is_verified'])
                        usernameIG = str(data['user']['username'])
                        followerIG = str(data['user']['followed_by']['count'])
                        profileIG = data['user']['profile_pic_url_hd']
                        privateIG = str(data['user']['is_private'])
                        followIG = str(data['user']['follows']['count'])
                        link = "Link: " + "https://www.instagram.com/" + instagram
                        text = "Name : "+namaIG+"\nUsername : "+usernameIG+"\nBiography : "+bioIG+"\nFollower : "+followerIG+"\nFollowing : "+followIG+"\nPost : "+mediaIG+"\nVerified : "+verifIG+"\nPrivate : "+privateIG+"" "\n" + link
                        yudha.sendText(msg.to, str(text))
                        yudha.sendImageWithURL(msg.to, profileIG)
                    except Exception as e:
                        yudha.sendText(msg.to, str(e))
                        
            elif "/postig" in msg.text:
                separate = msg.text.split(" ")
                user = msg.text.replace(separate[0] + " ","")
                if user.startswith("@"):
                    user = user.replace("@","")
                profile = "https://www.instagram.com/" + user
                with requests.session() as x:
                    x.headers['user-agent'] = 'Mozilla/5.0'
                    end_cursor = ''
                    for count in range(1, 999):
                        print('PAGE: ', count)
                        r = x.get(profile, params={'max_id': end_cursor})
                    
                        data = re.search(r'window._sharedData = (\{.+?});</script>', r.text).group(1)
                        j    = json.loads(data)
                    
                        for node in j['entry_data']['ProfilePage'][0]['user']['media']['nodes']: 
                            if node['is_video']:
                                page = 'https://www.instagram.com/p/' + node['code']
                                r = x.get(page)
                                url = re.search(r'"video_url": "([^"]+)"', r.text).group(1)
                                print(url)
                                yudha.sendVideoWithURL(msg.to,url)
                            else:
                                print (node['display_src'])
                                yudha.sendImageWithURL(msg.to,node['display_src'])
                        end_cursor = re.search(r'"end_cursor": "([^"]+)"', r.text).group(1)
                        
            elif msg.text.lower() == 'time':
                timeNow = datetime.now()
                timeHours = datetime.strftime(timeNow,"(%H:%M)")
                day = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday","Friday", "Saturday"]
                hari = ["Minggu", "Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu"]
                bulan = ["Januari", "Februari", "Maret", "April", "Mei", "Juni", "Juli", "Agustus", "September", "Oktober", "November", "Desember"]
                inihari = datetime.today()
                hr = inihari.strftime('%A')
                bln = inihari.strftime('%m')
                for i in range(len(day)):
                    if hr == day[i]: hasil = hari[i]
                for k in range(0, len(bulan)):
                    if bln == str(k): bulan = blan[k-1]
                rst = hasil + ", " + inihari.strftime('%d') + " - " + bln + " - " + inihari.strftime('%Y') + "\nJam : [ " + inihari.strftime('%H:%M:%S') + " ]"
                yudha.sendText(msg.to, rst)

            elif "Checkdate " in msg.text:
                tanggal = msg.text.replace("Checkdate ","")
                r=requests.get('https://script.google.com/macros/exec?service=AKfycbw7gKzP-WYV2F5mc9RaR7yE3Ve1yN91Tjs91hp_jHSE02dSv9w&nama=ervan&tanggal='+tanggal)
                data=r.text
                data=json.loads(data)
                lahir = data["data"]["lahir"]
                usia = data["data"]["usia"]
                ultah = data["data"]["ultah"]
                zodiak = data["data"]["zodiak"]
                yudha.sendText(msg.to,"============ I N F O R M A S I ============\n"+"Date Of Birth : "+lahir+"\nAge : "+usia+"\nUltah : "+ultah+"\nZodiak : "+zodiak+"\n============ I N F O R M A S I ============")

            elif msg.text.lower() == 'kalender':
	    	    wait2['setTime'][msg.to] = datetime.today().strftime('TANGGAL : %Y-%m-%d \nHARI : %A \nJAM : %H:%M:%S')
	            yudha.sendText(msg.to, "KALENDER\n\n" + (wait2['setTime'][msg.to]))
#==============================================================================#
            elif msg.text.lower() == 'ifconfig':
                    botKernel = subprocess.Popen(["ifconfig"], stdout=subprocess.PIPE).communicate()[0]
                    yudha.sendText(msg.to, botKernel + "\n\n===SERVER INFO NetStat===")
            elif msg.text.lower() == 'system':
                    botKernel = subprocess.Popen(["df","-h"], stdout=subprocess.PIPE).communicate()[0]
                    yudha.sendText(msg.to, botKernel + "\n\n===SERVER INFO SYSTEM===")
            elif msg.text.lower() == 'kernel':
                    botKernel = subprocess.Popen(["uname","-srvmpio"], stdout=subprocess.PIPE).communicate()[0]
                    yudha.sendText(msg.to, botKernel + "\n\n===SERVER INFO KERNEL===")
            elif msg.text.lower() == 'cpu':
                    botKernel = subprocess.Popen(["cat","/proc/cpuinfo"], stdout=subprocess.PIPE).communicate()[0]
                    yudha.sendText(msg.to, botKernel + "\n\n===SERVER INFO CPU===")
                    
            elif msg.text.lower() == 'reboot':
                    print "[Command]Restart"
                    try:
                        yudha.sendText(msg.to,"Restarting...")
                        yudha.sendText(msg.to,"Restart Success")
                        restart_program()
                    except:
                        yudha.sendText(msg.to,"Please wait")
                        restart_program()
                        pass
                    
            elif "Turn off" in msg.text:
                 try:
                     import sys
                     sys.exit()
                 except:
                     pass
                
            elif msg.text.lower() == 'runtime':
                yudha.sendText(msg.to,"「Please wait..」\nType  :Loading...\nStatus : Loading...")
                eltime = time.time() - mulai
                van = "Type : Bot Sedang Berjalan \nStatus : Aktif \nMySelbot sudah berjalan selama"+waktu(eltime)
                yudha.sendText(msg.to,van)                    
#==============================================================================#
#==============================================================================#
            
            elif "Ban @" in msg.text:
                if msg.toType == 2:
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip()
                    gs = yudha.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        yudha.sendText(msg.to,_nametarget + " Not Found")
                    else:
                        for target in targets:
                            try:
                                wait["blacklist"][target] = True
                                yudha.sendText(msg.to,_nametarget + " Succes Add to Blacklist")
                            except:
                                yudha.sendText(msg.to,"Error")
                                
            elif "Unban @" in msg.text:
                if msg.toType == 2:
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip()
                    gs = yudha.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        yudha.sendText(msg.to,_nametarget + " Not Found")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                yudha.sendText(msg.to,_nametarget + " Delete From Blacklist")
                            except:
                                yudha.sendText(msg.to,_nametarget + " Not In Blacklist")

            elif "Ban:" in msg.text:                  
                       nk0 = msg.text.replace("Ban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = yudha.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    yudha.sendText(msg.to,_name + " Succes Add to Blacklist")
                                except:
                                    yudha.sendText(msg.to,"Error")

            elif "Unban:" in msg.text:                  
                       nk0 = msg.text.replace("Unban:","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = yudha.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    yudha.sendText(msg.to,_name + " Delete From Blacklist")
                                except:
                                    yudha.sendText(msg.to,_name + " Not In Blacklist")
                                    
            elif msg.text in ["yudhaear"]:
                wait["blacklist"] = {}
                yudha.sendText(msg.to,"Blacklist Telah Dibersihkan")
            elif msg.text.lower() == 'ban:on':
                wait["wblacklist"] = True
                yudha.sendText(msg.to,"Send Contact")
            elif msg.text.lower() == 'unban:on':
                wait["dblacklist"] = True
                yudha.sendText(msg.to,"Send Contact")
            elif msg.text in ["Banlist"]:   
                if wait["blacklist"] == {}:
                    yudha.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    yudha.sendText(msg.to,"Daftar Banlist")
                    num=1
                    msgs="══════════List Blacklist═════════"
                    for mi_d in wait["blacklist"]:
                        msgs+="\n[%i] %s" % (num, yudha.getContact(mi_d).displayName)
                        num=(num+1)
                    msgs+="\n══════════List Blacklist═════════\n\nTotal Blacklist : %i" % len(wait["blacklist"])
                    yudha.sendText(msg.to, msgs)
            elif msg.text in ["Conban","Contactban","Contact ban"]:
                if wait["blacklist"] == {}:
                    yudha.sendText(msg.to,"Tidak Ada Blacklist")
                else:
                    yudha.sendText(msg.to,"Daftar Blacklist")
                    h = ""
                    for i in wait["blacklist"]:
                        h = yudha.getContact(i)
                        M = Message()
                        M.to = msg.to
                        M.contentType = 13
                        M.contentMetadata = {'mid': i}
                        yudha.sendMessage(M)
            elif msg.text in ["Midban","Mid ban"]:
                if msg.toType == 2:
                    group = yudha.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    num=1
                    cocoa = "══════════List Blacklist═════════"
                    for mm in matched_list:
                        cocoa+="\n[%i] %s" % (num, mm)
                        num=(num+1)
                        cocoa+="\n═════════List Blacklist═════════\n\nTotal Blacklist : %i" % len(matched_list)
                    yudha.sendText(msg.to,cocoa)
            elif msg.text.lower() == 'scan blacklist':
                if msg.toType == 2:
                    group = yudha.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        yudha.sendText(msg.to,"Tidak ada Daftar Blacklist")
                        return
                    for jj in matched_list:
                        try:
                            yudha.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass       
#==============================================#
        if op.type == 17:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
            if wait["protect"] == True:
                if wait["blacklist"][op.param2] == True:
                    try:
                        yudha.kickoutFromGroup(op.param1,[op.param2])
                        G = yudha.getGroup(op.param1)
                        G.preventJoinByTicket = True
                        yudha.updateGroup(G)
                    except:
                        try:
                            yudha.kickoutFromGroup(op.param1,[op.param2])
                            G = yudha.getGroup(op.param1)
                            G.preventJoinByTicket = True
                            yudha.updateGroup(G)
                        except:
                            pass
        if op.type == 19:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["protect"] == True:
                    wait ["blacklist"][op.param2] = True
                    yudha.kickoutFromGroup(op.param1,[op.param2])
                    yudha.inviteIntoGroup(op.param1,[op.param2])
        if op.type == 13:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["inviteprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    yudha.kickoutFromGroup(op.param1,[op.param2])
                    if op.param2 not in Bots:
                        if op.param2 in Bots:
                            pass
                        elif wait["inviteprotect"] == True:
                            wait ["blacklist"][op.param2] = True
                            yudha.cancelGroupInvitation(op.param1,[op.param3])
                            if op.param2 not in Bots:
                                if op.param2 in Bots:
                                    pass
                                elif wait["cancelprotect"] == True:
                                    wait ["blacklist"][op.param2] = True
                                    yudha.cancelGroupInvitation(op.param1,[op.param3])
        if op.type == 11:
            if op.param2 not in Bots:
                if op.param2 in Bots:
                    pass
                elif wait["linkprotect"] == True:
                    wait ["blacklist"][op.param2] = True
                    G = yudha.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    yudha.updateGroup(G)
                    yudha.kickoutFromGroup(op.param1,[op.param2])
        if op.type == 5:
            if wait["autoAdd"] == True:
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    yudha.sendText(op.param1,str(wait["message"]))

        if op.type == 11:
            if wait["linkprotect"] == True:
                if op.param2 not in Bots:
                    G = yudha.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    yudha.kickoutFromGroup(op.param1,[op.param3])
                    yudha.updateGroup(G)

#==============================================================================#
#------------------------------------------------------------------------------#
#==============================================================================#
        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
           
                    if op.param2 in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += op.param2
                    wait2['ROM'][op.param1][op.param2] = op.param2
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                else:
                    pass
            except:
                pass           
            
        
        if op.type == 59:
            print op
    
    
    except Exception as error:
        print error

def autolike():
    count = 1
    while True:
        try:
           for posts in yudha.activity(1)["result"]["posts"]:
             if posts["postInfo"]["liked"] is False:
                if wait["likeOn"] == True:
                   yudha.like(posts["userInfo"]["writerMid"], posts["postInfo"]["postId"], 1001)
                   print "Like"
                   if wait["commentOn"] == True:
                      if posts["userInfo"]["writerMid"] in wait["commentBlack"]:
                         pass
                      else:
                          yudha.comment(posts["userInfo"]["writerMid"],posts["postInfo"]["postId"],wait["comment"])
        except:
            count += 1
            if(count == 50):
                sys.exit(0)
            else:
                pass
thread2 = threading.Thread(target=autolike)
thread2.daemon = True
thread2.start()

def likefriend():
    for zx in range(0,20):
      hasil = yudha.activity(limit=20)
      if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
        try:
          yudha.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1001)
          print "Like"
        except:
          pass
      else:
          print "Already Liked"
time.sleep(0.60)

def likeme():
    for zx in range(0,20):
        hasil = yudha.activity(limit=20)
        if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
            if hasil['result']['posts'][zx]['userInfo']['mid'] in mid:
                try:
                    yudha.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
                    print "Like"
                except:
                    pass
            else:
                print "Status Sudah di Like"


while True:
    try:
        Ops = yudha.fetchOps(yudha.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(yudha.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            yudha.Poll.rev = max(yudha.Poll.rev, Op.revision)
            bot(Op)
