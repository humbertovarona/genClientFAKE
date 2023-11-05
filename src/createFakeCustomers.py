def createFakeCustomers(databasename, max_clients=1000, max_age=75):
    LOCALELIST = ['de_AT', 'de_CH', 'de_DE', 'en_AU',
                  'en_CA', 'en_GB', 'en_IE', 'en_IN', 'en_NZ', 'en_PH', 'en_TH', 'en_US', 'es_AR', 'es_CL',
                  'es_CO', 'es_ES', 'es_MX', 'fr_BE', 'fr_CA', 'fr_CH', 'fr_FR', 'fr_CA', 'ga_IE', 'it_CH', 'it_IT',
                  'pt_BR', 'pt_PT']

    conn = sqlite3.connect(databasename)
    conn.execute('PRAGMA encoding = "UTF-8"')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS fakeCustomers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            lastname TEXT,
            birthday DATE,
            age INTEGER,
            gender TEXT,
            language1 TEXT,
            language2 TEXT,
            raddress TEXT,
            city TEXT,
            country TEXT,
            institution TEXT
        )
    ''')

    for _ in range(max_clients):
        SelectedLocale = random.choice(LOCALELIST)
        fake = Faker(SelectedLocale)
        gender = fake.random_element(elements=('Male', 'Female'))
        name = fake.first_name_male() if gender == 'Male' else fake.first_name_female()
        lastname = fake.last_name()
        birthday = fake.date_of_birth(minimum_age=18, maximum_age=max_age)
        age = fake.random_int(min=18, max=max_age)
        language1 = get_language_name(SelectedLocale)
        if random.random() < 0.1:
            available_languages = ['English', 'Spanish', 'Italian', 'French', 'Portuguese', 'German']
            if language1 in available_languages:
                available_languages.remove(language1)
            language2 = fake.random_element(elements=available_languages)

        else:
            language2 = None
        raddress = fake.address()
        country = get_country_name(SelectedLocale)

        city = fake.city()
        institution = None

        if age >= 18 and age <= 65 and fake.random_element([True, False]):
            institution = fake.company_suffix() + ' ' + fake.company()

        cursor.execute('''
                    INSERT INTO fakeCustomers (name, lastname, birthday, age, gender, language1, language2, raddress, city, country, institution)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, lastname, birthday, age, gender, language1, language2, raddress, city, country, institution))
    conn.commit()
    conn.close()
    print("Fake data generation completed.")
