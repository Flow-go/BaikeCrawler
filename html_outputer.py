# coding:utf-8
class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', 'w', encoding='utf-8') # 这里的设置，是由于windows系统的限制

        fout.write("<html>")
        fout.write("<head><meta charset='utf-8'></head>") # 这里不进行设置，在浏览器中会出现乱码
        fout.write("<body>")
        fout.write("<table>")

        
        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'])
            fout.write("<td>%s</td>" % data['title'])
            fout.write("<td>%s</td>" % data['summary'])
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()
