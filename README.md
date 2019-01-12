# SublimeMicrosoftTranslator

Microsoft translator plugin for Sublime Text 3.

## Plugin settings

Preference > Package Settings > Microsoft Translator > Settings - Default (or User)

```json
{
    "api_key" : "",
    "from" : "ja",
    "to" : "en",
}
```

+ `api_key`: Set your subscription key of Translator Text API.
+ `from`: Set the language code of the text to be translated.
+ `to`: Set the language code of the translation.

In other words, the text is translated from `from` to `to`.

For supported languages, please see [https://docs.microsoft.com/en-us/azure/cognitive-services/translator/reference/v3-0-languages?tabs=curl](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/reference/v3-0-languages?tabs=curl).

If you do not have a subscription key, please register Microsoft Azure and obtain a subscription key of Translator Text API. 
In the free plan, you can translate up to 1M characters per month.

## How to use

1. Select text
2. Input `Command + Shift + m` or right click and select `Translate selected text`
3. The results are outputted to a new file.
