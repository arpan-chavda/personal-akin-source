
-------------------------------------------------------------------------------------
1 Overview
    The books directory in the root directory of the application stores custom RSS settings. Each file is a "book", corresponding to a book pushed to kindle.
    After the application starts, all py files in this directory will be automatically read, dynamically imported, and displayed under the "My Subscriptions" page, you can choose whether to push or not.
    The files in the books directory except __init__.py and base.py, the other files are free to delete if you do not need it.
    The "books" deleted under the books directory will be purged from the database in a single day.

2. py file format
  * py file is recommended for UTF-8 format, especially in Chinese words.
    So the first line of advice for each py file is:
    # - * - coding: utf-8 - * -
    or:
    #! / usr / bin / env python
    # - * - coding: utf-8 - * -

  * Each py file to achieve a function getBook (), returns the actual definition of the book "class" object:
    def getBook ():
        return Qiushibaike

  * Each book as a class (class name is best not to be exactly the same as the file name), the interface must be achieved only one:
    Items (self, opts = None)
    It is a generator or an iterator.
    Each time a tuple is returned:
    HTML tuple: (section title, URL, article title, article content, article summary) - Article content is a string
    Picture tuple: (picture MIME, URL, picture file name, picture content, None) - Picture content is byte string
    The picture MIME is: image / jpeg, image / gif and so on

  * The above definition of the book has finished, so if you are proficient in python, you can write your own books class.
  
  * But if you are lazy, you can also customize your own book class by inheriting one of the two book templates defined in the base module.
    The next section describes how to customize.

3. Book class custom methods
   Have written or read the caliber recipe basically will be direct.
   Because caliber recipe module relies on quite a lot, I am not enough time, lazy, it is not transplanted, directly based on
   The shape of the recipe wrote a processing module.
   * Depending on the RSS type, different base classes for books are imported from the base module
     from base import BaseFeedBook / WebpageBook / BaseComicBook
   * If you are interested in the site does not provide RSS subscriptions, you can inherit WebpageBook directly connected to the web page to extract information.
   * Sub-class customizable parameters are defined in the BaseFeedBook class, the comments are very detailed.
   * BeautifulSoup for HTML is version 4.x.
   * cartoonmadbase.py provides an example of grabbing comic pictures.


1. 概述
    此应用根目录下的books目录存放自定义RSS设置，每个文件为一本"书"，对应推送到kindle的一本书。
    应用启动后会自动读取此目录下的所有py文件，动态导入，并显示在网页“我的订阅”下，可以选择是否推送。
    books目录下的文件除了__init__.py和base.py，其他的文件都可以随意删除，如果你不需要的话。
    在books目录下删除的“书籍”会在一天内从数据库中清除。

2. py文件格式
  * py文件建议为UTF-8格式，特别是里面有中文的话。
    所以每个py文件的头一行建议为：
    # -*- coding:utf-8 -*-
    或者：
    #!/usr/bin/env python
    # -*- coding:utf-8 -*-

  * 每个py文件都要实现一个函数getBook()，返回书籍实际定义的"类"对象：
    def getBook():
        return Qiushibaike

  * 每本书为一个类(类名最好不要和文件名完全一样)，必须实现的接口只有一个：
    Items(self, opts=None)
    它是一个生成器或者返回一个迭代器。
    每次返回一个元组：
    HTML元组：(节标题, URL, 文章标题, 文章内容，文章摘要)  - 文章内容为字符串
    图片元组：(图片MIME, URL, 图片文件名, 图片内容，None) -图片内容为字节串
    其中图片MIME为：image/jpeg, image/gif 等

  * 上面已经说完了书籍定义的一切，所以如果你精通python，就可以自己写自己的书籍类了。
  
  * 不过如果你偷懒，也可以继承base模块中定义的两个书籍模板之一来定制自己的书籍类。
    下一节介绍如何定制。

3. 书籍类定制方法
   写过或看过calibre的recipe的基本上就直接会了。
   因为calibre的recipe模块依赖挺多的，我时间不够，偷懒了，就不移植了，直接根据
   recipe的外形写了一个处理模块。
   * 根据RSS类型，从base模块中导入不同的书籍基类
     from base import BaseFeedBook/WebpageBook/BaseComicBook
   * 如果你感兴趣的网站不提供RSS订阅，则可以继承WebpageBook直接连接网页提取信息。
   * 子类能定制的参数都在BaseFeedBook类的定义中，注释很详细。
   * 处理HTML的BeautifulSoup为4.x版本。
   * cartoonmadbase.py提供了抓取漫画图片的例子。
