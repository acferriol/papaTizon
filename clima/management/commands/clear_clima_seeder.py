from django.core.management.base import BaseCommand
from clima.models import Clima, Empresa, Estacion


class Command(BaseCommand):
    help = "Delete all seeded data: Clima, Empresa, and Estacion"

    def handle(self, *args, **options):
        models_to_clear = [
            (Clima, "Clima"),
            (Empresa, "Empresa"),
            (Estacion, "Estacion"),
        ]

        for model, name in models_to_clear:
            count = model.objects.count()
            if count > 0:
                if name == "Empresa":
                    Empresa.objects.filter(nombre__startswith="Empresa ").delete()
                elif name == "Estacion":
                    Estacion.objects.filter(num_estacion__startswith="EST").delete()
                else:
                    model.objects.all().delete()
                self.stdout.write(
                    self.style.WARNING(f"🗑️  Deleted {count} {name} objects.")
                )
            else:
                self.stdout.write(
                    self.style.NOTICE(f"🔍 No {name} objects found to delete.")
                )

        self.stdout.write(self.style.SUCCESS("✅ All seeded data has been removed."))
