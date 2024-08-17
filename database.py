from spider import fields, models


class Sensor(models.Model):    
    nome = fields.CharField(max_length=20,null=False)
    valor = fields.FloatField()
    min_val = fields.IntegerField()
    max_val = fields.IntegerField()
    intrevalo_leitura = fields.IntegerField()
    read_time = fields.DateTimeField(auto_now=True)
    ocorreu_erro = fields.BooleanField(default=False)

sensor_table = Sensor()
sensor_table.create_table()
