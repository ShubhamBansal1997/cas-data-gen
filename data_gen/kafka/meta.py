import uuid
from datetime import datetime

import jsonobject


class ChangeMeta(jsonobject.JsonObject):
    """
    Metadata about a change.
    """
    # stolen from CommCare HQ's ChangeMeta

    _allow_dynamic_properties = False

    document_id = jsonobject.DefaultProperty(required=True)

    # Only relevant for Couch documents
    document_rev = jsonobject.StringProperty()

    # 'couch' or 'sql'
    data_source_type = jsonobject.StringProperty(required=True)

    # couch database name or one of data sources listed in corehq.apps.change_feed.data_sources
    data_source_name = jsonobject.StringProperty(required=True)

    # doc_type property of doc or else the topic name
    document_type = jsonobject.DefaultProperty()

    document_subtype = jsonobject.StringProperty()
    domain = jsonobject.StringProperty()
    is_deletion = jsonobject.BooleanProperty()
    publish_timestamp = jsonobject.DateTimeProperty(default=datetime.utcnow)

    # note: this has been added and is different from commcarehq
    document = jsonobject.DefaultProperty()

    # track of retry attempts
    attempts = jsonobject.IntegerProperty(default=0)


def get_form_meta(document):
    # todo: other fields
    return ChangeMeta(
        document_id=uuid.uuid4().hex,
        data_source_type='sql',
        data_source_name='form-sql',
        document_type='XFormInstance',
        document=document,
    )


def get_case_meta():
    # todo: other fields
    return ChangeMeta(
        document_id=uuid.uuid4().hex,
        data_source_type='sql',
        data_source_name='case-sql',
        document_type='CommCareCase',
    )
