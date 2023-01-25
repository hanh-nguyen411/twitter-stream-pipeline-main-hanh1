import json


def create_schema():
    schema = dict()
    schema.update(
        {
            "$schema": "http://json-schema.org/draft-07/schema#",
            "$id": "http://example.com/myURI.schema.json",
            "title": "TweetRecord",
            "description": "Schema for a tweet record",
            "type": "object",
            "additionalProperties": False,
            "properties": {
                "id": {
                    "type": "string",
                    "description": "The unique identifier of the requested Tweet"
                },
                "text": {
                    "type": "string",
                    "description": "The actual UTF-8 text of the Tweet"
                },
                "created_at": {
                    "type": "string",
                    "description": "Creation time of the Tweet."
                }
            }
        }
    )

    schema = json.dumps(schema)
    return schema

