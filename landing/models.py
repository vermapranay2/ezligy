from django.core.validators import RegexValidator
from django.db import models
from multiselectfield import MultiSelectField
from django.shortcuts import render
from django.core.urlresolvers import reverse
from tinymce.models import HTMLField

# Create your models here.

class Register(models.Model):
    GENDERS =(('M', 'MALE'),
              ('F', 'FEMALE')

    )
    AREA =(
        ('CIVIL','Civil Matters'),('CRIMINAL','Criminal Matters'), ('FAMILY','Family Disputes Matters '), ('LABOUR','Labour Disputes Matters'), ('FOREST','Forest Matters'),
        ('ROC','Company Matters'),('CONSUMER','Consumer Matters'),('EXCISE','Excise Matters'),('ELECTRICITY','Electricity Board Matters'),('EPF','Employee Provident Fund'),('RAILWAY','railway Matters'),
        ('PENSION','Pension Matters'),('INCOME','Income Tax Matters'),('WRITS','Writs')

    )

    first_name = models.CharField(max_length=50,blank=False,default=None)
    last_name = models.CharField(max_length=50,blank=False,default=None )
    father_name = models.CharField(max_length=50,blank=False,default=None )
    date_of_birth=models.CharField(max_length=50,blank=False,default=None,)
    gender = models.CharField(choices=GENDERS, default='M', max_length=10,blank=False,)
    email = models.EmailField(max_length=50,blank=False,default=None)
    office_address = models.CharField(max_length=10000,blank=False,default=None)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    mobile_number = models.CharField(validators=[phone_regex], max_length=10,blank=False,default=None)  # validators should be a list
    office_landline = models.CharField(validators=[phone_regex], max_length=10,blank=False,default=None )
    State_BAR_Registration = models.CharField(max_length=20,blank=False,default=None)
    local_BAR =  models.CharField(max_length=20,blank=False,default=None)
    Place_Of_Practice = models.CharField(max_length=100,blank=False,default=None)
    area = MultiSelectField(choices=AREA,max_choices=3,max_length=100,blank=False,default=None)
    other_area = models.CharField(max_length=100,blank=True,default=None )



    def __str__(self):
        return str(self.pk) + str(self.first_name)



class Heads(models.Model):
    heading=models.CharField(max_length=100)

    def __str__(self):
        return  str(self.heading)







class Service(models.Model):
    heading = models.ForeignKey(Heads,null=True)
    services = models.CharField(max_length=100)
    cost = models.CharField(max_length=100)
    image = models.ImageField()
    url= models.CharField(max_length=100, default=None)

    def __str__(self):
        return str(self.services)


class Single(models.Model):
    name=models.ForeignKey(Service,null=True)
    image=models.ImageField()
    cost=models.CharField(max_length=100)
    defination=models.TextField()
    video=models.FileField()
    features=models.TextField()
    benefits = models.TextField()
    limitations=models.TextField()
    procedure = models.TextField()
    documents = models.TextField()
    faqs=models.TextField()

    def __str__(self):
        return str(self.name)



class Contact(models.Model):
    name=models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=10, blank=False, default=None)
    email = models.EmailField()
    service=models.ForeignKey(Service)
    message=models.TextField( default=None)



    def __str__(self):
        return str(self.name)



class Rti(models.Model):
    GENDERS = (('M', 'MALE'),
               ('F', 'FEMALE')

               )


    MINISTRY = (
                ('1','Cabinet Secretariat'),
                ('2','Comptroller and Auditor General of India'),
                ('3','Department of Administrative Reforms &amp; PG'),
                ('4','Department of Agricultural Research &amp; Education'),
                ('5','Department of Agriculture, Cooperation &amp; Farmers Welfare'),
                ('6','Department of Animal Husbandry, Dairying and Fisheries'),
                ('7','Department of Atomic Energy'),
                ('8','Department of Bio-Technology'),
                ('9','Department of Chemicals &amp; Petrochemicals'),
                ('10','Department of Commerce'),
                ('11','Department of Consumer Affairs'),
                ('12','Department of Defence'),
                ('13','Department of Defence Production'),
                ('14','Department of Economic Affairs'),
                ('15','Department of Electronics &amp; Information Technology'),
                ('16','Department of Empowerment of Persons with Disabilities'),
                ('17','Department of Expenditure'),
                ('18','Department of Ex-Servicemen Welfare'),
                ('19','Department of Fertilisers'),
                ('20','Department of Financial Services'),
                ('21','Department of Food &amp; Public Distribution'),
                ('22','Department of Health &amp; Family Welfare'),
                ('23','Department of Health Research'),
                ('24','Department of Heavy Industries'),
                ('25','Department of Higher Education, M/o Human Resource Development'),
                ('26','Department of Industrial Policy &amp; Promotion'),
                ('27','Department of Investment and Public Asset Management'),
                ('28','Department of Justice'),
                ('29','Department of Legal Affairs'),
                ('30','Department of Pensions &amp; Pensioners Welfare'),
                ('31','Department of Personnel &amp; Training'),
                ('32','Department of Pharmaceuticals'),
                ('33','Department of Posts'),
                ('34','Department of Public Enterprises'),
                ('35','Department of Revenue'),
                ('36','Department of School Education and Literacy, M/o Human Resource Development'),
                ('37','Department of Science &amp; Technology'),
                ('38','Department of Scientific &amp; Industrial Research'),
                ('39','Department of Space'),
                ('40','Department of Telecommunications'),
                ('41','Election Commission of India'),
                ('42','Food Safety &amp; Standards Authority of India(FSSAI)'),
                ('43','Legislative Department'),
                ('44','Lok Sabha Secretariat'),
                ('45','Ministry of AYUSH'),
                ('46','Ministry of Civil Aviation'),
                ('47','Ministry of Coal'),
                ('48','Ministry of Corporate Affairs'),
                ('49','Ministry of Culture'),
                ('50','Ministry of Development of North Eastern Region'),
                ('51','Ministry of Drinking Water and Sanitation'),
                ('52','Ministry of Earth Sciences'),
                ('53','Ministry of Environment, Forest and Climate Change'),
                ('54','Ministry of External Affairs'),
                ('55','Ministry of Food Processing Industries'),
                ('56','Ministry of Home Affairs'),
                ('57','Ministry of Housing &amp; Urban Poverty Alleviation'),
                ('58','Ministry of Information &amp; Broadcasting'),
                ('59','Ministry of Labour &amp; Employment'),
                ('60','Ministry of Micro, Small and Medium Enterprises'),
                ('61','Ministry of Mines'),
                ('62','Ministry of Minority Affairs'),
                ('63','Ministry of New &amp; Renewable Energy'),
                ('64','Ministry of Panchayati Raj'),
                ('65','Ministry of Parliamentary Affairs'),
                ('66','Ministry of Petroleum &amp; Natural Gas'),
                ('67','Ministry of Power'),
                ('68','Ministry of Railways'),
                ('69','Ministry of Road Transport &amp; Highways'),
                ('70','Ministry of Rural Development'),
                ('71','Ministry of Shipping'),
                ('72','Ministry of Skill Development &amp; Entrepreneurship'),
                ('73','Ministry of Social Justice &amp; Empowerment'),
                ('74','Ministry of Statistics &amp; Programme Implementation'),
                ('75','Ministry of Steel'),
                ('76','Ministry of Textiles'),
                ('77','Ministry of Tourism'),
                ('78','Ministry of Tribal Affairs'),
                ('79','Ministry of Urban Development'),
                ('80','Ministry of Water Resources, River Development &amp; Ganga Rejuvenation'),
                ('81','Ministry of Women &amp; Child Development'),
                ('82','Ministry of Youth Affairs &amp; Sports'),
                ('83','National Institution for Transforming India (NITI Aayog)'),
                ('84','Northeast Frontier(N.F) Railway'),
                ('85','President Secretariat'),
                ('86','Prime Minister&#039;s Office'),
                ('87','Rajya Sabha Secretariat'),
                ('88','Vice-President Secretariat'),
                ('89', 'Others'),
                )



    department = models.CharField(choices=MINISTRY, max_length=100)
    name = models.CharField(max_length=100)
    gender = models.CharField(choices=GENDERS, max_length=100)
    address = models.TextField()
    pin_code = models.CharField(max_length=50)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
    contact = models.CharField(validators=[phone_regex], max_length=10, blank=False, default=None)
    email = models.EmailField()
    text_for_RTI_Request_application = models.TextField()

    def __str__(self):
        return str(self.name)


class ParalegalContact(models.Model):
    COURT =(('HIGH','High Court Of MP at Gwalior'),('DISTRICT','District Court Gwalior'),('FAMILY','Family Court Gwalior'),('REVENUE','Board Of Revenue MP'),('CONSUMER','Consumer Forum Gwalior'),('LABOUR','Labour / Industrial Court Gwalior')

    )
    CASE =(('AA','AA'),('AC','AC'),('AR','AR'),('ARBA','ARBA'),('ARBC','ARBC'),('CEA','CEA'),('CER','CER'),('CESR','CESR'),('COMA','COMA'),('COMP','COMP'),('COMPA','COMPA'),('CONA','CONA'),('CONC','CONC'),('CONCR','CONCR'),('CONT','CONT'),('CONTR','CONTR'),('CR','CR'),('CRA','CRA'),('CRR','CRR'),('CRRE','CRRE'),('CRRF','CRRF'),('CRRFC','CRRFC'),('CS','CS'),('EP','EP'),('FA','FA'),('FEMA','FEMA'),('ITA','ITA'),('ITR','ITR'),('LPA','LPA'),('MA','MA'),('MACE','MACE'),('MACOM','MACOM'),('MACTR','MACTR'),('MAIT','MAIT'),('MAVAT','MAVAT'),('MCC','MCC'),('MCOMA','MCOMA'),('MCP','MCP'),('MCRC','MCRC'),('MCRP','MCRP'),('MP','MP'),('MWP','MWP'),('OTA','OTA'),('RP','RP'),('SA','SA'),('STR','STR'),('TR','TR'),('VATA','VATA'),('WA','WA'),('WP','WP'),('WPS','WPS'),('WTA','WTA'),('WTR','WTR'),)

    name=models.CharField(max_length=100)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")


    contact = models.CharField(validators=[phone_regex], max_length=10, blank=False, default=None)
    court = models.CharField(choices=COURT, max_length=500)
    case = models.CharField(choices=CASE, max_length=100, default=None)

    def __str__(self):
        return str(self.name)




















