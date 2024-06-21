# Generated by Django 4.2.9 on 2024-02-21 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registrations', '0018_delegate_generation_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Engagement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='delegate',
            name='career_confidence',
            field=models.CharField(blank=True, choices=[(None, 'Choose a number from 1 to 10'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='global_partner_for_key_note',
            field=models.CharField(blank=True, choices=[(None, 'Select a partner'), ('Alfa Laval', 'Alfa Laval'), ('Accenture', 'Accenture'), ('DHL Group', 'DHL Group'), ('DP WORLD', 'DP WORLD'), ('EATON', 'EATON'), ('Electrolux Group', 'Electrolux Group'), ('Electrolux Food Foundation', 'Electrolux Food Foundation'), ('EY', 'EY'), ('Global Leadership Foundation', 'Global Leadership Foundation'), ('Husqvarna Group', 'Husqvarna Group'), ('IE University', 'IE University'), ('International SOS', 'International SOS'), ('PwC', 'PwC'), ('Project Everyone', 'Project Everyone'), ('Kyndryl', 'Kyndryl'), ('Schneider Electric', 'Schneider Electric'), ('Tata Consultancy Services', 'Tata Consultancy Services'), ('Terrawind', 'Terrawind'), ('Toyota', 'Toyota'), ('Henkel', 'Henkel'), ('International Labour Organization', 'International Labour Organization'), ('Nexans', 'Nexans')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='how_to_make_partners_spaces_relevant',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='partners_for_career',
            field=models.CharField(blank=True, choices=[(None, 'Select a partner'), ('Alfa Laval', 'Alfa Laval'), ('Accenture', 'Accenture'), ('DHL Group', 'DHL Group'), ('DP WORLD', 'DP WORLD'), ('EATON', 'EATON'), ('Electrolux Group', 'Electrolux Group'), ('Electrolux Food Foundation', 'Electrolux Food Foundation'), ('EY', 'EY'), ('Global Leadership Foundation', 'Global Leadership Foundation'), ('Husqvarna Group', 'Husqvarna Group'), ('International SOS', 'International SOS'), ('PwC', 'PwC'), ('Kyndryl', 'Kyndryl'), ('Schneider Electric', 'Schneider Electric'), ('Tata Consultancy Services', 'Tata Consultancy Services'), ('Terrawind', 'Terrawind'), ('Toyota', 'Toyota'), ('Henkel', 'Henkel'), ('International Labour Organization', 'International Labour Organization'), ('Nexans', 'Nexans')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='partners_topics',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='shirt_size',
            field=models.CharField(blank=True, choices=[(None, 'Your t-shirt size'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('2XL', '2XL')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='what_do_you_want_to_know_about_partners',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='why_this_global_partner',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='work_experience',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='academic_background',
            field=models.CharField(blank=True, choices=[(None, 'Your academic background'), ('Associate degree', 'Associate degree'), ("Bachelor's degree", "Bachelor's degree"), ("Master's degree", "Master's degree"), ('Doctoral degree', 'Doctoral degree')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='entity',
            field=models.CharField(blank=True, choices=[(None, 'Your entity'), ('AIESEC in Albania', 'AIESEC in Albania'), ('AIESEC in Algeria', 'AIESEC in Algeria'), ('AIESEC in Argentina', 'AIESEC in Argentina'), ('AIESEC in Armenia', 'AIESEC in Armenia'), ('AIESEC in Australia', 'AIESEC in Australia'), ('AIESEC in Austria', 'AIESEC in Austria'), ('AIESEC in Azerbaijan', 'AIESEC in Azerbaijan'), ('AIESEC in Bahrain', 'AIESEC in Bahrain'), ('AIESEC in Bangladesh', 'AIESEC in Bangladesh'), ('AIESEC in Belgium', 'AIESEC in Belgium'), ('AIESEC in Benin', 'AIESEC in Benin'), ('AIESEC in Bolivia', 'AIESEC in Bolivia'), ('AIESEC in Bosnia Herzegovina', 'AIESEC in Bosnia Herzegovina'), ('AIESEC in Brazil', 'AIESEC in Brazil'), ('AIESEC in Bulgaria', 'AIESEC in Bulgaria'), ('AIESEC in Burkina Faso', 'AIESEC in Burkina Faso'), ('AIESEC in Cambodia', 'AIESEC in Cambodia'), ('AIESEC in Cameroon', 'AIESEC in Cameroon'), ('AIESEC in Canada', 'AIESEC in Canada'), ('AIESEC in Chile', 'AIESEC in Chile'), ('AIESEC in Colombia', 'AIESEC in Colombia'), ('AIESEC in Costa Rica', 'AIESEC in Costa Rica'), ("AIESEC in Cote D'Ivoire", "AIESEC in Cote D'Ivoire"), ('AIESEC in Croatia', 'AIESEC in Croatia'), ('AIESEC in Czech Republic', 'AIESEC in Czech Republic'), ('AIESEC in Denmark', 'AIESEC in Denmark'), ('AIESEC in Dominican Republic', 'AIESEC in Dominican Republic'), ('AIESEC in Ecuador', 'AIESEC in Ecuador'), ('AIESEC in Egypt', 'AIESEC in Egypt'), ('AIESEC in El Salvador', 'AIESEC in El Salvador'), ('AIESEC in Estonia', 'AIESEC in Estonia'), ('AIESEC in Ethiopia', 'AIESEC in Ethiopia'), ('AIESEC in Finland', 'AIESEC in Finland'), ('AIESEC in France', 'AIESEC in France'), ('AIESEC in Georgia', 'AIESEC in Georgia'), ('AIESEC in Germany', 'AIESEC in Germany'), ('AIESEC in Ghana', 'AIESEC in Ghana'), ('AIESEC in Greece', 'AIESEC in Greece'), ('AIESEC in Guatemala', 'AIESEC in Guatemala'), ('AIESEC in Hong Kong', 'AIESEC in Hong Kong'), ('AIESEC in Hungary', 'AIESEC in Hungary'), ('AIESEC in Iceland', 'AIESEC in Iceland'), ('AIESEC in India', 'AIESEC in India'), ('AIESEC in Indonesia', 'AIESEC in Indonesia'), ('AIESEC in Italy', 'AIESEC in Italy'), ('AIESEC in Japan', 'AIESEC in Japan'), ('AIESEC in Jordan', 'AIESEC in Jordan'), ('AIESEC in Kazakhstan', 'AIESEC in Kazakhstan'), ('AIESEC in Kenya', 'AIESEC in Kenya'), ('AIESEC in Korea', 'AIESEC in Korea'), ('AIESEC in Kuwait', 'AIESEC in Kuwait'), ('AIESEC in Kyrgyzstan', 'AIESEC in Kyrgyzstan'), ('AIESEC in Latvia', 'AIESEC in Latvia'), ('AIESEC in Lebanon', 'AIESEC in Lebanon'), ('AIESEC in Liberia', 'AIESEC in Liberia'), ('AIESEC in Lithuania', 'AIESEC in Lithuania'), ('AIESEC in Macedonia', 'AIESEC in Macedonia'), ('AIESEC in Mainland of China', 'AIESEC in Mainland of China'), ('AIESEC in Malawi', 'AIESEC in Malawi'), ('AIESEC in Malaysia', 'AIESEC in Malaysia'), ('AIESEC in Mexico', 'AIESEC in Mexico'), ('AIESEC in Moldova', 'AIESEC in Moldova'), ('AIESEC in Mongolia', 'AIESEC in Mongolia'), ('AIESEC in Montenegro', 'AIESEC in Montenegro'), ('AIESEC in Morocco', 'AIESEC in Morocco'), ('AIESEC in Mozambique', 'AIESEC in Mozambique'), ('AIESEC in Myanmar', 'AIESEC in Myanmar'), ('AIESEC in Namibia', 'AIESEC in Namibia'), ('AIESEC in Nepal', 'AIESEC in Nepal'), ('AIESEC in New Zealand', 'AIESEC in New Zealand'), ('AIESEC in Nicaragua', 'AIESEC in Nicaragua'), ('AIESEC in Nigeria', 'AIESEC in Nigeria'), ('AIESEC in Norway', 'AIESEC in Norway'), ('AIESEC in Pakistan', 'AIESEC in Pakistan'), ('AIESEC in Panama', 'AIESEC in Panama'), ('AIESEC in Paraguay', 'AIESEC in Paraguay'), ('AIESEC in Peru', 'AIESEC in Peru'), ('AIESEC in Philippines', 'AIESEC in Philippines'), ('AIESEC in Poland', 'AIESEC in Poland'), ('AIESEC in Portugal', 'AIESEC in Portugal'), ('AIESEC in Romania', 'AIESEC in Romania'), ('AIESEC in Russia', 'AIESEC in Russia'), ('AIESEC in Rwanda', 'AIESEC in Rwanda'), ('AIESEC in Senegal', 'AIESEC in Senegal'), ('AIESEC in Serbia', 'AIESEC in Serbia'), ('AIESEC in Singapore', 'AIESEC in Singapore'), ('AIESEC in Slovakia', 'AIESEC in Slovakia'), ('AIESEC in South Africa', 'AIESEC in South Africa'), ('AIESEC in Spain', 'AIESEC in Spain'), ('AIESEC in Sri Lanka', 'AIESEC in Sri Lanka'), ('AIESEC in Sweden', 'AIESEC in Sweden'), ('AIESEC in Switzerland', 'AIESEC in Switzerland'), ('AIESEC in Taiwan', 'AIESEC in Taiwan'), ('AIESEC in Tanzania', 'AIESEC in Tanzania'), ('AIESEC in Thailand', 'AIESEC in Thailand'), ('AIESEC in The Netherlands', 'AIESEC in The Netherlands'), ('AIESEC in Togo', 'AIESEC in Togo'), ('AIESEC in Tunisia', 'AIESEC in Tunisia'), ('AIESEC in Türkiye', 'AIESEC in Türkiye'), ('AIESEC in Uganda', 'AIESEC in Uganda'), ('AIESEC in Ukraine', 'AIESEC in Ukraine'), ('AIESEC in United Arab Emirates', 'AIESEC in United Arab Emirates'), ('AIESEC in United Kingdom', 'AIESEC in United Kingdom'), ('AIESEC in United States', 'AIESEC in United States'), ('AIESEC in Venezuela', 'AIESEC in Venezuela'), ('AIESEC in Vietnam', 'AIESEC in Vietnam')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='gender',
            field=models.CharField(blank=True, choices=[(None, 'Your gender'), ('Male', 'Male'), ('Female', 'Female'), ('Nonbinary', 'Nonbinary')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='generation',
            field=models.CharField(blank=True, choices=[(None, 'Your generation'), ('23.24', '23.24'), ('24.25', '24.25')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='position',
            field=models.CharField(blank=True, choices=[(None, 'Your position'), ('MCP', 'MCP'), ('MCVP EwA', 'MCVP EwA'), ('MCVP BD', 'MCVP BD'), ('MCVP B2B', 'MCVP B2B'), ('MCVP PR', 'MCVP PR'), ('MCVP MKTG', 'MCVP MKTG'), ('MCVP IM', 'MCVP IM'), ('MCVP OPS', 'MCVP OPS'), ('MCVP oGX', 'MCVP oGX'), ('MCVP oGV', 'MCVP oGV'), ('MCVP oGT', 'MCVP oGT'), ('MCVP oGTa', 'MCVP oGTa'), ('MCVP oGTe', 'MCVP oGTe'), ('MCVP iCX', 'MCVP iCX'), ('MCVP iGV', 'MCVP iGV'), ('MCVP iGT', 'MCVP iGT'), ('MCVP iGTa', 'MCVP iGTa'), ('MCVP iGTe', 'MCVP iGTe'), ('MCVP OD', 'MCVP OD'), ('MCVP ODM', 'MCVP ODM'), ('MCVP Expansions', 'MCVP Expansions'), ('MCVP MXP', 'MCVP MXP'), ('MCVP F&L', 'MCVP F&L'), ('MCVP FM', 'MCVP FM'), ('LCP', 'LCP'), ('CEEDer', 'CEEDer'), ('GS', 'GS'), ('Other', 'Other')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='pre_and_post_trips',
            field=models.CharField(blank=True, choices=[(None, 'Your trips preference'), ('Pre-conference trip', 'Pre-conference trip'), ('Post-conference trip', 'Post-conference trip'), ('Both', 'Both'), ('None', 'None')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='region',
            field=models.CharField(blank=True, choices=[(None, 'Your region'), ('Middle East and Africa', 'Middle East and Africa'), ('Europe', 'Europe'), ('Americas', 'Americas'), ('Asia Pacific', 'Asia Pacific')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='delegate',
            name='room_with_the_same_gender',
            field=models.CharField(blank=True, choices=[(None, 'Your room preference'), ('Female only', 'Female only'), ('Male only', 'Male only'), ('Female preferred', 'Female preferred'), ('Male preferred', 'Male preferred'), ('Mixed', 'Mixed')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='delegate',
            name='engagements',
            field=models.ManyToManyField(to='registrations.engagement'),
        ),
    ]