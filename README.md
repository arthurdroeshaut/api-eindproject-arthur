API Documentatie

Beschrijving van mijn gekozen onderwerp.

Dit is de documentatie voor de Star Wars API. Deze API biedt toegang tot informatie over personages, voertuigen en films uit de Star Wars franchise.
ik heb hiervan ook enkele voorbeelden in een json file gestopt.

alle nodige links geef ik hier ook nog even weer:

algemene eisen: 

api op github: https://github.com/arthurdroeshaut/api-eindproject-arthur

okteto hosted : https://system-service-arthurdroeshaut.cloud.okteto.net/(endpoints here)


gekozen uitbreiding: ik heb gekozen voor de Frontend + hosting op netlify als uitbreidingn

front-end op github: https://github.com/arthurdroeshaut/api-eindproject-frontend

website op netlify: https://exquisite-jalebi-13c555.netlify.app/

korte uitleg endpoints. 
minstens 3 gets, minstens 1 post, minstens 1 put en minstens 1 delete:
Met deze API kun je verschillende informatie uit de Star Wars universum ophalen en toevoegen. Er zijn 3 get-endpoints waarmee je de random naam van een personage, de random titel van een film en een random type van een voertuig kunt ophalen. Met de 3 post-endpoints kun je informatie over personages, films en voertuigen toevoegen. Met de put-endpoint kun je informatie over personages bijwerken op basis van hun ID en met de delete-endpoint kun je voertuigen verwijderen ook op basis van een ID.

verder is er ook nog een post endpoint post/token dit is voor de authenticatie en het aanmaken van je 'account', hierop kom ik later nog terug. Deze is aanwezig in mijn website maar werkt niet omdat het me niet echt praktisch lijkt voor gebruikers om deze token te hebben. je zou deze kunnen laten werken door de token weer te geven zodat de gebruikers deze ook zelf kunnen gebruiken maar dit heb ik niet gedaan. 


#note ik ga screenshots tonen uit fastapi, postman & de website om aan te tonen dat deze werken maar ik zet niet 3x van hetzelfde een screenshot erin dus er is wat afwisseling in de screenshots.


swagger/openapi endpoints screenshot: 
De volgende endpoints zijn beschikbaar onder docs bij je API:

<img width="950" alt="fastapi endpoints" src="https://user-images.githubusercontent.com/61418112/211170555-15a09457-5bb0-4590-a284-7b26d612ed5b.png">

onze eerste get request is de request voor een random personage zijn name op te vragen.
deze request krijg je door volgende link in te geven, dit heb ik gedaan in postman: 
https://system-service-arthurdroeshaut.cloud.okteto.net/characters/random/name

<img width="857" alt="get request random characters" src="https://user-images.githubusercontent.com/61418112/211170074-96923609-dd4c-49ca-a7e3-045e6590cec3.png">

onze tweede get request is de request voor een random film titel op te vragen.
deze request ziet er zo uit in fastapi:

<img width="853" alt="swagger screenshot random film titel" src="https://user-images.githubusercontent.com/61418112/211170373-93e1bf42-8969-404d-8889-215ef92c376a.png">

de derde get request is de request voor een random voertuigtype op te vragen 
deze request ziet er zo uit in postman:

<img width="650" alt="screenshot postman vehicle random" src="https://user-images.githubusercontent.com/61418112/211170595-526ffb56-5314-47ec-b747-0753cb308394.png">

en zo zien deze 3 requests eruit op de website:

<img width="393" alt="screenshots get request website" src="https://user-images.githubusercontent.com/61418112/211170672-ea4614f2-7006-4011-b559-5f51799b92f8.png">

nu over naar de post endpoints.

om te beginnen met de post request om een eigen personage aan te maken waarbij je zelf de naam, soort, geboorteplaats en kleur lichtzwaard kunt kiezen.
deze request ziet er zo uit in fastapi:

<img width="854" alt="image" src="https://user-images.githubusercontent.com/61418112/211171037-cb5d42e3-bfb9-484c-95ce-3e6939192264.png">
en als we het uitproberen in fastapi:

<img width="704" alt="image" src="https://user-images.githubusercontent.com/61418112/211171060-e4ec05f7-635d-42d4-b426-ce3097b594ad.png">

dit is een voorbeeld json hiervan, voor de gebruikte post:

<img width="164" alt="image" src="https://user-images.githubusercontent.com/61418112/211171254-beaf3579-fed4-4ed9-89c9-6b6139a88781.png">

als tweede post is er eentje om je eigen film aan te maken met titel, releasedatum en regisseur zelf te kiezen.
de request ziet er zo uit in postman, hier moet je wel zelf nog de body meegeven. (kopieren uit de json en dan de spaties weghalen tot je dit bekomt.

<img width="644" alt="image" src="https://user-images.githubusercontent.com/61418112/211171546-f8f3e1ce-3204-4ff1-b89e-b4ee7906667e.png">


als voorbeeld json hiervan: 

<img width="319" alt="image" src="https://user-images.githubusercontent.com/61418112/211171422-dd216366-38a1-4b32-b782-ab052a30e283.png">

als derder en laatste post is er eentje om je eigen voertuig te maken met zelfgekozen naam, type en affiliatie (tot welke groep ze behoren) 
deze request ziet er zo uit in fastapi: 

<img width="713" alt="image" src="https://user-images.githubusercontent.com/61418112/211171377-1b2b0734-0786-4e03-8a6d-6235ea506b86.png">


hier een voorbeeld binnen fastapi:

<img width="707" alt="image" src="https://user-images.githubusercontent.com/61418112/211171365-7796b2bf-e59e-4fa0-9f17-b77422427e9d.png">

als voorbeeld json hiervan: 

<img width="202" alt="image" src="https://user-images.githubusercontent.com/61418112/211171396-58b0c992-8035-49ff-bd61-08917a1100a0.png">

en op de website staan alle 3 de post requests en ziet dit er zo uit voor de request:

<img width="231" alt="image" src="https://user-images.githubusercontent.com/61418112/211171734-3d90259c-4bc6-4841-8308-8addabc9e8f1.png">


en zo ziet het eruit na de request:

<img width="235" alt="image" src="https://user-images.githubusercontent.com/61418112/211171704-273b5339-2dbf-4ba4-ab40-c30ead6e3ea6.png">



nu ga ik nog overgaan op de delete en put endpoints, deze zijn niet aanwezig in de website maar kan ik wel laten zien.

in fastapi:

<img width="719" alt="image" src="https://user-images.githubusercontent.com/61418112/211171751-54dd0a47-c95b-4d79-ab3b-160a0336cec3.png">

als eerste de put endpoint, deze put endpoint laat mij een ID ingeven en door deze ID in te geven kan ik de inhoud van deze ID aanpassen.
zoals je hieronder ziet heb ik characterID 2 ingevuld, nu kan ik hieronder de body aanpassen naar wat ik ervan wil maken in dit geval maak dit van:

<img width="718" alt="image" src="https://user-images.githubusercontent.com/61418112/211171809-75ad19db-9f6e-4166-a90c-49af7b7b25d6.png">

als dit werkt krijg je dit als response:

<img width="710" alt="image" src="https://user-images.githubusercontent.com/61418112/211171826-66f2e109-cbcf-4a7e-96e4-4b646fd23bbd.png">

nu voor de delete endpoint, hiermee kunnen we een voertuig compleet verwijderen uit de lijst op basis van hun ID, in het voorbeeld hieronder heb ik vehicle_id 3 verwijdert, dus nu zal vehicle met id 3 niet meer aanwezig zijn, tot we een nieuwe vehicle aanmaken. aangezien dat id 3 nu terug beschikbaar is.

<img width="532" alt="image" src="https://user-images.githubusercontent.com/61418112/211171852-202a6011-d369-4992-896d-6e122c0c2e6e.png">



nu hier komt het hasing & Oath gedeelte deels terug:
in de users & token endpoints.

dit is een endpoint en die geeft je een token waarmee jij aan versleutelde "data kan geraken zoals hier in deze foto staat een sleutel, hier kan je niet in zonder token, een token krijg je op deze manier:

foto versleutelde "data": je ziet de sleuter achter read users staan, omdat onze users hun data niet door iedereen gezien mag worden.

<img width="541" alt="image" src="https://user-images.githubusercontent.com/61418112/211171981-fb4c8da1-ab42-4684-8b00-ab4dec42749f.png">

hoe je aan deze sleuten komt is zo:
1. eerst doe je een user create

<img width="537" alt="image" src="https://user-images.githubusercontent.com/61418112/211172072-4e7671ca-3b4e-46db-a12d-ae563b0bbe16.png">

hierna doe je de /token endpoint en hier geef je je inloggegevens weer: 

<img width="540" alt="image" src="https://user-images.githubusercontent.com/61418112/211172090-58daa922-ddf8-4648-8324-60d1dcd7bd77.png">


als dit is gelukt krijg je hieronder je token te zien:

<img width="534" alt="image" src="https://user-images.githubusercontent.com/61418112/211172103-20889d82-5698-4396-a6db-126b504f4d18.png">


met deze token kun je je versleutelde gegevens bekijken, nu in mijn geval is dit niet veel want ik heb niet veel versleutelde gegevens.

<img width="640" alt="image" src="https://user-images.githubusercontent.com/61418112/211172220-23f42056-494a-4d64-b047-0063ce9233b7.png">

wat er gebeurt als je probeert de gegevens te bekijken zonder token:

<img width="637" alt="image" src="https://user-images.githubusercontent.com/61418112/211172250-a82e023e-199b-4270-9ac5-942c250f72ab.png">


dit waren al mijn endpoints en mijn website heb ik ook kunnen aantonen hoe deze werkt.
ik heb dus de volledige basis eisen gemaakt, en de frontend + netlify als extra eisen.
ik heb ook een beetje styling gedaan.
dus mijn maximumscore is 85%





