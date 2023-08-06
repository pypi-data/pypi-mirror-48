This packages permits easier access to Decipher's Beacon REST API. 

If you are a Beacon user, you can use the API to read and write your survey data, provision users, create surveys
and many other tasks.

If you are not a Decipher client, visit https://www.decipherinc.com/n/ to learn more about our services.

Documentation
-------------

For an introduction to using the API, see this Knowledge Base article: http://kb.decipherinc.com/index.php?View=entry&EntryID=5678

For current API reference documentation, see (production URL).

Quick Examples
--------------

Install the package::

  sudo pip install decipher
  
Visit Research Hub, and from the User Links menu (click on your picture in the upper right corner), select API Keys.

Provision a new key; then on the command line run::

  beacon login
  
  Enter your API key
  See  http://kb.decipherinc.com/index.php?View=entry&EntryID=5678
  
  API KEY:  1234567890abcdef1234567890abcdef
  
  Enter your host, or press Enter for the default v2.decipherinc.com
  Host: v2.decipherinc.com
   
The "login" action saves your API information in the file ~/.config/beacon.

From the command line you can now run the "beacon" script which lets you quickly run an API call::

  beacon -t get users select=id,email,fullname,last_login_from sort=-last_login_when limit=10

The above illustrates:
 * An API call with method GET
 * Targetting the "users" resource, which will be at /api/v1/users
 * Using the "projection" feature to select only 4 fields (id, email, full name and IP of last login)
 * Using the "sorting" feature to order the response by descending time of last login
 * Using the "pagination" feature to limit output to 10 first entries
 * Using the -t option to output the data as a formattet text table, rather than JSON.

If you replace the -t option with -p you will see the Python code needed for that same call::

 from decipher.beacon import api 
 users = api.get("users", select="id,email,fullname,last_login_from", 
  sort="-last_login_when", limit=10)
 for user in users:
    print "User #{id} <{email}> logged in last from {last_login_from}".format(user)
    

Authentication
--------------

You need an API key to use the API. You can supply this key in 3 ways when connecting remotely:

By specifying it in the ~/.config/beacon file which has this format::

 apikey=1234567890abcdef1234567890abcdef
 host=v2.decipherinc.com
 
By setting an environment variable::

    export BEACON_API=1234567890abcdef1234567890abcdef
    export BEACON_HOST=v2.decipherinc.com
  
Be aware that environment variables on most UNIX systems are visible to other programs running on the same machine.

By explicitly initializing the API with login information::

    from decipher.beacon import api
    api.login("1234567890abcdef1234567890abcdef", "v2.decipherinc.com") 
  

API Versioning
--------------

Current API uses version 1. This package will only do version 1 calls. To opt-in to a newer version of the API,
run (prior to doing any calls)::

 from decipher.beacon import api
 api.version = 2


Type hints
----------

The data returned from the API is serialized as JSON. However the API also provides a "type hint" for the real object
type. This is transmitted in the `x-typehint` header which is a JSON dictionary mapping field name to type.

Unless you disable it by using `api.typehint = False`, the API will turn some of the returned objects into "enriched"
objects, and convert some types. For example, the `rh/api` API returns an object containing a field named created_on which
is an ISO8601 string. The typehint header tells the API client that "created_on" is a "datetime" and the API turns
this serialized datetime into an actual datetime object.

The enriched object contain methods that correspond to what you can do to this type of resource in the API as well
as easier access to build another API call to the resource for methods not wrapped by this current library version.


