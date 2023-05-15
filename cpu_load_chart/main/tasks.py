from background_task import background
from .models import CPULoad
import psutil


@background
def save_data():
        cpu_load = psutil.cpu_percent(interval=None)       
        CPULoad.objects.create(load=cpu_load)
        
        
save_data(repeat=5)