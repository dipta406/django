from django.db import models

# Create your models here.
class cartItem(models.Model):
    cid = models.IntegerField(auto_created= True ,primary_key= True) 
    pid = models.IntegerField()
    qty = models.SmallIntegerField()
    uid = models.IntegerField()
    in_cart = models.IntegerField(default=True)
    
    def __str__(self) -> str:
        return f"CartItem(cid = {self.cid}, pid = {self.pid} , qty = {self.qty})"
    