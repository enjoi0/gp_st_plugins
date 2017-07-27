import sublime
import sublime_plugin


class CommentAndMoveToNextLine(sublime_plugin.WindowCommand):
    def run(self):
        self.window.run_command("toggle_comment")
        self.window.run_command("move", { "by": "lines", "forward": True })
