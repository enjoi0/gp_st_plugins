import sublime
import sublime_plugin

SETTINGS_PATH = "Preferences.sublime-settings"

class ChangeTheme(sublime_plugin.WindowCommand):
    def run(self, theme = 'dark'):
        settings = sublime.load_settings(SETTINGS_PATH)

        if theme == 'dark':
            settings.set("theme", "Cyanide - Wood.sublime-theme")
            settings.set("color_scheme", "Packages/gp_st_colorschemes/Dark/nimbostratus_night.tmTheme")
        else:
            settings.set("theme", "Boxy Yesterday.sublime-theme")
            settings.set("color_scheme", "Packages/gp_st_colorschemes/Light/NoNameYet.tmTheme")
            
        sublime.save_settings(SETTINGS_PATH)
