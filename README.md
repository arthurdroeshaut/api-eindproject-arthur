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










