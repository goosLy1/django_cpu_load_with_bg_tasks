import atexit

from django.core.management.commands.runserver import Command as RunserverCommand
from ...models import CPULoad
from background_task.models import Task


class Command(RunserverCommand):
    def __init__(self, *args, **kwargs):
        if CPULoad.objects.exists():
            CPULoad.objects.create(load=0)
        atexit.register(self.exit)
        return super(Command, self).__init__(*args, **kwargs)

    def kill_background_task(self):
        background_tasks = Task.objects.filter(task_name='main.tasks.save_data')
        for background_task in background_tasks:
            background_task.delete()


    def exit(self):
        self.kill_background_task() 
        CPULoad.objects.create(load=0)

    