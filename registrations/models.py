from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .user_activation import *
from datetime import datetime
# Create your models here.

POSITION_CHOICES = [
  (None, 'Your position'), 
  ('MCP', 'MCP'), ('MCVP EwA', 'MCVP EwA'),
  ('MCVP BD', 'MCVP BD'),
  ('MCVP B2B', 'MCVP B2B'),
  ('MCVP PR', 'MCVP PR'),
  ('MCVP MKTG', 'MCVP MKTG'),
  ('MCVP IM', 'MCVP IM'),
  ('MCVP OPS', 'MCVP OPS'),
  ('MCVP oGX', 'MCVP oGX'),
  ('MCVP oGV', 'MCVP oGV'),
  ('MCVP oGT', 'MCVP oGT'),
  ('MCVP oGTa', 'MCVP oGTa'),
  ('MCVP oGTe', 'MCVP oGTe'),
  ('MCVP iCX', 'MCVP iCX'),
  ('MCVP iGV','MCVP iGV' ),
  ('MCVP iGT', 'MCVP iGT'),
  ('MCVP iGTa', 'MCVP iGTa'),
  ('MCVP iGTe', 'MCVP iGTe'),
  ('MCVP OD', 'MCVP OD'),
  ('MCVP ODM', 'MCVP ODM'),
  ('MCVP Expansions', 'MCVP Expansions'),
  ('MCVP MXP', 'MCVP MXP'),
  ('MCVP F&L', 'MCVP F&L'),
  ('MCVP FM', 'MCVP FM'), 
  ('LCP', 'LCP'),
  ('CEEDer', 'CEEDer'),
  ('GS', 'GS'),
  ('Other', 'Other')
]
ENTITY_CHOICES = [(None, 'Your entity'), 
('AIESEC in Albania', 'AIESEC in Albania'),
('AIESEC in Algeria', 'AIESEC in Algeria'),
('AIESEC in Argentina', 'AIESEC in Argentina'),
('AIESEC in Armenia', 'AIESEC in Armenia'),
('AIESEC in Australia', 'AIESEC in Australia'),
('AIESEC in Austria', 'AIESEC in Austria'),
('AIESEC in Azerbaijan', 'AIESEC in Azerbaijan'),
('AIESEC in Bahrain', 'AIESEC in Bahrain'),
('AIESEC in Bangladesh', 'AIESEC in Bangladesh'),
('AIESEC in Belgium', 'AIESEC in Belgium'),
('AIESEC in Benin', 'AIESEC in Benin'),
('AIESEC in Bolivia', 'AIESEC in Bolivia'),
('AIESEC in Bosnia Herzegovina', 'AIESEC in Bosnia Herzegovina'),
('AIESEC in Brazil', 'AIESEC in Brazil'),
('AIESEC in Bulgaria', 'AIESEC in Bulgaria'),
('AIESEC in Burkina Faso', 'AIESEC in Burkina Faso'),
('AIESEC in Cambodia', 'AIESEC in Cambodia'),
('AIESEC in Cameroon', 'AIESEC in Cameroon'),
('AIESEC in Canada', 'AIESEC in Canada'),
('AIESEC in Chile', 'AIESEC in Chile'),
('AIESEC in Colombia', 'AIESEC in Colombia'),
('AIESEC in Costa Rica', 'AIESEC in Costa Rica'),
("AIESEC in Cote D'Ivoire", "AIESEC in Cote D'Ivoire"),
('AIESEC in Croatia', 'AIESEC in Croatia'),
('AIESEC in Czech Republic', 'AIESEC in Czech Republic'),
('AIESEC in Denmark', 'AIESEC in Denmark'),
('AIESEC in Dominican Republic', 'AIESEC in Dominican Republic'),
('AIESEC in Ecuador', 'AIESEC in Ecuador'),
('AIESEC in Egypt', 'AIESEC in Egypt'),
('AIESEC in El Salvador', 'AIESEC in El Salvador'),
('AIESEC in Estonia', 'AIESEC in Estonia'),
('AIESEC in Ethiopia', 'AIESEC in Ethiopia'),
('AIESEC in Finland', 'AIESEC in Finland'),
('AIESEC in France', 'AIESEC in France'),
('AIESEC in Georgia', 'AIESEC in Georgia'),
('AIESEC in Germany', 'AIESEC in Germany'),
('AIESEC in Ghana', 'AIESEC in Ghana'),
('AIESEC in Greece', 'AIESEC in Greece'),
('AIESEC in Guatemala', 'AIESEC in Guatemala'),
('AIESEC in Hong Kong', 'AIESEC in Hong Kong'),
('AIESEC in Hungary', 'AIESEC in Hungary'),
('AIESEC in Iceland', 'AIESEC in Iceland'),
('AIESEC in India', 'AIESEC in India'),
('AIESEC in Indonesia', 'AIESEC in Indonesia'),
('AIESEC in Italy', 'AIESEC in Italy'),
('AIESEC in Japan', 'AIESEC in Japan'),
('AIESEC in Jordan', 'AIESEC in Jordan'),
('AIESEC in Kazakhstan', 'AIESEC in Kazakhstan'),
('AIESEC in Kenya', 'AIESEC in Kenya'),
('AIESEC in Korea', 'AIESEC in Korea'),
('AIESEC in Kuwait', 'AIESEC in Kuwait'),
('AIESEC in Kyrgyzstan', 'AIESEC in Kyrgyzstan'),
('AIESEC in Latvia', 'AIESEC in Latvia'),
('AIESEC in Lebanon', 'AIESEC in Lebanon'),
('AIESEC in Liberia', 'AIESEC in Liberia'),
('AIESEC in Lithuania', 'AIESEC in Lithuania'),
('AIESEC in Macedonia', 'AIESEC in Macedonia'),
('AIESEC in Mainland of China', 'AIESEC in Mainland of China'),
('AIESEC in Malawi', 'AIESEC in Malawi'),
('AIESEC in Malaysia', 'AIESEC in Malaysia'),
('AIESEC in Mexico', 'AIESEC in Mexico'),
('AIESEC in Moldova', 'AIESEC in Moldova'),
('AIESEC in Mongolia', 'AIESEC in Mongolia'),
('AIESEC in Montenegro', 'AIESEC in Montenegro'),
('AIESEC in Morocco', 'AIESEC in Morocco'),
('AIESEC in Mozambique', 'AIESEC in Mozambique'),
('AIESEC in Myanmar', 'AIESEC in Myanmar'),
('AIESEC in Namibia', 'AIESEC in Namibia'),
('AIESEC in Nepal', 'AIESEC in Nepal'),
('AIESEC in New Zealand', 'AIESEC in New Zealand'),
('AIESEC in Nicaragua', 'AIESEC in Nicaragua'),
('AIESEC in Nigeria', 'AIESEC in Nigeria'),
('AIESEC in Norway', 'AIESEC in Norway'),
('AIESEC in Pakistan', 'AIESEC in Pakistan'),
('AIESEC in Panama', 'AIESEC in Panama'),
('AIESEC in Paraguay', 'AIESEC in Paraguay'),
('AIESEC in Peru', 'AIESEC in Peru'),
('AIESEC in Philippines', 'AIESEC in Philippines'),
('AIESEC in Poland', 'AIESEC in Poland'),
('AIESEC in Portugal', 'AIESEC in Portugal'),
('AIESEC in Romania', 'AIESEC in Romania'),
('AIESEC in Russia', 'AIESEC in Russia'),
('AIESEC in Rwanda', 'AIESEC in Rwanda'),
('AIESEC in Senegal', 'AIESEC in Senegal'),
('AIESEC in Serbia', 'AIESEC in Serbia'),
('AIESEC in Singapore', 'AIESEC in Singapore'),
('AIESEC in Slovakia', 'AIESEC in Slovakia'),
('AIESEC in South Africa', 'AIESEC in South Africa'),
('AIESEC in Spain', 'AIESEC in Spain'),
('AIESEC in Sri Lanka', 'AIESEC in Sri Lanka'),
('AIESEC in Sweden', 'AIESEC in Sweden'),
('AIESEC in Switzerland', 'AIESEC in Switzerland'),
('AIESEC in Taiwan', 'AIESEC in Taiwan'),
('AIESEC in Tanzania', 'AIESEC in Tanzania'),
('AIESEC in Thailand', 'AIESEC in Thailand'),
('AIESEC in The Netherlands', 'AIESEC in The Netherlands'),
('AIESEC in Togo', 'AIESEC in Togo'),
('AIESEC in Tunisia', 'AIESEC in Tunisia'),
('AIESEC in Türkiye', 'AIESEC in Türkiye'),
('AIESEC in Uganda', 'AIESEC in Uganda'),
('AIESEC in Ukraine', 'AIESEC in Ukraine'),
('AIESEC in United Arab Emirates', 'AIESEC in United Arab Emirates'),
('AIESEC in United Kingdom', 'AIESEC in United Kingdom'),
('AIESEC in United States', 'AIESEC in United States'),
('AIESEC in Venezuela', 'AIESEC in Venezuela'),
('AIESEC in Vietnam', 'AIESEC in Vietnam')]
REGION_CHOICES = [(None, 'Your region'), ('Middle East and Africa', 'Middle East and Africa'), ('Europe', 'Europe'), ('Americas', 'Americas'), ('Asia Pacific', 'Asia Pacific')]
YES_NO_CHOICES = [(None, '-------'), ('Yes', 'Yes'), ('No', 'No')]
GENDER_OPTIONS = [(None, 'Your gender'), ('Male', 'Male'), ('Female', 'Female'), ('Nonbinary', 'Nonbinary')]
ACADEMIC_BACKGROUND = [(None, 'Your academic background'), ('Associate degree', 'Associate degree'), ("Bachelor's degree", "Bachelor's degree"), ("Master's degree", "Master's degree"), ("Doctoral degree", "Doctoral degree")]
POST_PRE_TRIPS = [(None, 'Your trips preference'), ('Pre-conference trip', 'Pre-conference trip'), ('Post-conference trip', 'Post-conference trip'), ('Both', 'Both'), ('None', 'None')]
GENERATION =  [(None, 'Your generation'), ('23.24', '23.24'), ('24.25', '24.25')]
SHIRT_SIZES = [(None, 'Your t-shirt size'), ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('2XL', '2XL')]
GLOBAL_PARTNER_KEYNOTE = [(None, 'Select a partner'), ('Alfa Laval', 'Alfa Laval'),
('Accenture', 'Accenture'),
('DHL Group', 'DHL Group'),
('DP WORLD', 'DP WORLD'),
('EATON', 'EATON'),
('Electrolux Group', 'Electrolux Group'),
('Electrolux Food Foundation', 'Electrolux Food Foundation'),
('EY', 'EY'),
('Global Leadership Foundation', 'Global Leadership Foundation'),
('Husqvarna Group', 'Husqvarna Group'),
('IE University', 'IE University'),
('International SOS', 'International SOS'),
('PwC', 'PwC'),
('Project Everyone', 'Project Everyone'),
('Kyndryl', 'Kyndryl'),
('Schneider Electric', 'Schneider Electric'),
('Tata Consultancy Services', 'Tata Consultancy Services'),
('Terrawind', 'Terrawind'),
('Toyota', 'Toyota'),
('Henkel', 'Henkel'),
('International Labour Organization', 'International Labour Organization'),
('Nexans', 'Nexans')
]
CAREER_SCORE = [(None, 'Choose a number from 1 to 10'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')]
GLOBAL_PARTNER_CAREER = [(None, 'Select a partner'), 
('Alfa Laval', 'Alfa Laval'),
('Accenture', 'Accenture'),
('DHL Group', 'DHL Group'),
('DP WORLD', 'DP WORLD'),
('EATON', 'EATON'),
('Electrolux Group', 'Electrolux Group'),
('Electrolux Food Foundation', 'Electrolux Food Foundation'),
('EY', 'EY'),
('Global Leadership Foundation', 'Global Leadership Foundation'),
('Husqvarna Group', 'Husqvarna Group'),
('International SOS', 'International SOS'),
('PwC', 'PwC'),
('Kyndryl', 'Kyndryl'),
('Schneider Electric', 'Schneider Electric'),
('Tata Consultancy Services', 'Tata Consultancy Services'),
('Terrawind', 'Terrawind'),
('Toyota', 'Toyota'),
('Henkel', 'Henkel'),
('International Labour Organization', 'International Labour Organization'),
('Nexans', 'Nexans')
]
ROOM_OPTIONS = [(None, 'Your room preference'), ('Female only', 'Female only'), ('Male only', 'Male only'), ('Female preferred', 'Female preferred'), ('Male preferred', 'Male preferred'), ('Mixed', 'Mixed'),]
ENGAGEMENT_OPTIONS = [(None, '-------'),
('Worlds largest lesson', 'Worlds largest lesson'),
('Keynote', 'Keynote'),
('Workshop', 'Workshop'),
('Networking spaces', 'Networking spaces'),
('Other', 'Other')]


def validate_image_size(value):
    filesize = value.size
    
    # Here, you can specify the maximum file size in bytes
    if filesize > 2 * 1024 * 1024:  # 2 MB
        raise ValidationError(_("The maximum file size that can be uploaded is 2MB."))

class Food(models.Model):
  specification =  models.CharField(max_length=50, null=True, blank=True)

  def __str__(self):
   return self.specification
  
  

class Delegate(models.Model):
  created_at = models.DateTimeField(default=timezone.now, blank=True)
  
  first_name = models.CharField(max_length=50, null=True, blank=True)
  last_name = models.CharField(max_length=50, null=True, blank=True)
  nick_name = models.CharField(max_length=50, null=True, blank=True)
  aiesec_email = models.EmailField(max_length = 254, null=True, blank=True)
  personal_email = models.EmailField(max_length = 254, null=True, blank=True)
  whatsapp_number = models.CharField(max_length=50, null=True, blank=True)
  telegram_username = models.CharField(max_length=50, null=True, blank=True)
  position = models.CharField(max_length=50, choices=POSITION_CHOICES, null=True, blank=True)
  generation = models.CharField(max_length=50, choices=GENERATION, null=True, blank=True)
  other_roles = models.CharField(max_length=200, null=True, blank=True)
  entity = models.CharField(max_length=50, choices=ENTITY_CHOICES, null=True, blank=True)
  region = models.CharField(max_length=50, choices=REGION_CHOICES, null=True, blank=True)
  date_of_birth = models.DateField(null=True, blank=True)
  gender = models.CharField(max_length=50, choices=GENDER_OPTIONS, null=True, blank=True)
  picture_of_the_delegate = models.ImageField(upload_to ='', null=True, blank=True, validators=[validate_image_size])
  shirt_size = models.CharField(max_length=50, choices=SHIRT_SIZES, null=True, blank=True)

  name_as_per_passport = models.CharField(max_length=200, null=True, blank=True)
  natonality = models.CharField(max_length=50, null=True, blank=True)
  current_living_country_territory = models.CharField(max_length=50, null=True, blank=True)
  passport_scanned_photo = models.ImageField(upload_to ='', null=True, blank=True, validators=[validate_image_size])
  passport_issue_date = models.DateField(null = True, blank=True)
  passport_expiry_date = models.DateField(null = True, blank=True)

  academic_background = models.CharField(max_length=50, choices=ACADEMIC_BACKGROUND, null=True, blank=True)
  partners_topics = models.CharField(max_length=300, null=True, blank=True)
  how_to_make_partners_spaces_relevant = models.CharField(max_length=300, null=True, blank=True)
  global_partner_for_key_note = models.CharField(max_length=50, choices=GLOBAL_PARTNER_KEYNOTE, null=True, blank=True)
  what_do_you_want_to_know_about_partners = models.CharField(max_length=300, null=True, blank=True)
  career_confidence = models.CharField(max_length=50, choices=CAREER_SCORE, null=True, blank=True)
  work_experience = models.CharField(max_length=300, null=True, blank=True)
  partners_for_career = models.CharField(max_length=50, choices=GLOBAL_PARTNER_CAREER, null=True, blank=True)
  why_this_global_partner = models.CharField(max_length=300, null=True, blank=True)
  engagements = models.CharField(max_length=50, choices=ENGAGEMENT_OPTIONS, null=True, blank=True)

  room_preference = models.CharField(max_length=50, choices=ROOM_OPTIONS, null=True, blank=True)
  food = models.ManyToManyField('Food')
  allergies = models.CharField(max_length=100, null=True, blank=True)
  pre_and_post_trips = models.CharField(max_length=50, choices=POST_PRE_TRIPS, null=True, blank=True)
  merchandise = models.CharField(max_length=50, choices=YES_NO_CHOICES, null=True, blank=True)
  egyptian_nights_expectations = models.CharField(max_length=400, null=True, blank=True)
  cc_team_expecations = models.CharField(max_length=400, null=True, blank=True)
  logistical_expectations = models.CharField(max_length=400, null=True, blank=True)
  agenda_expectations = models.CharField(max_length=400, null=True, blank=True)
  visa_support = models.CharField(max_length=50, choices=YES_NO_CHOICES, null=True, blank=True)

  user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

  def __str__(self):
    return self.first_name + " " + self.last_name
  