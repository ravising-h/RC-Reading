# RC Reading

## Using Google-Tesseract and Google.Vision API for Extracting Information from RC Book.

![](RC/txt_mudit_b8_1_807.jpg)

                               *Image of a typical RC Book*
To Use this repo
Clone this repo in your pc
`$ git clone https://github.com/ravising-h/RC-Reading`
If you want to use tesseract then keep Images in Image folder and make a Text folder and type command
`$ python extractingInfo.py t Image Text`
If you want to use Google.Vision API then Set Up the Enviroment for more help [visit here](https://cloud.google.com/vision/?utm_source=google&utm_medium=cpc&utm_campaign=japac-IN-all-en-dr-bkws-all-all-trial-b-dr-1003987&utm_content=text-ad-none-none-DEV_c-CRE_252375308317-ADGP_Hybrid+%7C+AW+SEM+%7C+BKWS+~+T1+%7C+BMM+%7C+ML+%7C+M:1+%7C+IN+%7C+en+%7C+Vision+%7C+OCR-KWID_43700030447551997-kwd-327501810122&userloc_9061667&utm_term=KW_%2Bgoogle%20%2Bocr%20%2Bapi&ds_rl=1264446&gclid=CjwKCAiAzanuBRAZEiwA5yf4utfSwOb9bqzpQvLuAQ7ywFZmw4PreT7EPI_VN8mTyBIB6yxOwv5cRBoCDzMQAvD_BwE). Then type the command by repeating above process mentioned in tesseract

`$  python extractingInfo.py g Image Text` 

requirments:
`1. tqdm`
`2. google SDK`
`3. Tesseract`
`4. Pandas`
`5. io`
`6. difflib`
`7. re`

The Output file looks like this:
`GOVERNMENT OF HARYANA
CERTIFICATE OF REGISTRATION
(FORM NO. 23 RULE 48)
HR10-P-5470
Registration No.
Name & Address
DAVENDER SINGH
of Regd. Owner
S/o MAHENDER SINGH
VPO. NANGAL KHURD,
DISTT. SONIPAT
Previous Regn. No. N/A
Previous Owner N/A
MALCM41VR9M079263* L
Chasis No.
Engine No.
Month/Yr of
Seating Capacity 5
D4FA9U817848
31/12/2009
(including driver)
Diesel
Fuel Used
2609 2011 17:14
GOVERNMENTOFHARYANACERTIFICATEOFREGISTRATION(FORMNO.23RULE48)HR10-P-5470RegistrationNo.Name&AddressDAVENDERSINGHofRegd.OwnerS/oMAHENDERSINGHVPO.NANGALKHURD,DISTT.SONIPATPreviousRegn.No.N/APreviousOwnerN/AMALCM41VR9M079263*LChasisNo.EngineNo.Month/YrofSeatingCapacity5D4FA9U81784831/12/2009(includingdriver)DieselFuelUsed2609201117:14`

### Methos to extract Data

#### 1.Registration Number
To extract registration number I tried to understand the pattern in it.
I observed the pattern and then made regex according to it which stored in `utils` folder. From the text file I first tried to know the state for which I find `Delhi or Haryana` in text file by the help of difflib. This Library helps in finding word with spelling mistakes.

#### 2.Registration Date
Generally the date more then current year is validation date if we minus `15 yrs` to it we can achieve Registration date. I used this method.
Also there are 3 dates in RC the oldest is of Mfg date middle one is Regn Date last is Expiry date.
#### 3.Chasis Number
I made combination of `Regex` of Chasis Number. I achived good results. regex is stored in `Utils`
#### 3.Engine Number
I made combination of `Regex` of Engine Number. I achived good results. regex is stored in `Utils`
### 4.Name
String stored after keywords like :
* name
* owner's name
* S/W/D of

#### 5.Mfg Date
I made combination of regex for it. Typically found in format like 08/2008 (NO Date)
