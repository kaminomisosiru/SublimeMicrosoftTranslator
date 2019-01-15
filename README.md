# SublimeMicrosoftTranslator

Translate your code using Microsoft Translator Text API.

**Important**: In order to use this extension, you'll need to provide a Microsoft Translator Text API key of your own. 
**Without the API key, this extension is useless for you.** 

## Installation

1. Clone the repository in your Sublime Text Packages directory:

    ```shell
    git clone https://github.com/kaminomisosiru/SublimeMicrosoftTranslator.git
    ```

    or download the latest source from GitHub and copy the whole directory into the Packages directory.

2. Create Microsoft Translator Text API Key. You can use [How to sign up for the Translator Text API](https://docs.microsoft.com/en-us/azure/cognitive-services/translator/translator-text-how-to-signup).
3. Add your API key in user settings configuration.
4. Configure desired 'translate to' (and 'translate from' if necessary) language in user settings configuration.

See below for configuration details.

## Package settings

`Preference > Package Settings > Microsoft Translator > Settings - Default (or User)`

```json
{
    "api_key" : "",
    "show_result_in_new_file": false,
    "from" : "ja",
    "to" : "en",
}
```

+ `api_key`: Set your Translator Text API key.
+ `show_result_in_new_file`: If `true`, the translation result is outputted to a new file; otherwise, the the translation result is showed on blow panel.
+ `from`: Set 'translate from' language code .
+ `to`: Set 'translate to' language code.

For supported languages, please see [Language code table](https://gist.github.com/kaminomisosiru/7a8511d239a0848d8689ed0cd0ab1b2d).

## How to use

### Translate selected text

Translate the text from `from` to `to`.

1. Select the text
2. Use the shortcut `Command + Shift + m`, or right click and select `Translate selected text`
3. The results are outputted to a new file or panel.

### Reverse translate selected text

Translate the text from `to` to `from`.

1. Select the text
2. Use the shortcut `Command + Shift + Alt + m`, or right click and select `Reverse translate selected text`

## License

MIT License

## References

[Bing Translator APIを使ったSublime Text 2の翻訳プラグインが無かったので作った話](http://visible-true.blogspot.com/2012/12/bing-translator-apisublime-text-2.html)
