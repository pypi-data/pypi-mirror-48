"""
analyze chemical input/output filetype 
"""


import os
import re
import configparser
import atomtools


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_FILETYPE_REGEXP_CONF = 'default_extension.conf'
REG_ANYSTRING = '[\s\S]*?'

global FORMATS_REGEXP
FORMATS_REGEXP = dict()


def update_config(path=None):
    global FORMATS_REGEXP
    path = path or os.path.join(BASE_DIR, DEFAULT_FILETYPE_REGEXP_CONF)
    if os.path.exists(path):
        conf = configparser.ConfigParser(delimiters=('='))
        conf.optionxform=str
        conf.read(path)
        for section in conf.sections():
            FORMATS_REGEXP.update(conf._sections[section])


def filetype(fileobj=None, isfilename=False, debug=False):
    """
    >>> filetype("a.gjf")
    gaussian
    >>> filetype("1.gro")
    gromacs
    """
    if isfilename:
        filename = fileobj
    else:
        filename = atomtools.file.get_filename(fileobj)
    content = atomtools.file.get_file_content(fileobj)
    if filename is None and content is None:
        return None
    for fmt_regexp, fmt_filetype in FORMATS_REGEXP.items():
        name_regexp, content_regexp = (fmt_regexp.split('&&') + [None])[:2]
        if debug:
            print(name_regexp, content_regexp)
        if filename and re.match(re.compile(name_regexp.strip()), filename) or filename is None:
            if content and content_regexp:
                if not content_regexp.startswith('^'):
                    content_regexp = REG_ANYSTRING + content_regexp.strip() 
                if not content_regexp.endswith('$'):
                    content_regexp = content_regexp.strip() + REG_ANYSTRING
                if debug:
                    print(content_regexp)
                    import pdb; pdb.set_trace()
                if re.match(re.compile(content_regexp.strip()), content):
                    return fmt_filetype
            else:
                return fmt_filetype
    return None


def list_supported_formats():
    return list(FORMATS_REGEXP.values())



update_config()



