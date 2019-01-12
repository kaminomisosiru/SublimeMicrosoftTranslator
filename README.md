# SublimeMicrosoftTranslator

Microsoft translator plugin for Sublime Text 3.

## Plugin settings

Preference > Package Settings > Microsoft Translator > Settings - Default (or User)

```json
{
    "api_key" : "",
    "profanity": "NoAction",
    "from" : "ja",
    "to" : "en",
}
```

+ `api_key`: Set your subscription key of Translator Text API.
+ `profanity`: Profanities should be treated in translations. Possible values are: `NoAction` (default), `Marked` or `Deleted`. See [Handle profanity](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/reference/v3-0-translate?tabs=curl#handle-profanity) for more details.
+ `from`: Set the language code of the text to be translated.
+ `to`: Set the language code of the translation.

In other words, the text is translated from `from` to `to`.

For supported languages, please see [Translator Text API 3.0: Languages](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/reference/v3-0-languages).

If you do not have a subscription key, please register Microsoft Azure and obtain a subscription key of Translator Text API. 
In the free plan, you can translate up to 1M characters per month.

## How to use

1. Select text
2. Input `Command + Shift + m` or right click and select `Translate selected text`
3. The results are outputted to a new file.

## License

MIT License

## Reference

[Bing Translator APIを使ったSublime Text 2の翻訳プラグインが無かったので作った話](http://visible-true.blogspot.com/2012/12/bing-translator-apisublime-text-2.html)
