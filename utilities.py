import re
# Formatter

from coding.settings_local import STATIC_URL


def OAAMarkupToHTML(str):
  str1 = ""
  
  if str and len(str):
    str = str.replace("%s", "must")
  
    code = "<code>"
    for c in str:
      if c == '@':
        str1 += code;
        if code == "<code>":
          code = "</code>"
        else:
          code = "<code>"
      else:
        str1 += c      
  return str1

def OAAMarkupToText(str):
  str1 = ""

  if str and len(str):
    str = str.replace("%s", "must")
  
    for c in str:
      if c != '@':
        str1 += c    
          
  return str1



def HTMLToSourceCodeFormat(text):
    """A filter to format the sample HTML for rendering the soruce code"""
    try:
        out = re.sub(r'&','&amp;', text)
        out = re.sub(r'\t', '&#160;&#160;', out)
        out = re.sub(r'<', '&lt;', out)
        out = re.sub(r'>', '&gt;', out)
        out = re.sub(r'&lt;HL1&gt;', '<strong>', out)
        out = re.sub(r'&lt;/HL1&gt;', '</strong>', out)
        out = re.sub(r'&lt;HL2&gt;', '<em>', out)
        out = re.sub(r'&lt;/HL2&gt;', '</em>', out)
        out = re.sub(r'\n', '<br/>\n', out)
        out = re.sub(r'  ', '&#160;&#160;', out)
        out = re.sub(r'{{EXAMPLE_MEDIA}}',  STATIC_URL + 'examples/', out)
        return out
    except (TypeError, NameError, AttributeError):
        return ''


def OAAMarkupRemoveHighlightCode(text):

    """Remove tags for highlighting for rendering the code as HTML."""

    try:
        out = re.sub(r'<HL1>', '', text)
        out = re.sub(r'</HL1>', '', out)
        out = re.sub(r'<HL2>', '', out)
        out = re.sub(r'</HL2>', '', out)
        out = re.sub(r'{{EXAMPLE_MEDIA}}', STATIC_URL + 'examples/', out)
        return out
    except (TypeError, NameError, AttributeError):
        return ''

   
