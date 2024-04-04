pet = {
    "type": "object",
    "required": ["name", "type"],
    "properties": {
        "id": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        },
        "type": {
            "type": "string",
            "enum": ["cat", "dog", "fish"]
        },
        "status": {
            "type": "string",
            "enum": ["available", "sold", "pending"]
        },
    }
}
pet_order = {
    "type": "object",

    "required": ["pet_id"],

      "properties": {
          
        "id": {
            "type": "integer"
        },
         "pet_id": {
            "type": "integer"
        } ,

      }
}