# Simple Serializable Credential Holder
This is a simple class for handling credentials. It is serializable for data transfer and is able to securely hold
credentials in its constructed form.

## Usage
To get a serialized credential holder, start by picking a passphrase (that you must remember or keep track of) for usage
as an encryption key. Then, create an instance of the CredentialHolder object using the credential you want to encrypt
and the passphrase and you can serialize it and use the string to store or communicate the credentials.

```Python
from credential_holder.holder import CredentialHolder
from credential_holder.serializer import  CredentialHolderSerializer


credential_holder = CredentialHolder("passphrase", "password")
serialized_credential_holder = CredentialHolderSerializer.serialize_credential_holder(credential_holder)
```

This creates something along the lines of 
```Python

serialized_credential = 'aG9sZGVyLl' + 'GQzXHInKQ==' # shortened representation of a large base64 string

```

This value can be then transferred and used elsewhere as follows

```Python
from credential_holder.serializer import  CredentialHolderSerializer

serialized_credential = "same_as_above"

serialized_credential_holder = CredentialHolderSerializer.deserialize_credential_holder(serialized_credential)

serialized_credential_holder.get_credential("passphrase")
```

Using the wrong passphrase will cause an Exception - you will not be able to decrypt a Credential Holder or serialized
string unless you have the same passphrase that was used to create it.