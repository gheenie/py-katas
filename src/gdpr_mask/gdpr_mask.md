# GDPR Mask

You are working on a customer and stock application. The application has a number of functions that produce responses for an API. These responses sometimes include personally identifiable information (PII) which cannot be exposed to certain users under GDPR regulation. You are required to write a _decorator_ (called `mask`) that can be applied to these functions to obscure personal data. The user should be able to specify which fields to 

For example:
```python
@mask('name', 'email', 'mobile')
def get_client_details():
    return {
        'name': 'Jane Smith',
        'email': 'jane@coolmail.com',
        'telephones': {
            'mobile': '07999 987654'
        },
        'status': 'excellent'
    }
```

When we call `get_client`, we should see:
```python
{
        'name': 'J*** S****',
        'email': 'j***@********.com',
        'telephones': {
            'mobile': '***** ******'
        },
        'status': 'excellent'
}
```

The rules for obscuring are:
1. Numbers (or text containing numbers) should have all digits replaced by '*'.
1. Emails should obscure all characters except the first, the '@' symbol, the full stops, and the domain (e.g. '.com')
1. All other text should have all but the first letter of every word obscured.
1. Spaces should not be obscured.
1. Fields not specified in the decorator arguments should be left unchanged.
1. All fields matching a specified field at any level of nesting should be changed. (In the example shown, specifying 'mobile' is enough to match 'telephones.mobile'.)