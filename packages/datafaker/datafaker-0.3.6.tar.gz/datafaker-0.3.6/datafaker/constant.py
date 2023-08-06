#!/usr/bin/env python
# -*- coding: UTF-8 -*-

__version__ = '0.3.6'

# 每次批量插入数据条数
BATCH_SIZE = 1000

# multiprocessing  queue 最大为32767，超过会报错
MAX_QUEUE_SIZE = 30000

# 产生流数据间隔时间(秒)
DEFAULT_INTERVAL = 1

# 任务并发数
WORKERS = 4

# 最小并行产生记录数（小于该值为单线程）
MIN_RECORDS_FOR_PARALLEL = 10

# 输出数据格式
TEXT_FORMAT = 'text'
JSON_FORMAT = 'json'
DEFAULT_FORMAT = TEXT_FORMAT

# 语言类型
DEFAULT_LOCALE = 'zh_CN'

# ENUM类型，从文件中读取枚举值
ENUM_FILE = 'file://'

# 判断哪些需要加上引号
STR_TYPES = ['date', 'time', 'datetime', 'char', 'varchar', 'tinyblob',
             'tinytext', 'text', 'mediumtext', 'longtext', 'string']


INT_TYPES = ['tinyint', 'smallint', 'mediumint', 'int', 'integer', 'bigint', ]

FLOAT_TYPES = ['float', 'double', 'decimal', ]



