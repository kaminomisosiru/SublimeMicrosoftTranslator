# SublimeMicrosoftTranslator

Microsoft translator plugin for Sublime Text 3.

## Installation

Clone the repository in your Sublime Text Packages directory:

```shell
git clone https://github.com/kaminomisosiru/SublimeMicrosoftTranslator.git
```

or download the latest source from GitHub and copy the whole directory into the Packages directory.

## Plugin settings

Preference > Package Settings > Microsoft Translator > Settings - Default (or User)

```json
{
    "api_key" : "",
    "show_result_in_new_file": false,
    "profanity": "NoAction",
    "from" : "ja",
    "to" : "en",
}
```

+ `api_key`: Set your subscription key of Translator Text API.
+ `show_result_in_new_file`: If `true`, the translation result is outputted to a new file; otherwise, the the translation result is showed on panel.
+ `profanity`: Profanities should be treated in translations. Possible values are: `NoAction` (default), `Marked` or `Deleted`. See [Handle profanity](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/reference/v3-0-translate?tabs=curl#handle-profanity) for more details.
+ `from`: Set the language code of the text to be translated.
+ `to`: Set the language code of the translation.

In other words, the text is translated from `from` to `to`.

For supported languages, please see [Translator Text API 3.0: Languages](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/reference/v3-0-languages).

If you do not have a subscription key, please register Microsoft Azure and obtain a subscription key of Translator Text API. 
In the free plan, you can translate up to 2M characters per month.

## How to use

### Translate selected text

1. Select text
2. Input `Command + Shift + m`, or right click and select `Translate selected text`
3. The results are outputted to a new file or panel.

### Reverse translate selected text

Translate the text from `to` to `_from`.

1. Select text
2. Input `Command + Shift + Alt + m`, or right click and select `Reverse translate selected text`
3. The results are outputted to a new file or panel.

### Example

If settings are:

```json
{
    "from": "ja",
    "to": "en"
}
```

then

"吾輩は猫である。" is translated into "I am a cat." by `Translate selected text`, and<br>
"I am a cat." is translated into "吾輩は猫である。" by `Reverse translate selected text`.


## License

MIT License

## Reference

[Bing Translator APIを使ったSublime Text 2の翻訳プラグインが無かったので作った話](http://visible-true.blogspot.com/2012/12/bing-translator-apisublime-text-2.html)
