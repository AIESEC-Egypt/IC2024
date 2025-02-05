# Generated by Django 4.2.9 on 2024-02-19 18:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0010_delegate_gender_alter_delegate_age_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='delegate',
            old_name='expectation_from_cc_team',
            new_name='agenda_expectations',
        ),
        migrations.RenameField(
            model_name='delegate',
            old_name='expectation_from_egyptian_nights',
            new_name='cc_team_expecations',
        ),
        migrations.RenameField(
            model_name='delegate',
            old_name='allergies',
            new_name='other_roles',
        ),
        migrations.RenameField(
            model_name='delegate',
            old_name='passport_size_picture_of_the_candidate',
            new_name='picture_of_the_candidate',
        ),
        migrations.RemoveField(
            model_name='delegate',
            name='age',
        ),
        migrations.RemoveField(
            model_name='delegate',
            name='place_of_birth',
        ),
        migrations.AddField(
            model_name='delegate',
            name='academic_background',
            field=models.CharField(blank=True, choices=[(None, 'Please select your academic background'), ('Associate degree', 'Associate degree'), ("Bachelor's degree", "Bachelor's degree"), ("Master's degree", "Master's degree"), ('Doctoral degree', 'Doctoral degree')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='covid_certificate',
            field=models.CharField(blank=True, choices=[(None, 'Are you interested?'), ('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='egyptian_nights_expectations',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='food',
            field=models.CharField(blank=True, choices=[(None, 'Please select your food preferences'), ('Vegetarian', 'Vegetarian'), ('Non Vegetarian', 'Non Vegetarian'), ('Vegan', 'Vegan'), ('Halal', 'Halal'), ('Lactose Intolerant', 'Lactose Intolerant'), ('Other', 'Other')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='logistical_expectations',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='room_preference',
            field=models.CharField(blank=True, choices=[(None, 'Please select your room preference'), ('Double', 'Double'), ('Triple', 'Triple')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='visa_support',
            field=models.CharField(blank=True, choices=[(None, 'Are you interested?'), ('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='created_at',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='current_living_country',
            field=models.CharField(blank=True, choices=[(None, 'Please select the country territory you currently live in'), ('Russia', 'Russia'), ('Antarctica', 'Antarctica'), ('Canada', 'Canada'), ('China', 'China'), ('United States', 'United States'), ('Brazil', 'Brazil'), ('Australia', 'Australia'), ('India', 'India'), ('Argentina', 'Argentina'), ('Kazakhstan', 'Kazakhstan'), ('Algeria', 'Algeria'), ('Democratic Republic of the Congo', 'Democratic Republic of the Congo'), ('Kingdom of Denmark', 'Kingdom of Denmark'), ('Greenland', 'Greenland'), ('Saudi Arabia', 'Saudi Arabia'), ('Mexico', 'Mexico'), ('Indonesia', 'Indonesia'), ('Sudan', 'Sudan'), ('Libya', 'Libya'), ('Iran', 'Iran'), ('Mongolia', 'Mongolia'), ('Peru', 'Peru'), ('Chad', 'Chad'), ('Niger', 'Niger'), ('Angola', 'Angola'), ('Mali', 'Mali'), ('South Africa', 'South Africa'), ('Colombia', 'Colombia'), ('Ethiopia', 'Ethiopia'), ('Bolivia', 'Bolivia'), ('Mauritania', 'Mauritania'), ('Egypt', 'Egypt'), ('Tanzania', 'Tanzania'), ('Nigeria', 'Nigeria'), ('Venezuela', 'Venezuela'), ('Pakistan', 'Pakistan'), ('Namibia', 'Namibia'), ('Mozambique', 'Mozambique'), ('Turkey', 'Turkey'), ('Chile', 'Chile'), ('Zambia', 'Zambia'), ('Myanmar', 'Myanmar'), ('Afghanistan', 'Afghanistan'), ('South Sudan', 'South Sudan'), ('France', 'France'), ('Somalia', 'Somalia'), ('Central', 'Central'), ('Ukraine', 'Ukraine'), ('Madagascar', 'Madagascar'), ('Botswana', 'Botswana'), ('Kenya', 'Kenya'), ('France', 'France'), ('Yemen', 'Yemen'), ('Thailand', 'Thailand'), ('Spain', 'Spain'), ('Turkmenistan', 'Turkmenistan'), ('Cameroon', 'Cameroon'), ('Papua New Guinea', 'Papua New Guinea'), ('Uzbekistan', 'Uzbekistan'), ('Sweden', 'Sweden'), ('Morocco', 'Morocco'), ('Iraq', 'Iraq'), ('Paraguay', 'Paraguay'), ('Zimbabwe', 'Zimbabwe'), ('Norway', 'Norway'), ('Japan', 'Japan'), ('Germany', 'Germany'), ('Congo', 'Congo'), ('Finland', 'Finland'), ('Vietnam', 'Vietnam'), ('Malaysia', 'Malaysia'), ('Norway', 'Norway'), ('Ivory Coast', 'Ivory Coast'), ('Poland', 'Poland'), ('Oman', 'Oman'), ('Italy', 'Italy'), ('Philippines', 'Philippines'), ('Ecuador', 'Ecuador'), ('Burkina Faso', 'Burkina Faso'), ('New Zealand', 'New Zealand'), ('Gabon', 'Gabon'), ('Western Sahara', 'Western Sahara'), ('Guinea', 'Guinea'), ('United', 'United'), ('Uganda', 'Uganda'), ('Ghana', 'Ghana'), ('Romania', 'Romania'), ('Laos', 'Laos'), ('Guyana', 'Guyana'), ('Belarus', 'Belarus'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Senegal', 'Senegal'), ('Syria', 'Syria'), ('Cambodia', 'Cambodia'), ('Somaliland', 'Somaliland'), ('Uruguay', 'Uruguay'), ('Suriname', 'Suriname'), ('Tunisia', 'Tunisia'), ('Bangladesh', 'Bangladesh'), ('Nepal', 'Nepal'), ('Tajikistan', 'Tajikistan'), ('Greece', 'Greece'), ('Nicaragua', 'Nicaragua'), ('North Korea', 'North Korea'), ('Malawi', 'Malawi'), ('Eritrea', 'Eritrea'), ('Benin', 'Benin'), ('Honduras', 'Honduras'), ('Liberia', 'Liberia'), ('Bulgaria', 'Bulgaria'), ('Cuba', 'Cuba'), ('Guatemala', 'Guatemala'), ('Iceland', 'Iceland'), ('South Korea', 'South Korea'), ('Hungary', 'Hungary'), ('Portugal', 'Portugal'), ('Jordan', 'Jordan'), ('Serbia', 'Serbia'), ('Azerbaijan', 'Azerbaijan'), ('Austria', 'Austria'), ('United Arab Emirates', 'United Arab Emirates'), ('Czech Republic', 'Czech Republic'), ('Panama', 'Panama'), ('Sierra Leone', 'Sierra Leone'), ('Ireland', 'Ireland'), ('Georgia', 'Georgia'), ('Sri Lanka', 'Sri Lanka'), ('Lithuania', 'Lithuania'), ('Latvia', 'Latvia'), ('Svalbard', 'Svalbard'), ('Togo', 'Togo'), ('Croatia', 'Croatia'), ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'), ('Costa Rica', 'Costa Rica'), ('Slovakia', 'Slovakia'), ('Dominican Republic', 'Dominican Republic'), ('Estonia', 'Estonia'), ('Denmark', 'Denmark'), ('Netherlands', 'Netherlands'), ('Switzerland', 'Switzerland'), ('Bhutan', 'Bhutan'), ('Taiwan', 'Taiwan'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Moldova', 'Moldova'), ('Belgium', 'Belgium'), ('Lesotho', 'Lesotho'), ('Armenia', 'Armenia'), ('Solomon', 'Solomon'), ('Albania', 'Albania'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Burundi', 'Burundi'), ('Haiti', 'Haiti'), ('Rwanda', 'Rwanda'), ('North', 'North'), ('Djibouti', 'Djibouti'), ('Belize', 'Belize'), ('El Salvador', 'El Salvador'), ('Slovenia', 'Slovenia'), ('New Caledonia', 'New Caledonia'), ('Fiji', 'Fiji'), ('Kuwait', 'Kuwait'), ('Eswatini', 'Eswatini'), ('East Timor', 'East Timor'), ('Bahamas', 'Bahamas'), ('Montenegro', 'Montenegro'), ('Vanuatu', 'Vanuatu'), ('Falkland Islands', 'Falkland Islands'), ('Qatar', 'Qatar'), ('Gambia', 'Gambia'), ('Jamaica', 'Jamaica'), ('Kosovo', 'Kosovo'), ('Lebanon', 'Lebanon'), ('Cyprus', 'Cyprus'), ('Puerto Rico', 'Puerto Rico'), ('Abkhazia', 'Abkhazia'), ('French Southern Territories', 'French Southern Territories'), ('Palestine', 'Palestine'), ('Brunei', 'Brunei'), ('Trinidad and Tobago', 'Trinidad and Tobago'), ('French Polynesia', 'French Polynesia'), ('Transnistria', 'Transnistria'), ('Cape Verde', 'Cape Verde'), ('South Georgia and the South Sandwich Islands', 'South Georgia and the South Sandwich Islands'), ('South Ossetia', 'South Ossetia'), ('Northern Cyprus', 'Northern Cyprus'), ('Samoa', 'Samoa'), ('Luxembourg', 'Luxembourg'), ('Bir Tawil', 'Bir Tawil'), ('Mauritius', 'Mauritius'), ('Comoros', 'Comoros'), ('Åland', 'Åland'), ('Faroe Islands', 'Faroe Islands'), ('Hong Kong', 'Hong Kong'), ('São Tomé and Príncipe', 'São Tomé and Príncipe'), ('Turks and Caicos Islands', 'Turks and Caicos Islands'), ('Kiribati', 'Kiribati'), ('Bahrain', 'Bahrain'), ('Domin', 'Domin'), ('Tonga', 'Tonga'), ('Singapore', 'Singapore'), ('Microne', 'Microne'), ('Saint Lucia', 'Saint Lucia'), ('Isle of Man', 'Isle of Man'), ('Guam', 'Guam'), ('Andorra', 'Andorra'), ('Palau', 'Palau'), ('Northern Mariana Islands', 'Northern Mariana Islands'), ('Seychelles', 'Seychelles'), ('Curaçao', 'Curaçao'), ('Antigua and Barbuda', 'Antigua and Barbuda'), ('Barbados', 'Barbados'), ('Heard Island and McDonald Islands', 'Heard Island and McDonald Islands'), ('Saint Helena, Ascension and Tristan da Cunha', 'Saint Helena, Ascension and Tristan da Cunha'), ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'), ('Jan Mayen', 'Jan Mayen'), ('U.S. Virgin Islands', 'U.S. Virgin Islands'), ('Grenada', 'Grenada'), ('Malta', 'Malta'), ('Maldives', 'Maldives'), ('Bonaire', 'Bonaire'), ('Cayman Islands', 'Cayman Islands'), ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'), ('Niue', 'Niue'), ('Akrotiri and Dhekelia', 'Akrotiri and Dhekelia'), ('Saint Pierre and Miquelon', 'Saint Pierre and Miquelon'), ('Cook Islands', 'Cook Islands'), ('American Samoa', 'American Samoa'), ('Marshall Islands', 'Marshall Islands'), ('Aruba', 'Aruba'), ('Easter Island', 'Easter Island'), ('Liechtenstein', 'Liechtenstein'), ('British Virgin Islands', 'British Virgin Islands'), ('Wallis and Futuna', 'Wallis and Futuna'), ('Christmas Island', 'Christmas Island'), ('Jersey', 'Jersey'), ('Montserrat', 'Montserrat'), ('Anguilla', 'Anguilla'), ('Guernsey', 'Guernsey'), ('San Marino', 'San Marino'), ('British Indian Ocean Territory', 'British Indian Ocean Territory'), ('Bermuda', 'Bermuda'), ('Saint Martin', 'Saint Martin'), ('Bouvet Island', 'Bouvet Island'), ('Pitcairn Islands', 'Pitcairn Islands'), ('Norfolk Island', 'Norfolk Island'), ('Sint Maarten', 'Sint Maarten'), ('U.S. Minor Outlying Islands', 'U.S. Minor Outlying Islands'), ('Macao', 'Macao'), ('Tuvalu', 'Tuvalu'), ('Saint Barthélemy', 'Saint Barthélemy'), ('Nauru', 'Nauru'), ('Sint Eustatius', 'Sint Eustatius'), ('Cocos', 'Cocos'), ('Saba', 'Saba'), ('Tokelau', 'Tokelau'), ('Gibraltar', 'Gibraltar'), ('Clipperton Island', 'Clipperton Island'), ('Ashmore and Cartier Islands', 'Ashmore and Cartier Islands'), ('Coral Sea Islands', 'Coral Sea Islands'), ('Spratly Islands', 'Spratly Islands'), ('Monaco', 'Monaco'), ('Vatican City', 'Vatican City')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='entity',
            field=models.CharField(blank=True, choices=[(None, 'Please select your entity'), ('AIESEC in Turkey', 'AIESEC in Turkey'), ('AIESEC in India', 'AIESEC in India'), ('AIESEC in VIETNAM', 'AIESEC in VIETNAM'), ('AIESEC in Egypt', 'AIESEC in Egypt'), ('AIESEC in Tunisia', 'AIESEC in Tunisia'), ('AIESEC in Colombia', 'AIESEC in Colombia'), ('AIESEC in Sri Lanka', 'AIESEC in Sri Lanka'), ('AIESEC in Cambodia', 'AIESEC in Cambodia'), ('AIESEC in Brazil', 'AIESEC in Brazil'), ('AIESEC in Spain', 'AIESEC in Spain'), ('AIESEC in Ecuador', 'AIESEC in Ecuador'), ('AIESEC in El Salvador', 'AIESEC in El Salvador'), ('AIESEC in Guatemala', 'AIESEC in Guatemala'), ('AIESEC in Dominican Republic', 'AIESEC in Dominican Republic'), ('AIESEC in Poland', 'AIESEC in Poland'), ('AIESEC in Algeria', 'AIESEC in Algeria'), ('AIESEC in Nicaragua', 'AIESEC in Nicaragua'), ('AIESEC in Paraguay', 'AIESEC in Paraguay'), ('AIESEC in Mali', 'AIESEC in Mali'), ('AIESEC in Kuwait', 'AIESEC in Kuwait'), ('AIESEC in Bangladesh', 'AIESEC in Bangladesh'), ('AIESEC in Benin', 'AIESEC in Benin'), ('AIESEC in Tajikistan', 'AIESEC in Tajikistan'), ('AIESEC in Senegal', 'AIESEC in Senegal'), ('AIESEC in Kazakhstan', 'AIESEC in Kazakhstan'), ('AIESEC in Mainland of China', 'AIESEC in Mainland of China'), ('AIESEC in Ghana', 'AIESEC in Ghana'), ('AIESEC in Singapore', 'AIESEC in Singapore'), ('AIESEC in Czech Republic', 'AIESEC in Czech Republic'), ('AIESEC in Ethiopia', 'AIESEC in Ethiopia'), ('AIESEC in Monaco', 'AIESEC in Monaco'), ('AIESEC in Tanzania', 'AIESEC in Tanzania'), ('AIESEC in Andorra', 'AIESEC in Andorra'), ('AIESEC in Austria', 'AIESEC in Austria'), ('AIESEC in Macedonia', 'AIESEC in Macedonia'), ('AIESEC in Iceland', 'AIESEC in Iceland'), ('AIESEC in Russia', 'AIESEC in Russia'), ('AIESEC in Puerto Rico', 'AIESEC in Puerto Rico'), ('AIESEC in Chile', 'AIESEC in Chile'), ('AIESEC in Haiti', 'AIESEC in Haiti'), ('AIESEC in Kingdom of Saudi Arabia', 'AIESEC in Kingdom of Saudi Arabia'), ('AIESEC in Venezuela', 'AIESEC in Venezuela'), ('AIESEC in Qatar', 'AIESEC in Qatar'), ('AIESEC in New Zealand', 'AIESEC in New Zealand'), ('AIESEC in Honduras', 'AIESEC in Honduras'), ('AIESEC in Switzerland', 'AIESEC in Switzerland'), ('AIESEC in Liechtenstein', 'AIESEC in Liechtenstein'), ('AIESEC in Australia', 'AIESEC in Australia'), ('AIESEC in Barbados', 'AIESEC in Barbados'), ('AIESEC in Botswana', 'AIESEC in Botswana'), ('AIESEC in Hong Kong', 'AIESEC in Hong Kong'), ('AIESEC in Burkina Faso', 'AIESEC in Burkina Faso'), ('AIESEC in Kenya', 'AIESEC in Kenya'), ('AIESEC in Zimbabwe', 'AIESEC in Zimbabwe'), ('AIESEC in United States', 'AIESEC in United States'), ('AIESEC in Canada', 'AIESEC in Canada'), ('AIESEC in Iran', 'AIESEC in Iran'), ('AIESEC in Cabo Verde', 'AIESEC in Cabo Verde'), ('AIESEC in Pakistan', 'AIESEC in Pakistan'), ('AIESEC in Belgium', 'AIESEC in Belgium'), ('AIESEC in Croatia', 'AIESEC in Croatia'), ('AIESEC in Global Teams', 'AIESEC in Global Teams'), ('AIESEC in Estonia', 'AIESEC in Estonia'), ('AIESEC in Finland', 'AIESEC in Finland'), ('AIESEC in Armenia', 'AIESEC in Armenia'), ('AIESEC in Argentina', 'AIESEC in Argentina'), ('AIESEC in Romania', 'AIESEC in Romania'), ('AIESEC in Slovenia', 'AIESEC in Slovenia'), ('AIESEC in Jamaica', 'AIESEC in Jamaica'), ('AIESEC in Swaziland', 'AIESEC in Swaziland'), ('AIESEC in Italy', 'AIESEC in Italy'), ('AIESEC in Serbia', 'AIESEC in Serbia'), ('AIESEC in Sierra Leone', 'AIESEC in Sierra Leone'), ('AIESEC in Germany', 'AIESEC in Germany'), ('AIESEC in Ukraine', 'AIESEC in Ukraine'), ('AIESEC in Portugal', 'AIESEC in Portugal'), ('AIESEC in Maldives', 'AIESEC in Maldives'), ('AIESEC in Belarus', 'AIESEC in Belarus'), ('AIESEC in The Netherlands', 'AIESEC in The Netherlands'), ('AIESEC in Uganda', 'AIESEC in Uganda'), ('AIESEC in Latvia', 'AIESEC in Latvia'), ('AIESEC in Cyprus', 'AIESEC in Cyprus'), ('AIESEC in Moldova', 'AIESEC in Moldova'), ('AIESEC in Malaysia', 'AIESEC in Malaysia'), ('AIESEC in Bahrain', 'AIESEC in Bahrain'), ('AIESEC in Hungary', 'AIESEC in Hungary'), ('AIESEC in Morocco', 'AIESEC in Morocco'), ('AIESEC in Cameroon', 'AIESEC in Cameroon'), ('AIESEC in Namibia', 'AIESEC in Namibia'), ('AIESEC in Taiwan', 'AIESEC in Taiwan'), ('AIESEC in Niger', 'AIESEC in Niger'), ('AIESEC in Greece', 'AIESEC in Greece'), ('AIESEC in United Arab Emirates', 'AIESEC in United Arab Emirates'), ('AIESEC in Sultanate of Oman', 'AIESEC in Sultanate of Oman'), ('AIESEC in Norway', 'AIESEC in Norway'), ('AIESEC in Zambia', 'AIESEC in Zambia'), ('AIESEC in Myanmar', 'AIESEC in Myanmar'), ('AIESEC in Slovakia', 'AIESEC in Slovakia'), ("AIESEC in Cote D'Ivoire", "AIESEC in Cote D'Ivoire"), ('AIESEC in Bulgaria', 'AIESEC in Bulgaria'), ('AIESEC in Peru', 'AIESEC in Peru'), ('AIESEC in Liberia', 'AIESEC in Liberia'), ('AIESEC in Rwanda', 'AIESEC in Rwanda'), ('AIESEC in Madagascar', 'AIESEC in Madagascar'), ('AIESEC in Nepal', 'AIESEC in Nepal'), ('AIESEC in Korea', 'AIESEC in Korea'), ('AIESEC in Bosnia and Herzegovina', 'AIESEC in Bosnia and Herzegovina'), ('AIESEC in Sweden', 'AIESEC in Sweden'), ('AIESEC in Gabon', 'AIESEC in Gabon'), ('AIESEC in Togo', 'AIESEC in Togo'), ('AIESEC in Ireland', 'AIESEC in Ireland'), ('AIESEC in Malawi', 'AIESEC in Malawi'), ('AIESEC in Laos', 'AIESEC in Laos'), ('AIESEC in Azerbaijan', 'AIESEC in Azerbaijan'), ('AIESEC in Georgia', 'AIESEC in Georgia'), ('AIESEC in Thailand', 'AIESEC in Thailand'), ('AIESEC in Mexico', 'AIESEC in Mexico'), ('AIESEC in Bhutan', 'AIESEC in Bhutan'), ('AIESEC in Indonesia', 'AIESEC in Indonesia'), ('AIESEC in Nigeria', 'AIESEC in Nigeria'), ('AIESEC in South Africa', 'AIESEC in South Africa'), ('AIESEC in France', 'AIESEC in France'), ('AIESEC in Montenegro', 'AIESEC in Montenegro'), ('AIESEC in Panama', 'AIESEC in Panama'), ('AIESEC in United Kingdom', 'AIESEC in United Kingdom'), ('AIESEC in Lithuania', 'AIESEC in Lithuania'), ('AIESEC in Bolivia', 'AIESEC in Bolivia'), ('AIESEC in Seychelles', 'AIESEC in Seychelles'), ('AIESEC in Costa Rica', 'AIESEC in Costa Rica'), ('AIESEC in Mongolia', 'AIESEC in Mongolia'), ('AIESEC in Philippines', 'AIESEC in Philippines'), ('AIESEC in Albania', 'AIESEC in Albania'), ('AIESEC in Denmark', 'AIESEC in Denmark'), ('AIESEC in Kyrgyzstan', 'AIESEC in Kyrgyzstan'), ('AIESEC in Malta', 'AIESEC in Malta'), ('AIESEC in Mozambique', 'AIESEC in Mozambique'), ('AIESEC in Afghanistan', 'AIESEC in Afghanistan'), ('AIESEC in Jordan', 'AIESEC in Jordan'), ('AIESEC in Lebanon', 'AIESEC in Lebanon'), ('AIESEC in Uruguay', 'AIESEC in Uruguay'), ('AIESEC in Mauritius', 'AIESEC in Mauritius'), ('AIESEC in Japan', 'AIESEC in Japan'), ('AIESEC in Uzbekistan', 'AIESEC in Uzbekistan'), ('AIESEC in Fiji', 'AIESEC in Fiji')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='first_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='gender',
            field=models.CharField(blank=True, choices=[(None, 'Please select your gender'), ('Male', 'Male'), ('Female', 'Female'), ('Nonbinary', 'Nonbinary')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='merchandise',
            field=models.CharField(blank=True, choices=[(None, 'Are you interested?'), ('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='natonality',
            field=models.CharField(blank=True, choices=[(None, 'Please select your nationality as per passport'), ('Afghanistan', 'Afghanistan'), ('Albania', 'Albania'), ('Algeria', 'Algeria'), ('Andorra', 'Andorra'), ('Angola', 'Angola'), ('Antigua and Barbuda', 'Antigua and Barbuda'), ('Argentina', 'Argentina'), ('Armenia', 'Armenia'), ('Australia', 'Australia'), ('Austria', 'Austria'), ('Azerbaijan', 'Azerbaijan'), ('The Bahamas', 'The Bahamas'), ('Bahrain', 'Bahrain'), ('Bangladesh', 'Bangladesh'), ('Barbados', 'Barbados'), ('Belarus', 'Belarus'), ('Belgium', 'Belgium'), ('Belize', 'Belize'), ('Benin', 'Benin'), ('Bhutan', 'Bhutan'), ('Bolivia', 'Bolivia'), ('Bosnia and Herzegovina', 'Bosnia and Herzegovina'), ('Botswana', 'Botswana'), ('Brazil', 'Brazil'), ('Brunei', 'Brunei'), ('Bulgaria', 'Bulgaria'), ('Burkina Faso', 'Burkina Faso'), ('Burundi', 'Burundi'), ('Cabo Verde', 'Cabo Verde'), ('Cambodia', 'Cambodia'), ('Cameroon', 'Cameroon'), ('Canada', 'Canada'), ('Central African Republic', 'Central African Republic'), ('Chad', 'Chad'), ('Chile', 'Chile'), ('China', 'China'), ('Colombia', 'Colombia'), ('Comoros', 'Comoros'), ('Congo, Democratic Republic of the', 'Congo, Democratic Republic of the'), ('Congo, Republic of the', 'Congo, Republic of the'), ('Costa Rica', 'Costa Rica'), ('Côte d’Ivoire', 'Côte d’Ivoire'), ('Croatia', 'Croatia'), ('Cuba', 'Cuba'), ('Cyprus', 'Cyprus'), ('Czech Republic', 'Czech Republic'), ('Denmark', 'Denmark'), ('Djibouti', 'Djibouti'), ('Dominica', 'Dominica'), ('Dominican Republic', 'Dominican Republic'), ('East Timor "Timor-Leste"', 'East Timor "Timor-Leste"'), ('Ecuador', 'Ecuador'), ('Egypt', 'Egypt'), ('El Salvador', 'El Salvador'), ('Equatorial Guinea', 'Equatorial Guinea'), ('Eritrea', 'Eritrea'), ('Estonia', 'Estonia'), ('Eswatini', 'Eswatini'), ('Ethiopia', 'Ethiopia'), ('Fiji', 'Fiji'), ('Finland', 'Finland'), ('France', 'France'), ('Gabon', 'Gabon'), ('The Gambia', 'The Gambia'), ('Georgia', 'Georgia'), ('Germany', 'Germany'), ('Ghana', 'Ghana'), ('Greece', 'Greece'), ('Grenada', 'Grenada'), ('Guatemala', 'Guatemala'), ('Guinea', 'Guinea'), ('Guinea-Bissau', 'Guinea-Bissau'), ('Guyana', 'Guyana'), ('Haiti', 'Haiti'), ('Honduras', 'Honduras'), ('Hungary', 'Hungary'), ('Iceland', 'Iceland'), ('India', 'India'), ('Indonesia', 'Indonesia'), ('Iran', 'Iran'), ('Iraq', 'Iraq'), ('Ireland', 'Ireland'), ('Italy', 'Italy'), ('Jamaica', 'Jamaica'), ('Japan', 'Japan'), ('Jordan', 'Jordan'), ('Kazakhstan', 'Kazakhstan'), ('Kenya', 'Kenya'), ('Kiribati', 'Kiribati'), ('Korea, North', 'Korea, North'), ('Korea, South', 'Korea, South'), ('Kosovo', 'Kosovo'), ('Kuwait', 'Kuwait'), ('Kyrgyzstan', 'Kyrgyzstan'), ('Laos', 'Laos'), ('Latvia', 'Latvia'), ('Lebanon', 'Lebanon'), ('Lesotho', 'Lesotho'), ('Liberia', 'Liberia'), ('Libya', 'Libya'), ('Liechtenstein', 'Liechtenstein'), ('Lithuania', 'Lithuania'), ('Luxembourg', 'Luxembourg'), ('Madagascar', 'Madagascar'), ('Malawi', 'Malawi'), ('Malaysia', 'Malaysia'), ('Maldives', 'Maldives'), ('Mali', 'Mali'), ('Malta', 'Malta'), ('Marshall Islands', 'Marshall Islands'), ('Mauritania', 'Mauritania'), ('Mauritius', 'Mauritius'), ('Mexico', 'Mexico'), ('Micronesia, Federated States of', 'Micronesia, Federated States of'), ('Moldova', 'Moldova'), ('Monaco', 'Monaco'), ('Mongolia', 'Mongolia'), ('Montenegro', 'Montenegro'), ('Morocco', 'Morocco'), ('Mozambique', 'Mozambique'), ('Myanmar (Burma)', 'Myanmar (Burma)'), ('Namibia', 'Namibia'), ('Nauru', 'Nauru'), ('Nepal', 'Nepal'), ('Netherlands', 'Netherlands'), ('New Zealand', 'New Zealand'), ('Nicaragua', 'Nicaragua'), ('Niger', 'Niger'), ('Nigeria', 'Nigeria'), ('North Macedonia', 'North Macedonia'), ('Norway', 'Norway'), ('Oman', 'Oman'), ('Pakistan', 'Pakistan'), ('Palau', 'Palau'), ('Panama', 'Panama'), ('Papua New Guinea', 'Papua New Guinea'), ('Paraguay', 'Paraguay'), ('Peru', 'Peru'), ('Philippines', 'Philippines'), ('Poland', 'Poland'), ('Portugal', 'Portugal'), ('Qatar', 'Qatar'), ('Romania', 'Romania'), ('Russia', 'Russia'), ('Rwanda', 'Rwanda'), ('Saint Kitts and Nevis', 'Saint Kitts and Nevis'), ('Saint Lucia', 'Saint Lucia'), ('Saint Vincent and the Grenadines', 'Saint Vincent and the Grenadines'), ('Samoa', 'Samoa'), ('San Marino', 'San Marino'), ('Sao Tome and Principe', 'Sao Tome and Principe'), ('Saudi Arabia', 'Saudi Arabia'), ('Senegal', 'Senegal'), ('Serbia', 'Serbia'), ('Seychelles', 'Seychelles'), ('Sierra Leone', 'Sierra Leone'), ('Singapore', 'Singapore'), ('Slovakia', 'Slovakia'), ('Slovenia', 'Slovenia'), ('Solomon Islands', 'Solomon Islands'), ('Somalia', 'Somalia'), ('South Africa', 'South Africa'), ('Spain', 'Spain'), ('Sri Lanka', 'Sri Lanka'), ('Sudan', 'Sudan'), ('Sudan, South', 'Sudan, South'), ('Suriname', 'Suriname'), ('Sweden', 'Sweden'), ('Switzerland', 'Switzerland'), ('Syria', 'Syria'), ('Taiwan', 'Taiwan'), ('Tajikistan', 'Tajikistan'), ('Tanzania', 'Tanzania'), ('Thailand', 'Thailand'), ('Togo', 'Togo'), ('Tonga', 'Tonga'), ('Trinidad and Tobago', 'Trinidad and Tobago'), ('Tunisia', 'Tunisia'), ('Turkey', 'Turkey'), ('Turkmenistan', 'Turkmenistan'), ('Tuvalu', 'Tuvalu'), ('Uganda', 'Uganda'), ('Ukraine', 'Ukraine'), ('United Arab Emirates', 'United Arab Emirates'), ('United Kingdom', 'United Kingdom'), ('United States', 'United States'), ('Uruguay', 'Uruguay'), ('Uzbekistan', 'Uzbekistan'), ('Vanuatu', 'Vanuatu'), ('Vatican City', 'Vatican City'), ('Venezuela', 'Venezuela'), ('Vietnam', 'Vietnam'), ('Yemen', 'Yemen'), ('Zambia', 'Zambia'), ('Zimbabwe', 'Zimbabwe')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='nick_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='position',
            field=models.CharField(blank=True, choices=[(None, 'Please select your position'), ('MCP', 'MCP'), ('MCVP EwA', 'MCVP EwA'), ('MCVP BD', 'MCVP BD'), ('MCVP B2B', 'MCVP B2B'), ('MCVP PR', 'MCVP PR'), ('MCVP MKTG', 'MCVP MKTG'), ('MCVP IM', 'MCVP IM'), ('MCVP OPS', 'MCVP OPS'), ('MCVP oGX', 'MCVP oGX'), ('MCVP oGV', 'MCVP oGV'), ('MCVP oGT', 'MCVP oGT'), ('MCVP oGTa', 'MCVP oGTa'), ('MCVP oGTe', 'MCVP oGTe'), ('MCVP iCX', 'MCVP iCX'), ('MCVP iGV', 'MCVP iGV'), ('MCVP iGT', 'MCVP iGT'), ('MCVP iGTa', 'MCVP iGTa'), ('MCVP iGTe', 'MCVP iGTe'), ('MCVP OD', 'MCVP OD'), ('MCVP MXP', 'MCVP MXP'), ('MCVP F&L', 'MCVP F&L'), ('MCVP FM', 'MCVP FM'), ('LCP', 'LCP')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='pre_and_post_trips',
            field=models.CharField(blank=True, choices=[(None, 'Are you interested?'), ('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='region',
            field=models.CharField(blank=True, choices=[(None, 'Please select your region'), ('Middle East and Africa', 'Middle East and Africa'), ('Europe', 'Europe'), ('Americas', 'Americas'), ('Asia Pacific', 'Asia Pacific')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='telegram_username',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='whatsapp_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='workshops_with_partners',
            field=models.CharField(blank=True, choices=[(None, 'Are you interested?'), ('Yes', 'Yes'), ('No', 'No')], max_length=50, null=True),
        ),
    ]
