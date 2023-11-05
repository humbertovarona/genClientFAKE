def get_country_name(locale):
    country_code = locale.split('_')[-1]
    try:
        country = pycountry.countries.get(alpha_2=country_code)
        country_name = country.name
    except (KeyError, AttributeError):
        country_name = "Unknown"
    return country_name
