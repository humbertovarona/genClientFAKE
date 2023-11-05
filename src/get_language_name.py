def get_language_name(locale):
    try:
        lang = locale.split('_')[0]
        language = pycountry.languages.get(alpha_2=lang)
        language_name = language.name
        return language_name
    except (KeyError, AttributeError):
        return "Unknown"
