from pathlib import Path
import csv, json, re, subprocess, zipfile, posixpath
from urllib.parse import unquote, urlsplit
from lxml import etree
import fitz
from PIL import Image, ImageOps, ImageDraw

ROOT=Path(__file__).parent
OUT=ROOT/'output'
TMP=ROOT/'tmp'/'pdfs'
inventory=list(csv.DictReader((ROOT/'reading-pack'/'theorem-inventory.csv').open()))
summary={}
for name in ['research-article','dissertation']:
    pdf=OUT/'pdf'/(name+'.pdf')
    d=fitz.open(pdf)
    alltext='\n'.join(p.get_text() for p in d)
    (TMP/(name+'-extracted.txt')).write_text(alltext)
    issues=[]
    for i,p in enumerate(d):
        for b in p.get_text('dict')['blocks']:
            for line in b.get('lines',[]):
                for span in line['spans']:
                    x0,y0,x1,y1=span['bbox']
                    if x0<70.5 or x1>541.5 or y1>724:issues.append((i+1,span['text'],span['bbox']))
        if len(p.get_text().strip())<50:issues.append((i+1,'near-empty page'))
    assert not issues,issues[:10]
    assert '\ufffd' not in alltext
    assert '[R0' not in alltext and 'Table: ' not in alltext
    if name=='dissertation':
        assert all(row['name'] in alltext for row in inventory),[r['name'] for r in inventory if r['name'] not in alltext]
        ids=re.findall(r'^\d{2}\. ',alltext,re.M)
        assert len(ids)==67,len(ids)
    dest=TMP/name;dest.mkdir(exist_ok=True)
    subprocess.run(['pdftoppm','-r','60','-png',str(pdf),str(dest/'page')],check=True,capture_output=True)
    pages=sorted(dest.glob('page-*.png'))
    sheets=[]
    for k in range(0,len(pages),16):
        sheet=Image.new('RGB',(1200,1664),'#dddddd');draw=ImageDraw.Draw(sheet)
        for j,p in enumerate(pages[k:k+16]):
            im=Image.open(p).convert('RGB');im.thumbnail((286,380))
            x=(j%4)*300+(300-im.width)//2;y=(j//4)*416+24
            sheet.paste(im,(x,y));draw.text(((j%4)*300+10,(j//4)*416+5),f'{name} / {k+j+1}',fill='black')
        fn=TMP/f'{name}-contact-{k//16+1}.jpg';sheet.save(fn,quality=90);sheets.append(str(fn))

    epub=OUT/'epub'/(name+'.epub')
    with zipfile.ZipFile(epub) as z:
        assert z.infolist()[0].filename=='mimetype' and z.infolist()[0].compress_type==zipfile.ZIP_STORED
        assert z.read('mimetype')==b'application/epub+zip'
        files=set(z.namelist());trees={};anchors={}
        for f in files:
            if f.endswith(('.xhtml','.opf','.ncx','.xml')):
                trees[f]=etree.fromstring(z.read(f));anchors[f]={v for v in trees[f].xpath('//@id')}
        errors=[]
        for f,t in trees.items():
            for href in t.xpath('//@href'):
                u=urlsplit(href)
                if u.scheme or href.startswith('//'):continue
                target=posixpath.normpath(posixpath.join(posixpath.dirname(f),unquote(u.path))) if u.path else f
                if target not in files:errors.append((f,href,'missing file'))
                elif u.fragment and target in anchors and unquote(u.fragment) not in anchors[target]:errors.append((f,href,'missing anchor'))
        assert not errors,errors[:20]
        epubtext=' '.join(' '.join(t.itertext()) for f,t in trees.items() if f.endswith('.xhtml'))
        assert 'Table 1' in epubtext
        if name=='dissertation':assert all(r['name'] in epubtext for r in inventory)
        math_nodes=sum(len(t.xpath('//*[local-name()="math"]')) for f,t in trees.items() if f.endswith('.xhtml'))
    summary[name]=dict(pages=len(d),bookmarks=len(d.get_toc()),pdf_bytes=pdf.stat().st_size,epub_bytes=epub.stat().st_size,epub_mathml_equations=math_nodes,contact_sheets=sheets,geometry_issues=issues,epub_link_issues=errors)
    print(name, 'pages:',len(d),'EPUB math:',math_nodes)
    print('Major sections:',[(r[1],r[2]) for r in d.get_toc() if r[0]==1])
(OUT/'quality-checks.json').write_text(json.dumps(summary,indent=2))
