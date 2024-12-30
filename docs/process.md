# Design Pattern: Repository Pattern

## Waarom dit patroon?
- Duidelijke scheiding tussen data-operaties en businesslogica.
- Herbruikbaarheid van code door abstracties.
- Eenvoudige testbaarheid via dependency injection.

## Implementatie
- Data wordt beheerd via een 'DataRepository'-klasse.
- Validatie- en filtermethodes worden losgekoppeld in een aparte module.

## Voorbeeld code-structuur:
- src/repositories/data_repository.py (verwerking en validatie van data)
- src/services/data_service.py (analyse en aggregatie)
- src/utils/validators.py (validatiefuncties)

