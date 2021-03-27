#usr/bin/python3

import os
import sys
import pickle
from optparse import OptionParser
from optparse import IndentedHelpFormatter
from publisher import jsonp
from publisher import xmlp
from publisher import yamlp
from publisher import inip
#from pyfiglet import Figlet
#print(Figlet(font='slant').renderText('HeyTranser'))
"""
    __  __          ______
   / / / /__  __  _/_  __/________ _____  ________  _____
  / /_/ / _ \/ / / // / / ___/ __ `/ __ \/ ___/ _ \/ ___/
 / __  /  __/ /_/ // / / /  / /_/ / / / (__  )  __/ /
/_/ /_/\___/\__, //_/ /_/   \__,_/_/ /_/____/\___/_/
           /____/
"""
print(__doc__)
class NoWrapFormatter(IndentedHelpFormatter) :
    def _format_text(self, text) :
        "[Does not] format a text, return the text as it is."
        return text

parser = OptionParser(prog='HeyTranser Publisher',
                              usage="",
                              description="HeyTranser Publisher",
                              version="1.0",
                              formatter=NoWrapFormatter(),
                              epilog="""Thanks for using!
                              """)

#源语言,程序语言/自定义语言规则,是否首次,是否已部署trs函数,trs函数是否带ID,

#自定义指定/排除函数规则,自定义指定/排除字符串规则,
#工程根目录,HT工程根目录,强制使用格式

parser.add_option("-f", "--format",
                 dest="format", default="json",
                help="print format")
             
                                
#(options, args) = parser.parse_args()
#opt=options
type(parser.parse_args())                       
(options, args) = parser.parse_args()



values=options.__dict__
def CheckValue(values):
    """
    values
    """
    if values['format']=='' :
        print("Error format")
        exit()
    else:
        if values['format']=='json':
            jsonp.__doc__

        elif values['format']=='xml':
            pass
        elif values['format']=='ini':
            pass        
        elif values['format']=='toml':
            pass
        elif values['format']=='yaml':
            pass
        else:
            print("None format")
            exit()