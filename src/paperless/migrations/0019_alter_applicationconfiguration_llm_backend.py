from django.db import migrations
from django.db import models


class Migration(migrations.Migration):
    dependencies = [("paperless", "0018_applicationconfiguration_barcode_store_values")]

    operations = [
        migrations.AlterField(
            model_name="applicationconfiguration",
            name="llm_backend",
            field=models.CharField(
                blank=True,
                choices=[
                    ("openai-like", "OpenAI-compatible"),
                    ("ollama", "Ollama"),
                    ("minimax", "MiniMax"),
                ],
                max_length=128,
                null=True,
                verbose_name="Sets the LLM backend",
            ),
        ),
    ]
