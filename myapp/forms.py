from django import forms
from .models import Producto, Stock

class ProductoForm(forms.ModelForm):
    cantidad = forms.IntegerField(label='Cantidad en Stock', min_value=0)

    class Meta:
        model = Producto
        fields = ['cod_prod', 'nombre', 'descripcion', 'precio', 'categoria', 'cantidad']

    def __init__(self, *args, **kwargs):
        if 'instance' in kwargs:
            instance = kwargs['instance']
            initial = kwargs.setdefault('initial', {})
            if instance.pk:
                try:
                    initial['cantidad'] = instance.stock.cantidad
                except Stock.DoesNotExist:
                    initial['cantidad'] = 0
        super().__init__(*args, **kwargs)