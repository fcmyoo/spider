import docx
import jinja2
from docxtpl import DocxTemplate

doc = DocxTemplate('1.docx')
context = {'myname': '李胜'}
jinja_env = jinja2.Environment()
jinja_env.filters['myname'] = '李胜'
doc.render(context, jinja_env)
doc.save('2.docx')
doc1 = docx.Document('1.docx')
doc1.save()
