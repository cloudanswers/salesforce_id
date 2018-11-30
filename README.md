# salesforce_id

Salesforce uses an ID scheme with some nuances and this library simplifies working with them

    > from salesforce_id import SalesforceID
    > # instanciate the object with an existing sobject id:
    > contact_id = SalesforceID('0030000009rifh3')
    > print(contact_id)
    0030000009rifh3
    
    > # increment the id
    > contact_id.add(1)
    0030000009rifh4

## TODO

- unit tests
- upload to pypi

