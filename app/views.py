from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Employee,Department, Function, EmployeeHistory, Benefit, MenuItem, MenuCategory, News, NewsCategory, camera
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db
from flask_appbuilder.baseviews import expose, BaseView


def department_query():
    return db.session.query(Department)


class EmployeeHistoryView(ModelView):
    datamodel = SQLAInterface(EmployeeHistory)
    #base_permissions = ['can_add', 'can_show']
    list_columns = ['department', 'begin_date', 'end_date']


class EmployeeView(ModelView):
    datamodel = SQLAInterface(Employee)

    list_columns = ['full_name', 'department.name', 'employee_number']
    edit_form_extra_fields = {'department':  QuerySelectField('Department',
                                query_factory=department_query,
                                widget=Select2Widget(extra_classes="readonly"))}


    related_views = [EmployeeHistoryView]
    show_template = 'appbuilder/general/model/show_cascade.html'


class FunctionView(ModelView):
    datamodel = SQLAInterface(Function)
    related_views = [EmployeeView]


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)
    related_views = [EmployeeView]


class BenefitView(ModelView):
    datamodel = SQLAInterface(Benefit)
    add_columns = ['name']
    edit_columns = ['name']
    show_columns = ['name']
    list_columns = ['name']

class MenuItemView(ModelView):
    datamodel = SQLAInterface(MenuItem)
    list_columns = ['id', 'name', 'link', 'menu_category_id']

class MenuCategoryView(ModelView):
    datamodel = SQLAInterface(MenuCategory)
    list_columns = ['id', 'name']

class NewsView(ModelView):
    datamodel = SQLAInterface(News)
    list_columns = ['id', 'title', 'content', 'date', 'newsCat_id']

class NewsCategoryView(ModelView):
    datamodel = SQLAInterface(NewsCategory)
    list_columns = ['id', 'name']
    
    
    
class cameraView(ModelView):
    datamodel = SQLAInterface(camera)
    list_columns = ['id', 'name']




class NewsPageView(BaseView):
    default_view = 'local_news'

    @expose('/local_news/')
    def local_news(self):
        param1 = 'Local News'
        self.update_redirect()
        return self.render_template('news.html', param1 = param1)

    @expose('/global_news/')
    def global_news(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('news.html', param1=param1)
        
    @expose('/news/')
    def news(self):
        param1 = '新聞中心'
        self.update_redirect()
        return self.render_template('news.html', param1=param1)

    @expose('/camera/')
    def camera(self):
        param1 = 'camera'
        self.update_redirect()
        return self.render_template('camera.html', param1=param1)
        
    @expose('/lens/')
    def lens(self):
        param1 = 'lens'
        self.update_redirect()
        return self.render_template('lens.html', param1=param1)
        
    @expose('/phones/')
    def phones(self):
        param1 = 'phones'
        self.update_redirect()
        return self.render_template('phones.html', param1=param1)
        
    @expose('/tablets/')
    def tablets(self):
        param1 = 'tablets'
        self.update_redirect()
        return self.render_template('tablets.html', param1=param1)
        
    @expose('/cars/')
    def cars(self):
        param1 = 'cars'
        self.update_redirect()
        return self.render_template('cars.html', param1=param1)
        
    @expose('/items/')
    def items(self):
        param1 = 'items'
        self.update_redirect()
        return self.render_template('items.html', param1=param1)
        
    @expose('/masterpiece/')
    def masterpiece(self):
        param1 = 'masterpiece'
        self.update_redirect()
        return self.render_template('masterpiece.html', param1=param1)
        
    @expose('/masters/')
    def masters(self):
        param1 = 'masters'
        self.update_redirect()
        return self.render_template('masters.html', param1=param1)  #html not done
        
    @expose('/model/')
    def model(self):
        param1 = 'model'
        self.update_redirect()
        return self.render_template('model.html', param1=param1)    #html not done
        
    @expose('/forums/')
    def forums(self):
        param1 = 'forums'
        self.update_redirect()
        return self.render_template('forums.html', param1=param1)   #html not done
        
    @expose('/travel/')
    def travel(self):
        param1 = 'travel'
        self.update_redirect()
        return self.render_template('travel.html', param1=param1)   #html not done

db.create_all()

""" Page View """
appbuilder.add_view(NewsPageView, 'Local News', category="News")
appbuilder.add_link("Global News", href="/newspageview/global_news/", category="News")

appbuilder.add_link("新聞中心", href="/newspageview/news/", category="新聞中心")

appbuilder.add_link("相機", href="/newspageview/camera/", category="相機鏡頭")
appbuilder.add_link('鏡頭', href="/newspageview/lens/", category="相機鏡頭")

appbuilder.add_link('手機', href="/newspageview/phones/", category="手機頻道")
appbuilder.add_link('平版', href="/newspageview/tablets/", category="手機頻道")

appbuilder.add_link('汽車', href="/newspageview/cars/", category="汽車熱話")

appbuilder.add_link('物品', href="/newspageview/items/", category="二手市集")

appbuilder.add_link('作品', href="/newspageview/masterpiece/", category="作品發表")

appbuilder.add_link('Fever達人', href="/newspageview/masters/", category="攝影圈")    # NO
appbuilder.add_link('FeverModel', href="/newspageview/model/", category="攝影圈")      # NO
appbuilder.add_link('討論區', href="/newspageview/forums/", category="攝影圈")          # NO
appbuilder.add_link('攝影旅遊', href="/newspageview/travel/", category="攝影圈")        # NO



""" Custom Views """
appbuilder.add_view(MenuItemView, "MenuItem", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MenuCategoryView, "MenuCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsView, "News", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsCategoryView, "NewsCategory", icon="fa-folder-open-o", category="Admin")


appbuilder.add_view(cameraView, "camera", icon="fa-folder-open-o", category="Admin")
