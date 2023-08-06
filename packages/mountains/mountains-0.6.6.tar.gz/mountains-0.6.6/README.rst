
.. role:: raw-html-m2r(raw)
   :format: html



mountains
=========

.. image:: https://travis-ci.org/restran/mountains.svg?branch=master
   :target: https://travis-ci.org/restran/mountains
   :alt: travis-ci


.. image:: https://coveralls.io/repos/github/restran/mountains/badge.svg?branch=master
   :target: https://coveralls.io/github/restran/mountains?branch=master
   :alt: Coverage Status


.. image:: https://img.shields.io/pypi/v/mountains.svg
   :target: https://pypi.python.org/pypi/mountains/
   :alt: pypi package



在开发Python的过程中经常会有一些常用的方法和工具类，因此将这些代码集成在一起，在开发新东西的时候就能直接调用，加速开发。

:raw-html-m2r:`<img src="docs/icon.png" style="margin-left: auto; margin-right: auto; text-align: center; display: block;">`

安装
----

.. code-block::

   pip install mountains



功能
----

. Python 2-3 兼容，大部分代码都尽可能做了兼容
=============================================

. 日期转换，各种日期、字符串、时间戳直接的转换
==============================================

. SSHClient
===========

. Tornado 的异步请求
====================

. Random HTTP User Agent
========================

. 文件、Excel、json 读写
========================

. ...
=====

日期转换
^^^^^^^^

datetime、time、时间戳、日期字符串之间的转换

.. code-block:: python


   import time
   from datetime import datetime
   from mountains.datetime import converter

   date_str = '2016-10-30 12:30:30'
   dt = datetime(year=2016, month=10, day=30, hour=12, minute=30, second=30)
   t = dt.timetuple()
   ts = int(time.mktime(t))
   ts_ms = int(time.mktime(t) * 1000)

   # 字符串转 datetime
   dt = converter.str2datetime(date_str)
   # 字符串转 time
   converter.str2time(date_str)
   # 日期字符串转时间戳，结果为秒
   converter.str2timestamp(date_str)
   # 日期字符串转时间戳，结果为毫秒
   converter.str2timestamp(date_str, millisecond=True)
   # datetime 转字符串，默认格式 %Y-%m-%d %H:%M:%S
   converter.datetime2str(dt)
   # datetime 转字符串，指定格式
   converter.datetime2str(dt, '%Y-%m-%d')


日志功能
^^^^^^^^

对原生的 logging 进行了封装，使用起来更简单

.. code-block:: python

   from mountains import logging
   from mountains.logging import StreamHandler, FileHandler, RotatingFileHandler, TimedRotatingFileHandler

   # 配置日志，输出到控制台、保存到文件、日志级别、输出格式等，文件默认保存到 log.txt
   logging.init_log(StreamHandler(format=logging.FORMAT_SIMPLE), FileHandler(format=logging.FORMAT_VERBOSE, level=logging.DEBUG))
   # RotatingFileHandler 按文件大小分割日志文件
   logging.init_log(StreamHandler(format=logging.FORMAT_SIMPLE), RotatingFileHandler(format=logging.FORMAT_VERBOSE, level=logging.DEBUG))
   # TimedRotatingFileHandler 按时间分割日志文件
   logging.init_log(StreamHandler(format=logging.FORMAT_SIMPLE), TimedRotatingFileHandler(format=logging.FORMAT_VERBOSE, level=logging.DEBUG))

   # 使用方法与原生的 logging 一样
   logger = logging.getLogger(__name__)
   logger.debug('hello')


Excel 读写
----------

.. code-block:: python

   from mountains.file.excel import read_excel, write_excel, edit_excel

读 Excel 文件
=============

   data = read_excel('filename.xlsx')

写新的 Excel
============

   excel_data = [
       {
           'col1': '123',
           'col2': '456'
       },
       {
           'col1': '123',
           'col2': '456'
       },
   ]

   headers = ['col1', 'col2']
   write_excel(headers, excel_data, 'filename.xlsx')

编辑 Excel，打开已有的 Excel，往里面填充数据
============================================

   edit_data = {
       'I2': '123'
   }
   edit_excel('test.xlsx', sheet_index=0, data=edit_data, output_filename='new_test.xlsx')
