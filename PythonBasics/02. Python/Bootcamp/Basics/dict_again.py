# -*- coding: utf-8 -*-
"""
Created on Fri Dec 29 13:21:43 2023

@author: manoj
"""

countries = {
    'France': {'Capital': 'Paris', 'Language': 'French'},
    'United Kingdom': {'Capital': 'London', 'Language': 'English'},
    'United States of America': {'Capital': 'Washington DC', 'Language': 'English'},
    'Italy': {'Capital': 'Rome', 'Language': 'Italian'},
    'India': {'Capital': 'Delhi', 'Language': 'Hindi, Tamil, Malayalam, Bengali, Assamese, Oriya, Marathi, Telugu, Kannada, Punjabi, Gujarati, Urdu, Sindhi, Kashmiri, Nepali, Konkani, Sindhi, Dogri, Maithili, Santali, Manipuri, Bodo, and various others'},
    'Canada': {'Capital': 'Ottawa', 'Language': 'English, French'},
    'Australia': {'Capital': 'Canberra', 'Language': 'English'},
    'Germany': {'Capital': 'Berlin', 'Language': 'German'},
    'Spain': {'Capital': 'Madrid', 'Language': 'Spanish'},
    'China': {'Capital': 'Beijing', 'Language': 'Mandarin'},
    'Japan': {'Capital': 'Tokyo', 'Language': 'Japanese'},
    'Brazil': {'Capital': 'Brasília', 'Language': 'Portuguese'},
    'South Korea': {'Capital': 'Seoul', 'Language': 'Korean'},
    'Mexico': {'Capital': 'Mexico City', 'Language': 'Spanish'},
    'Russia': {'Capital': 'Moscow', 'Language': 'Russian'},
    'South Africa': {'Capital': 'Pretoria, Cape Town, Bloemfontein', 'Language': 'Afrikaans, English, Zulu, Xhosa, Sotho, Tswana, Venda, Tsonga, Swazi, Ndebele'},
    'Argentina': {'Capital': 'Buenos Aires', 'Language': 'Spanish'},
    'Egypt': {'Capital': 'Cairo', 'Language': 'Arabic'},
    'Nigeria': {'Capital': 'Abuja', 'Language': 'English'},
    'Saudi Arabia': {'Capital': 'Riyadh', 'Language': 'Arabic'},
    'Turkey': {'Capital': 'Ankara', 'Language': 'Turkish'},
    'Indonesia': {'Capital': 'Jakarta', 'Language': 'Indonesian'},
    'Thailand': {'Capital': 'Bangkok', 'Language': 'Thai'},
    'Sweden': {'Capital': 'Stockholm', 'Language': 'Swedish'},
    'Norway': {'Capital': 'Oslo', 'Language': 'Norwegian'},
    'Switzerland': {'Capital': 'Bern', 'Language': 'German, French, Italian, Romansh'},
    'Netherlands': {'Capital': 'Amsterdam', 'Language': 'Dutch'},
    'Belgium': {'Capital': 'Brussels', 'Language': 'Dutch, French, German'},
    'Portugal': {'Capital': 'Lisbon', 'Language': 'Portuguese'},
}


for key, value in countries.items():
    print(f"Capital of {key} is {value['Capital']}. They speak {value['Language']}.")