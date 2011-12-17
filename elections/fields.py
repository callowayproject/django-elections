from django.db.models import CharField
from django.utils.translation import ugettext as _

from .settings import TEST_DATA_ONLY

class TestFlagField(CharField):
    """
    t is test data and l is live data field
    
    Can't override choices or max_length
    """
    def __init__(self, **kwargs):
        default_args = {
            'choices': (('t', _('Test Data')), ('l', _('Live Data'))),
            'max_length': 1,
            'default': {True: 't', False: 'l'}[TEST_DATA_ONLY]
        }
        if 'choices' in kwargs:
            kwargs.pop('choices')
        if 'max_length' in kwargs:
            kwargs.pop('max_length')
        default_args.update(kwargs)
        super(TestFlagField, self).__init__(**default_args)


try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^elections\.fields\.TestFlagField"])
except ImportError:
    pass
