# -*- coding: utf-8 -*-

import yuda
from yuda.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re,requests,urllib
#from gtts import gTTS
import goslate


kr = yuda.LINE()
#kr.login(qr=True)
kr.login(token="isi token mu")
kr.loginResult()

print "login success boss"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage ="""╔═════════════
║        ✰ ΥυδHΔ βΟτ ✰
╠═════════════
║    ᴏᴡɴᴇʀ : ᴍ.ᴡɪʀᴀ ʏᴜᴅʜᴀ ᴘ
╠═════════════
║╔════════════
║╠❂➣Apakah (kerang ajaib)
║╠❂➣kedapkedip = coba aja
║╠❂➣Dosa @(by tag) 
║╠❂➣Pahala @(by tag) 
║╠❂➣Steal dp @(by tag)
║╠❂➣Steal home @(by tag)
║╠❂➣Yud say = teks ke suara
║╠❂➣Yud cctv 
║╠❂➣Yud intip 
║╠❂➣Yud tagall 
║╠❂➣trid = translate ing > ind
║╠❂➣tren= translate ind > ing
║╠❂➣Yud gcreator 
║╠❂➣Yud ginfo = Info grup
║╠❂➣Yud cancel = Mmbtalkn undangan
║╠❂➣Yud ourl = Invite by link on
║╠❂➣Yud curl = Invite by link off
║╠❂➣Yud help = Menampilkan keyword
║╠❂➣Yud bye = Bot keluar room
║╠❂➣Yud creator = melihat creator bot
║╠❂➣Yud musik <penyanyi> <judul>
║╚════════════
╠═════════════
║Suport By:>>>> Yudha <<<<<
║line.me/ti/p/~iniyud
║line.me/ti/p~@ikj9968f
╚═════════════
"""


KAC=[kr]
DEF=[kr]
mid = kr.getProfile().mid

Bots=[mid]
admin=["uecc57cb55f480ee2a45d81434a9b864d","u3bec4cf8da7f4403f9228651c4fde5ea","ubdf4908b063316d7a64cea9e00ac418d",mid]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":20},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':True,
    'message':"Thanks for add\ncreator :\nline.me/ti/p/~@ikj9968f\nline.me/ti/p~iniyud",
    "lang":"JP",
    "comment":"Thanks for add ",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "atjointicket":True,
    "Protectcancl":False,
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']


def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1

def NOTIFIED_READ_MESSAGE(op):
    try:
        if op.param1 in wait2['readPoint']:
            Name = kr.getContact(op.param2).displayName
            if Name in wait2['readMember'][op.param1]:
                pass
            else:
                wait2['readMember'][op.param1] += "\n・" + Name
                wait2['ROM'][op.param1][op.param2] = "・" + Name
        else:
            pass
    except:
        pass

#---------------------------[AutoLike-nya]---------------------------#
#def autolike():
     #for zx in range(0,100):
        #hasil = kr.activity(limit=100)
        #if hasil['result']['posts'][zx]['postInfo']['liked'] == False:
          #try:    
            #kr.like(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],likeType=1002)
            #kr.comment(hasil['result']['posts'][zx]['userInfo']['mid'],hasil['result']['posts'][zx]['postInfo']['postId'],"AutoLike by kris\n\nCAB => Cyber Army Bot")
            #print "Like"
          #except:
            #pass
        #else:
            #print "Already Liked"
     #time.sleep(500)
#thread2 = threading.Thread(target=autolike)
#thread2.daemon = True
#thread2.start()
#---------------------------[AutoLike-nya]---------------------------#









#-------------------

def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                kr.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    kr.sendText(op.param1,str(wait["message"]))

        #------Protect Group Kick start------#
        if op.type == 11:
           if wait["Protectgr"] == True:
               if op.param2 not in Bots:
                   G = kr.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                   random.choice(DEF).updateGroup(G)
        #------Protect Group Kick finish-----#

        #------Cancel Invite User start------#
        if op.type == 13:
           if wait["Protectcancl"] == True:
               if op.param2 not in Bots:
                  group = kr.getGroup(op.param1)
                  gMembMids = [contact.mid for contact in group.invitee]
                  random.choice(DEF).cancelGroupInvitation(op.param1, gMembMids)
        #------Cancel Invite User Finish------#
        if op.type == 13:
            if op.param3 in mid:
                kr.acceptGroupInvitation(op.param1)

            if op.param3 in admin:
                kr.acceptGroupInvitation(op.param1)

            if op.param2 in admin:
                kr.acceptGroupInvitation(op.param1)

            if op.param2 not in admin:
                kr.acceptGroupInvitation(op.param1)

#            if op.param3 in admin:
#                if op.param2 not in Bots:
#                    G = kr.getGroup(op.param1)
#                    G.preventJoinByTicket = False
#                    kr.updateGroup(G)
#                    Ticket = kr.reissueGroupTicket(op.param1)
#                    kr.acceptGroupInvitationByTicket(op.param1,Ticket)
#                    G.preventJoinByTicket = True
#                    kr.updateGroup(G)
#                    Ticket = kr.reissueGroupTicket(op.param1)

            if op.param3 in admin:
                if op.param2 not in Bots:
                    kr.getGroup(op.param1)
                    kr.inviteIntoGroup(op.param1,[op.param3])
                    kr.kickoutFromGroup(op.param1,[op.param2])

            if op.param3 in admin:
                if op.param2 not in Bots:
                    M = kr.getGroup(op.param1)
                    X = kr.findAndAddContactsByMid(op.param1,M)
                    X.preventJoinByMid = False
                    kr.updateGroup(X,M)
                    Tm = kr.reissueGroupByMid(op.param1)
                    admin.acceptGroupInvitationByMid(op.param1,Tm)
                    X.preventJoinByMid = True
                    kr.updateGroup(X,M)
                    Tm = kr.reissueGroupTicket(op.param1)

            if op.param3 in mid:
                if op.param2 not in Bots:
                    X = random.choice(DEF).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(DEF).updateGroup(X)
                    Ti = random.choice(DEF).reissueGroupTicket(op.param1)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kr.updateGroup(X)
                    Ti = kr.reissueGroupTicket(op.param1)

        if op.type == 13:
            if mid in op.param3:
                G = kr.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            kr.rejectGroupInvitation(op.param1)
                        else:
                            kr.acceptGroupInvitation(op.param1)
                    else:
                        kr.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        kr.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    kr.cancelGroupInvitation(op.param1, matched_list)

#-------------------------------------------------------------------------------
        if op.type == 15:
            if op.param2 in Bots:
                return
            kr.sendText(op.param1, "Good Bye " + cl.getContact(op.param2).displayName +  "\nSemoga Tenang Di Alam Sana..(p′︵‵。) 🤗")
            #print "MemberLeft"

#------------------------------------------------------

        #------Joined User Kick start------#
        if op.type == 17:
           if wait["Protectjoin"] == False:
               if op.param2 not in Bots:
                   random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
               
        #------Joined User Kick start------#
        
        if op.type == 19:
           if op.param2 not in Bots:
              random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
              random.choice(DEF).inviteIntoGroup(op.param1,[op.param3])
           else: 
               pass

        if op.type == 19:
           if op.param3 in admin:
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              kr.inviteIntoGroup(op.param1,admin)
           else:
               pass

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    if op.param2 in admin:
                        pass
                    try:
                        kr.kickoutFromGroup(op.param1,[op.param2])
                        kr.kickoutFromGroup(op.param1,[op.param2])
                        kr.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(G)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    kr.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = kr.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    kr.updateGroup(X)
                    Ti = kr.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
 
        if op.type == 13:
            if mid in op.param3:
                G = kr.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            kr.rejectGroupInvitation(op.param1)
                        else:
                            kr.acceptGroupInvitation(op.param1)
                    else:
                        kr.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        kr.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    kr.cancelGroupInvitation(op.param1, matched_list)
                    
        if op.type == 22:
            if wait["leaveRoom"] == True:
                kr.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                kr.leaveRoom(op.param1)


        if op.type == 26:
            msg = op.message
            try:
                if msg.contentType == 0:
                    try:
                        if msg.to in wait2['readPoint']:
                            if msg.from_ in wait2["ROM"][msg.to]:
                                del wait2["ROM"][msg.to][msg.from_]
                            else:
                                pass
                    except:
                        pass
                    else:
                        pass
            except KeyboardInterrupt:
                sys.exit(0)
            except Exception as error:
                print error
                print ("\n\nRECEIVE_MESSAGE\n\n")
                return

        if op.type == 26:
            msg = op.message

            if 'MENTION' in mid:
                kr.sendText(msg.to, '[AUTO_RESPON]\nNah kenapa ngetag bot\nMau ditikung juga ya..!!!')
            else:
                pass
            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    kr.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                kr.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        kr.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        kr.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        kr.sendText(msg.to,"deleted")
                        kr.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        kr.sendText(msg.to,"It is not in the black list")
                        kr.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        kr.sendText(msg.to,"already")
                        kr.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        kr.sendText(msg.to,"aded")
                        kr.sendText(msg.to,"aded")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        kr.sendText(msg.to,"deleted")
                        kr.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        kr.sendText(msg.to,"It is not in the black list")
                        kr.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    kr.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = kr.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = kr.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        kr.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = kr.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = kr.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        kr.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    kr.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Yud help"]:
                if wait["lang"] == "JP":
                    kr.sendText(msg.to,helpMessage)
                else:
                    kr.sendText(msg.to,helpMessage)
#            elif msg.text in ["Set group"]:
#              if msg.from_ in admin:
#                if wait["lang"] == "JP":
#                    kr.sendText(msg.to,Setgroup)
#                else:
#                    kr.sendText(msg.to,Setgroup)
            elif ("Yud gn " in msg.text):
                    X = kr.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    kr.updateGroup(X)
            elif "Kick " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Kick ","")
                kr.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("Invite ","")
                kr.findAndAddContactsByMid(midd)
                kr.inviteIntoGroup(msg.to,[midd])
            elif "sinvite " in msg.text:
              if msg.from_ in admin:
                midd = msg.text.replace("sinvite ","")
                kr.findAndAddContactsByMid(midd)
                kr.inviteIntoGroup(msg.to,[midd])
            elif msg.text in ["yud bot"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                kr.sendMessage(msg)

                

            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                random.choice(KAC).sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","/gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': '89131c1a-e549-4bd5-9e60-e24de0d2e252',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                kr.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                kr.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kr.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                msg.text = None
                kr.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                kr.sendMessage(msg)
                kr.sendMessage(msg)
            elif msg.text in ["Yud cancel"]:
                if msg.toType == 2:
                    X = kr.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        kr.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"No one is inviting")
                        else:
                            kr.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kr.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print kr.getGroup(msg.to)
                ##kr.sendMessage(msg)
            elif msg.text in ["Yud ourl"]:
                    X = kr.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kr.updateGroup(X)
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Invite by link open")
                    else:
                        kr.sendText(msg.to,"Already open")
            elif msg.text in ["Aa ourl","aa link on"]:
                if msg.toType == 2:
                    X = kr.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kr.updateGroup(X)
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Done Chivas")
                    else:
                        kr.sendText(msg.to,"already open")
                else:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kr.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Yud curl"]:
                    X = kr.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kr.updateGroup(X)
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Invite by link Close")
                    else:
                        kr.sendText(msg.to,"Already close")
            elif msg.text in ["Aa curl","aa link off"]:
                if msg.toType == 2:
                    X = kr.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    kr.updateGroup(X)
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Done Chivas")
                    else:
                        kr.sendText(msg.to,"already close")
                else:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kr.sendText(msg.to,"Not for use less than group")
            elif "jointicket " in msg.text.lower():
                rplace=msg.text.lower().replace("jointicket ")
                if rplace == "on":
                    wait["atjointicket"]=True
            elif rplace == "off":
                wait["atjointicket"]=False
                kr.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
                link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
                links = link_re.findall(msg.text)
                n_links=[]
                for l in links:
                    if l not in n_links:
                        n_links.append(l)
                for ticket_id in n_links:
                    if wait["atjointicket"] == True:
                        group=kr.findGroupByTicket(ticket_id)
                        kr.acceptGroupInvitationByTicket(group.mid,ticket_id)
                        kr.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Yud ginfo":
                if msg.toType == 2:
                    ginfo = kr.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        kr.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        kr.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Can not be used outside the group")
                    else:
                        kr.sendText(msg.to,"Not for use less than group")
            elif "idgrup" == msg.text:
                kr.sendText(msg.to,msg.to)
            elif "my mid" == msg.text:
                random.choice(KAC).sendText(msg.to, msg.from_)
            elif "mid bot" == msg.text:
                kr.sendText(msg.to,mid)
            elif msg.text in ["Wkwkwk","Wkwk","Wk","wkwkwk","wkwk","wk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kr.sendMessage(msg)
                kr.sendMessage(msg)
            elif msg.text in ["Hehehe","Hehe","He","hehehe","hehe","he"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kr.sendMessage(msg)
                kr.sendMessage(msg)
            elif msg.text in ["Galau"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kr.sendMessage(msg)
                kr.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kr.sendMessage(msg)
                kr.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kr.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kr.sendMessage(msg)
                kr.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kr.sendMessage(msg)
                kr.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kr.sendMessage(msg)
                kr.sendMessage(msg)
            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                kr.sendMessage(msg)
                kr.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                kr.sendMessage(msg)
                kr.sendMessage(msg)
            elif msg.text in ["TL: "]:
                tl_text = msg.text.replace("TL: ","")
                kr.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+kr.new_post(tl_text)["result"]["post"]["postInfo"]["postId"]) 

            elif "Yud rename " in msg.text:
              if msg.from_ in admin:
                string = msg.text.replace("aa rename ","")
                if len(string.decode('utf-8')) <= 10000:
                    profile = kr.getProfile()
                    profile.displayName = string
                    kr.updateProfile(profile)
                    kr.sendText(msg.to,"Update Names >" + string + "<")

            elif msg.text in ["Mc "]:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                kr.sendMessage(msg)
            elif msg.text in ["Joinn on","joinn on"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"kick Joined Group On")
                    else:
                        kr.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"kick Joined Group On")
                    else:
                        kr.sendText(msg.to,"done")
            elif msg.text in ["Joinn off","joinn off"]:
              if msg.from_ in admin:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"kick Joined Group Off")
                    else:
                        kr.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"kick Joined Group Off")
                    else:
                        kr.sendText(msg.to,"done")
            elif msg.text in ["Cancl on","cancl on"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Cancel All Invited On")
                    else:
                        kr.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Cancel All Invited On")
                    else:
                        kr.sendText(msg.to,"done")
            elif msg.text in ["Cancl off","cancl off"]:
              if msg.from_ in admin:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Cancel All Invited Off")
                    else:
                        kr.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Cancel All Invited Off")
                    else:
                        kr.sendText(msg.to,"done")
            elif msg.text in ["Gr on","gr on"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protect Group On")
                    else:
                        kr.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protect Group On")
                    else:
                        kr.sendText(msg.to,"done")
            elif msg.text in ["Gr off","gr off"]:
              if msg.from_ in admin:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protect Group Off")
                    else:
                        kr.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Protect Group Off")
                    else:
                        kr.sendText(msg.to,"done")
            elif msg.text in ["K On","K on","k on"]:
              if msg.from_ in admin:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        kr.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        kr.sendText(msg.to,"done")
            elif msg.text in ["K Off","K off","k off"]:
              if msg.from_ in admin:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        kr.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        kr.sendText(msg.to,"done")
            elif msg.text in ["Join on"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"already on")
                    else:
                        kr.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"already on")
                    else:
                        kr.sendText(msg.to,"done")
            elif msg.text in ["Join off"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"already off")
                    else:
                        kr.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"already off")
                    else:
                        kr.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            kr.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        num =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            kr.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            kr.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Value is wrong")
                    else:
                        kr.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"already on")
                    else:
                        kr.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"done")
                    else:
                        kr.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"already off")
                    else:
                        kr.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"done")
                    else:
                        kr.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"already on")
                    else:
                        kr.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"done")
                    else:
                        kr.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"already off")
                    else:
                        kr.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"done")
                    else:
                        kr.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Status"]:
                md = ""
                if wait["Protectjoin"] == True: md+="􀔃􀆑lock􏿿  Block Join\n"
                else: md+=" Block Join Off\n"
                if wait["Protectgr"] == True: md+="􀔃􀆑lock􏿿   Block Group\n"
                else: md+=" Block Group Off\n"
                if wait["Protectcancl"] == True: md+="􀔃􀆑lock􏿿 Cancel All Invited\n"
                else: md+=" Cancel All Invited Off\n"
                if wait["contact"] == True: md+=" Contact    : on\n"
                else: md+=" Contact    : off\n"
                if wait["autoJoin"] == True: md+=" Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Group cancel : off\n"
                if wait["leaveRoom"] == True: md+=" Auto leave    : on\n"
                else: md+=" Auto leave : off\n"
                if wait["timeline"] == True: md+=" Share   : on\n"
                else:md+=" Share   : off\n"
                if wait["autoAdd"] == True: md+=" Auto add : on\n"
                else:md+=" Auto add : off\n"
                if wait["commentOn"] == True: md+=" Comment : on\n"
                else:md+=" Comment : off\n"
                kr.sendText(msg.to,md)
            elif "album merit " in msg.text:
                gid = msg.text.replace("album merit ","")
                album = kr.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"There is no album")
                    else:
                        kr.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    kr.sendText(msg.to,mg)
            elif "album " in msg.text:
                gid = msg.text.replace("album ","")
                album = kr.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"There is no album")
                    else:
                        kr.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
                gid = msg.text.replace("album remove ","")
                albums = kr.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        kr.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    kr.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    kr.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id"]:
                gid = kr.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (kr.getGroup(i).name,i)
                kr.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
                gid = kr.getGroupIdsInvited()
                for i in gid:
                    kr.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    kr.sendText(msg.to,"All invitations have been refused")
                else:
                    kr.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeat’" in msg.text:
                gid = msg.text.replace("album removeat’","")
                albums = kr.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        kr.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    kr.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    kr.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"already on")
                    else:
                        kr.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"done")
                    else:
                        kr.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"already off")
                    else:
                        kr.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"done")
                    else:
                        kr.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
                wait["message"] = msg.text.replace("Message change: ","")
                kr.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    kr.sendText(msg.to,"message changed")
                else:
                    kr.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
                if wait["lang"] == "JP":
                    kr.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    kr.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    kr.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    kr.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    kr.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    kr.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé–‹"]:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"done")
                    else:
                        kr.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"done")
                    else:
                        kr.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"done")
                    else:
                        kr.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"done")
                    else:
                        kr.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª�"]:
                kr.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
                if msg.toType == 2:
                    x = kr.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kr.updateGroup(x)
                    gurl = kr.reissueGroupTicket(msg.to)
                    kr.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Can't be used outside the group")
                    else:
                        kr.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Yud gurl"]:
                if msg.toType == 2:
                    x = kr.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        kr.updateGroup(x)
                    gurl = kr.reissueGroupTicket(msg.to)
                    kr.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        kr.sendText(msg.to,"Can't be used outside the group")
                    else:
                        kr.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Comment bl "]:
                wait["wblack"] = True
                kr.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
                wait["dblack"] = True
                kr.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
                if wait["commentBlack"] == {}:
                    kr.sendText(msg.to,"confirmed")
                else:
                    kr.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +kr.getContact(mi_d).displayName + "\n"
                    kr.sendText(msg.to,mc)
                    
        #-------------Fungsi Jam on/off Start-------------------#            
            elif msg.text in ["Jam on"]:
                if wait["clock"] == True:
                    kr.sendText(msg.to,"Bot 4 jam on")
                else:
                    wait["clock"] = True
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kr.getProfile()
                    profile.displayName = wait["cName4"] + nowT
                    kr.updateProfile(profile)
                    kr.sendText(msg.to,"Jam Selalu On")
            elif msg.text in ["Jam off"]:
                if wait["clock"] == False:
                    kr.sendText(msg.to,"Bot 4 jam off")
                else:
                    wait["clock"] = False
                    kr.sendText(msg.to,"Jam Sedang Off")
         #-------------Fungsi Jam on/off Finish-------------------#           
         
         #-------------Fungsi Change Clock Start------------------#
            elif msg.text in ["Change clock"]:
                n = msg.text.replace("Change clock","")
                if len(n.decode("utf-8")) > 13:
                    kr.sendText(msg.to,"changed")
                else:
                    wait["cName"] = n
                    kr.sendText(msg.to,"changed to\n\n" + n)
         #-------------Fungsi Change Clock Finish-----------------#

#--------------------#

            elif "Yud lirik " in msg.text.lower():
                songname = msg.text.replace("aa lirik ","")
                params = {"songname":songname}
                r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/' + urllib.urlencode(params))
                data = r.text
                data = json.loads(data)
                for song in data:
                    kr.sendText(msg.to, 'Tunggu....')
                    kr.sendText(msg.to,song[5])
                    print "[Command] Lirik"


            elif msg.text in ["Yud gcreator"]:
                if msg.toType == 2:
                    msg.contentType = 13
                    ginfo = kr.getGroup(msg.to)
                    gCreator = ginfo.creator.mid
                    try:
                        msg.contentMetadata = {'mid': gCreator}
                        gCreator1 = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                        kr.sendText(msg.to, "Group Creator : " + gCreator1)
                        kr.sendMessage(msg)

            elif "kedapkedip " in msg.text.lower():
                txt = msg.text.replace("kedapkedip ", "")
                kr.kedapkedip(msg.to,txt)

#--------------ListGroup------------------#
            elif msg.text in ["List grup"]:
              if msg.from_ in admin:
                gid = kr.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[🛫] %s\n" % (kr.getGroup(i).name +"→["+str(len(kr.getGroup(i).members))+"]")
                    kr.sendText(msg.to,"▒▒▓█[List Grup]█▓▒▒\n"+ h +"Total Group ="+"["+str(len(gid))+"]")





















#-------------------#

            elif "Steal dp @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Steal dp @","")
                _nametarget = _name.rstrip(' ')
                gs = kr.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                    kr.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = kr.getContact(target)
                            path = "http://dl.profile.line-cdn.net/" + contact.pictureStatus
                            kr.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"


            elif "Steal home @" in msg.text:
                print "[Command]dp executing"
                _name = msg.text.replace("Steal home @","")
                _nametarget = _name.rstrip(' ')
                gs = kr.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   kr.sendText(msg.to,"Contact not found")
                else:
                    for target in targets:
                        try:
                            contact = kr.getContact(target)
                            cu = kr.channel.getCover(target)
                            path = str(cu)
                            kr.sendImageWithURL(msg.to, path)
                        except:
                            pass
                print "[Command]dp executed"

#-----------------------------------------------
            elif "Yud say " in msg.text:
                 psn = msg.text.replace("aa say ","")
                 tts = gTTS(psn, lang='id', slow=False)
                 tts.save('tts.mp3')
                 kr.sendAudio(msg.to, 'tts.mp3')

#-----------------------------------------------

            elif 'Yud musik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('aa musik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        kr.sendText(msg.to, hasil)
                        kr.sendText(msg.to, "Please Wait for audio...")
                        kr.sendAudioWithURL(msg.to, song[4])
                except Exception as njer:
                        kr.sendText(msg.to, str(njer))

            elif 'lirik ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('lirik ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(param))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = song[5]
                        kr.sendText(msg.to, hasil)
                except Exception as njer:
                        kr.sendText(msg.to, str(njer))

            elif "Gbc " in msg.text:
                if msg.from_ in admin:
                    bctxt = msg.text.replace("Gbc ", "")
                    n = kr.getGroupIdsJoined()
                    for manusia in n:
                        kr.sendText(manusia, (bctxt))

            elif "Cbc " in msg.text:
                if msg.from_ in admin:
                    bctxt = msg.text.replace("Cbc ", "")
                    t = kr.getAllContactIds()
                    for manusia in t:
                        kr.sendText(manusia, (bctxt))

#--------------------------------- TRANSLATE --------------------------------
            elif "tren" in msg.text:
                txt = msg.text.replace("tren","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'en')
                    kr.sendText(msg.to,trs)
                    print '[Command] Translate EN'
                except:
                    kr.sendText(msg.to,'Error.')

            elif "trid " in msg.text:
                txt = msg.text.replace("trid ","")
                try:
                    gs = goslate.Goslate()
                    trs = gs.translate(txt,'id')
                    kr.sendText(msg.to,trs)
                    print '[Command] Translate ID'
                except:
                    kr.sendText(msg.to,'Error.')

	#-----------KERANG---------#
            elif "Apakah " in msg.text:
                tanya = msg.text.replace("Apakah ","")
                jawab = ("Iya","Tidak")
                jawaban = random.choice(jawab)
                tts = gTTS(text=jawaban, lang='id')
                tts.save('tts.mp3')
                kr.sendAudio(msg.to,'tts.mp3')

#----------------------
            elif "Dosa @" in msg.text:
                tanya = msg.text.replace("Dosa @","")
                jawab = ("60%","70%","80%","90%","100%","Tak terhingga")
                jawaban = random.choice(jawab)
                kr.sendText(msg.to,"Dosanya " + tanya + "adalah " + jawaban + " Banyak banyak tobat Nak ")
#----------------------
            elif "Pahala @" in msg.text:
                tanya = msg.text.replace("Pahala @","")
                jawab = ("0%","20%","40%","50%","60%","Tak ada")
                jawaban = random.choice(jawab)
                kr.sendText(msg.to,"Pahalanya " + tanya + "adalah " + jawaban + "\nTobatlah nak")

	#-------------------------------#

            elif "Steal group" in msg.text:
                   group = kr.getGroup(msg.to)
                   path =("http://dl.profile.line-cdn.net/" + group.pictureStatus)
                   kr.sendImageWithURL(msg.to, path)


         #-------------Fungsi Jam Update Start---------------------#            
            elif msg.text in ["Jam Update"]:
                if wait["clock"] == True:
                    now2 = datetime.now()
                    nowT = datetime.strftime(now2,"(%H:%M)")
                    profile = kr.getProfile()
                    profile.displayName = wait["cName"] + nowT
                    kr.updateProfile(profile)
                    kr.sendText(msg.to,"Sukses update")
                else:
                    kr.sendText(msg.to,"Aktifkan jam terlebih dulu")
         #-------------Fungsi Jam Update Finish-------------------#
            elif msg.text in ["Yud cctv"]:
                if msg.toType == 2:
                    kr.sendText(msg.to, "Set reading point\nSilahkan ketik 「aa intip」")
                    try:
                        del wait2['readPoint'][msg.to]
                        del wait2['readMember'][msg.to]
                    except:
                        pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        print "Lurkset"

            elif msg.text in ["Yud intip"]:
                if msg.toType == 2:
                    print "\nSider check aktif..."
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                print rom
                                chiya += rom[1] + "\n"
                                kr.sendText(msg.to, "Pembaca:\n_________________________________%s\n\nSidernya:\n_________________________________\n%s\n\n_________________________________\nIn the last seen point:\n[%s]\n_________________________________" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                                print "\nReading Point Set..."
                                try:
                                    del wait2['readPoint'][msg.to]
                                    del wait2['readMember'][msg.to]
                                except:
                                    pass
                                    wait2['readPoint'][msg.to] = msg.id
                                    wait2['readMember'][msg.to] = ""
                                    wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                                    wait2['ROM'][msg.to] = {}
                                    print "lukers"
                                    kr.sendText(msg.to, "Auto set reading point\nSilahkan ketik 「aa intip」")
                                else:
                                    kr.sendText(msg.to, "Ketik 「aa cctv」 dulu kaka...\nHehe")

         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["Yud masuk"]:
                if msg.from_ in admin:
                    G = kr.getGroup(msg.to)
                    ginfo = kr.getGroup(msg.to)
                    G.preventJoinByTicket = False
                    kr.updateGroup(G)
                    invsend = 0
                    Ticket = kr.reissueGroupTicket(msg.to)
                    kr.acceptGroupInvitationByTicket(msg.to,Ticket)
                    time.sleep(0.1)
                    G = kr.getGroup(msg.to)
                    G.preventJoinByTicket = True
                    kr.updateGroup(G)
                    print "Bot Complete"
                    G.preventJoinByTicket(G)
                    kr.updateGroup(G)

    #----------------------Fungsi Join Group Finish---------------#

    #-------------Fungsi Leave Group Start---------------#

            elif msg.text in ["Yud bye"]:
                if msg.toType == 2:
                    ginfo = kr.getGroup(msg.to)
                    try:
                        kr.leaveGroup(msg.to)
                    except:
                        pass
    #-------------Fungsi Leave Group Finish---------------#

    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Yud tagall"]:
                group = kr.getGroup(msg.to)
                nama = [contact.mid for contact in group.members]

                cb = ""
                cb2 = ""
                strt = int(0)
                akh = int(0)
                for md in nama:
                    akh = akh + int(6)

                    cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                    strt = strt + int(7)
                    akh = akh + 1
                    cb2 += "@nrik \n"

                cb = (cb[:int(len(cb)-1)])
                msg.contentType = 0
                msg.text = cb2
                msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}
                try:
                    kr.sendMessage(msg)
                except Exception as error:
                    print error
    #-------------Fungsi Tag All Finish---------------#

         #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Killban"]:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        group = kr.getGroup(msg.to)
                        gMembMids = [contact.mid for contact in group.members]
                        matched_list = []
                        for tag in wait["blacklist"]:
                            matched_list+=filter(lambda str: str == tag, gMembMids)
                        if matched_list == []:
                            kr.sendText(msg.to,"Selamat tinggal")
                            kr.sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
                            return
                        for jj in matched_list:
                            try:
                                klist=[kr]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[jj])
                                print (msg.to,[jj])
                            except:
                                pass
         #----------------Fungsi Banned Kick Target Finish----------------------#                

            elif "Cleanse" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        print "ok"
                        _name = msg.text.replace("Cleanse","")
                        gs = kr.getGroup(msg.to)
                        kr.sendText(msg.to,"maaf kalo gak sopan")
                        kr.sendText(msg.to,"makasih semuanya..")
                        kr.sendText(msg.to,"hehehhehe")
                        msg.contentType = 13
                        msg.contentMetadata = {'mid': mid}
                        kr.sendMessage(msg)
                        targets = []
                        for g in gs.members:
                            if _name in g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            kr.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                              if target not in Bots:
                                try:
                                    klist=[kr]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    kr.sendText(msg.to,"Group cleanse")

        #----------------Fungsi Kick User Target Start----------------------#
            elif "Nk " in msg.text:
                if msg.from_ in admin:
                    nk0 = msg.text.replace("Nk ","")
                    nk1 = nk0.lstrip()
                    nk2 = nk1.replace("@","")
                    nk3 = nk2.rstrip()
                    _name = nk3
                    gs = kr.getGroup(msg.to)
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
                                klist=[kr]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                kr.sendText(msg.to,"Kasian Di Kick....")
                                kr.sendText(msg.to,"Kasihan Bangeet haha")
        #----------------Fungsi Kick User Target Finish----------------------#      
            elif "Blacklist @ " in msg.text:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = kr.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            kr.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    kr.sendText(msg.to,"Succes ")
                                except:
                                    kr.sendText(msg.to,"error")
            
            #----------------Fungsi Banned User Target Start-----------------------#
            elif "Ban @" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        print "[Banned] Sukses"
                        _name = msg.text.replace("Ban @","")
                        _nametarget = _name.rstrip('  ')
                        gs = kr.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            kr.sendText(msg.to,"Dilarang Banned Bot")
                            kr.sendText(msg.to,"Dilarang Banned Bot")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    kr.sendText(msg.to,"Akun telah sukses di banned")
                                except:
                                    kr.sendText(msg.to,"Error")
            #----------------Fungsi Banned User Target Finish-----------------------# 
            
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
                if msg.from_ in admin:
                    if msg.toType == 2:
                        print "[Unban] Sukses"
                        _name = msg.text.replace("Unban @","")
                        _nametarget = _name.rstrip('  ')
                        gs = kr.getGroup(msg.to)
                        targets = []
                        for g in gs.members:
                            if _nametarget == g.displayName:
                                targets.append(g.mid)
                        if targets == []:
                            kr.sendText(msg.to,"Tidak Ditemukan.....")
                            kr.sendText(msg.to,"Tidak Ditemukan.....")
                        else:
                            for target in targets:
                                try:
                                    del wait["blacklist"][target]
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    kr.sendText(msg.to,"Akun Bersih Kembali")
                                except:
                                    kr.sendText(msg.to,"Error")
           #----------------Fungsi Unbanned User Target Finish-----------------------#
           
        #-------------Fungsi Spam Start---------------------#
            elif msg.text in ["Up","up","Up Chat","Up chat","up chat","Upchat","upchat"]:
                if msg.from_ in admin:
                    kr.sendText(msg.to,"Kita nge-spam Woy!")
                    kr.sendText(msg.to,"Woy 􀜁􀅔XD􏿿")
                    kr.sendText(msg.to,"Woy 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔XD􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔XD􏿿")
                    kr.sendText(msg.to,"Kita nge-spam Woy!")
                    kr.sendText(msg.to,"Woy 􀜁􀅔XD􏿿")
                    kr.sendText(msg.to,"Woy 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔XD􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔XD􏿿")
                    kr.sendText(msg.to,"Kita nge-spam Woy!")
                    kr.sendText(msg.to,"Woy 􀜁􀅔XD􏿿")
                    kr.sendText(msg.to,"Woy 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔XD􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔XD􏿿")
                    kr.sendText(msg.to,"Kita nge-spam Woy!")
                    kr.sendText(msg.to,"Woy 􀜁􀅔XD􏿿")
                    kr.sendText(msg.to,"Woy 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔XD􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔XD􏿿")
                    kr.sendText(msg.to,"Kita nge-spam Woy!")
                    kr.sendText(msg.to,"Woy 􀜁􀅔XD􏿿")
                    kr.sendText(msg.to,"Woy 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔haha􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔XD􏿿")
                    kr.sendText(msg.to,"Up 􀜁􀅔XD􏿿")
                    kr.sendText(msg.to,"MAKASIH SEMUA 􀜁􀅔XD􏿿")
        #-------------Fungsi Spam Finish---------------------#

        #-------------Fungsi Broadcast Start------------#
            elif msg.text in ["join"]:
                if msg.from_ in admin:
                    kr.sendText(msg.to,"join")
       #--------------Fungsi Broadcast Finish-----------#

            elif msg.text in ["hai"]:
                kr.sendText(msg.to,"Hai 􀜁􀅔Har Har􏿿")
                kr.sendText(msg.to,"Hai 􀜁􀅔Har Har􏿿")

#-----------------------------------------------

            elif msg.text in ["Yud creator"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': "uecc57cb55f480ee2a45d81434a9b864d"}
                kr.sendMessage(msg)
            elif msg.text in ["bobo ah","Bobo dulu ah"]:
                kr.sendText(msg.to,"Have a nice dream  􀜁􀅔Har Har􏿿")
                kr.sendText(msg.to,"Have a nice dream  􀜁􀅔Har Har􏿿")
                kr.sendText(msg.to,"Have a nice dream  􀜁􀅔Har Har􏿿")

            elif msg.text in ["welcome"]:
                kr.sendText(msg.to,"Selamat datang")
                kr.sendText(msg.to,"Jangan nakal ok!")
#-----------------------------------------------
            elif msg.text in ["PING","Ping","ping"]:
                kr.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kr.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
                kr.sendText(msg.to,"PONG 􀨁􀄻double thumbs up􏿿􀜁􀅔Har Har􏿿")
#-----------------------------------------------

       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["test","Aa","AA"]:
                kr.sendText(msg.to,"Test")
                kr.sendText(msg.to,"Test")
                kr.sendText(msg.to,"Satu tetes")
                kr.sendText(msg.to,"Nah Hati-hati")
                kr.sendText(msg.to,"Hahahaha")
      #-------------Fungsi Respon Finish---------------------#

       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["sp","speed","Speed","Sp"]:
                start = time.time()
                kr.sendText(msg.to, "Tunggu...")
                elapsed_time = time.time() - start
                kr.sendText(msg.to, "%sseconds" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#

      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["Ban"]:
                if msg.from_ in admin:
                    wait["wblacklist"] = True
                    kr.sendText(msg.to,"send contact")
                    
            elif msg.text in ["Unban"]:
                if msg.from_ in admin:
                    wait["dblacklist"] = True
                    kr.sendText(msg.to,"send contact")
                    
      #-------------Fungsi Banned Send Contact Finish------------------#
      
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["Banlist"]:
                if wait["blacklist"] == {}:
                    kr.sendText(msg.to,"Tidak Ada Akun Terbanned")
                else:
                    kr.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +kr.getContact(mi_d).displayName + "\n"
                    kr.sendText(msg.to,mc)
      #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in ["Cek ban"]:
                if msg.toType == 2:
                    group = kr.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    kr.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
                if msg.toType == 2:
                    group = kr.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kr.sendText(msg.to,"There was no blacklist user")
                        kr.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        kr.kickoutFromGroup(msg.to,[jj])
                        kr.kickoutFromGroup(msg.to,[jj])
                        kr.kickoutFromGroup(msg.to,[jj])
                        kr.kickoutFromGroup(msg.to,[jj])
                    kr.sendText(msg.to,"Blacklist emang pantas tuk di usir")
                    kr.sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["Clear"]:
                if msg.toType == 2:
                    group = kr.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        kr.cancelGroupInvitation(msg.to,[_mid])
                    kr.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "random: " in msg.text:
              if msg.from_ in admin:
                if msg.toType == 2:
                    strnum = msg.text.replace("random: ","")
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    try:
                        num = int(strnum)
                        group = kr.getGroup(msg.to)
                        for var in range(0,num):
                            name = "".join([random.choice(source_str) for x in xrange(10)])
                            time.sleep(0.01)
                            group.name = name
                            kr.updateGroup(group)
                    except:
                        kr.sendText(msg.to,"Error")
            elif "albumat'" in msg.text:
                try:
                    albumtags = msg.text.replace("albumat'","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    kr.createAlbum(gid,name)
                    kr.sendText(msg.to,name + "created an album")
                except:
                    kr.sendText(msg.to,"Error")
            elif "fakecat'" in msg.text:
                try:
                    source_str = 'abcdefghijklmnopqrstuvwxyz1234567890@:;./_][!&%$#)(=~^|'
                    name = "".join([random.choice(source_str) for x in xrange(10)])
                    anu = msg.text.replace("fakecat'","")
                    kr.sendText(msg.to,str(kr.channel.createAlbum(msg.to,name,anu)))
                except Exception as e:
                    try:
                        kr.sendText(msg.to,str(e))
                    except:
                        pass

        if op.type == 55:
            try:
                if op.param1 in wait2['readPoint']:
                    Name = kr.getContact(op.param2).displayName
                    if Name in wait2['readMember'][op.param1]:
                        pass
                    else:
                        wait2['readMember'][op.param1] += "\n・ " + Name + datetime.today().strftime(' [%d - %H:%M:%S]')
                        wait2['ROM'][op.param1][op.param2] = "・ " + Name
                        wait2['setTime'][msg.to] = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
                else:
                    pass
            except:
                pass

        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                nowT = datetime.strftime(now2,"(%H:%M)")
                profile = kr.getProfile()
                profile.displayName = wait["cName"]
                kr.updateProfile(profile)

                profile2 = kr.getProfile()
                profile2.displayName = wait["cName2"]
                kr.updateProfile(profile2)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = kr.fetchOps(kr.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(kr.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            kr.Poll.rev = max(kr.Poll.rev, Op.revision)
            bot(Op)
