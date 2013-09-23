from django.shortcuts import render
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

    user = request.user
    context["menu"] = []

    if user.is_authenticated():
        context["name"] = user.fullname()
        context["user"] = request.user
        context.update(csrf(request))

        speedMenu = MenuObject("High Speed")
        speedMenu.addSubitem("Normal High Speed", "home")
        speedMenu.addSubitem("Very High Speed", "home")
        speedMenu.addSubitem("Extreme High Speed", "home")
        context["menu"].append(speedMenu)

        priceMenu = MenuObject("Low price")
        priceMenu.addSubitem("Normal Low price", "home")
        priceMenu.addSubitem("Very Low price", "home")
        priceMenu.addSubitem("Extreme Low price", "home")
        context["menu"].append(priceMenu)

        securityMenu = MenuObject("High Security")
        securityMenu.addSubitem("Normal High Security", "home")
        securityMenu.addSubitem("Very High Security", "home")
        securityMenu.addSubitem("Extreme High Security", "home")
        context["menu"].append(securityMenu)

        return render(request, template_name, context)

    else:
        context["user"] = None
        context["name"] = "Login or sign up"

        return render(request, template_name, context)
