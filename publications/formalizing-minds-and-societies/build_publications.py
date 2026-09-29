from pathlib import Path
import hashlib, html, json, re, subprocess, textwrap
from xml.sax.saxutils import escape

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image, XPreformatted
from reportlab.platypus.tableofcontents import TableOfContents
import matplotlib
matplotlib.use('Agg')
from matplotlib.mathtext import math_to_image
from matplotlib.font_manager import FontProperties
from PIL import Image as PILImage
matplotlib.rcParams['mathtext.fontset']='stix'

ROOT=Path(__file__).parent
PACK=ROOT/'reading-pack'
OUT=ROOT/'output'
PDFOUT=OUT/'pdf'
EOUT=OUT/'epub'
TMP=ROOT/'tmp'/'pdfs'
for p in [OUT,PDFOUT,EOUT,TMP]:p.mkdir(parents=True,exist_ok=True)
metadata=json.loads((ROOT/'manuscript-metadata.json').read_text())

fontroot=Path('/usr/share/fonts/truetype/dejavu')
for name,variant in [('APARoman','Regular'),('APABold','Bold'),('APAItalic','Italic'),('APABoldItalic','BoldItalic')]:
    face=pdfmetrics.EmbeddedType1Face('/usr/share/fonts/type1/urw-base35/NimbusRoman-'+variant+'.afm','/usr/share/fonts/X11/Type1/NimbusRoman-'+variant+'.pfb')
    pdfmetrics.registerTypeFace(face)
    pdfmetrics.registerFont(pdfmetrics.Font(name,face.name,'WinAnsiEncoding'))
pdfmetrics.registerFontFamily('APARoman',normal='APARoman',bold='APABold',italic='APAItalic',boldItalic='APABoldItalic')
for name,file in [('DSerif','DejaVuSerif.ttf'),('DSerifB','DejaVuSerif-Bold.ttf'),('Mono','DejaVuSansMono.ttf'),('MonoB','DejaVuSansMono-Bold.ttf'),('MonoI','DejaVuSansMono-Oblique.ttf'),('MonoBI','DejaVuSansMono-BoldOblique.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(fontroot/file)))
pdfmetrics.registerFontFamily('Mono',normal='Mono',bold='MonoB',italic='MonoI',boldItalic='MonoBI')

styles={
 'body':ParagraphStyle('body',fontName='APARoman',fontSize=12,leading=24,firstLineIndent=36,spaceBefore=0,spaceAfter=0,allowWidows=0,allowOrphans=0,splitLongWords=1),
 'noindent':ParagraphStyle('noindent',fontName='APARoman',fontSize=12,leading=24,firstLineIndent=0,allowWidows=0,allowOrphans=0),
 'title':ParagraphStyle('title',fontName='APABold',fontSize=12,leading=24,alignment=TA_CENTER,spaceAfter=24),
 'center':ParagraphStyle('center',fontName='APARoman',fontSize=12,leading=24,alignment=TA_CENTER),
 'h1':ParagraphStyle('h1',fontName='APABold',fontSize=12,leading=24,alignment=TA_CENTER,spaceBefore=12,spaceAfter=0,keepWithNext=True),
 'h2':ParagraphStyle('h2',fontName='APABold',fontSize=12,leading=24,spaceBefore=12,spaceAfter=0,keepWithNext=True),
 'h3':ParagraphStyle('h3',fontName='APABoldItalic',fontSize=12,leading=24,spaceBefore=12,spaceAfter=0,keepWithNext=True),
 'ref':ParagraphStyle('ref',fontName='APARoman',fontSize=12,leading=24,leftIndent=36,firstLineIndent=-36,spaceAfter=0,allowWidows=0,allowOrphans=0,splitLongWords=1),
 'table':ParagraphStyle('table',fontName='APARoman',fontSize=10,leading=13,spaceAfter=0,allowWidows=1,allowOrphans=1),
 'tablehead':ParagraphStyle('tablehead',fontName='APABold',fontSize=10,leading=13),
 'captionnumber':ParagraphStyle('captionnumber',fontName='APABold',fontSize=12,leading=24,keepWithNext=True,spaceBefore=12),
 'caption':ParagraphStyle('caption',fontName='APAItalic',fontSize=12,leading=24,keepWithNext=True),
 'code':ParagraphStyle('code',fontName='Mono',fontSize=8.5,leading=13,spaceBefore=12,spaceAfter=12,leftIndent=0),
 'list':ParagraphStyle('list',fontName='APARoman',fontSize=12,leading=24,leftIndent=36,firstLineIndent=0,bulletIndent=12,allowWidows=0,allowOrphans=0),
}
styles['body'].rightIndent=3

def safe(s):
    # Use a consistent supported glyph for technical Unicode outside WinAnsi.
    s=s.replace('\u2011','-').replace('\u2010','-')
    result=[]
    for ch in s:
        try:ch.encode('cp1252');result.append(escape(ch))
        except UnicodeEncodeError:result.append('<font name="DSerif">'+escape(ch)+'</font>')
    return ''.join(result)

def plain(inlines):
    out=[]
    for n in inlines:
        t,c=n['t'],n.get('c')
        if t=='Str':out.append(c)
        elif t in ['Space','SoftBreak','LineBreak']:out.append(' ')
        elif t in ['Strong','Emph','SmallCaps','Strikeout','Superscript','Subscript']:out.append(plain(c))
        elif t in ['Code','Math']:out.append(c[1])
        elif t in ['Link','Image']:out.append(plain(c[1]))
        elif t=='Quoted':out.append(plain(c[1]))
        elif t=='Span':out.append(plain(c[1]))
    return ''.join(out)

def inline(nodes):
    out=[]
    for n in nodes:
        t,c=n['t'],n.get('c')
        if t=='Str':out.append(safe(c))
        elif t in ['Space','SoftBreak']:out.append(' ')
        elif t=='LineBreak':out.append('<br/>')
        elif t=='Emph':out.append('<i>'+inline(c)+'</i>')
        elif t=='Strong':out.append('<b>'+inline(c)+'</b>')
        elif t=='Code':out.append('<font name="Mono" size="9.2">'+safe(c[1])+'</font>')
        elif t=='Link':
            target=c[2][0]
            out.append('<link href="'+html.escape(target,quote=True)+'" color="#000000">'+inline(c[1])+'</link>')
        elif t=='Quoted':out.append(('“' if c[0]['t']=='DoubleQuote' else '‘')+inline(c[1])+('”' if c[0]['t']=='DoubleQuote' else '’'))
        elif t=='Superscript':out.append('<super>'+inline(c)+'</super>')
        elif t=='Subscript':out.append('<sub>'+inline(c)+'</sub>')
        elif t=='Math':out.append(safe(c[1]))
        elif t=='Span':out.append(inline(c[1]))
        elif t in ['SmallCaps','Strikeout']:out.append(inline(c))
        elif t=='RawInline':pass
        else:raise ValueError(('Unknown inline',t))
    return ''.join(out)

def ast(markdown):
    p=subprocess.run(['pandoc','-f','markdown+autolink_bare_uris','-t','json'],input=markdown,text=True,capture_output=True,check=True)
    return json.loads(p.stdout)['blocks']

class APADoc(BaseDocTemplate):
    def __init__(self,filename,meta):
        super().__init__(str(filename),pagesize=(612,792),leftMargin=72,rightMargin=72,topMargin=72,bottomMargin=72,title=meta['title'],author=meta['author'],subject=meta['subtitle'],pageCompression=1)
        self.meta=meta
        frame=Frame(72,72,468,648,leftPadding=0,rightPadding=0,topPadding=0,bottomPadding=0,id='body')
        self.addPageTemplates(PageTemplate(id='main',frames=[frame],onPage=self.header))
    def header(self,canv,doc):
        canv.saveState();canv.setFont('APARoman',12)
        canv.drawString(72,756,self.meta['short'])
        canv.drawRightString(540,756,str(doc.page));canv.restoreState()
    def afterFlowable(self,f):
        if isinstance(f,Paragraph) and hasattr(f,'bookmark_key'):
            self.canv.bookmarkPage(f.bookmark_key)
            lev=f.bookmark_level
            label=getattr(f,'bookmark_label',f.getPlainText())
            self.canv.addOutlineEntry(label,f.bookmark_key,level=lev,closed=lev>0)
            if lev==0 and not f.getPlainText().startswith('Abstract'):
                self.notify('TOCEntry',(0,label,self.page,f.bookmark_key))

class Renderer:
    def __init__(self,meta):
        self.meta=meta;self.table=0;self.ref=False;self.abstract=False;self.headingcount=0;self.seenbody=False;self.after_appendix=False
    def equation(self,expr):
        expr=' '.join(expr.split())
        expr=expr.replace('\\mathbin{+\\!+}','{+}{+}').replace('\\Longleftrightarrow','\\Leftrightarrow').replace('\\land','\\wedge')
        fn=TMP/('eq-stix-'+hashlib.md5(expr.encode()).hexdigest()+'.png')
        if not fn.exists():
            math_to_image('$'+expr+'$',str(fn),prop=FontProperties(family='serif',size=12),dpi=300,format='png',color='black')
        with PILImage.open(fn) as im:w,h=im.size
        width=w*72/300;height=h*72/300
        if width>455:height*=455/width;width=455
        im=Image(str(fn),width=width,height=height,hAlign='CENTER')
        im.spaceBefore=12;im.spaceAfter=12
        return im
    def blocks(self,blocks):
        out=[]
        for block_index,b in enumerate(blocks):
            t,c=b['t'],b.get('c')
            if t=='Header':
                level,attr,ins=c;txt=plain(ins)
                if txt=='References':self.ref=True;out.append(PageBreak())
                elif txt.startswith('Appendix '):self.ref=False;self.after_appendix=True;out.append(PageBreak())
                elif txt=='Abstract':self.abstract=True
                elif level==1:
                    if self.abstract:self.abstract=False;out.append(PageBreak())
                    elif self.seenbody and self.meta['filename']=='dissertation':out.append(PageBreak())
                    self.seenbody=True
                style=styles['h'+str(min(level,3))]
                if self.after_appendix and level==2:
                    style=styles['h1'];self.after_appendix=False
                p=Paragraph(inline(ins),style)
                # Skip appendix titles as duplicate same-level outline entries.
                if level<=2 and not (style==styles['h1'] and level==2):
                    self.headingcount+=1;p.bookmark_key='heading-'+str(self.headingcount);p.bookmark_level=min(level-1,1)
                    if level==2 and self.headingcount==1:p.bookmark_level=0
                    if txt.startswith('Appendix ') and block_index+1<len(blocks) and blocks[block_index+1]['t']=='Header':
                        p.bookmark_label=txt+': '+plain(blocks[block_index+1]['c'][2])
                out.append(p)
            elif t in ['Para','Plain']:
                if len(c)==1 and c[0]['t']=='Math' and c[0]['c'][0]['t']=='DisplayMath':out.append(self.equation(c[0]['c'][1]));continue
                sty=styles['ref'] if self.ref else styles['noindent'] if self.abstract else styles['body']
                if len(c)==1 and c[0]['t']=='Link':sty=styles['noindent']
                # Abstract keywords are indented like APA's keyword line.
                if plain(c).startswith('Keywords:'):sty=styles['body']
                out.append(Paragraph(inline(c),sty))
            elif t=='Table':
                self.table+=1
                cap=c[1][1]
                captext=' '.join(plain(x['c']) for x in cap)
                out.append(Paragraph('Table '+str(self.table),styles['captionnumber']))
                out.append(Paragraph(safe(captext),styles['caption']))
                heads=c[3][1]
                data=[]
                def row(r,header=False):
                    return [Paragraph('<br/>'.join(inline(z['c']) for z in cell[4] if z['t'] in ['Plain','Para']),styles['tablehead'] if header else styles['table']) for cell in r[1]]
                data.extend(row(r,True) for r in heads)
                for body in c[4]:
                    data.extend(row(r) for r in body[2]);data.extend(row(r) for r in body[3])
                cols=len(data[0])
                if cols==2:widths=[164,304]
                elif cols==3:
                    widths=[122,67,279] if self.meta['filename']=='research-article' else [113,175,180]
                elif cols==4:widths=[74,128,143,123]
                else:widths=[468/cols]*cols
                tb=Table(data,colWidths=widths,repeatRows=len(heads),hAlign='LEFT')
                tb.setStyle(TableStyle([('VALIGN',(0,0),(-1,-1),'TOP'),('LEFTPADDING',(0,0),(-1,-1),4),('RIGHTPADDING',(0,0),(-1,-1),6),('TOPPADDING',(0,0),(-1,-1),6),('BOTTOMPADDING',(0,0),(-1,-1),6),('LINEABOVE',(0,0),(-1,0),0.8,colors.black),('LINEBELOW',(0,len(heads)-1),(-1,len(heads)-1),0.6,colors.black),('LINEBELOW',(0,-1),(-1,-1),0.8,colors.black)]))
                tb.spaceAfter=12;out.append(tb)
            elif t=='CodeBlock':
                lines=[]
                for line in c[1].splitlines():
                    lines+=textwrap.wrap(line,width=86,replace_whitespace=False,drop_whitespace=False,subsequent_indent='  ') or ['']
                out.append(XPreformatted(escape('\n'.join(lines)),styles['code']))
            elif t in ['OrderedList','BulletList']:
                start=1
                items=c
                if t=='OrderedList':start=c[0][0];items=c[1]
                for idx,item in enumerate(items):
                    first=True
                    for it in item:
                        if it['t'] in ['Plain','Para']:
                            bullet=str(start+idx)+'.' if t=='OrderedList' else '•'
                            out.append(Paragraph(inline(it['c']),styles['list'],bulletText=bullet if first else None));first=False
                        else:out.extend(self.blocks([it]))
            elif t=='BlockQuote':out.extend(self.blocks(c))
            elif t=='Div':out.extend(self.blocks(c[1]))
            elif t in ['RawBlock','HorizontalRule','Null']:pass
            else:raise ValueError(('Unknown block',t))
        return out

def titlepage(m):
    return [Spacer(1,72),Paragraph(safe(m['title']),styles['title']),Paragraph(safe(m['author']),styles['center']),Paragraph('Independent Research Project',styles['center']),Spacer(1,24),Paragraph(safe(m['subtitle']),styles['center']),Paragraph(safe(m['date']),styles['center']),Spacer(1,48),Paragraph('Author Note',styles['h1']),Paragraph('This manuscript was prepared with ChatGPT from the project’s earlier reader’s guide and inspected source materials. The cited repository records the authorship and provenance of the Lean development. The manuscript presents a source audit, methodological synthesis, and proposed research program.',styles['body']),PageBreak()]

css='''
body { font-family: serif; line-height: 1.75; color: #111; }
p { margin: 0; text-indent: 1.5em; }
h1,h2,h3 { font-size: 1em; line-height: 1.7; margin: 1.4em 0 0; font-weight: bold; }
h1 { text-align: center; } h2 { text-align: left; } h3 { font-style: italic; }
section#abstract p { text-indent: 0; }
.references p, section#references p { padding-left: 1.5em; text-indent: -1.5em; }
code { font-family: monospace; font-size: .85em; overflow-wrap: anywhere; }
pre { white-space: pre-wrap; line-height: 1.35; }
table { border-collapse: collapse; width: 100%; margin: 1em 0; font-size: .9em; line-height: 1.4; }
th,td { vertical-align: top; text-align: left; padding: .4em; border: none; }
thead { border-top: 1px solid; border-bottom: 1px solid; }
tbody { border-bottom: 1px solid; }
caption { text-align: left; font-style: italic; padding: .5em 0; }
a { color: inherit; } nav a { text-decoration: none; }
math { font-size: 1em; }
.titlepage { text-align: center; } .titlepage p { text-indent: 0; }
'''
(OUT/'epub-style.css').write_text(css)

results={}
for kind,m in metadata.items():
    markdown=(PACK/(m['filename']+'.md')).read_text()
    if kind=='article' and '\n## Method\n' in markdown:
        main,appendix=markdown.split('# Appendix A',1)
        main=re.sub(r'^(#{2,3}) ',lambda match:match[1][1:]+' ',main,flags=re.M)
        markdown=main+'# Appendix A'+appendix
    blocks=ast(markdown)
    # APA body repeats the full title on its first page.
    bodytitle='From Social Explanations to Checkable Proofs' if kind=='article' else 'Formalizing Minds and Societies'
    markdown=markdown.replace('# '+bodytitle+'\n','# '+m['title']+'\n')
    (PACK/(m['filename']+'.md')).write_text(markdown)
    blocks=ast(markdown)
    rend=Renderer(m)
    story=titlepage(m)
    if kind=='dissertation':
        # Abstract precedes contents; body begins on a new page.
        split=next(i for i,b in enumerate(blocks[1:],1) if b['t']=='Header' and b['c'][0]==1)
        story+=rend.blocks(blocks[:split])
        story.append(PageBreak());story.append(Paragraph('Contents',styles['h1']))
        toc=TableOfContents();toc.levelStyles=[ParagraphStyle('toc',fontName='APARoman',fontSize=12,leading=24,spaceBefore=0,spaceAfter=0,rightIndent=24)]
        story.append(toc)
        story+=rend.blocks(blocks[split:])
    else:story+=rend.blocks(blocks)
    fn=PDFOUT/(m['filename']+'.pdf')
    doc=APADoc(fn,m);doc.multiBuild(story)
    # EPUB title and production note carry the same authorship information.
    yml='---\ntitle: '+json.dumps(m['title'])+'\nauthor: '+json.dumps(m['author'])+'\nsubtitle: '+json.dumps(m['subtitle'])+'\ndate: '+json.dumps(m['date'])+'\nlang: en-US\nrights: "Prepared for scholarly review; source rights remain with their respective authors."\n---\n\n'
    epubmd=TMP/(m['filename']+'-epub.md')
    note='## Author Note\n\nThis manuscript was prepared with ChatGPT from the project’s earlier reader’s guide and inspected source materials. The cited repository records the authorship and provenance of the Lean development. The manuscript presents a source audit, methodological synthesis, and proposed research program.\n\n'
    table_index=[0]
    def epub_caption(match):
        table_index[0]+=1
        return f'Table: **Table {table_index[0]}**<br/>*{match[1]}*'
    epubtext=re.sub(r'^Table: (.+)$',epub_caption,markdown,flags=re.M)
    epubmd.write_text(yml+note+epubtext)
    efn=EOUT/(m['filename']+'.epub')
    subprocess.run(['pandoc',str(epubmd),'-f','markdown+autolink_bare_uris','-o',str(efn),'--toc','--toc-depth=2','--split-level=1','--mathml','--css',str(OUT/'epub-style.css')],check=True)
    results[kind]={'pdf':str(fn),'epub':str(efn),'words':m['words'],'tables':rend.table}
(OUT/'build-results.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))
