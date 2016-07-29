from pymongo import MongoClient

client = MongoClient()

abc = { 'name': 'Contact Name',
  'dob': '1980-01-01',
  'notes': 'Notes about contact',
  'details': [
    { 'type': 'email',
      'data': 'something@something.com'
    }, {
      'type': 'phone',
      'data': '555-555-5555'
    } ]
}
my_collection = client.my_database.my_collection
my_collection.insert(abc)

def find_object(primary_key):
    '''finds and returns an object matching the primary key. returns None if not found'''
    my_object = my_collection.find_one({'name': 'Contact Name'})

def update_object(new_object):
    '''updates an object if it exists, inserts if it does not exist'''
    if my_object is None:
        raise ValueError('Not Found!')
    my_object['details'].append({'type': 'mobile', 'data': '555-555-5432'})
    my_collection.update({'name': 'Contact Name'}, my_object)

def remove_object(primary_key):
    ''''deletes the object matching primary key. returns true if deleted false if not found'''

    del_result = my_collection.delete_one({'name': 'Contact Name'})
    print 'deleted %d documents' % (del_result.deleted_count,)

