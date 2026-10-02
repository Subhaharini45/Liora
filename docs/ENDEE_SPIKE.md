# ENDEE SPIKE

## Context
Phase 0 requires understanding the exact API contract of Endee Vector DB and verifying CRUD behavior, tenant isolation, and connection behavior.

## Results

**Connection Verified?**: NO (Local instance unavailable). Connection returns `ConnectionError` on `/api/v2/health` when local instance is not running. 

### API Contract (CONFIRMED via `endee` Python module 2.2.0)

**CONFIRMED**:
- **Initialization**: `client = endee.Endee(token=...)`
- **Configuration**: `client.set_base_url(...)`
- **Collection Creation**: `client.create_collection(name, fields=[...])`
- **Field Types**: Supports `"vector"`, `"sparse"`, `"multi_vector"`.
- **Insert/Update**: `Collection.upsert(objects: List[Dict])`. Objects follow layout `{"id", "meta", "filter", "fields"}`.
- **Search**: `Collection.search(fields, filter, ef_search)` where `fields` defines query per field.
- **Metadata Filtering**: Supported during search via `filter` argument using array syntax (e.g., `[{"tenant_id": {"$eq": "user_a"}}]`).
- **Update**: `Collection.update_filters(updates: List[Dict])`.
- **Delete Object**: `Collection.delete_object(id: str)`.
- **Delete by Filter**: `Collection.delete_by_filter(filter)`.
- **Delete Collection**: `client.delete_collection(name: str)`.
- **Tenant Isolation**: Can be achieved by enforcing filter payloads containing `"tenant_id": {"$eq": "user_123"}` for every search. This isolation occurs at the query layer (since filtering happens server-side natively).

**ASSUMED**:
- We assume persistence after restart works robustly based on Endee's architecture, but it could not be practically tested without a running service.
- We assume concurrent requests are supported as the Python client utilizes HTTP connection pooling natively (e.g. `requests` or `httpx`).
- We assume empty results return an empty `results` dict/list gracefully based on standard vector db behavior.

**NOT SUPPORTED / UNKNOWN**:
- True physical tenant isolation at the database/collection level per user is unknown/unverified (likely cost-prohibitive). We plan to use logical isolation via `filter` tags.
- Behavior on extreme scale metadata updates.

## Actions for Phase 1
- Provision a remote Endee Cloud instance or install Endee natively/Docker on a properly equipped host.
- Run `experiments/endee/test_endee.py` against the real instance to finalize behavior verification.
