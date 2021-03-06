# -*- coding:utf-8 -*-
import sublime
import sublime_plugin
import requests
import json
import threading

class MicrosoftTranslatorSettings:
    view_id = None
    thread = None
    translate_end_point = "https://api.cognitive.microsofttranslator.com/translate?api-version=3.0"

#global settings
settings = MicrosoftTranslatorSettings()
translate_settings = sublime.load_settings("Microsoft Translator.sublime-settings");

class MicrosoftTranslator:

    def __call__(self, command, edit, source_text, _from, to):
        sublime.set_timeout(lambda: sublime.status_message("Translating...."), 100)
        translated = self.doTranslate(source_text, _from, to)
        if translate_settings.get("show_result_in_new_file"):
            sublime.set_timeout(lambda: self.show_result_in_new_file(source_text, translated), 100)
        else:
            sublime.set_timeout(lambda: self.show_result_on_panel(source_text, translated), 100)
        sublime.status_message("Finish translation!")

    def translate(self, command, edit, _from, to):
        global settings
        sublime.status_message("Start translation...")
        sels = command.view.sel()
        source_text = ""
        for sel in sels:
            source_text += command.view.substr(sel)+" "
        source_text = source_text.strip()
        if len(source_text) == 0:
            sublime.message_dialog("Not selected. Can't translate.")
            return
        if settings.thread != None and settings.thread.isAlive() == True:
            sublime.message_dialog("Already translate now. Please wait.")
            return
        settings.thread = threading.Thread(target=self, args=(command, edit, source_text, _from, to,))
        settings.thread.setDaemon(True)
        settings.thread.start()

    def doTranslate(self, text, _from, to):
        headers = {
            'Ocp-Apim-Subscription-Key': translate_settings.get('api_key'),
            'Content-type': 'application/json',
        }
        params = {
            'to': to,
            'from': _from
        }

        body = [{
            'text' : text
        }]
        response = requests.post(settings.translate_end_point, headers=headers, params=params, json=body)
        result = response.json()
        if isinstance(result, list):
            return response.json()[0]['translations'][0]['text']
        else:
            return "Error!: " + result['error']['message']

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
        result = translated
        view.set_read_only(False)
        view.run_command('append', {'characters': result})
        view.show(0)

    def show_result_on_panel(self, source_text, translated):
        output_view = self.get_result_view_panel()
        result = "Translate Result:\n"
        result += "\n"
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
    def run(self, edit):
        self.translator.translate(self, edit, translate_settings.get("from"), translate_settings.get("to"))
    def description(self, args):
        return "Microsoft translator package for Sublime Text 3"

class SelectTranslateReverseCommand(sublime_plugin.TextCommand):
    translator = MicrosoftTranslator()
    def __init__(self, *args, **kwargs):
        sublime_plugin.TextCommand.__init__(self, *args, **kwargs)
    def run(self, edit):
        self.translator.translate(self, edit, translate_settings.get("to"), translate_settings.get("from"))
    def description(self, args):
        return "Microsoft translator package for Sublime Text 3"