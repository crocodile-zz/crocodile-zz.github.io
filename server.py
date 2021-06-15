# 导入这三个模块用来处理http的各种请求
from re import A
import tornado.ioloop
import tornado.web
import tornado.httpserver


###创建一个类来处理请求,主页
class MainPageHandler(tornado.web.RequestHandler):  # 继承这个类，可以接收到来自http的get请求和post的请求
    def get(self):
        self.render("index.html")  # render：渲染 #网页存放的路径


###今日计划页面
class PlanPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("plan.html")

###日期页面
class DatePageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("date.html")


###什么是时间四象限页面
class TimeQuadrantPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("timeQuadrant.html")


###解压放松页面
class RelaxPageHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("relax.html")


# 配置路由
if __name__ == "__main__":
    # 实例化一个application对象
    application = tornado.web.Application([
        (r'/', MainPageHandler),
        (r'/plan', PlanPageHandler),
        (r'/date', DatePageHandler),
        (r'/timeQuadrant', TimeQuadrantPageHandler),
        (r'/relax', RelaxPageHandler)
    ])  # 说明：Application是与服务器对应的接口，里面保存了路由映射表
    application.listen(8600)  # 对8600端口进行监听,url:http://127.0.0.1:8600/
    tornado.ioloop.IOLoop.instance().start()
