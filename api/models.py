from django.db import models
import string, random

class A(models.Model):
   a = models.CharField(max_length=63, unique=True,)  # ["asia","africa","america","antarctica","australia","austria","aachen","aberdeen","abu dhabhi","addis ababa","adelaide","aizuwakamatsu","aktobe","alexandria","algeris","amandora","amsterdam","alaska","ankara","antwerp","arad","arak","athens","auckland","agra","ahmedabad","ahmednagar","aizwal","ajax","ajmer","akola","algeris","alwar","ambala","americana","amravati","atlanta","augusta","aurangabad","austin","amritsar","arunachal pradesh","assam","agartala","azerbaijan","andhra pradesh","andaman islands","argentina","angola","abuja","asunican","alberta","arizona","antigua","alappuzha","alabama","andora","alicante","afghanistan","annapolis","arkanas city","atlantic city","augsburg","aceh","awaji islands","akita","algeria","albania","anand","aomori","anantpur"];
   def __str__(self):
       return self.a

class B(models.Model):
   b = models.CharField(max_length=63, unique=True,)  # ["bengaluru","brisbane","botswana","bermuda","bristol","budapest","bucharest","birmingham","bhuj","berlin","bikaner","bhaghdad","belgium","brazil","bulgaria","burkina","bhutan","bhadrak","bhubhaneshwar","bihar","brasilia","buenos aires","bangladesh","beijing","boston","bay city","barcelona","baraboo","barbados","boonville","baku","bandung","basel","bharuch","bhopal","bijapur","boyota","bangkok","buldhana","bern","bilbao","binghamton","blacksburg","bordeaux","brighton","brooklyn","brussels"] ;
   def __str__(self):
       return self.b

class C(models.Model):
   c = models.CharField(max_length=63, unique=True,)  # ["canada","cameroon","california","canberra","chandigarh","chattisgarh","cairo","cambodia","chiplun","coimbatore","cambridge","cape town","czech republic","cuba","columbia","chile","cyprus","china","chad","chicago","charlotte","central african republic","costa rica","croatia","carcas","cape coral","celina","charleston","chester","clinton","columbo","christchurch","columbus","copenhagen","canton","chennai","carolina"] ;
   def __str__(self):
       return self.c
class D(models.Model):
   d = models.CharField(max_length=63, unique=True,)  # ["delhi","damascus","dublin","diu","daman","dispur","daimabad","doha","dhaka","daulatabad","darjeeling","dallas","durango","dominican republic","dubai","dholavira","durham","davenport","dortmund","dundee","dibrugarh","darwin","denpasar","denver","dar essalam","deoli","derby","dhule","donetsk","djibouti","durban"] ;
   def __str__(self):
       return self.d

class E(models.Model):
   e = models.CharField(max_length=63, unique=True, )  # ["egypt","eucador","el paso","erie","estonia","england","ethopia"] ;
   def __str__(self):
       return self.e

class F(models.Model):
   f = models.CharField(max_length=63, unique=True, )  # ["finland"," frankfurt","florida","firodabad","ferozpur","france","fiji","florence","friedericksburg"] ;
   def __str__(self):
       return self.f

class G(models.Model):
   g = models.CharField(max_length=63, unique=True, )  # ["ghana","gangtok","guinea","ghaziabad","germany","guanghzou","gandinagar","gandhidham","greece","goa","guwahati","greenland","gwailor","gabon","gulbarga","georgia","geneva","greenevilla","gorakhpur","guyana","guatemala"] ;
   def __str__(self):
       return self.g

class H(models.Model):
   h = models.CharField(max_length=63, unique=True, )  # ["helsinki","holand","himachal pradesh","hokkaido","hungary","hiroshima","houston","honduras","hubli","hyderabad","halifax","hamilton","hollywood","hong kong","hawaii","hanoi"] ;
   def __str__(self):
       return self.h

class I(models.Model):
   i = models.CharField(max_length=63, unique=True, )  # ["india","indonesia","italy","ireland","iceland","indiana","indianapollis","indira point","ichalkaranji","igatpuri","islamabad","istanbul","istambul","indore","illinois","iran","iraq","itanagar","imphal"] ;
   def __str__(self):
       return self.i

class J(models.Model):
   j = models.CharField(max_length=63, unique=True, )  # ["jamshedpur","jamnagar","jersey city","jhelum","jabalpur","jerusalem","jeddha","jaipur","jhansi","jharkhand","japan","jalandhar","jodhpur","jalpaiguri","jammu","jakarta","jamaica"] ;
   def __str__(self):
       return self.j

class K(models.Model):
   k = models.CharField(max_length=63, unique=True, )  # ["karnataka","kuala lumpur","kabul","kashmir","krygyztan","kota","kolkata","kazakhstan","kerala","kiribati","kolhapur","kochi","karachi","kuwait","kanpur","kenya","kentucy","kathmandu","kohima","kingston","kalol","kandy","kishanganj","kofu","kyoto","kargil","katra","kedarnath","kalpa","kullu"] ;
   def __str__(self):
       return self.k

class L(models.Model):
   l = models.CharField(max_length=63, unique=True, )  # ["lachung","lucknow","latur","ladhakh","lisbon","lawasa","luxemburg","london","lahore","libya","los angeles","las vegas","lincoln","lynn","liverpool","ludhiana","lakshadweep islands"] ;
   def __str__(self):
       return self.l

class M(models.Model):
   m = models.CharField(max_length=63, unique=True, )  # ["mumbai","maharashtra","madhya pradesh","moscow","madrid","mongolia","malaysia","meerut","manglore","massachusetts","madagascar","melbourne","manchester","manila","mirzapur","manipur","meghalaya","mizoram","manhattan","marshal islands","madurai","multan","mysore","mecca","medina","maldives","mahabaleshwar","matheran","mohenjodaro","mexico","mexico city","myanmar","malappuram","miami","milan","montreal","munich","muscat","monacco","morocco","mozambique","madina","matsudo","matsusaka","matsuyama","malawi","moldova","malta","mali"] ;
   def __str__(self):
       return self.m

class N(models.Model):
   n = models.CharField(max_length=63, unique=True, )  # ["nagaland","nigeria","new york","new delhi","navi mumbai","new zealand","nottingham","new jersey","nagasaki","nepal","nainital","nashik","nagpur","newcastle","northern island","new orleans","niger","nairobi","norway","netherlands","north carolina","north korea","namibia","north america","north macedonia","nanded","nandurbar","navsari","newport","noida","norwich","northampton","nagahama","nicobar islands","nizampur"] ;
   def __str__(self):
       return self.n

class O(models.Model):
   o = models.CharField(max_length=63, unique=True, )  # ["odisha","orleans","ottawa","osaka","osmanabad","ohio","oman","orleans","ontario","oaxaca","odisha","olympia","orlando","oshawa","oxford","oslo","ozamiz","oklahoma","oklahoma city","ongole","orange","oyo"] ;
   def __str__(self):
       return self.o

class P(models.Model):
   p = models.CharField(max_length=63, unique=True, )  # ["patna","palembang","paris","perth","peru","pakistan","punjab","pune","pathanhkot","papa new guinea","port of spain","poland","phillipines","paraguay","palatine","panama","panama city","philadelphia","porto","prague","pennyslyavania","petoria","puri","puducherry"] ;
   def __str__(self):
       return self.p

class Q(models.Model):
   q = models.CharField(max_length=63, unique=True, )  # ["qatar","queensland","quebec city","quebec","quezon city","quincy","qwakertown"] ;
   def __str__(self):
       return self.q

class R(models.Model):
   r = models.CharField(max_length=63, unique=True, )  # ["rome","ranchi","rajasthan","rio de janerio","rampur","rawalpindi","raipur","roha","rhodesia","rajkot","reading","riyadh","rohtak","rotterdam","rabat","rossov-on-don","ratlam","roorkee","rotherham","russia"];
   def __str__(self):
       return self.r

class S(models.Model):
   s = models.CharField(max_length=63, unique=True, )  # ["sikkim","switzerland","saudi arabia","shimla","srinagar","surat","silvasa","satara","siliguri","siachen","sudan","sweden","sao paulo","san marino","san fransisco","san diego","san pedro","san antonio","san andreas","san jose","san gabriel","san macos","san juan","san luis","santiago","sri lanka","siberia","serbia","sydney","saudi arabia","south korea","shanghai","seoul","somalia","south africa","south carolina","southampton","saki","slovenia","surrey","stockholm","sindhudurg","sofia","sarajevo","stuggart","salt lake city","sangli","santos","secunderabad","sendai","sharjah","sheffield","shillong","swansea","sparta","smithvilla","spain","south america","st petersberg"] ;
   def __str__(self):
       return self.s


class T(models.Model):
   t = models.CharField(max_length=63, unique=True, )  # ["tripura","toronto","tanzania","telengana","taiwan","toronto","texas","timbaktu","turkmenistan","turkey","tiruvananthapuram","tokyo","tehran","tehran","tehri city","tamil nadu","tucson","tennesse","taipei","tasmania","trinidad and tobago","tajikistan","thane"] ;
   def __str__(self):
       return self.t

class U(models.Model):
   u = models.CharField(max_length=63, unique=True, )  # ["uganda","uruguay","ukraine","uunited states of america","united kingdom","united arab emirates","uttarakhand","uttar pradesh","udaipur","ujjain","uzbekistan","ube","uji"] ;
   def __str__(self):
       return self.u

class V(models.Model):
   v = models.CharField(max_length=63, unique=True, )  # ["letanasi","victoria","vatican city","vietnam","venezuela","vishakapatnam","vadodra","vapi","valsad","valencia"] ;
   def __str__(self):
       return self.v

class W(models.Model):
   w = models.CharField(max_length=63, unique=True, )  # ["washington dc","warsaw","wellington","wardha","wolverhampton","winston","westminster","wuhan","westland","waco","waterloo","warren","wolfsburg","winston"] ;
   def __str__(self):
       return self.w

class X(models.Model):
   x = models.CharField(max_length=63, unique=True, )  # ["xia xia","xianyang","xiangyang","xichang","xalapa","xiamen","xintai"] ;
   def __str__(self):
       return self.x

class Y(models.Model):
   y = models.CharField(max_length=63, unique=True, )  # ["yokohama","yongzhou","yalta","yumen","yamagata","yavatmal","york","yemen"] ;
   def __str__(self):
       return self.y

class Z(models.Model):
   z = models.CharField(max_length=63, unique=True, )  # ["zambia","zimbabwe","zanzibar city","zagazig","zabol","zaoyang","zaria","zurich","zagreb","zandvoort","zenica"] ;
   def __str__(self):
       return self.z

'''
def generate_code():
    length=4
    while True:
        code = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if Room.objects.filter(code=code).count() == 0:
            break
    return code


# Create your models here.
class Room(models.Model):
    code = models.CharField(max_length=4, unique=True, default=generate_code)
    host = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=16, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
'''
