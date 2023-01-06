API Documentatie
Dit is de documentatie voor de Star Wars API. Deze API biedt toegang tot informatie over personages, voertuigen en films uit de Star Wars franchise.

Endpoints
De volgende endpoints zijn beschikbaar:

Personages
GET /characters: Retourneert een lijst met alle personages.
GET /characters/{id}: Retourneert het personage met het opgegeven ID.
POST /characters: Maakt een nieuw personage aan.
PUT /characters/{id}: Wijzigt het personage met het opgegeven ID.
DELETE /characters/{id}: Verwijdert het personage met het opgegeven ID.

Voertuigen
GET /vehicles: Retourneert een lijst met alle voertuigen.
GET /vehicles/{id}: Retourneert het voertuig met het opgegeven ID.
POST /vehicles: Maakt een nieuw voertuig aan.
PUT /vehicles/{id}: Wijzigt het voertuig met het opgegeven ID.
DELETE /vehicles/{id}: Verwijdert het voertuig met het opgegeven ID.

Films
GET /movies: Retourneert een lijst met alle films.
GET /movies/{id}: Retourneert de film met het opgegeven ID.
POST /movies: Maakt een nieuwe film aan.
PUT /movies/{id}: Wijzigt de film met het opgegeven ID.
DELETE /movies/{id}: Verwijdert de film met het opgegeven ID.

Authenticatie
De API ondersteunt OAuth 2.0 voor authenticatie. Om een aanvraag te doen, moet je een geldig access token opgeven in de Authorization header.
