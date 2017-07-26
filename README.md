# G Card ~ _______Express Way To E-Commerce_______
![GCard Logo]()
G Card your express way to buying products on internet without **Sharing Credit Card Info**.                                   
You can use this card to charge your main card once. You can get the disposable cards from the selected mall in the your city (more info: /wcibd-cards/)

## How Work G Card System
We have x reseller mall. They are selling Disposable GCards. 
Procsess of the buying a product:

1. Register G Cards and get a card ID
2. Select one of them and get their adress. 
3. Enter /wcibd-cards/ in your browser. Select your city and district and see the list of offical sellers list
4. Buy a disposable card (what amount what you want) and open G Card Site again
5. Click Add Balance & Click A Product and Buy IT 

and you get the product 😄 Good Luck
# GCard Models Description
GCard is a open-source project for the contirbuting open-source system and we are sharing our all code in github.
This Page is telling developers our model classes.

### card_digit_gen function
```python
def card_digit_gen ():
    return uuid.uuid4().hex[:8]
```
This function provides us to generate unique main card id 
## Card Model
```python
class Card(models.Model):
    digits = models.CharField(max_length=8, default=card_digit_gen, unique=True)
    balance = models.PositiveSmallIntegerField(default=0)
    def __str__(self):
        return "Card No: {no} \n Card Balance: {balance}".format(no=self.digits, balance=self.balance)
```
_This Model Provides Us To Generate Main Card._ 
***

**Digits:**
```digits = generating unique id for main card```

***

**Balance:**
```balance = Storages Total Card Balance as Positive S. Integer```

***

### Card's __str__
```python
def __str__(self):
    return "Card No: {no} \n Card Balance: {balance}".format(no=self.digits, balance=self.balance)
```
**Example Result:**
``` Card No: 6ff2dj5t 
    Card Balance: 150 
```

***

***
## Product Model
```python
class Product(models.Model):
    title = models.CharField(max_length=100)
    desc = models.TextField()
    price = models.PositiveSmallIntegerField(default=0)
    image = models.URLField()
    def __str__(self):
	return "Title: {title} \n Description: {desc} \n Price: {price} \n Image Url:                             {im}".format(title=self.title, desc=self.desc, price=self.price, im=self.image)
```
_This Model Provides Us To Add A Product To Database._ 
***
**Title:**
```title = It contains product's name```
***
**Desc:**
```desc = It contains product's description```
***
**Price:**
```price = It contains product's price as integer```
***
**Image:**
```image = It contains product's as URL```
***
```python
def __str__(self):
    return "Title: {title} \n Description: {desc} \n Price: {price} \n Image Url:  {im}".format(title=self.title, desc=self.desc, price=self.price, im=self.image)
```
**Example Result:**
```Title: Logitech M130
   Description: A Logitech Mouse with 4 Button in the Left side
   Price: 70
   Image Url: https://imageurl.com
```
***

### card_digit_gen function
```python
def paymentcard_digit_gen ():
    return uuid.uuid4().hex[:10]
```
This function provides us to generate unique disposable card id 
## Card Model
```python
class PaymentCard(models.Model):
    digits = models.CharField(max_length=10, default=paymentcard_digit_gen, unique=True)
    balance = models.PositiveSmallIntegerField(default=0)
    used = models.BooleanField(default=False)
    def __str__(self):
return "Card No: {dig} \n Card Balance: {bal} \n Is Card Used: {used} ".format(dig=self.digits, bal=self.balance, used=self.used)
```
_This Model Provides Us To Generate Main Card._ 
***

**Digits:**
```digits = generating unique id for disposable card```

***

**Balance:**
```balance = storages disposable card balance as Positive S. Integer```

***
**Used:**
```used = Is the disposable card used or not```

***
```python
def __str__(self):
    return "Card No: {dig} \n Card Balance: {bal} \n Is Card Used: {used} ".format(dig=self.digits, bal=self.balance, used=self.used)
```
**Example Result:**
``` Card No: 6ff2dj5tad 
    Card Balance: 50 
```
*** 

