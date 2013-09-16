from django.shortcuts import render_to_response
from django.core.context_processors import csrf


class MenuObject:
    name = None
    url = None
    forceSubmenu = False
    icon = None

    submenu = []

    def __init__(self, name, url=None, icon=None, disabled=False):
        self.name = name
        self.icon = icon

        self.forceSubmenu = False
        self.submenu = []

        if url is None:
            self.forceSubmenu = True
        else:
            self.url = url

        self.disabled = disabled

    def addSubMenu(self, menu):
        self.submenu.append(menu)

    def addSubitem(self, name, url, icon=None, disabled=False):
        self.submenu.append(MenuObject(name, url, icon, disabled))

    def hasSubmenu(self):
        return self.submenu

    def canShow(self):
        if self.forceSubmenu and self.hasSubmenu():
            return True
        elif not self.forceSubmenu:
            return True
        return False


def render_with_user(request, template_name, context={}):
    from website.settings import DEBUG

    context["debugMode"] = DEBUG

    if request.User is not None:
        context["menu"] = []

        evaluationsMenu = MenuObject("Evaluations")
        if request.User.hasAnyPermissions("evaluation.all.create", "evaluation.department.create", "evaluation.self.create"):
            evaluationsMenu.addSubitem("New Evaluation", "newEvaluation")
        if request.User.hasAnyPermissions("evaluation.all.create", "evaluation.department.create", "evaluation.all.view", "evaluation.department.view", "evaluation.self.view"):
            evaluationsMenu.addSubitem("View Evaluations", "evaluationList")

        context["menu"].append(evaluationsMenu)

        memosMenu = MenuObject("Memos", "memos")

        if not request.User.isSuper and not request.User.hasPermission("manager"):
            context["menu"].append(memosMenu)

        formsMenu = MenuObject("Forms", "forms")
        if request.User.hasAnyPermissions("evaluation.all.create", "forms"):
            context["menu"].append(formsMenu)

        accountMenu = MenuObject("Accounts")
        if request.User.hasAnyPermissions("teacher.all.create", "teacher.department.create") or request.User.isSuper:
            accountMenu.addSubitem("Create New Account", "createAccount")
        if request.User.hasAnyPermissions("teacher.all.create", "teacher.department.create", "teacher.all.delete", "teacher.department.delete") or request.User.isSuper:
            accountMenu.addSubitem("View All Accounts", "accountList")
        if request.User.hasAnyPermissions("teacher.all.create", "teacher.all.delete") or request.User.isSuper:
            accountMenu.addSubitem("Manage Groups", "departmentList")
        if request.User.hasAnyPermissions("teacher.all.create", "teacher.all.delete") or request.User.isSuper:
            accountMenu.addSubitem("Manage Schools", "schoolList")
        if request.User.isSuper:
            accountMenu.addSubitem("Batch Create", "importData")

        context["menu"].append(accountMenu)

        reportMenu = MenuObject("Reports")
        if request.User.hasPermission("reports"):
            stateMenu = MenuObject("State")
            stateMenu.addSubitem("Massachusetts", "reports/state_ma")
            stateMenu.addSubitem("Other states (coming soon)", "reports", None,True)

            reportMenu.addSubitem("Overview", "reportsList")
            reportMenu.addSubMenu(stateMenu)
            reportMenu.addSubitem("Custom", "customReport")

        context["menu"].append(reportMenu)

        if request.User.hasPermission("manager"):
            context["menu"].append(MenuObject("Create Super Account", "manage/createSuper"))
            context["menu"].append(MenuObject("Manage Super Accounts", "manage/supers"))
            context["menu"].append(MenuObject("Manage Forms", "forms"))
            context["menu"].append(MenuObject("Change Password", "manage/changePassword"))

        context["user"] = request.User

    context.update(csrf(request))
    return render_to_response(template_name, context)
