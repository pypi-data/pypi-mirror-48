# -*- coding: utf-8 -*-
from guillotina import configure
from guillotina.json.serialize_schema import SerializeFactoryToJson
from guillotina.interfaces import IFactorySerializeToJson
from guillotina.component.interfaces import IFactory
from guillotina_cms.interfaces import ICMSLayer
from guillotina_cms.directives import fieldset
from guillotina_cms.directives import merged_tagged_value_dict_merged
from guillotina.schema.interfaces import ISource
from guillotina import app_settings


@configure.adapter(
    for_=(IFactory, ICMSLayer),
    provides=IFactorySerializeToJson)
class SerializeCMSFactoryToJson(SerializeFactoryToJson):

    async def __call__(self):
        result = await super(SerializeCMSFactoryToJson, self).__call__()

        # Adding fieldsets to schema
        fieldsets_dict = {}
        for key, value in merged_tagged_value_dict_merged(self.factory.schema, fieldset.key).items():
            if key not in fieldsets_dict:
                fieldsets_dict[key] = value.copy()
            else:
                fieldsets_dict[key].extend(value)

        for schema in self.factory.behaviors or ():
            for key, value in merged_tagged_value_dict_merged(schema, fieldset.key).items():
                behavior_fields = [schema.__identifier__ + '.' + field for field in value]
                if key not in fieldsets_dict:
                    fieldsets_dict[key] = behavior_fields.copy()
                else:
                    fieldsets_dict[key].extend(behavior_fields)

        fieldsets = [{'fields': value, 'id': key, 'title': key} for key, value in fieldsets_dict.items()]
        # Some naive order
        result['fieldsets'] = []
        to_append = None
        for fsobj in fieldsets:
            if fsobj['id'] == 'default':
                result['fieldsets'].insert(0, fsobj)
            elif fsobj['id'] == 'settings':
                to_append = fsobj
            else:
                result['fieldsets'].append(fsobj)

        if to_append is not None:
            result['fieldsets'].append(to_append)

        result['layouts'] = app_settings['layouts'].get(self.factory.schema.__identifier__, [])
        return result


@configure.value_serializer(ISource)
def source_converter(source):
    result = {}
    for key in source.keys():
        try:
            result[key] = source.getTerm(key)
        except KeyError:
            pass
    return result
