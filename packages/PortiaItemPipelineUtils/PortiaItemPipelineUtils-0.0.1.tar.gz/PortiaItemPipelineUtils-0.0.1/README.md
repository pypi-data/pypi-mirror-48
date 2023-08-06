### Description
Scrapy portia pipeline which allow you to do resultant items related stuff.

### Install
**Official install**
```
pip install PortiaItemPipelineUtils
```

**Git install**
```
git clone https://github.com/asiellb/portia-item-pipeline-utils.git
cd portia-item-pipeline-utils
pip install .
```

### Usage (Configure settings.py:)
- PortiaItemPipelineUtils.ReplaceDashesFields

  ```bash
  ITEM_PIPELINES = {
    'portiaitempipelineutils.portiaitempipelineutils.ReplaceDashesFields': 499
  }
  ```
