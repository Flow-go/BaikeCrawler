# BaikeCrawler
从imooc网站学习爬虫实战，爬取百度百科python页面相关链接的简介。遇到了几个问题：

1. 编码。
   * windows 下默认编码是*gbk*，因此在outputer调用write方法时出错，解决方法是open(filename, 'w', **encoding='utf-8**')指定文件的编码方式。
   * html中也需要声明编码方式。
   * 我把教程中使用的urllib替换成了requests，而requests和Beautifulsoup都会自己猜测编码，不一定能猜对。
2. pycharm。 模块不会创建，功能不熟悉。搁置。
