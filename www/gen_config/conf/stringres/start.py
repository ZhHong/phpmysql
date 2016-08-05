#!/usr/bin/env python
# encoding: utf-8
import os
#from __future__ import with_statement

import xlrd
import sys

sys.path.append("../")
from script.util import _int
from script.util import _utf8
from script.util import _j2f
from script.util import multilanguagefd
from script.util import multilanguage
from script.util import converter_0
from script.util import converter_3
from script.util import gen_file
from script.util import gen_adminserver_file

def stringres(argv_platform):
    """
    """
    excel_file = 'stringres.xlsx'
    server_template = 'stringres.php'  # 后端配置文件模版
    server_output = 'stringres.php'  #  后端配置输出文件

    server_configs = {
        'stringres': {
            'data_type': ['unicode', 'unicode', 'unicode'],
            'data_template': '"%(s0)s"=>"%(s1)s"',
            'placeholder': '$STRINGRES$'
        }
    }
    server_output_dict = converter_0(excel_file, server_configs, argv_platform)
    gen_file(server_template, server_output, server_output_dict, True)

if __name__ == '__main__':

    #argv_platform = sys.argv[1]
    #argv_jf = sys.argv[2]
    #argv_conftype = sys.argv[3]
    


    argv_platform = ""
    stringres(argv_platform)
