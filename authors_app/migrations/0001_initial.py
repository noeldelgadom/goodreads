# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-04 16:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128)),
                ('last_name', models.CharField(max_length=128)),
                ('nationality', models.CharField(choices=[('AF', 'Afghan'), ('AL', 'Albanian'), ('DZ', 'Algerian'), ('AD', 'Andorran'), ('AO', 'Angolan'), ('AR', 'Argentinian'), ('AM', 'Armenian'), ('AU', 'Australian'), ('AT', 'Austrian'), ('AZ', 'Azerbaijani'), ('BS', 'Bahamian'), ('BH', 'Bahraini'), ('BD', 'Bangladeshi'), ('BB', 'Barbadian'), ('BY', 'Belorussian'), ('BE', 'Belgian'), ('BZ', 'Belizian'), ('BJ', 'Beninese'), ('BT', 'Bhutanese'), ('BO', 'Bolivian'), ('BA', 'Bosnian'), ('BW', 'Botswanan'), ('BR', 'Brazilian'), ('GB', 'British'), ('BN', 'Bruneian'), ('BG', 'Bulgarian'), ('BF', 'Burkinese'), ('MM', 'Burmese'), ('BF', 'Burundian'), ('BI', 'Cambodian'), ('CM', 'Cameroonian'), ('CA', 'Canadian'), ('CV', 'Cape Verdean'), ('TD', 'Chadian'), ('CL', 'Chilean'), ('CN', 'Chinese'), ('CO', 'Colombian'), ('CG', 'Congolese'), ('CR', 'Costa Rican'), ('HR', 'Croatian'), ('CU', 'Cuban'), ('CY', 'Cypriot'), ('CZ', 'Czech'), ('DK', 'Danish'), ('DJ', 'Djiboutian'), ('DM', 'Dominican'), ('DO', 'Dominican'), ('EC', 'Ecuadorean'), ('EG', 'Egyptian'), ('SV', 'Salvadorean'), ('GB', 'English'), ('ER', 'Eritrean'), ('EE', 'Estonian'), ('ET', 'Ethiopian'), ('FJ', 'Fijian'), ('FI', 'Finnish'), ('FR', 'French'), ('GA', 'Gabonese'), ('GM', 'Gambian'), ('GE', 'Georgian'), ('DE', 'German'), ('GH', 'Ghanaian'), ('GR', 'Greek'), ('GD', 'Grenadian'), ('GT', 'Guatemalan'), ('GQ', 'Guinean'), ('GY', 'Guyanese'), ('HT', 'Haitian'), ('NL', 'Dutch'), ('HN', 'Honduran'), ('HU', 'Hungarian'), ('IS', 'Icelandic'), ('IO', 'Indian'), ('ID', 'Indonesian'), ('IR', 'Iranian'), ('IQ', 'Iraqi'), ('IE', 'Irish'), ('IL', 'Israeli'), ('IT', 'Italian'), ('JM', 'Jamaican'), ('JP', 'Japanese'), ('JO', 'Jordanian'), ('KZ', 'Kazakh'), ('KE', 'Kenyan'), ('KW', 'Kuwaiti'), ('LA', 'Laotian'), ('LV', 'Latvian'), ('LB', 'Lebanese'), ('LR', 'Liberian'), ('LY', 'Libyan'), ('LT', 'Lithuanian'), ('MK', 'Macedonian'), ('MG', 'Malagasay'), ('MW', 'Malawian'), ('MY', 'Malaysian'), ('MV', 'Maldivian'), ('ML', 'Malian'), ('MT', 'Maltese'), ('MR', 'Mauritanian'), ('MU', 'Mauritian'), ('MX', 'Mexican'), ('MD', 'Moldovan'), ('MC', 'Monacan'), ('MN', 'Mongolian'), ('ME', 'Montenegrin'), ('MA', 'Moroccan'), ('MZ', 'Mozambican'), ('NA', 'Namibian'), ('NP', 'Nepalese'), ('NI', 'Nicaraguan'), ('NE', 'Nigerien'), ('NG', 'Nigerian'), ('KP', 'North Korean'), ('NO', 'Norwegian'), ('OM', 'Omani'), ('PK', 'Pakistani'), ('PA', 'Panamanian'), ('PG', 'Guinean'), ('PY', 'Paraguayan'), ('PE', 'Peruvian'), ('PH', 'Philippine'), ('PL', 'Polish'), ('PT', 'Portuguese'), ('QA', 'Qatari'), ('RO', 'Romanian'), ('RU', 'Russian'), ('RW', 'Rwandan'), ('SA', 'Saudi'), ('AE', 'Scottish'), ('SN', 'Senegalese'), ('RS', 'Serbian'), ('SC', 'Seychellois'), ('SL', 'Sierra Leonian'), ('SG', 'Singaporean'), ('SK', 'Slovak'), ('SI', 'Slovenian'), ('SO', 'Somali'), ('ZA', 'South African'), ('KR', 'South Korean'), ('ES', 'Spanish'), ('LK', 'Sri Lankan'), ('SD', 'Sudanese'), ('SR', 'Surinamese'), ('SZ', 'Swazi'), ('SE', 'Swedish'), ('CH', 'Swiss'), ('SY', 'Syrian'), ('TW', 'Taiwanese'), ('TJ', 'Tadjik'), ('TZ', 'Tanzanian'), ('TH', 'Thai'), ('TG', 'Togolese'), ('TT', 'Trinidadian'), ('TN', 'Tunisian'), ('TR', 'Turkish'), ('TM', 'Turkmen'), ('TV', 'Tuvaluan'), ('UG', 'Ugandan'), ('UA', 'Ukrainian'), ('UY', 'Uruguayan'), ('UZ', 'Uzbek'), ('VU', 'Vanuatuan'), ('VE', 'Venezuelan'), ('VN', 'Vietnamese'), ('GB', 'Welsh'), ('YE', 'Yemeni'), ('ZM', 'Zambian'), ('ZW', 'Zimbabwean')], max_length=2)),
                ('biography', models.TextField()),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('genre', models.CharField(choices=[('FA', 'Fantasy'), ('FI', 'Fiction'), ('CH', 'Children'), ('SF', 'Sci-Fiction'), ('RO', 'Romance'), ('ME', 'Memoirs'), ('SH', 'Self-Help'), ('HI', 'History'), ('RE', 'Religion'), ('BI', 'Biography')], max_length=2)),
                ('age', models.PositiveIntegerField()),
                ('alive', models.BooleanField()),
            ],
        ),
    ]
