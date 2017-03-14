import urllib
from bs4 import BeautifulSoup
import string
import pandas as pd

def active_player_list():
    alf_range=string.ascii_lowercase
    player_info=[]
    for j in range(0,26):
      try:
          page = urllib.request.urlopen('http://basketball-reference.com/players/' + alf_range[j]).read()
          soup = BeautifulSoup(page,"lxml")
          rows = soup.findAll('tr')
          for i in range(1,len(rows)):
              r_str=str(rows[i])
              url = "http://basketball-reference.com" + r_str[r_str.find("a href")+8:r_str.find(".html")+5]
              rs1=r_str[r_str.find(".html"):len(r_str)]
              name = rs1[rs1.find(">")+1:rs1.find("<")]
              rs2 = rs1[rs1.find("class"):len(rs1)]
              nba_from = int(rs2[rs2.find(">")+1:rs2.find("<")])
              rs3 = rs2[rs2.find("class",rs2.find("class")+1):len(rs2)]
              nba_to = int(rs3[rs3.find(">")+1:rs3.find("<")])
              rs4 = rs3[rs3.find("class",rs3.find("class")+1):len(rs3)]
              pos = rs4[rs4.find(">")+1:rs4.find("<")]
              rs5 = rs4[rs4.find("class",rs4.find("class")+1):len(rs4)]
              ht = rs5[rs5.find(">")+1:rs5.find("<")]
              rs6 = rs5[rs5.find("class",rs5.find("class")+1):len(rs5)]
              wt = rs6[rs6.find(">")+1:rs6.find("<")]
              rs7 = rs6[rs6.find("csk"):len(rs6)]
              dob = rs7[rs7.find("=")+2:rs7.find("=")+10]
              player_info.append([name,url,nba_from,nba_to,pos,ht,wt,dob])
      except:
          print("no players have last names that start with: " + alf_range[j])

    for i in player_info:
      if i[3]==max([sublist[3] for sublist in player_info]):
          i.append("Active")
      else:
          i.append("Retired")

    active_list = []
    for i in player_info:
      if i[8]=='Active':
          active_list.append(i)

    pinfo = pd.DataFrame(player_info, columns=['player','url','dt_from','dt_to','pos','ht','wt','dob','status'])
    active = pinfo[pinfo['status']=="Active"]
    return active
