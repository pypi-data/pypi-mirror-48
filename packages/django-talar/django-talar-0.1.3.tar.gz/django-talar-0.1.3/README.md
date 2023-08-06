# django-talar

Simple Django app for https://talar.app service. 

## Installation
1. Add `talar` to your django settings `INSTALLED_APPS`.
2. Modify code below and also insert it into django settings:
    ```
    TALAR = {
        "project_id": env.str("TALAR_PROJECT_ID", None),
        "secret_key": env.str("TALAR_SECRET_KEY", None),
        "token": env.str("TALAR_TOKEN", None)
    }
     ``` 
 3. Include this into your core urls:
    ```
    path('talar/', include(('talar.urls', 'talar'))),
    ```

## Basic usage
django-talar contains basic form `talar.forms.PaymentForm` and template 
`talar/talar_make_payment.html` for payment making. It is suggested to
use it by adding your own view like so:
```
def make_payment(request):
    data = {
        'external_id': EXTERNAL_ID, # You order/payment unique key that will be used to identify payment
        'amount': AMOUNT, # your data
        'currency': CURRENCY, # your data
        'continue_url': CONTINUE_URL, # Insert address for redirection after successfull payment
    }

    talar = Talar()
    url = talar.url
    data = talar.create_payment_data(data)

    payment_form = PaymentForm(data={'key_id': talar.key_id, 'encrypted': data})
    ctx = {'url': url, 'payment_form': payment_form}
    return TemplateResponse(
        request, 'talar/make_payment.html', ctx
    )
```

html code will handle redirection if everything is correct:
```
    <div>
        <p>{% trans 'After continuing you will be redirected to payment provider site.' %}</p>
        <form action="{{ url }}" method="post" class="form-inline">
            {{ payment_form.as_p }}
            <button type=submit class="btn btn-primary">{% trans 'Pay' %}</button>
        </form>
    </div>
```