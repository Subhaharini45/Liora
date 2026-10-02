import endee
import time
import os
import json

print("--- ENDEE SPIKE ---")

# We attempt to connect to a local instance or one specified by ENDEE_URL/ENDEE_TOKEN
token = os.getenv("ENDEE_TOKEN", "mock_token")
base_url = os.getenv("ENDEE_URL", "http://localhost:8000/api/v2")

try:
    client = endee.Endee(token=token)
    client.set_base_url(base_url)
    
    print("Testing connection...")
    health = client.health()
    print("Health:", health)
    
    # 2. Index creation
    collection_name = "test_spike_collection"
    print(f"Creating collection '{collection_name}'...")
    try:
        client.delete_collection(collection_name)
    except:
        pass
        
    client.create_collection(collection_name, fields=[
        {"name": "embedding", "type": "vector", "params": {"dimension": 384, "space_type": "cosine", "precision": "fp32"}}
    ])
    
    # 3. Index listing
    cols = client.list_collections()
    print("Collections:", [c.get("name") for c in cols])
    
    col = client.get_collection(collection_name)
    
    # 4. Vector insertion + 5. Metadata/payload insertion
    print("Inserting data (User A & User B)...")
    col.upsert([
        {
            "id": "doc1", 
            "meta": {"text": "Liora is a learning assistant"}, 
            "filter": {"tenant_id": "user_a"}, 
            "fields": {"embedding": [0.1] * 384}
        },
        {
            "id": "doc2", 
            "meta": {"text": "User B secret notes"}, 
            "filter": {"tenant_id": "user_b"}, 
            "fields": {"embedding": [0.2] * 384}
        }
    ])
    
    # 6. Vector search & 7. Metadata filtering & Tenant Isolation
    print("Searching for User A...")
    res_a = col.search(
        fields={"embedding": {"query": [0.1] * 384, "limit": 10}},
        filter=[{"tenant_id": {"$eq": "user_a"}}]
    )
    print("User A search results (should only see doc1):")
    for hit in res_a.get("results", {}).get("embedding", []):
        print(" -", hit.get("id"), hit.get("meta"))
        if hit.get("id") == "doc2":
            print("BLOCKER: User A retrieved User B data!")
            
    # 8. Update behavior
    print("Updating doc1 filter...")
    col.update_filters([{"id": "doc1", "filter": {"tenant_id": "user_a", "updated": True}}])
    
    # 9. Delete behavior
    print("Deleting doc2...")
    col.delete_object("doc2")
    
    print("Search after delete User B:")
    res_b = col.search(
        fields={"embedding": {"query": [0.2] * 384}},
        filter=[{"tenant_id": {"$eq": "user_b"}}]
    )
    print("User B results:", len(res_b.get("results", {}).get("embedding", [])))

    print("Endee Spike completed successfully (Remote/Local instance reached).")

except Exception as e:
    print(f"\nENDEE CONNECTION/EXECUTION FAILED: {type(e).__name__} - {str(e)}")
    print("Note: This is expected if there is no Endee DB running locally or configured.")
    print("We have collected the API contract from the Python module documentation.")
