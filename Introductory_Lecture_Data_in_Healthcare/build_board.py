import json, html
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'Board_Previews'
OUT.mkdir(exist_ok=True)
elements, scenes = [], []
INK, BLUE, AMBER, GREEN = '#17324D', '#2563EB', '#B46A12', '#16785B'
PALE, GOLD, MINT = '#EFF5FF', '#FFF5DE', '#EAF7F1'
W,H = 1600,1000
current = None

def el(kind,x,y,w,h,**kw):
    i = len(elements)+1
    item = dict(id=f'health_{i:04}',type=kind,x=x+current['x'],y=y+current['y'],width=w,height=h,
        angle=0,strokeColor=INK,backgroundColor='transparent',fillStyle='solid',strokeWidth=2,
        strokeStyle='solid',roughness=0,opacity=100,groupIds=[],frameId=current['id'],
        roundness=None,seed=1000+i,version=1,versionNonce=2000+i,isDeleted=False,
        boundElements=[],updated=1792530000000,link=None,locked=False)
    item.update(kw); elements.append(item); return item

def rect(x,y,w,h,fill='#FFFFFF',stroke='#D7E1EB'):
    return el('rectangle',x,y,w,h,backgroundColor=fill,strokeColor=stroke,roundness={'type':3})

def text(s,x,y,w,size=32,color=INK,align='center',link=None):
    return el('text',x,y,w,len(s.split('\n'))*size*1.3,text=s,originalText=s,fontSize=size,
        fontFamily=2,textAlign=align,verticalAlign='top',containerId=None,autoResize=False,
        lineHeight=1.3,strokeColor=color,strokeWidth=1,link=link)

def arrow(x,y,dx,dy,color=BLUE):
    return el('arrow',x,y,abs(dx),abs(dy),points=[[0,0],[dx,dy]],lastCommittedPoint=None,
        startBinding=None,endBinding=None,startArrowhead=None,endArrowhead='arrow',elbowed=False,
        strokeColor=color)

def card(x,y,w,h,title,subtitle='',body='',fill=PALE,color=BLUE):
    rect(x,y,w,h,fill)
    text(title,x+18,y+20,w-36,36,color)
    if subtitle: text(subtitle,x+18,y+75,w-36,23,color)
    if body: text(body,x+22,y+128,w-44,29)

def begin(n,title,sub,time,x=None,y=None):
    global current
    k=n-1 if isinstance(n,int) else 9
    x = (k%3)*1800 if x is None else x
    y = (k//3)*1200 if y is None else y
    current={'id':f'scene_{n}','x':x,'y':y,'name':f'{n} | {title}','key':str(n)}
    scenes.append(current)
    frame=el('frame',0,0,W,H,name=current['name'],frameId=None,strokeColor='#CBD5E1')
    frame['id']=current['id']
    rect(0,0,W,H,'#FFFFFF','#CBD5E1')
    text(f'{n}   /   DATA IN HEALTHCARE',55,30,650,20,BLUE,'left')
    text(time,1250,30,290,20,'#64748B','right')
    text(title,65,85,1470,48)
    text(sub,80,152,1440,24,'#64748B')
    rect(55,918,1490,2,'#D7E1EB','#D7E1EB')
    text('تقليل عدم اليقين • Reduce uncertainty',65,944,800,22,GREEN,'left')
    text('سؤال واضح • دليل قابل للمراجعة',1020,944,515,22,'#64748B','right')

begin(1,'البيانات في الرعاية الصحية','من مشكلة يومية إلى قرار أفضل', '00–05 min')
card(75,260,390,300,'شخص يحتاج الدواء','A person','وصل لاستلام الدواء\nهل سيجده؟')
card(605,260,390,300,'المنشأة الصحية','A facility','طلب • تسجيل • مخزون')
card(1135,260,390,300,'غير متوفر','Unavailable','ما الذي نحتاج معرفته؟',GOLD,AMBER)
arrow(480,410,105,0); arrow(1010,410,105,0)
text('قبل ما نختار الحل، محتاجين نعرف شنو؟',100,620,1400,42)
rect(240,715,1120,128,MINT)
text('نقلل عدم اليقين عشان نختار خطوة على أساس أوضح',270,746,1060,36,GREEN)
text('بداية مشتركة — لا تحتاج لحضور المحاضرات السابقة',150,865,1300,25,'#64748B')

begin(2,'من الفرد إلى المنظومة','نفس المشكلة تظهر على أكثر من مستوى','05–12 min')
for x,title,en,body in [(60,'الفرد','Person','الوصول • التكلفة\nاستمرار الخدمة'),(460,'المنشأة','Facility','المخزون • الانتظار\nالتسجيل'),(860,'المجتمع','Community','من لم يصل؟\nمن غاب عن السجلات؟'),(1260,'الأنظمة','Systems','الشراء • النقل\nالميزانية • السياسات')]:
    card(x,280,280,310,title,en,body)
for x in [350,750,1150]: arrow(x,425,95,0)
text('منو كمان بيأثر على وصول الخدمة؟',100,650,1400,42)
rect(180,745,1240,115,MINT)
text('نفس الأسئلة تمتد إلى الغذاء والمياه والتعليم والنقل',200,778,1200,34,GREEN)

begin(3,'من السؤال إلى الجدول','البيانات = ملاحظات سجلناها للإجابة عن سؤال','12–20 min')
text('أين يتكرر عدم توفر الدواء؟',100,235,1400,40,BLUE)
for y,lab,num in [(330,'المنشأة','محاولات مسجلة غير ناجحة'),(415,'A','40'),(500,'B','30')]:
    rect(220,y,1160,78,PALE if y==330 else '#FFFFFF')
    text(lab,245,y+17,300,30); text(num,590,y+17,750,30)
text('صف واحد = منشأة واحدة خلال شهر واحد',120,625,1360,33)
text('Row / record',180,675,500,23,BLUE); text('Column / variable',920,675,500,23,BLUE)
text('كل عمود يسجل صفة أو قياساً محدداً',850,710,650,25)
text('Question → Collect → Check → Compare → Explain → Act → Review',80,765,1440,28,GREEN)
text('أرقام افتراضية • نفس الدواء ونفس الشهر • الصف لا يمثل مريضاً',80,850,1440,24,AMBER)

begin(4,'دوركم تحللوا','أي منشأة نراجع أولاً؟ وما المعلومة الناقصة؟','20–32 min')
card(170,290,540,330,'المنشأة A','Recorded unsuccessful attempts','',PALE)
text('40',200,430,480,100,BLUE)
card(890,290,540,330,'المنشأة B','Recorded unsuccessful attempts','',PALE)
text('30',920,430,480,100,BLUE)
text('اختاروا إجابة مؤقتة… واذكروا ما تحتاجون معرفته',100,690,1400,38)
text('أكبر عدد؟ أعلى نسبة؟ أم نحتاج معلومات أكثر؟',100,760,1400,33,AMBER)
text('مثال تعليمي افتراضي — انتقل إلى الإطار 4B بعد المناقشة',100,855,1400,24,'#64748B')

begin(5,'أربعة أنواع… لتقليل عدم اليقين','كل نوع يساعدنا نجاوب سؤالاً مختلفاً','32–40 min')
card(65,235,630,235,'حصل شنو؟','Descriptive Analytics • وصفي','أين وكم مرة سُجل عدم التوفر؟')
card(905,235,630,235,'ممكن يكون حصل ليه؟','Diagnostic Analytics • تشخيصي','هل تدعم السجلات فرضية تأخر التوريد؟',GOLD,AMBER)
card(65,650,630,235,'متوقع يحصل شنو؟','Predictive Analytics • تنبؤي','ما الطلب المتوقع تحت افتراضات محددة؟')
card(905,650,630,235,'نعمل شنو؟','Prescriptive Analytics • توجيهي','أي خيار يناسب الهدف والميزانية والقيود؟',MINT,GREEN)
rect(500,510,600,100,MINT,GREEN)
text('تقليل عدم اليقين',520,520,560,36,GREEN)
text('Reduce uncertainty',520,565,560,24,GREEN)
arrow(500,535,-145,-50);arrow(1100,535,145,-50)
arrow(500,585,-145,50);arrow(1100,585,145,50)
text('سبب محتمل ≠ سبب مثبت',65,540,400,25,AMBER)
text('توقع ≠ ضمان',1150,540,385,27,AMBER)
text('حدود الدليل تظل مهمة',600,615,400,21,'#64748B')
text('KMS • Four types of healthcare analytics',55,891,1000,17,'#64748B','left', 'https://kms-technology.com/blog/data-analytics-in-healthcare/')

begin(6,'أثر محلي وعالمي','المعلومات الغائبة جزء من السؤال','40–49 min')
card(65,245,710,550,'السودان: التقارير والإنذار المبكر','WHO • March–April 2025','غياب التقرير لا يعني صفر حالات',PALE)
text('تقرير → مراجعة → تحقيق → استجابة',95,465,650,30,BLUE)
text('?',285,535,270,125,AMBER)
text('هل وصلت البيانات كاملة وفي وقتها؟',90,705,660,29)
card(825,245,710,550,'العالم: من يختفي وراء المتوسط؟','WHO • Health Inequality Monitor','النتيجة العامة قد تخفي اختلافات',MINT,GREEN)
text('نتيجة عامة',1015,465,330,34,GREEN)
arrow(1180,520,-160,75,GREEN);arrow(1180,520,160,75,GREEN)
text('مجموعة أ',850,625,300,35);text('مجموعة ب',1200,625,300,35)
text('نقارن المجموعات ونراجع من لم تُمثله البيانات',850,720,660,26)
text('مثال السودان تاريخي • الرسم العالمي توضيحي بلا إحصاءات فعلية',75,850,1450,25,AMBER)
text('WHO Sudan report',80,890,600,17,BLUE,'left','https://cdn.who.int/media/docs/default-source/2021-dha-docs/20250527_sudan-emergency-sitrep-10.pdf')
text('WHO inequality data',920,890,600,17,GREEN,'right','https://www.who.int/data/inequality-monitor/data')

begin(7,'ممكن أساهم وين؟','معرفة المجال + مهارات التحليل + تواصل واضح','49–58 min')
for x,title,en,body in [(65,'المنظمات والبرامج','Reporting / M&E','أي المناطق تتأخر تقاريرها؟\n\nالناتج: ملخص اكتمال التقارير'),(575,'الإمداد والتشغيل','Supply / Operations','أي أصناف يتكرر نفادها؟\n\nالناتج: مقارنة للمخزون والتواريخ'),(1085,'البحث والبيانات','Research data support','أين البيانات الناقصة؟\n\nالناتج: تقرير جودة وسجل تنظيف')]:
    card(x,275,450,400,title,en,body)
text('صحة رقمية • جودة • سياسات • تحليل في قطاعات أخرى',100,735,1400,34,GREEN)
text('ابدأ بسؤال ونتيجة تستطيع شرحها ومراجعتها',100,805,1400,33)
text('مسارات ممكنة؛ المتطلبات تختلف، وبعض الأدوار تحتاج تدريباً متخصصاً',100,867,1400,23,AMBER)

begin(8,'بداية تقدر تعملها','كل مهارة تساعدك تنتج شيئاً مفيداً','58–65 min')
rows=[('Spreadsheets','أنظم الجدول وأراجع القيم'),('SQL','أستخرج البيانات وأربط الجداول'),('Visualization / Tableau','أوضح المقارنة برسم مفهوم'),('Applied statistics','أقيّم التباين وقوة الدليل'),('Python — if included','أكرر التحليل بعد مراجعته')]
for i,(en,ar) in enumerate(rows):
    y=235+i*91;rect(150,y,1300,80,PALE if i%2==0 else '#FFFFFF');text(en,175,y+20,540,28,BLUE,'left');text(ar,735,y+20,680,30)
rect(150,735,1300,130,MINT)
text('تمرين دقيقتين: سؤالك؟ معلومتان تحتاجهما؟ أول نتيجة؟',175,757,1250,34,GREEN)
text('المشروع: سؤال + تحليل موثق + نتيجة وحدودها + خطوة مقترحة',175,814,1250,25)

begin(9,'خطوتي الجاية','نقاش ثم خطوة شخصية تبدأ بها','65–75 min')
for y,label,en in [(260,'أنا مهتم أفهم…','My question'),(425,'محتاج بيانات عن…','Needed data'),(590,'أول نتيجة ممكن أعملها…','First output')]:
    rect(170,y,1260,135,PALE);text(label,195,y+17,1210,38);text(en,205,y+78,1190,22,BLUE)
text('سؤال → دليل → خطوة → مراجعة النتيجة',150,780,1300,38,GREEN)
text('نقلل عدم اليقين، ونوضح ما لا نعرفه بعد',150,850,1300,34)

begin('4B','العدد والنسبة يجاوبوا سؤالين مختلفين','إظهار الإجابة بعد التصويت والمناقشة','Activity reveal',x=5400,y=1200)
card(80,235,670,245,'المنشأة A','40 / 200 = 20%','أكبر عدد مسجل من المحاولات غير الناجحة')
card(850,235,670,245,'المنشأة B','30 / 60 = 50%','أعلى نسبة مسجلة من المحاولات غير الناجحة',GOLD,AMBER)
for x,title,en,body,fill,col in [(65,'دليل','Evidence','النسبة أعلى في B\nخلال هذا الشهر',PALE,BLUE),(575,'فرضية','Hypothesis','ربما تأخر التوريد\nنحتاج نفحص السجلات',GOLD,AMBER),(1085,'خطوة مقترحة','Proposed action','نراجع التسجيل والمخزون\nقبل اختيار تدخل',MINT,GREEN)]:
    card(x,535,450,265,title,en,body,fill,col)
text('المحاولات ليست أشخاصاً فريدين • من لم يصل لا يظهر في الجدول',90,835,1420,26,AMBER)
text('الأرقام افتراضية؛ المقارنة وحدها لا تثبت السبب أو أفضل توزيع للموارد',90,880,1420,23,'#64748B')

data={'type':'excalidraw','version':2,'source':'https://excalidraw.com','elements':elements,
    'appState':{'viewBackgroundColor':'#EDF2F7','gridSize':None,'zoom':{'value':0.65},'scrollX':50,'scrollY':40},'files':{}}
(ROOT/'Data_in_Healthcare.excalidraw').write_text(json.dumps(data,ensure_ascii=False,indent=2),encoding='utf-8')

def render_scene(scene):
    shapes=[]
    for e in elements:
        if e['frameId']!=scene['id']: continue
        x,y=e['x']-scene['x'],e['y']-scene['y'];w,h=e['width'],e['height'];c=e['strokeColor']
        if e['type']=='text':
            rtl=any('\u0600'<=z<='\u06ff' for z in e['text'])
            s=html.escape(e['text']).replace('\n','<br>')
            shapes.append(f'<div class="txt" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;font-size:{e["fontSize"]}px;line-height:1.3;text-align:{e["textAlign"]};color:{c};direction:{"rtl" if rtl else "ltr"}">{s}</div>')
        elif e['type']=='rectangle':
            shapes.append(f'<div style="position:absolute;left:{x}px;top:{y}px;width:{w}px;height:{h}px;background:{e["backgroundColor"]};border:2px solid {c};border-radius:14px;box-sizing:border-box"></div>')
        elif e['type']=='arrow':
            dx,dy=e['points'][1]
            shapes.append(f'<svg style="position:absolute;inset:0;width:1600px;height:1000px"><defs><marker id="{e["id"]}" markerWidth="10" markerHeight="10" refX="8" refY="3" orient="auto"><path d="M0,0 L0,6 L9,3 z" fill="{c}"/></marker></defs><line x1="{x}" y1="{y}" x2="{x+dx}" y2="{y+dy}" stroke="{c}" stroke-width="3" marker-end="url(#{e["id"]})"/></svg>')
    return '<!doctype html><meta charset="utf-8"><style>body{margin:0;background:white;font-family:Arial,sans-serif}.txt{position:absolute;white-space:nowrap}main{position:relative;width:1600px;height:1000px;overflow:hidden}</style><main>'+''.join(shapes)+'</main>'

for scene in scenes:
    (OUT/f'scene_{scene["key"]}.html').write_text(render_scene(scene),encoding='utf-8')
(OUT/'scenes.json').write_text(json.dumps(scenes,ensure_ascii=False),encoding='utf-8')
assert len({e['id'] for e in elements})==len(elements)
assert all(e['frameId'] is None or e['frameId'] in {s['id'] for s in scenes} for e in elements)
print(f'Created {len(scenes)} frames and {len(elements)} editable elements.')
