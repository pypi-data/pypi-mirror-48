import event_model
from intake_bluesky.core import documents_to_xarray


def no_event_pages(descriptor_uid):
    yield from ()


def test_no_descriptors():
    run_bundle = event_model.compose_run()
    start_doc = run_bundle.start_doc
    stop_doc = run_bundle.compose_stop()
    documents_to_xarray(
        start_doc=start_doc,
        stop_doc=stop_doc,
        descriptor_docs=[],
        get_event_pages=no_event_pages,
        filler=event_model.Filler({}),
        get_resource=None,
        lookup_resource_for_datum=None,
        get_datum_pages=None)


def test_no_events():
    run_bundle = event_model.compose_run()
    start_doc = run_bundle.start_doc
    desc_bundle = run_bundle.compose_descriptor(
        data_keys={'x': {'source': '...', 'shape': [], 'dtype': 'number'}},
        name='primary')
    descriptor_doc = desc_bundle.descriptor_doc
    stop_doc = run_bundle.compose_stop()
    documents_to_xarray(
        start_doc=start_doc,
        stop_doc=stop_doc,
        descriptor_docs=[descriptor_doc],
        get_event_pages=no_event_pages,
        filler=event_model.Filler({}),
        get_resource=None,
        lookup_resource_for_datum=None,
        get_datum_pages=None)
