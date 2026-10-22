import json, html, math, shutil
from pathlib import Path
R=Path(__file__).resolve().parent
O=R/'Freeform_Previews'; O.mkdir(exist_ok=True)
old=R/'Data_in_Healthcare.excalidraw'
backup=R/'Archive'/'Data_in_Healthcare_framed_arabic.excalidraw'
if old.exists() and not backup.exists():
    backup.parent.mkdir(exist_ok=True); shutil.copy2(old,backup)
E=[]
INK='#243047'; PURPLE='#7950B8'; BLUE='#32799C'; GREEN='#287B62'; ORANGE='#AA692C'
def shape(t,x,y,w,h,**kw):
    n=len(E)+1
    e=dict(id=f'free_{n:04}',type=t,x=x,y=y,width=w,height=h,angle=0,strokeColor=INK,backgroundColor='transparent',fillStyle='solid',strokeWidth=2,strokeStyle='solid',roughness=1.4,opacity=100,groupIds=[],frameId=None,roundness=None,seed=4200+n,version=1,versionNonce=8400+n,isDeleted=False,boundElements=[],updated=1792530000000,link=None,locked=False)
    e.update(kw);E.append(e);return e
def txt(s,x,y,w=600,size=32,c=INK,align='center'):
    return shape('text',x,y,w,len(s.split('\n'))*size*1.3,text=s,originalText=s,fontSize=size,fontFamily=1,textAlign=align,verticalAlign='top',containerId=None,autoResize=False,lineHeight=1.3,strokeColor=c,roughness=0)
def oval(x,y,w,h,fill='transparent',c=PURPLE): return shape('ellipse',x,y,w,h,backgroundColor=fill,strokeColor=c)
def line(points,c=INK,width=2,arrow=False):
    x,y=points[0];ps=[[a-x,b-y] for a,b in points]
    return shape('arrow' if arrow else 'line',x,y,max(a for a,b in ps)-min(a for a,b in ps),max(b for a,b in ps)-min(b for a,b in ps),points=ps,strokeColor=c,strokeWidth=width,roundness={'type':2},lastCommittedPoint=None,startBinding=None,endBinding=None,startArrowhead=None,endArrowhead='arrow' if arrow else None,elbowed=False)
def note(s,x,y,w=500,c=INK,size=30):return txt(s,x,y,w,size,c)
def bubble(title,sub,x,y,w=540,h=210,c=BLUE,fill='#ECF6FA'):
    oval(x,y,w,h,fill,c);txt(title,x+35,y+45,w-70,35,c);txt(sub,x+35,y+110,w-70,26)
def heading(n,s,x,y,w=1000):
    txt(f'{n}  {s}',x,y,w,48);line([(x+100,y+72),(x+w*.6,y+78),(x+w-100,y+69)],PURPLE,4)
def person(x,y):
    oval(x+50,y,90,90,'transparent',INK);line([(x+95,y+92),(x+95,y+250)]);line([(x+5,y+155),(x+95,y+125),(x+185,y+160)]);line([(x+95,y+250),(x+15,y+340)]);line([(x+95,y+250),(x+180,y+340)])

# An open, winding map: no frames or slide backgrounds.
txt('DATA IN HEALTHCARE',1820,40,1900,88,PURPLE)
txt('From everyday problems to better decisions',1920,160,1700,42)
note('Follow the questions.\nKeep asking: what do we still not know?',2350,250,850,29 if False else INK)

heading('1','Start with a person',100,330,1100)
person(160,520);note('Needs a regular\nmedicine',70,895,400)
shape('rectangle',650,510,450,330,roundness={'type':3},backgroundColor='#F2F9F4')
line([(700,510),(875,420),(1050,510)]);txt('HEALTH CENTRE',670,565,410,32,GREEN)
line([(855,635),(855,725)],GREEN,7);line([(810,680),(900,680)],GREEN,7)
line([(375,700),(500,745),(630,700)],BLUE,3,True)
oval(650,900,470,160,'#FFF2DA',ORANGE);txt('Medicine unavailable',680,950,410,31,ORANGE)
note('Demand? Delivery?\nDistribution? Recording?',230,1130,800,ORANGE,34)
note('Before choosing a solution,\nwhat would you want to know?',140,1290,1050,INK,38)

heading('2','Zoom out',100,1630,1100)
bubble('One person','Access / cost / continuity',400,1790,500,210)
bubble('A facility','Stock / queues / records',70,2150,520,210,c=GREEN,fill='#ECF8EF')
bubble('A community','Who never reached care?',700,2180,540,210,c=ORANGE,fill='#FFF5DF')
line([(530,2010),(390,2060),(330,2140)],GREEN,3,True)
line([(790,2010),(930,2050),(970,2170)],ORANGE,3,True)
note('Transport    Purchasing    Budgets\nWater    Education    Public policy',120,2520,1150,PURPLE,36)
line([(350,2380),(500,2480)],PURPLE,3,True);line([(1000,2410),(900,2480)],PURPLE,3,True)
note('Your role is one part of a connected system.',100,2710,1150,INK,31)

heading('3','Make observations useful',1700,470,1500)
note('A clear question',1750,630,500,BLUE,37)
line([(2240,670),(2380,620),(2520,665)],BLUE,3,True)
note('A small, organized table',2500,630,700,BLUE,37)
shape('rectangle',1860,790,1330,340,roundness={'type':3})
line([(1860,900),(3190,900)]);line([(1860,1010),(3190,1010)]);line([(2300,790),(2300,1130)])
txt('Facility',1900,825,350,31);txt('Recorded unsuccessful attempts',2350,825,790,30)
txt('A',1900,935,350,36);txt('40',2350,935,790,36,BLUE)
txt('B',1900,1045,350,36);txt('30',2350,1045,790,36,BLUE)
note('One row = one facility, one month\nOne column = one recorded attribute',1900,1190,1250,INK,32)
note('Same medicine / same month / synthetic data',1900,1300,1250,ORANGE,26)
note('Question → collect → check → compare\nExplain → act → review',1830,1430,1400,GREEN,34)

heading('4','Your turn to investigate',3650,390,1600)
oval(3700,620,560,300,'#ECF6FA',BLUE);txt('Facility A\n40 unsuccessful attempts',3740,690,480,38,BLUE)
oval(4580,680,560,300,'#FFF5DF',ORANGE);txt('Facility B\n30 unsuccessful attempts',4620,750,480,38,ORANGE)
note('Which would you investigate first?\nWhat information is missing?',3750,1100,1350,INK,42)
line([(4230,990),(4450,1050),(4540,1100)],PURPLE,3,True)
note('Pause here. Discuss before revealing the totals.',3780,1280,1300,PURPLE,29)

# Central anchor and orbiting analytics questions.
heading('5','Four types of analytics',1900,1670,1650)
oval(2420,2380,1000,370,'#F1EBFF',PURPLE)
txt('REDUCE\nUNCERTAINTY',2490,2440,860,61,PURPLE)
line([(2590,2645),(2880,2670),(3250,2640)],PURPLE,5)
bubble('What happened?','Descriptive Analytics',1710,1930,710,250,BLUE)
note('Where and how often was\nmedicine unavailable?',1750,2210,630,BLUE,29)
bubble('What might explain it?','Diagnostic Analytics',3500,1960,760,250,ORANGE,'#FFF5DF')
note('Do delivery records support\na possible explanation?',3550,2250,660,ORANGE,29)
bubble('What might happen next?','Predictive Analytics',1690,2940,760,250,BLUE)
note('Estimate next month’s demand\nunder stated assumptions.',1740,3230,660,BLUE,29)
bubble('What should we do?','Prescriptive Analytics',3490,2960,760,250,GREEN,'#ECF8EF')
note('Compare feasible options:\ngoal + budget + constraints.',3540,3250,660,GREEN,29)
line([(2460,2430),(2510,2290),(2370,2150)],BLUE,3,True)
line([(3360,2430),(3500,2360),(3690,2225)],ORANGE,3,True)
line([(2470,2720),(2260,2810),(2160,2920)],BLUE,3,True)
line([(3350,2730),(3550,2830),(3720,2940)],GREEN,3,True)
note('A possible cause is not a proven cause.\nA forecast is not a guarantee.',2450,2810,940,ORANGE,27)
note('Good analysis also reveals what we still do not know.',2200,3430,1450,PURPLE,34)
src=txt('Source: KMS Technology • Healthcare analytics',2420,3500,1000,22,BLUE)
src['link']='https://kms-technology.com/blog/data-analytics-in-healthcare/'

heading('6','Local questions. Global relevance.',4550,1670,1600)
bubble('Sudan: reporting gaps','WHO report / March–April 2025',4560,1900,800,250)
note('No report ≠ zero events',4650,2200,620,ORANGE,39)
note('Report → review → investigate → respond',4520,2330,1100,BLUE,31)
bubble('Who disappears in an average?','WHO Health Inequality Monitor',5190,2580,850,260,GREEN,'#ECF8EF')
line([(5600,2870),(5440,2950),(5300,3040)],GREEN,3,True)
line([(5660,2870),(5860,2940),(6020,3040)],GREEN,3,True)
oval(5060,3060,480,170,'transparent',GREEN);txt('Group A',5100,3110,400,35)
oval(5780,3060,480,170,'transparent',GREEN);txt('Group B',5820,3110,400,35)
note('Check coverage, dates, definitions\nand the people missing from the data.',4650,3370,1500,INK,33)
src=txt('WHO Sudan report (historical example)',4550,2460,1100,22,BLUE);src['link']='https://cdn.who.int/media/docs/default-source/2021-dha-docs/20250527_sudan-emergency-sitrep-10.pdf'
src=txt('WHO inequality data • conceptual sketch, no actual statistics',4800,3500,1500,22,GREEN);src['link']='https://www.who.int/data/inequality-monitor/data'

heading('7','Where could you contribute?',100,3120,1500)
oval(350,3400,850,260,'#F1EBFF',PURPLE);txt('Domain knowledge\n+ analytical skills',400,3450,750,45,PURPLE)
for x,y,title,sub in [(20,3890,'Humanitarian reporting','Check completeness + timeliness'),(1010,3850,'Supply & operations','Investigate recurring shortages'),(500,4310,'Research support','Document missingness + cleaning')]:
    bubble(title,sub,x,y,700,220,GREEN,'#ECF8EF')
line([(450,3670),(310,3750),(310,3870)],GREEN,3,True)
line([(1130,3650),(1350,3720),(1350,3830)],GREEN,3,True)
line([(780,3690),(830,4070),(830,4290)],GREEN,3,True)
note('Also: digital health / quality / policy / other sectors\nDifferent paths require different further skills.',100,4630,1550,INK,29)

heading('8','Build something useful',2100,3820,1700)
for x,y,a,b in [(2080,4010,'Spreadsheets','Organize + check'),(3060,4140,'SQL','Retrieve + connect'),(2180,4460,'Visualization','Make comparisons clear'),(3290,4600,'Statistics','Judge variation + evidence')]:
    bubble(a,b,x,y,700,210,BLUE)
line([(2800,4110),(2930,4120),(3040,4230)],BLUE,3,True)
line([(3180,4380),(3000,4470),(2890,4520)],BLUE,3,True)
line([(2890,4580),(3080,4620),(3270,4700)],BLUE,3,True)
note('Python, if included: repeat a checked analysis\nProject: question + evidence + limits + recommendation',2200,4890,1800,GREEN,31)

heading('9','Your first step',4500,3920,1550)
note('I want to understand…',4650,4140,1150,PURPLE,48)
line([(4600,4290),(5200,4310),(5940,4290)],PURPLE,2)
note('I would need data about…',4650,4410,1150,BLUE,48)
line([(4600,4560),(5200,4580),(5940,4560)],BLUE,2)
note('My first useful output would be…',4520,4680,1450,GREEN,43)
line([(4600,4830),(5200,4850),(5940,4830)],GREEN,2)
note('Ask → check → explain → act → review',4500,4970,1550,INK,34)

# Answer branch well away from the opening activity view.
heading('4B','Now reveal the denominators',6650,460,1500)
bubble('A: 40 / 200 = 20%','More unsuccessful attempts',6680,710,700,250,BLUE)
bubble('B: 30 / 60 = 50%','Higher unsuccessful proportion',7520,1030,700,250,ORANGE,'#FFF5DF')
note('Different questions → different comparisons',6700,1430,1500,PURPLE,39)
note('Evidence: B has the higher recorded proportion.\nHypothesis: delivery delays may contribute.\nNext step: check stock and delivery records.',6660,1600,1600,INK,34)
note('Synthetic example. Attempts are not unique people.\nThis alone does not prove a cause or the best allocation.',6690,1850,1550,ORANGE,29)

data={'type':'excalidraw','version':2,'source':'https://excalidraw.com','elements':E,'appState':{'viewBackgroundColor':'#FFFEFA','gridSize':None,'zoom':{'value':0.7},'scrollX':50,'scrollY':-250},'files':{}}
old.write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')
assert not any(e['type']=='frame' for e in E)
assert not any('\u0600'<=c<='\u06ff' for e in E for c in e.get('text',''))

# SVG preview: editable deliverable uses native Excalidraw sketch rendering.
svg=['<svg xmlns="http://www.w3.org/2000/svg" width="8400" height="5250" viewBox="0 0 8400 5250"><rect width="100%" height="100%" fill="#FFFEFA"/>']
for e in E:
    x,y,w,h=e['x'],e['y'],e['width'],e['height'];c=e['strokeColor'];t=e['type'];fill=e['backgroundColor'];fill='none' if fill=='transparent' else fill
    if t=='text':
        size=e['fontSize']; anchor={'left':'start','center':'middle','right':'end'}[e['textAlign']]; xx=x+({'left':0,'center':w/2,'right':w}[e['textAlign']])
        for i,s in enumerate(e['text'].split('\n')):svg.append(f'<text x="{xx}" y="{y+size+i*size*1.3}" text-anchor="{anchor}" fill="{c}" font-family="Comic Sans MS, cursive" font-size="{size}">{html.escape(s)}</text>')
    elif t=='ellipse':svg.append(f'<ellipse cx="{x+w/2}" cy="{y+h/2}" rx="{w/2}" ry="{h/2}" fill="{fill}" stroke="{c}" stroke-width="{e["strokeWidth"]}"/>')
    elif t=='rectangle':svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="14" fill="{fill}" stroke="{c}" stroke-width="2"/>')
    else:
        p=[(x+a,y+b) for a,b in e['points']];d=f'M {p[0][0]} {p[0][1]} '
        if len(p)==3:d+=f'Q {p[1][0]} {p[1][1]} {p[2][0]} {p[2][1]}'
        else:d+=' '.join(f'L {a} {b}' for a,b in p[1:])
        svg.append(f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{e["strokeWidth"]}" stroke-linecap="round"/>')
        if t=='arrow':
            a,b=p[-2],p[-1];ang=math.atan2(b[1]-a[1],b[0]-a[0]);ps=[(b[0]-20*math.cos(ang+z),b[1]-20*math.sin(ang+z)) for z in [-.45,.45]]
            svg.append(f'<path d="M {ps[0][0]} {ps[0][1]} L {b[0]} {b[1]} L {ps[1][0]} {ps[1][1]}" fill="none" stroke="{c}" stroke-width="3"/>')
svg.append('</svg>');(O/'Map.svg').write_text(''.join(svg),encoding='utf-8')
print(f'Built freeform English board: {len(E)} editable elements, no frames.')
