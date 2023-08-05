# evidencer

Work In Progress

```python
import evidencer
import os

e = evidencer.Evidencer()

# Add directory with custom extractors plugins
e.append_extractors_plugin_directory("test_extractors")

# Add directory with custom extractors pre configurations
e.append_extractors_pre_configurations_directory("test_extractor_pre_configurations")

extractions = e.extract_by_file(os.path.join("test_user_configurations", "with_pre_configuration.json"))
for extraction_key, extraction in extractions.items():
    print("%s: %s" % (extraction.result.label, extraction.result.value))
```

