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
from script.util import gen_file


def converter_4(excel_file, sheet_name, isServer=True):
    """
        PlanItems
        id:[planItem1,planItem2],    
    """
    book = xlrd.open_workbook(excel_file)
    sheet = book.sheet_by_name(sheet_name)
    print sheet.name
    
    if isServer:
        data_template = '%(s0)s:[%(s1)s]'
    else:
        data_template = '[%(s0)s] = {%(s1)s}'
    
    rows_text = ''
    last_row_s0 = ''
    row_dict = {}
    row_list = ''

    for i in xrange(1, sheet.nrows):

        # 循环sheet中的行
        
        current_row_s0 = str(_int(sheet.cell_value(i, 0)))      
        if last_row_s0 == '':
            last_row_s0 = current_row_s0
        
        if last_row_s0 != current_row_s0:
            if row_list != '':
                row_list = row_list[:-1]     
            row_dict['s1'] = row_list
            row_data = data_template % row_dict
            rows_text = rows_text + ' ' * 12 + row_data + ',\n'
            row_dict = {}
            row_list = ''
            last_row_s0 = current_row_s0
        
        
        row_dict['s0'] = current_row_s0
        if isServer:                
            row_list = row_list + "["+str(_int(sheet.cell_value(i,1)))+","+str(_int(sheet.cell_value(i,2)))+"],"
        else:
            row_list = row_list +"{"+str(_int(sheet.cell_value(i,1)))+","+str(_int(sheet.cell_value(i,2)))+"},"            
    
    if row_list != '':
        row_list = row_list[:-1]       
   
    row_dict['s1'] = row_list
    row_data = data_template % row_dict
    rows_text = rows_text + ' ' * 12 + row_data + ',\n'
        
    return rows_text[:-2]

def converter_5(excel_file, sheet_name, isServer=True):
    """
        AchievementAwards
        id:[type,itemid,num,''],    
    """
    book = xlrd.open_workbook(excel_file)
    sheet = book.sheet_by_name(sheet_name)
    print sheet.name
    
    if isServer:
        data_template = '%(s0)s:[%(s1)s]'
    else:
        data_template = '[%(s0)s] = {%(s1)s}'
    
    rows_text = ''
    last_row_s0 = ''
    row_dict = {}
    row_list = ''

    for i in xrange(1, sheet.nrows):

        # 循环sheet中的行
        
        current_row_s0 = str(_int(sheet.cell_value(i, 0)))      
        if last_row_s0 == '':
            last_row_s0 = current_row_s0
        
        if last_row_s0 != current_row_s0:
            if row_list != '':
                row_list = row_list[:-1]    
            
            row_dict['s1'] = row_list
            row_data = data_template % row_dict
            rows_text = rows_text + ' ' * 12 + row_data + ',\n'
            row_dict = {}
            row_list = ''
            last_row_s0 = current_row_s0
        
        
        row_dict['s0'] = current_row_s0
        if isServer:
            if argv_jf:
                row_list = row_list + "['"+_j2f(sheet.cell_value(i,1),argv_jf, argv_multi, argv_multi_fd)+"',"+str(_int(sheet.cell_value(i,2)))+","+str(_int(sheet.cell_value(i,3)))+",'"+_j2f(sheet.cell_value(i,4),argv_jf, argv_multi, argv_multi_fd)+"'], "
            else:
                row_list = row_list + "['"+_utf8(sheet.cell_value(i,1))+"',"+str(_int(sheet.cell_value(i,2)))+","+str(_int(sheet.cell_value(i,3)))+",'"+_utf8(sheet.cell_value(i,4))+"'], "
        else:
            if argv_jf:
                row_list = row_list +' ' * 22+ "{'"+_j2f(sheet.cell_value(i,1),argv_jf, argv_multi, argv_multi_fd)+"',"+str(_int(sheet.cell_value(i,2)))+","+str(_int(sheet.cell_value(i,3)))+",'"+_j2f(sheet.cell_value(i,4),argv_jf, argv_multi, argv_multi_fd)+"'} ,\n"
            else:
                row_list = row_list + "{'"+_utf8(sheet.cell_value(i,1))+"',"+str(_int(sheet.cell_value(i,2)))+","+str(_int(sheet.cell_value(i,3)))+",'"+_utf8(sheet.cell_value(i,4))+"'},"
    
    if row_list != '':
        row_list = row_list[:-1]    
    
    row_dict['s1'] = row_list
    row_data = data_template % row_dict
    rows_text = rows_text + ' ' * 12 + row_data + ',\n'
        
    return rows_text[:-2]
        


def converter_dialymission_awards(excel_file, sheet_name, isServer = False ):

    book = xlrd.open_workbook(excel_file)
    sheet = book.sheet_by_name(sheet_name)
    print sheet.name
    
    if isServer:
        data_template = '%(s0)s:[%(s2)s]'
    else:
        data_template = '[%(s0)s] = {\n%(s2)s\n'+' '*20+'}'
    
    rows_text = ''
    last_row_s0 = ''
    row_dict = {}
    row_list = ''

    for i in xrange(1, sheet.nrows):


        # 循环sheet中的行
        
        current_row_s0 = str(_int(sheet.cell_value(i,0)))        
        if last_row_s0 == '':
            last_row_s0 = current_row_s0
        
        if last_row_s0 != current_row_s0:
            if row_list != '':
                row_list = row_list[:-2]
            
            row_dict['s2'] = row_list
            row_data = data_template % row_dict
            rows_text = rows_text + ' ' * 12 + row_data + ',\n'
            row_dict = {}
            row_list = ''
            last_row_s0 = current_row_s0
        
        
        row_dict['s0'] = current_row_s0
        if isServer:
            if argv_jf:
                row_list = row_list + "['"+_j2f(sheet.cell_value(i,1),argv_jf, argv_multi, argv_multi_fd)+"',"+str(_int(sheet.cell_value(i,2)))+","+str(_int(sheet.cell_value(i,3)))+",'"+_j2f(sheet.cell_value(i,4),argv_jf, argv_multi, argv_multi_fd)+"'], "
            else:
                row_list = row_list + "['"+_utf8(sheet.cell_value(i,1))+"',"+str(_int(sheet.cell_value(i,2)))+","+str(_int(sheet.cell_value(i,3)))+",'"+_utf8(sheet.cell_value(i,4))+"'], "
        else:
            if argv_jf:
                row_list = row_list +' ' * 22+ "{'"+_j2f(sheet.cell_value(i,1),argv_jf, argv_multi, argv_multi_fd)+"',"+str(_int(sheet.cell_value(i,2)))+","+str(_int(sheet.cell_value(i,3)))+",'"+_j2f(sheet.cell_value(i,4),argv_jf, argv_multi, argv_multi_fd)+"'} ,\n"
            else:
                row_list = row_list +' ' * 22+ "{'"+_utf8(sheet.cell_value(i,1))+"',"+str(_int(sheet.cell_value(i,2)))+","+str(_int(sheet.cell_value(i,3)))+",'"+_utf8(sheet.cell_value(i,4))+"'} ,\n"
   
    if row_list != '':
        row_list = row_list[:-2]
    
    row_dict['s2'] = row_list
    row_data = data_template % row_dict
    rows_text = rows_text + ' ' * 12 + row_data + ',\n'    
    return rows_text[:-2]


def achievement(argv_jf,argv_platform, argv_multi, argv_multi_fd):
    """
    """
    excel_file = 'achievement.xls'  # excel配置文件，xls格式
    server_template = 'achievement.xml'  # 后端配置文件模版
    server_output = 'achievement'  #  后端配置输出文件
    client_template = 'achievementDB.lua'
    client_output = 'achievementDB'

    if argv_jf in ['multi_gbk','multi_big5','multi_en']:
        if argv_jf == 'multi_gbk':
            argv_jf = 'gbk'
            server_output = server_output + '.xml'
            client_output = client_output + '.lua'
        if argv_jf == 'multi_big5':
            argv_jf = 'big5'
            server_output = server_output + '_big5.xml'
            client_output = client_output + '_big5.lua'
        if argv_jf == 'multi_en':
            argv_jf = 'en'
            server_output = server_output + '_en.xml'
            client_output = client_output + '_en.lua'
    else:
        server_output = server_output + '.xml'
        client_output = client_output + '.lua'

    server_configs = {
        'AchievementPlans': {
            'data_type': ['int', 'unicode','unicode'],
            'data_template': '%(s0)d:"%(s1)s"',
            'placeholder': '$ACHIEVEMENT_PLANS$'
        },
        'AchievementTargets' : {
            'data_type' : ['int','unicode','unicode','int','int','int','int','int','int','int','int','int','int','int','int','int','int','int','int'],
            'data_template': '%(s0)d:[%(s3)d,%(s4)d,%(s5)d,%(s6)d,%(s7)d,%(s8)d,%(s14)d,%(s15)d,%(s16)d,%(s17)d,%(s18)d]',
            'placeholder': '$ACHIEVEMENT_TARGETS$'            
        },
        'AchievementItems' : {
            'data_type' : ['int','int','int','unicode','unicode','int','int','str','int'],
            'data_template': '%(s0)d:[%(s1)d,%(s2)d,%(s5)d,%(s6)d]',
            'placeholder': '$ACHIEVEMENT_ITEMS$'            
        },
        'PlotConditions' : {
            'data_type' : ['int','int'],
            'data_template' : '%(s0)d:%(s1)d',
            'placeholder': '$PLOT_CONDITIONS$'
        }              
    }
    
    client_configs = {
        'AchievementPlans': {
            'data_type': ['int', 'unicode','unicode'],
            'data_template': '[%(s0)d]={"%(s1)s","%(s2)s"}',
            'placeholder':  '$ACHIEVEMENT_PLANS$'
        },
        'AchievementTargets' : {
            'data_type' : ['int','unicode','unicode','int','int','int','int','int','int','int','int','int','int','int','int','int','int','int','int'],
            'data_template': '[%(s0)d]={"%(s1)s","%(s2)s",%(s3)d,%(s9)d,%(s10)d,%(s11)d,%(s12)d,%(s13)d,%(s14)d,%(s15)d,%(s16)d,%(s17)d,%(s18)d}',
            'placeholder': '$ACHIEVEMENT_TARGETS$'            
        },
        'AchievementItems' : {
            'data_type' : ['int','int','int','unicode','unicode','int','int','str','int'],
            'data_template': '[%(s0)d]={"%(s3)s","%(s4)s",%(s5)d,%(s6)d,"%(s7)s",%(s8)d}',
            'placeholder': '$ACHIEVEMENT_ITEMS$'            
        }                      
    }    
    
    server_output_dict = converter_0(excel_file, server_configs, argv_jf, argv_multi, argv_multi_fd)
    server_output_dict['$PLAN_ITEMS$'] = converter_4(excel_file, 'PlanItems')
    server_output_dict['$ACHIEVEMENT_AWARDS$'] = converter_5(excel_file, 'AchievementAwards')    
    gen_file(server_template, server_output, server_output_dict, True)
    
    client_output_dict = converter_0(excel_file, client_configs, argv_jf, argv_multi, argv_multi_fd)
    client_output_dict['$PLAN_ITEMS$'] = converter_4(excel_file, 'PlanItems', False )
    client_output_dict['$ACHIEVEMENT_AWARDS$'] = converter_5(excel_file, 'AchievementAwards', False )
    gen_file(client_template, client_output, client_output_dict)



def dailymession(argv_jf,argv_platform, argv_multi, argv_multi_fd):
    #if argv_platform == 'android':
    #    excel_file = "dialymission_android.xls" # excel配置文件，xls格式
    #else:
    #    excel_file = "dialymission_ios.xls" # excel配置文件，xls格式
    excel_file = "dialymission.xls"
    server_template = 'daily_join.xml'  # 后端配置文件模版
    server_output = 'daily_join'  #  后端配置输出文件        
    client_template = 'DailymsnDB.lua'
    client_output = 'DailymsnDB'
    

    if argv_jf in ['multi_gbk','multi_big5','multi_en']:
        if argv_jf == 'multi_gbk':
            argv_jf = 'gbk'
            server_output = server_output + '.xml'
            client_output = client_output + '.lua'
        if argv_jf == 'multi_big5':
            argv_jf = 'big5'
            server_output = server_output + '_big5.xml'
            client_output = client_output + '_big5.lua'
        if argv_jf == 'multi_en':
            argv_jf = 'en'
            server_output = server_output + '_en.xml'
            client_output = client_output + '_en.lua'
    else:
        server_output = server_output + '.xml'
        client_output = client_output + '.lua'


    server_configs = {
        'dailyMission': {
            'data_type':['int','int','int','unicode','unicode','int','unicode'],
            'data_template': '%(s0)d:[%(s1)d, %(s2)d]',
            'placeholder': '$DAILY_MISSION$'
        },
        'dailyMissionAwards' : {
            'data_type':['int','int'],
            'data_template': '%(s0)d:[%(s1)d]',
            'placeholder': '$DAILY_MISSION_AWARDS$'
        },
        'doubleDate' : {
            'data_type':['str'],
            'data_template': '"%(s0)s"',
            'placeholder': '$DOUBLE_DATE$'
        }
                                            
    }        

    client_configs = {
        'dailyMission': {
            'data_type':['int','int','int','unicode','unicode','int','unicode'],
            'data_template': '[%(s0)d]={%(s1)d, %(s2)d,"%(s3)s","%(s4)s",%(s5)d,"%(s6)s"}',
            'placeholder': '$DAILY_MISSION$'
        },
        'dailyMissionAwards' : {
            'data_type':['int','int'],
            'data_template': '[%(s0)d]={%(s1)d}',
            'placeholder': '$DAILY_MISSION_AWARDS$'
        },
        'dailymsnSetting' : {
            'data_type':['str','int'],
            'data_template': '%(s0)s=%(s1)d',
            'placeholder': '$DAILY_MISSION_SETTING$'
        },
    }
    server_output_dict = converter_0(excel_file, server_configs, argv_jf, argv_multi, argv_multi_fd)
    server_output_dict['$DAILYMSN_AWARD_ITMES$'] = converter_dialymission_awards(excel_file, 'dailymsnAwardItems', True)    
    gen_file(server_template, server_output, server_output_dict, True)
    
    client_output_dict = converter_0(excel_file, client_configs, argv_jf, argv_multi, argv_multi_fd)
    client_output_dict['$DAILYMSN_AWARD_ITMES$'] = converter_dialymission_awards(excel_file, 'dailymsnAwardItems', False)
    gen_file(client_template, client_output, client_output_dict)  


if __name__ == '__main__':
    argv_jf = sys.argv[1]
    argv_platform = sys.argv[2]

    #载入多语言对照表，格式{简体中文:英文}，如有其它以后再扩展
    argv_multi = multilanguage()
    #产生所有中文文字列表临时文件
    argv_multi_fd = multilanguagefd()
    
    if argv_jf == 'multi':
        for temp_jf in ['multi_gbk','multi_big5','multi_en']:
            achievement(temp_jf,argv_platform, argv_multi, argv_multi_fd)
            dailymession(temp_jf,argv_platform, argv_multi, argv_multi_fd)
    else:
        achievement(argv_jf,argv_platform, argv_multi, argv_multi_fd)
        dailymession(argv_jf,argv_platform, argv_multi, argv_multi_fd)

    #close fd
    argv_multi_fd.close()