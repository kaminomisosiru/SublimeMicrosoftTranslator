# -*- coding:utf-8 -*-
import sublime
import sublime_plugin
import sys
import urllib.request
import json
import threading

# Microsoft translator
class MicrosoftTranslatorSettings:
    view_id = None
    thread = None
    token_end_point = "https://api.cognitive.microsoft.com/sts/v1.0/issueToken";
    translate_end_point = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0"

#global settings
settings = MicrosoftTranslatorSettings()
translate_settings = sublime.load_settings("Microsoft Translator.sublime-settings");

class MicrosoftTranslator:

    def __call__(self, command, edit, source_text, _from, to):
        global translate_settings
        sublime.set_timeout(lambda: sublime.status_message("translate...."), 100)
        token = self.get_access_token()
        translated = self.doTranslate(source_text, _from, to, token)
        if translate_settings.get("show_result_in_new_file"):
            sublime.set_timeout(lambda: self.show_result_in_new_file(source_text, translated), 100)
        else:
            sublime.set_timeout(lambda: self.show_result_on_panel(source_text, translated), 100)

    def translate(self, command, edit, _from, to):
        global settings
        sublime.status_message("start translate...")
        sels = command.view.sel()
        source_text = ""
        for sel in sels:
            source_text += command.view.substr(sel)+" "
        if len(source_text) == 1:
            sublime.status_message("not selected. can't translate.")
            return
        if settings.thread != None and settings.thread.isAlive() == True:
            sublime.status_message("already translate now. wait please.")
            return
        settings.thread = threading.Thread(target=self, args=(command, edit, source_text, _from, to,))
        settings.thread.setDaemon(True)
        settings.thread.start()

    def get_access_token(self):
        global settings
        global translate_settings
        headers = {
            'Ocp-Apim-Subscription-Key': translate_settings.get('api_key'),
            'Content-Length': 0
        };
 
        req = urllib.request.Request(settings.token_end_point, headers=headers, method='POST')
        with urllib.request.urlopen(req) as res:
            body = res.read()
        return body.decode('utf-8')

    def doTranslate(self, text, _from, to, token):
        global settings
        global translate_settings
        headers = {
            'Authorization': 'Bearer ' + token,
            'Content-type': 'application/json',
            'profanityAction': translate_settings.get('profanity')
        }
        url = settings.translate_end_point + '&to=' + to
        if _from != '':
            url = url + '&from=' + _from

        body = [{
            'text' : text
        }]
     
        req = urllib.request.Request(url, data=json.dumps(body).encode(), headers=headers, method='POST')
        with urllib.request.urlopen(req) as res:
            response = res.read()
        return json.loads(response.decode('utf-8'))[0]['translations'][0]['text']

    def get_result_view(self):
        active_window = sublime.active_window()
        for view in active_window.views():
            if view.id() == settings.view_id:
                return view
        new_view = active_window.new_file()
        settings.view_id = new_view.id()
        new_view.set_name("Microsoft Transrator Results")
        new_view.set_scratch(True)
        return new_view

    def get_result_view_panel(self):
        window = sublime.active_window()
        output_view = window.create_output_panel("MicrosoftTransratorResults")
        window.run_command("show_panel",{"panel": "output.MicrosoftTransratorResults"})
        return output_view

    def show_result_in_new_file(self, source_text, translated):
        view = self.get_result_view()
        result = "Translate Result\n"
        result += "------------------------\n"
        result += source_text + "\n"
        result += "- - - - - - - - - - - - \n"
        result += translated + "\n"
        result += "------------------------\n"
        result += "\n"
        view.set_read_only(False)
        view.run_command('append', {'characters': result})
        view.run_command('goto_line', {"line": 0})
        view.show(0)

    def show_result_on_panel(self, source_text, translated):
        output_view = self.get_result_view_panel()
        result = "Translate Result\n"
        # result = "------------------------\n"
        result += "\n"
        # result += source_text + "\n"
        # result += "↓\n"
        result += translated + "\n"
        result += "\n"
        output_view.set_read_only(False)
        output_view.settings().set("word_wrap", True)
        output_view.run_command('append', {'characters': result})
        output_view.set_read_only(True)

class SelectTranslateCommand(sublime_plugin.TextCommand):
    translator = MicrosoftTranslator()
    def __init__(self, *args, **kwargs):
        sublime_plugin.TextCommand.__init__(self, *args, **kwargs)
        self.setting = sublime.load_settings("SublimeMicrosoftTranslator.sublime-settings")
    def run(self, edit):
        global settings
        global translate_settings
        self.translator.translate(self, edit, translate_settings.get("from"), translate_settings.get("to"))
    def description(self, args):
        return "Microsoft translator plugin for Sublime Text 3"

class SelectTranslateReverseCommand(sublime_plugin.TextCommand):
    translator = MicrosoftTranslator()
    def __init__(self, *args, **kwargs):
        sublime_plugin.TextCommand.__init__(self, *args, **kwargs)
    def run(self, edit):
        global settings
        global translate_settings
        self.translator.translate(self, edit, translate_settings.get("to"), translate_settings.get("from"))
    def description(self, args):
        return "Microsoft translator plugin for Sublime Text 3"