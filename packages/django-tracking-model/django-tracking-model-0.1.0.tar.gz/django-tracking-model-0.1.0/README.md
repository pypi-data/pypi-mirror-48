# Django Tracking Model 🏁
Track changes made to your model's instance.  
Changes are cleared on save.  
This package is intented to be used mainly with signals.  
Mutable fields (e.g. JSONField) are not handled with deepcopy to keep it fast and simple.  
Meant to be model_utils's FieldTracker fast alternative.


## Usage
```python
from django.db import models
from tracking_model import TrackingModelMixin

# order matters
class Example(TrackingModelMixin, models.Model)
    text = models.TextField(null=True)
    self = models.ForeignKey("self", null=True)
    array= models.ArrayField(TextField())
```
```python
In [1]: e = Example.objects.create(id=1, text="Sample Text")
In [2]: e.tracker.changed, e.tracker.newly_created
Out[1]: ({}, True)
In [3]: e.text = "Different Text"
In [4]: e.tracker.changed
Out[2]: {"text": "Sample Text"}
In [5]: e.save()
In [6]: e.tracker.changed, e.tracker.newly_created
Out[3]: ({}, False)
```
DTM will also detect changes made to ForeignKey/OneToOne fields
```python
In [1]: Example.objects.create(self=e)
In [2]: e.self = None
In [3]: e.tracker.changed
Out[1]: {"self_id": 1}
```
Because DTM does not handle mutable fields well you handle them with copy/deepcopy
```python
In [1]: e = Example.objects.create(array=['I', 'am', 'your'])
In [2]: copied = copy(e.array)
In [3]: copied.append('father')
In [4]: e.array = copied
In [5]: e.tracker.changed
Out[1]: {'array': ['I', 'am', 'your', 'father']}
```
DTM works best with \*\_save signals
```python
def pre_save_example(instance, *args, **kwargs):
    # .create() does not populate .changed, we use newly_created
    if 'text' in instance.tracker.changed or instance.tracker.newly_created:
      if instance.text
          instance.array = instance.text.split()

pre_save.connect(pre_save_example, sender=Example)
```
```python
In [1]: e = Example.objects.create(text='I am your father')
In [2]: e.refresh_from_db() # not needed
In [3]: e.array
Out[1]: ['I', 'am', 'your', 'father']
```

## Requirements
 * Python >= 2.7, <= 3.7
 * Django >= 1.9, <= 2.2

## Todo
- [ ] Tests could be more readable
- [ ] Signals decorators
