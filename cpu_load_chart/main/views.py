import json
from django.shortcuts import render
from .tasks import save_data
from datetime import datetime, timedelta
from .utils import prepare_data_for_template
from .models import CPULoad


# Create your views here.
def index(request):
   
    save_data(repeat=5)

    filter_value = datetime.today() - timedelta(hours=1)
    print(filter_value)
    output_data = CPULoad.objects.filter(added_at__gte=filter_value).values('load', 'added_at')
   
    data_for_template = prepare_data_for_template(output_data)
    
    def custom_serializer(obj):
        if isinstance(obj, datetime):
            serial = obj.isoformat("#","seconds")
            return serial
    
    dataJSON = json.dumps(data_for_template, default=custom_serializer)
    return render(request, 'main/index.html', {'data': dataJSON})