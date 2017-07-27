import sublime
import sublime_plugin

SETTINGS_PATH = "Preferences.sublime-settings"

class ChangeTheme(sublime_plugin.WindowCommand):
    settings = sublime.load_settings(SETTINGS_PATH)

    def run(self, theme = 'dark'):
        if theme == 'dark':
            self.settings.set("theme", "Cyanide - Wood.sublime-theme")
            self.settings.set("color_scheme", "Packages/gp_st_colorschemes/Dark/nimbostratus_night.tmTheme")
        else:
            self.settings.set("theme", "Boxy Yesterday.sublime-theme")
            self.settings.set("color_scheme", "Packages/gp_st_colorschemes/Light/NoNameYet.tmTheme")
        sublime.save_settings(SETTINGS_PATH)
